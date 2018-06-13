""" Generate JSONld

"""
import os
from typing import Union, TextIO

import click
from jsonasobj import as_json, loads

from metamodel.metamodel import SchemaDefinition
from metamodel.utils.generator import Generator

biolink_context = "https://github.com/hsolbrig/biolink-model/raw/master/context.jsonld"
meta_context = "https://raw.githubusercontent.com/hsolbrig/biolink-model/master/metamodel/context.jsonld"


class JSONLDGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['jsonld']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'jsonld') -> None:
        super().__init__(schema, fmt)

    def end_schema(self, context: str = biolink_context) -> None:
        json_str = as_json(self.schema)
        json_obj = loads(json_str)
        json_obj["@context"] = context
        print(as_json(json_obj))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='jsonld', type=click.Choice(['jsonld']), help="Output format")
@click.option("--context", default=biolink_context, help="JSONLD context file (default: biolink context.jsonld)")
def cli(yamlfile, format, context):
    """ Generate JSONLD file from biolink schema """
    print(JSONLDGenerator(yamlfile, format).serialize(context=context))
