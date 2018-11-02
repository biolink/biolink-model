import abc
from contextlib import redirect_stdout
from io import StringIO
from typing import List, Set, Union, TextIO, Optional, TypeVar

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    TypeDefinition, Element, SlotDefinitionName, TypeDefinitionName, PrefixLocalName
from metamodel.utils.builtins import builtin_names, DEFAULT_BUILTIN_TYPE_NAME
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.schemaloader import SchemaLoader
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.typereferences import References

CLASS_OR_CLASSNAME = TypeVar('CLASS_OR_CLASSNAME', ClassDefinitionName, ClassDefinition)
SLOT_OR_SLOTNAME = TypeVar('SLOT_OR_SLOTNAME', SlotDefinitionName, SlotDefinition)
TYPE_OR_TYPENAME = TypeVar('TYPE_OR_TYPENAME', TypeDefinitionName, TypeDefinition)
ELEMENT_NAME = TypeVar('ELEMENT_NAME', ClassDefinitionName, SlotDefinitionName, TypeDefinitionName)


class Generator(metaclass=abc.ABCMeta):
    generatorname: str = None        # Set to os.path.basename(__file__)
    generatorversion: str = None
    valid_formats: List[str] = []
    visit_all_class_slots: bool = False    # False means only visit direct slots, True means visit all slots

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str=None) -> None:
        assert fmt in self.valid_formats, f"Unrecognized format: {fmt}"
        self.format = fmt
        self.schema = schema if isinstance(schema, SchemaDefinition) else SchemaLoader(schema).resolve()
        self.synopsis: SchemaSynopsis = SchemaSynopsis(self.schema)

    def serialize(self, **kwargs) -> str:
        output = StringIO()
        with redirect_stdout(output):
            self.visit_schema(**kwargs)
            for cls in sorted(self.schema.classes.values(), key=lambda c: c.name.lower()):
                if self.visit_class(cls):
                    for slot in self.all_slots(cls) if self.visit_all_class_slots else self.cls_slots(cls):
                        self.visit_class_slot(cls, self.aliased_slot_name(slot), slot)
                    self.end_class(cls)
            for sn, slot in sorted(self.schema.slots.items(), key=lambda c: c[0].lower()):
                self.visit_slot(self.aliased_slot_name(slot), slot)
            self.end_schema(**kwargs)
        return output.getvalue()

    def visit_schema(self, **kwargs) -> None:
        """ Visit once at the beginning

        @param kwargs: Arguments passed through from CLI -- implementation dependent
        """
        ...

    def end_schema(self, **kwargs) -> None:
        """ Visited at end of generation

        @param kwargs: Arguments passed through from CLI -- implementation dependent
        """
        ...

    def visit_class(self, cls: ClassDefinition) -> bool:
        """ Visited once per class in the schema

        @param cls: class being visited
        @return: Visit slots and end class.  False means skip and go on
        """
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        """ Visited after visit_class_slots (if visit_class returned true)

        @param cls: class being visited
        """
        ...

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        """ Visited for each slot in a class.  If class level visit_all_slots is true, this is visited once
        for any class that is inherited (class itself, is_a, mixin, apply_to).  Otherwise just the class slots.

        @param cls: containing class
        @param aliased_slot_name: Aliased slot name.  May not be unique across all class slots
        @param slot: slot being visited
        """
        ...

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        """ Visited once for every slot in the schema.

        @param aliased_slot_name: Aliased name of the slot.  May not be unique
        @param slot: visited slot
        """
        ...

    #
    # Helper methods
    def cls_slots(self, cls: CLASS_OR_CLASSNAME) -> List[SlotDefinition]:
        """ Return the list of slots directly included in the class definition.  Includes slots whose
        domain is cls -- as declared in slot.domain or class.slots

        Does not include slots declared in mixins, apply_to or is_a links

        @param cls: class name or class definition name
        @return: all direct class slots
        """
        if not isinstance(cls, ClassDefinition):
            cls = self.schema.classes[cls]
        return [self.schema.slots[s] for s in cls.slots]

    def all_slots(self, cls: CLASS_OR_CLASSNAME, *, cls_slots_first: bool = False) \
            -> List[SlotDefinition]:
        """ Return all slots that are part of the class definition.  This includes all is_a, mixin and apply_to slots
        but does NOT include slot_usage targets.  If class B has a slot_usage entry for slot "s", only the slot
        definition for the redefined slot will be included, not its base.  Slots are added in the order they appear
        in classes, with recursive is_a's being added first followed by mixins and finally apply_tos

        @param cls: class definition or class definition name
        @param cls_slots_first: True means return class slots at the top of the list
        @return: ordered list of slots in the class with slot usages removed
        """
        def merge_definitions(cls_name: Optional[ClassDefinitionName]) -> None:
            if cls_name:
                for slot in self.all_slots(cls_name):
                    aliased_name = self.aliased_slot_name(slot)
                    if aliased_name not in known_slots:
                        known_slots.add(aliased_name)
                        rval.append(slot)

        if not isinstance(cls, ClassDefinition):
            cls = self.schema.classes[cls]
        known_slots: Set[str] = self.aliased_slot_names(cls.slots)
        rval: List[SlotDefinition] = []

        if cls_slots_first:
            rval += self.cls_slots(cls)
            for mixin in cls.mixins:
                merge_definitions(mixin)
            merge_definitions(cls.is_a)
        else:
            merge_definitions(cls.is_a)
            for mixin in cls.mixins:
                merge_definitions(mixin)
            rval += self.cls_slots(cls)

        return rval

    def ancestors(self, definition: Union[SLOT_OR_SLOTNAME,
                                          CLASS_OR_CLASSNAME]) \
            -> List[Union[SlotDefinitionName, ClassDefinitionName]]:
        """ Return an ordered list of ancestor names for the supplied slot or class

        @param definition: Slot or class name or definition
        @return: List of ancestor names
        """
        definition = self.obj_for(definition)
        return [definition.name] + (self.ancestors(definition.is_a) if definition.is_a is not None else [])

    def neighborhood(self, elements: List[ELEMENT_NAME]) \
            -> References:
        """ Return a list of all slots, classes and types that touch any element in elements, including the element
        itself

        @param elements: Elements to do proximity with
        @return: All slots and classes that touch element
        """
        touches = References()
        for element in elements:
            if element in self.schema.classes:
                touches.classrefs.add(element)
                if None in touches.classrefs:
                    raise ValueError("1")
                cls = self.schema.classes[element]
                if cls.is_a:
                    touches.classrefs.add(cls.is_a)
                if None in touches.classrefs:
                    raise ValueError("1")
                # Mixins include apply_to's
                touches.classrefs.update(set(cls.mixins))
                for slotname in cls.slots:
                    slot = self.schema.slots[slotname]
                    if slot.range in self.schema.classes:
                        touches.classrefs.add(slot.range)
                    elif slot.range in self.schema.types:
                        touches.typerefs.add(slot.range)
                    if None in touches.classrefs:
                        raise ValueError("1")
                if element in self.synopsis.rangerefs:
                    for slotname in self.synopsis.rangerefs[element]:
                        touches.slotrefs.add(slotname)
                        if self.schema.slots[slotname].domain:
                            touches.classrefs.add(self.schema.slots[slotname].domain)
            elif element in self.schema.slots:
                touches.slotrefs.add(element)
                slot = self.schema.slots[element]
                touches.slotrefs.update(set(slot.mixins))
                if slot.is_a:
                    touches.slotrefs.add(slot.is_a)
                if element in self.synopsis.inverses:
                    touches.slotrefs.update(self.synopsis.inverses[element])
                if slot.domain:
                    touches.classrefs.add(slot.domain)
                if slot.range in self.schema.classes:
                    touches.classrefs.add(slot.range)
                elif slot.range in self.schema.types:
                    touches.typerefs.add(slot.range)
            elif element in self.schema.types:
                if element in self.synopsis.rangerefs:
                    touches.slotrefs.update(self.synopsis.rangerefs[element])

        return touches

    def grounded_slot_range(self, slot: Optional[Union[SlotDefinition, Optional[str]]]) -> str:
        """ Chase the slot range to its final form

        @param slot: slot to check
        @return: name of resolved range
        """
        if slot is not None and not isinstance(slot, str):
            slot = slot.range
        if slot is None:
            return DEFAULT_BUILTIN_TYPE_NAME         # Default type name
        elif slot in builtin_names:
            return slot
        elif slot in self.schema.types:
            return self.grounded_slot_range(self.schema.types[slot].typeof)
        else:
            return slot

    def aliased_slot_name(self, slot: SLOT_OR_SLOTNAME) -> str:
        """ Return the overloaded slot name -- the alias if one exists otherwise the actual name

        @param slot: either a slot name or a definition
        @return: overloaded name
        """
        if isinstance(slot, str):
            slot = self.schema.slots[slot]
        return slot.alias if slot.alias else slot.name

    def aliased_slot_names(self, slot_names: List[SlotDefinitionName]) -> Set[str]:
        """ Return the aliased slot names for all members of the list

        @param slot_names: actual slot names
        @return: aliases w/ duplicates removed
        """
        return {self.aliased_slot_name(sn) for sn in slot_names}

    def obj_for(self, obj_or_name: Union[str, Element]) -> Optional[Union[str, Element]]:
        """ Return the class, slot or type that represents name or name itself if it is a builtin

        @param obj_or_name: Object or name
        @return: Corresponding element or None if not found (most likely cause is that it is a builtin type)
        """
        name = obj_or_name.name if isinstance(obj_or_name, Element) else obj_or_name
        return self.schema.classes[name] if name in self.schema.classes \
            else self.schema.slots[name] if name in self.schema.slots \
            else self.schema.types[name] if name in self.schema.types else name if name in builtin_names \
            else None

    def obj_name(self, obj: Union[str, Element]) -> str:
        """ Return the formatted name used for the supplied definition """
        if isinstance(obj, str):
            obj = self.obj_for(obj)
        if isinstance(obj, SlotDefinition):
            return underscore(self.aliased_slot_name(obj))
        else:
            return camelcase(obj if isinstance(obj, str) else obj.name)

    @staticmethod
    def id_to_url(id_: str) -> str:
        uri = id_
        if ':' in id_:
            # TODO! use PC
            if id_.startswith('SIO:'):
                uri = id_.replace('SIO:', 'http://semanticscience.org/resource/SIO_')
            elif id_.startswith('HGNC:'):
                uri = 'https://monarchinitiative.org/gene/' + id_
            else:
                frag = id_.replace(':', '_')
                base = 'http://purl.obolibrary.org/obo/'
                uri = base+frag
        return uri

    def default_uri(self) -> Optional[str]:
        if self.schema.default_prefix:
            if '://' in self.schema.default_prefix:
                return self.schema.default_prefix
            elif self.schema.default_prefix in self.schema.prefixes:
                return self.schema.prefixes[PrefixLocalName(self.schema.default_prefix)].prefix_uri
            else:
                raise ValueError(f"Default prefix: {self.schema.default_prefix} is not defined")
        return None
