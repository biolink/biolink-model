"""Generate CSVs

"""
import os
import sys
from csv import DictWriter
from typing import List, Union, TextIO, Set

import click

from metamodel.metamodel import ClassDefinition, ClassDefinitionName, SchemaDefinition
from metamodel.utils.formatutils import underscore, be
from metamodel.utils.generator import Generator


class CsvGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['csv', 'tsv']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='csv') -> None:
        super().__init__(schema, fmt)
        self.sep: str = None
        self.closure: Set[ClassDefinitionName] = None
        self.writer: DictWriter = None
        
    def visit_schema(self, classes: List[ClassDefinitionName]=None) -> None:
        self.closure = set()
        for clsname in classes:
            if clsname not in self.schema.classes:
                raise ValueError(f"Unrecognized class: {clsname}")
            else:
               self.closure.update(self.ancestors(clsname))

        dialect: str = "excel" if self.format == 'csv' else "excel-tab"
        self.writer = DictWriter(sys.stdout, ['id', 'mappings', 'description'], dialect=dialect)
        self.writer.writeheader()

    def visit_class(self, cls: ClassDefinition) -> bool:
        if not self.closure or cls.name in self.closure:
            self.writer.writerow({'id': underscore(cls.name),
                                  'mappings': "|".join(cls.mappings),
                                  'description': be(cls.description)})
            return True
        return False


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--root", "-r", default=None, multiple=True, help="Class(es) to transform")
@click.option("--format", "-f", default='csv', type=click.Choice(['csv', 'tsv']), help="Output format")
def cli(yamlfile, root, format):
    """ Generate CSV/TSV file from biolink model """
    print(CsvGenerator(yamlfile, format).serialize(classes=root))
