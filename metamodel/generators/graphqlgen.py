import os
from typing import Union, TextIO

import click

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition
from metamodel.utils.formatutils import camelcase, lcamelcase
from metamodel.utils.generator import Generator


class GraphqlGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['graphql']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='csv') -> None:
        super().__init__(schema, fmt)

    def visit_class(self, cls: ClassDefinition) -> bool:
        etype = 'interface' if cls.abstract or cls.mixin else 'type'
        mixins = ', '.join([camelcase(mixin) for mixin in cls.mixins])
        print(f"{camelcase(cls.name)} {etype}" + (f"implements {mixins}" if mixins else ""))
        print("  {")
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        print("  }")
        print()

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        slotrange = camelcase(slot.range) if slot.range in self.schema.classes else "String"
        if slot.multivalued:
            slotrange = f"[{slotrange}]"
        if slot.required or slot.primary_key:
            slotrange = slotrange + '!'
        print(f"    {lcamelcase(aliased_slot_name)}: {slotrange}")


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='graphql', type=click.Choice(['graphql']), help="Output format")
def cli(yamlfile, format):
    """ Generate graphql representation of a biolink model """
    print(GraphqlGenerator(yamlfile, format).serialize())
