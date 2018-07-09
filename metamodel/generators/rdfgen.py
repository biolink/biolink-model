"""Generate RDF

"""
import os
from typing import Union, TextIO, Optional

import click
from rdflib import Graph
from rdflib.plugin import plugins as rdflib_plugins, Parser as rdflib_Parser

from metamodel.generators.jsonldgen import JSONLDGenerator, biolink_context
from metamodel.metamodel import SchemaDefinition
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import BIOENTITY, META


class RDFGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = [x.name for x in rdflib_plugins(None, rdflib_Parser) if '/' not in str(x.name)]
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'ttl') -> None:
        super().__init__(schema, fmt)

    def _data(self, g: Graph) -> str:
        return g.serialize(format='turtle' if self.format == 'ttl' else self.format).decode()

    def end_schema(self, output: Optional[str], context: str=biolink_context) -> None:
        jsonld_str = JSONLDGenerator(self.schema).serialize(context=context)
        graph = Graph()
        # TODO: retrieve the base out of the JSON_LD (generalize how it is fetched from the schema when generating
        # context
        graph.parse(data=jsonld_str, format="json-ld", base="http://bioentity.io/vocab/")
        if output:
            with open(output, 'w') as outf:
                outf.write(self._data(graph))
        else:
            print(self._data(graph))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='ttl', type=click.Choice(RDFGenerator.valid_formats),
              help="Output format")
@click.option("-o", "--output", help="Output file name")
@click.option("--context", default=biolink_context, help="JSONLD context file (default: biolink context.jsonld)")
def cli(yamlfile, format, output, context):
    """ Generate an RDF representation of a biolink model """
    print(RDFGenerator(yamlfile, format).serialize(output=output, context=context))
