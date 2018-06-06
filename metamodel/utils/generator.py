import abc
from contextlib import redirect_stdout
from io import StringIO
from typing import List, Set, Union, TextIO, Optional

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    TypeDefinition, Element, SlotDefinitionName, TypeDefinitionName
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.schemaloader import SchemaLoader
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.typereferences import References


class Generator(metaclass=abc.ABCMeta):
    generatorname: str = None        # Set to os.path.basename(__file__)
    generatorversion: str = None
    valid_formats: List[str] = []
    visit_all__class_slots: bool = False    # False means only visit direct slots, True means visit all slots

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str=None) -> None:
        assert fmt in self.valid_formats, f"Unrecognized format: {fmt}"
        self.format = fmt
        self.schema = schema if isinstance(schema, SchemaDefinition) else SchemaLoader(schema).resolve()
        self.synopsis: SchemaSynopsis = SchemaSynopsis(self.schema)
        self.visit_all_slots = False

    def serialize(self, **kwargs) -> str:
        output = StringIO()
        with redirect_stdout(output):
            self.visit_schema(**kwargs)
            for cls in sorted(self.schema.classes.values(), key=lambda c: c.name.lower()):
                if self.visit_class(cls):
                    for slot in self.all_slots(cls) if self.visit_all_slots else self.cls_slots(cls):
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
    def cls_slots(self, cls: Union[ClassDefinitionName, ClassDefinition]) -> List[SlotDefinition]:
        """ Return the list of slots directly included in the class definition.  Includes:
        1. Slots whose domain is cls -- as declared in slot.domain or class.slots
        2. Slots defined in classes with apply_to
        Does not include slots declared in mixins or is_a reference

        @param cls: class name or class definition name
        @return: all direct class slots
        """
        if not isinstance(cls, ClassDefinition):
            cls = self.schema.classes[cls]
        return [self.schema.slots[s] for s in cls.slots]

    def all_slots(self, cls: Union[ClassDefinitionName, ClassDefinition]) -> List[SlotDefinition]:
        """ Return all slots that are part of the class definition.  This includes all is_a, mixin and apply_to slots
        but does NOT include slot_usage targets.  If class B has a slot_usage entry for slot "s", only the slot
        definition for the redefined slot will be included, not its base.  Slots are added in the order they appear
        in classes, with recursive is_a's being added first followed by mixins and finally apply_tos

        @param cls: class definition or class definition name
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

        merge_definitions(cls.is_a)
        for applier in self.synopsis.applytos:
            merge_definitions(applier)
        for mixin in cls.mixins:
            merge_definitions(mixin)
        rval += self.cls_slots(cls)

        return rval

    def ancestors(self, definition: Union[SlotDefinitionName, SlotDefinition]) \
            -> List[Union[SlotDefinitionName, ClassDefinitionName]]:
        """ Return an ordered list of ancestors for a class or a slot, inclusive """
        definition = self.obj_for(definition)
        return [definition.name] + self.ancestors(definition.is_a) if definition.is_a else []

    def root_closure(self, roots: List[Union[SlotDefinitionName, ClassDefinitionName]]) \
            -> Set[Union[SlotDefinitionName, ClassDefinitionName]]:
        """ Return the union of the ancesters of the elements in roots """
        closure: Set[Union[SlotDefinitionName, SlotDefinition]] = set()
        for root in roots:
            if root not in self.schema.classes and root not in self.schema.slots:
                raise ValueError("Unknown root: {root}")
            else:
                closure.update(set(self.ancestors(root)))
        return closure

    def neighborhood(self, elements: List[Union[SlotDefinitionName, ClassDefinitionName, TypeDefinitionName]]) \
            -> References:
        """ Return a list of all slots ane delements that touch any element in elements

        @param elements: Elements to do proximity with
        @return: All slots and classes that touch element
        """
        touches = References()
        for element in elements:
            if element in self.schema.classes:
                cls = self.schema.classes[element]
                if cls.is_a:
                    touches.classrefs.add(cls.is_a)
                touches.classrefs.update(set(cls.mixins))
                if element in self.synopsis.applytos:
                    touches.classrefs.update(self.synopsis.applytos[element].classrefs)
                for slotname in cls.slots:
                    slot = self.schema.slots[slotname]
                    if slot.range in self.schema.classes:
                        touches.classrefs.add(slot.range)
                    elif slot.range in self.schema.types:
                        touches.typerefs.add(slot.range)
            elif element in self.schema.slots:
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

    def aliased_slot_name(self, slot: Union[SlotDefinitionName, SlotDefinition]) -> str:
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

    def obj_for(self, name: str) -> Optional[Element]:
        """ Return the class, slot or type that represents name

        @param name:
        @return:
        """
        return self.schema.classes[name] if name in self.schema.classes \
            else self.schema.slots[name] if name in self.schema.slots \
            else self.schema.types[name] if name in self.schema.types else None

    def obj_name(self, obj: Union[str, ClassDefinition, SlotDefinition, TypeDefinition]) -> str:
        """ Return the name used for the supplied definition """
        if isinstance(obj, str):
            obj = self.obj_for(obj)
        if isinstance(obj, SlotDefinition):
            return underscore(self.aliased_slot_name(obj))
        else:
            return camelcase(obj.name) if obj else 'String'

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
