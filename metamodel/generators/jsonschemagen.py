import os
from typing import Union, TextIO

import click
from jsonasobj import JsonObj, as_json

from metamodel.utils.generator import Generator
from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition
from metamodel.utils.formatutils import camelcase, be, underscore


class JsonSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = "[json]"
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='json') -> None:
        super().__init__(schema, fmt)
        self.schemaobj: JsonObj = None
        self.clsobj: JsonObj = None
        self.inline = False
        # JSON-Schema does not have inheritance,
        # so we duplicate slots from inherited parents and mixins
        self.visit_all_slots = True

    def visit_schema(self, inline: bool=False, **kwargs) -> None:
        self.inline = inline
        self.schemaobj = JsonObj(title=self.schema.name,
                                 type="object",
                                 properties=JsonObj(),
                                 definitions=JsonObj())
        self.schemaobj['$schema'] = "http://json-schema.org/draft-04/schema#"
        self.schemaobj['$id'] = self.schema.id

    def end_schema(self, **kwargs) -> None:
        print(as_json(self.schemaobj, sort_keys=True))

    def visit_class(self, cls: ClassDefinition) -> bool:
        if cls.abstract:
            return False
        self.clsobj = JsonObj(title=camelcase(cls.name),
                              type='object',
                              properties=JsonObj(),
                              description=be(cls.description))
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        self.schemaobj.properties[camelcase(cls.name)] = self.clsobj

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if self.inline:
            # If inline we have to include redefined slots
            prop = JsonObj(type=JsonObj())
            prop.type['$ref'] = self.jref(underscore(slot.name))
        elif slot.multivalued:
            prop = JsonObj(type="array", items=self.type_or_ref(slot.range))
        else:
            prop = JsonObj(type="string")
        if slot.description:
            prop.description = slot.description
        if slot.required:
            prop.required = True
        self.clsobj.properties[underscore(aliased_slot_name)] = prop

    def visit_slot(self, slot_name: str, slot: SlotDefinition) -> None:
        # Don't emit redefined slots unless we are inlining
        if slot_name == slot.name or self.inline:
            defn = JsonObj(type="array", items=self.type_or_ref(slot.range)) if slot.multivalued \
                   else self.type_or_ref(slot.range)
            if slot.description:
                defn.description = slot.description
            self.schemaobj.definitions[underscore(slot.name)] = defn


    @staticmethod
    def type_or_ref(rng: str) -> JsonObj:
        # TODO jref
        return JsonObj(type="string")

    @staticmethod
    def jref(slot_name: str) -> str:
        return f"#/definitions/{slot_name}"


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("-i", "--inline", is_flag=True, help="Generate references to types rather than inlining them")
@click.option("--format", "-f", default='json', type=click.Choice(['json']), help="Output format")
def cli(yamlfile, inline, format):
    """ Generate JSON Schema representation of a biolink model """
    print(JsonSchemaGenerator(yamlfile, format).serialize(inline=inline))
