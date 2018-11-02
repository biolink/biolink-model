from typing import List, Union, TextIO

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    TypeDefinition, Element, SlotDefinitionName, TypeDefinitionName, PrefixLocalName
from metamodel.utils.generator import Generator, SLOT_OR_SLOTNAME, CLASS_OR_CLASSNAME

from collections import defaultdict

class ToolkitGenerator(Generator):
    """
    A shell of an implementation of Generator, for the sole purpose of accessing
    it's methods.
    """
    valid_formats = [None]
    def __init__(self, schema: Union[str, TextIO, SchemaDefinition]) -> None:
        super().__init__(schema, None)

        self.mappings = defaultdict(set)

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if 'related to' in self.ancestors(slot):
            slot.edge_label = slot.name.replace(' ', '_')

            for curie in slot.mappings:
                self.mappings[curie].add(slot.edge_label)

    def visit_class(self, cls: ClassDefinition) -> bool:
        if 'named thing' in self.ancestors(cls):
            for curie in cls.mappings:
                self.mappings[curie].add(cls.name)
