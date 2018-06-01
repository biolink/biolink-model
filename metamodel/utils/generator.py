import abc
from contextlib import redirect_stdout
from io import StringIO
from typing import List, Set, Union, TextIO, Optional

from metamodel.utils.loadschema import load_schema
from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, DefinitionName, \
    TypeDefinition, Element, SlotDefinitionName
from metamodel.utils.formatutils import camelcase, underscore


class Generator(metaclass=abc.ABCMeta):
    generatorname: str = None        # Set to os.path.basename(__file__)
    generatorversion: str = None
    valid_formats: List[str] = []

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str) -> None:
        self.schema = schema if isinstance(schema, SchemaDefinition) else load_schema(schema)
        assert fmt in self.valid_formats, f"Unrecognized format: {fmt}"
        self.format = fmt
        self.visit_all_slots = False

    def serialize(self, **kwargs) -> str:
        output = StringIO()
        with redirect_stdout(output):
            self.visit_schema(**kwargs)
            for cls in sorted(self.schema.classes.values(), key=lambda c: c.name.lower()):
                if self.visit_class(cls):
                    for slot in self.all_slots(cls) if self.visit_all_slots else self.cls_slots(cls):
                        self.visit_class_slot(cls, self.slot_name(slot), slot)
                    self.end_class(cls)
            for sn, slot in sorted(self.schema.slots.items(), key=lambda c: c[0].lower()):
                self.visit_slot(self.slot_name(slot), slot)
            self.end_schema(**kwargs)
        return output.getvalue()

    def visit_schema(self, **kwargs) -> None:
        ...

    def end_schema(self, **kwargs) -> None:
        ...

    def visit_class(self, cls: ClassDefinition) -> bool:
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        ...

    def visit_class_slot(self, cls: ClassDefinition, slot_name: str, slot: SlotDefinition) -> None:
        """ Visit a slot in class cls

        @param cls: containing class
        @param slot_name: slot name within the context of the class.  This name may not be unique
        @param slot: Actual slot.  Note that slot.name is unique and may be qualified by the containing class
        @return:
        """
        ...

    def visit_slot(self, slot_name: str, slot: SlotDefinition) -> None:
        ...

    #
    # Helper methods - not generally overridden
    def cls_slots(self, cls: ClassDefinition) -> List[SlotDefinition]:
        return [self.schema.slots[s] for s in cls.slots]

    def all_slots(self, cls: ClassDefinition) -> List[SlotDefinition]:
        return self.cls_slots(cls) + (self.all_slots(self.schema.classes[cls.is_a]) if cls.is_a else [])

    def ancestors(self, cn: ClassDefinitionName) -> Set[DefinitionName]:
        c = self.schema.classes[cn]
        return {cn}.union(self.ancestors(c.is_a) if c.is_a else {})

    def root_closure(self, roots: List[ClassDefinitionName]) -> Set[ClassDefinitionName]:
        closure: Set[ClassDefinitionName] = set()
        for root in roots:
            if root not in self.schema.classes:
                raise ValueError("Unknown root class: {root}")
            else:
                closure.update(self.ancestors(root))
        return closure

    def slot_name(self, slot: Union[str, SlotDefinition]) -> str:
        """ Return the underlying slot name

        @param slot:
        @return: actual name
        """
        if isinstance(slot, str):
            slot = self.schema.slots[SlotDefinitionName(DefinitionName(slot))]
        return slot.alias if slot.alias else slot.name

    def obj_for(self, name: str) -> Optional[Element]:
        return self.schema.classes[name] if name in self.schema.classes \
            else self.schema.slots[name] if name in self.schema.slots \
            else self.schema.types[name] if name in self.schema.types else None


    def obj_name(self, obj: Union[str, ClassDefinition, SlotDefinition, TypeDefinition]) -> str:
        if isinstance(obj, str):
            obj = self.obj_for(obj)
        if isinstance(obj, SlotDefinition):
            return underscore(self.slot_name(obj))
        else:
            return camelcase(obj.name)

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
