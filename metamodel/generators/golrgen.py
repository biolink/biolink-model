"""
Generate GOlr YAML schema definitions.

These can be converted to solr schema-xml, and used in amigo-bbop tools

See the golr-views directory in this repo for examples

"""
import os
from typing import Union, TextIO, List, Optional

import click
from dataclasses import dataclass

from metamodel.utils.generator import Generator
from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition
from metamodel.utils.metamodelcore import empty_list
from metamodel.utils.formatutils import underscore
from metamodel.utils.yamlutils import YAMLRoot, as_yaml


@dataclass
class GOLRField(YAMLRoot):
    id: str
    description: str
    display_name: str
    property: List = empty_list()
    cardinality: Optional[str] = None


@dataclass
class GOLRClass(YAMLRoot):
    id: str
    schema_generating: bool
    description: str
    display_name: str
    document_category: str
    weight: int
    fields: List[GOLRField] = empty_list()


class GolrSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = "[golr]"
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='csv') -> None:
        super().__init__(schema, fmt)
        self.dirname: str = None
        self.class_obj: GOLRClass = None

    def visit_schema(self, dirname: str) -> None:
        self.dirname = dirname
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        # write_golr_yaml_to_dir(schema, dir)

    def visit_class(self, cls: ClassDefinition) -> bool:
        if not cls.abstract:
            self.class_obj = GOLRClass(id=underscore(cls.name),
                                       schema_generating=True,
                                       description=cls.description,
                                       display_name=cls.name,
                                       document_category=cls.name,
                                       weight=20)
            return True
        else:
            return False

    def end_class(self, cls: ClassDefinition) -> None:
        fn = os.path.join(self.dirname, underscore(cls.name + '-config.yaml'))
        with open(fn, 'w') as f:
            f.write(as_yaml(self.class_obj))

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        field = GOLRField(id=underscore(aliased_slot_name), description=slot.description, display_name=slot.name)
        if slot.multivalued:
            field.cardinality = 'multi'
        self.class_obj.fields.append(field)


@click.command()
@click.option("--dir", "-d", default='golr-views', help="Output directory")
@click.argument("file", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='golr', type=click.Choice(['golr']), help="Output format")
def cli(file, dir, format):
    """ Generate GOLR representation of a biolink model """
    print(GolrSchemaGenerator(file, format).serialize(dirname=dir))

