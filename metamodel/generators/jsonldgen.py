""" Generate JSONld

"""
import os
from typing import Union, TextIO, Dict, Any, List, Set, Optional

import click
from jsonasobj import as_json, loads, JsonObj, as_dict

from metamodel.metamodel import SchemaDefinition, ClassDefinitionName, SlotDefinitionName, TypeDefinitionName, \
    ElementName
from metamodel.utils.builtins import builtin_names, builtin_uri
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.yamlutils import YAMLRoot

biolink_context = "https://github.com/hsolbrig/biolink-model/raw/master/context.jsonld"
meta_context = "https://raw.githubusercontent.com/hsolbrig/biolink-model/master/metamodel/context.jsonld"


class JSONLDGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['jsonld']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'jsonld') -> None:
        super().__init__(schema, fmt)

    def _visit(self, node: Any) -> Optional[Any]:
        """ Traverse the schema looking for Class / Slot / Type definition references, converting the names
        to the RDF format

        @param node: Any node in a schema
        @return: Replacement node if required
        """
        if isinstance(node, (YAMLRoot, dict)):
            if isinstance(node, YAMLRoot):
                node = node.__dict__
            for k, v in list(node.items()):
                if v:
                    new_v = self._visit(v)
                    if new_v is not None:
                        node[k] = new_v
        elif isinstance(node, list):
            for i in range(0, len(node)):
                new_v = self._visit(node[i])
                if new_v is not None:
                    node[i] = new_v
        elif isinstance(node, set):
            for v in list(node):
                new_v = self._visit(v)
                if new_v is not None:
                    node.remove(v)
                    node.add(new_v)
        elif isinstance(node, ClassDefinitionName):
            return ClassDefinitionName(camelcase(node))
        elif isinstance(node, SlotDefinitionName):
            return SlotDefinitionName(underscore(node))
        elif isinstance(node, TypeDefinitionName):
            return TypeDefinitionName(underscore(node))
        elif isinstance(node, ElementName):
            return ClassDefinitionName(camelcase(node)) if node in self.schema.classes else \
                SlotDefinitionName(underscore(node)) if node in self.schema.slots else \
                TypeDefinitionName(underscore(node)) if node in self.schema.types else \
                builtin_uri(str(node)) if str(node) in builtin_names else None
        elif str(node) in builtin_names:
            return builtin_uri(str(node))
        return None

    def end_schema(self, context: str = biolink_context) -> None:
        self._visit(self.schema)
        json_str = as_json(self.schema)
        json_obj = loads(json_str)
        json_obj["@context"] = context
        json_obj["@id"] = self.schema.id
        print(as_json(json_obj))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='jsonld', type=click.Choice(['jsonld']), help="Output format")
@click.option("--context", default=biolink_context, help="JSONLD context file (default: biolink context.jsonld)")
def cli(yamlfile, format, context):
    """ Generate JSONLD file from biolink schema """
    print(JSONLDGenerator(yamlfile, format).serialize(context=context))
