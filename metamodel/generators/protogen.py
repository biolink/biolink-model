import os
from typing import Union, TextIO

import click

from metamodel.metamodel import ClassDefinition, SlotDefinition, SchemaDefinition
from metamodel.utils.builtins import DEFAULT_BUILTIN_TYPE_NAME
from metamodel.utils.formatutils import camelcase, lcamelcase
from metamodel.utils.generator import Generator


class ProtoGenerator(Generator):
    """
    A `Generator` for creating Protobuf schemas from a metamodel schema.
    
    """
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['proto']
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='proto') -> None:
        super().__init__(schema, fmt)
        self.relative_slot_num = 0

    def visit_class(self, cls: ClassDefinition) -> bool:
        if cls.mixin or cls.abstract or not cls.slots:
            return False
        if cls.description:
            for dline in cls.description.split('\n'):
                print(f'// {dline}')
        print(f'message {camelcase(cls.name)}')
        print(" {")
        self.relative_slot_num = 0
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        print(" }")

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        qual = 'repeated ' if slot.multivalued else 'optional ' if not slot.required or slot.primary_key else ''
        slotname = lcamelcase(aliased_slot_name)
        slot_range = self.obj_name(slot.range)
        self.relative_slot_num += 1
        print(f"  {qual}{slotname} {slot_range} = {self.relative_slot_num}")


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='proto', type=click.Choice(['proto']),
              help="Output format")
def cli(yamlfile, format):
    """ Generate proto representation of biolink model """
    print(ProtoGenerator(yamlfile, format).serialize())
