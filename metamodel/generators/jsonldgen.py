""" Generate JSONld

"""
import os
from typing import Union, TextIO, Any, Optional
from urllib.parse import urljoin
from urllib.request import pathname2url

import click
from jsonasobj import as_json, loads

from metamodel.metamodel import SchemaDefinition, ClassDefinitionName, SlotDefinitionName, TypeDefinitionName, \
    ElementName, SlotDefinition, ClassDefinition
from metamodel.utils.builtins import builtin_names, builtin_uri, Builtin
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

    def adjust_slot(self, slot: SlotDefinition) -> None:
        if slot.range in self.schema.classes:
            slot.range = ClassDefinitionName(camelcase(slot.range))
        elif slot.range in self.schema.slots:
            slot.range = SlotDefinitionName(underscore(slot.range))
        elif slot.range in self.schema.types:
            slot.range = TypeDefinitionName(underscore(slot.range))
        elif slot.range in (Builtin.uri, Builtin.anytype):
            slot.range = '@id'
        elif slot.range in builtin_names and builtin_names[slot.range] not in (Builtin.anytype, Builtin.uri):
            slot.range = builtin_uri(slot.range)

    def visit_class(self, cls: ClassDefinition) -> bool:
        self._visit(cls)
        for slot_usage in cls.slot_usage.values():
            self.adjust_slot(slot_usage)
        return False

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        self._visit(slot)
        self.adjust_slot(slot)

    def end_schema(self, context: str = biolink_context) -> None:
        # self._visit(self.schema)
        json_str = as_json(self.schema)
        json_obj = loads(json_str)
        if '://' not in context:
            context = urljoin('file:', pathname2url(os.path.abspath(context)))
        base_prefix = self.default_uri()
        json_obj["@context"] = [context, {'@base': base_prefix}] if base_prefix else context
        json_obj["@id"] = self.schema.id
        print(as_json(json_obj, indent="  "))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='jsonld', type=click.Choice(['jsonld']), help="Output format")
@click.option("--context", default=biolink_context, help="JSONLD context file (default: biolink context.jsonld)")
def cli(yamlfile, format, context):
    """ Generate JSONLD file from biolink schema """
    print(JSONLDGenerator(yamlfile, format).serialize(context=context))
