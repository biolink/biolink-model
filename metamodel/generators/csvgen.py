"""Generate CSVs

"""
import os
import sys
from csv import DictWriter
from typing import List, Union, TextIO

import click

from metamodel.utils.generator import Generator
from metamodel.metamodel import ClassDefinition, ClassDefinitionName, SchemaDefinition
from metamodel.utils.formatutils import underscore, be


class CsvGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['csv', 'tsv']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='csv') -> None:
        super().__init__(schema, fmt)
        self.sep = None
        self.closure = None
        self.writer = None
        
    def visit_schema(self, root: List[ClassDefinitionName]=None) -> None:
        roots = [] if root is None else list(root)
        self.closure = self.root_closure(roots)
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
@click.argument("yamlfile", type=click.File('r'))
@click.option("--root", "-r", default=None, multiple=True, help="Class(es) to transform")
@click.option("--format", "-f", default='csv', type=click.Choice(['csv', 'tsv']), help="Output format")
def cli(yamlfile, root, format):
    """ Generate CSV/TSV file from biolink model """
    print(CsvGenerator(yamlfile, format).serialize(root=root))
