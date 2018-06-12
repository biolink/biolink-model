"""Generate JSON-LD contexts

"""

import json
import logging
import os
from typing import Union, TextIO

import click
from prefixcommons import curie_util as cu

from metamodel.utils.generator import Generator
from metamodel.metamodel import SchemaDefinition, SlotDefinition, ClassDefinition
from metamodel.utils.namespaces import BIOENTITY
from metamodel.utils.formatutils import be

# highest to lowest priority
default_curie_maps = [cu.read_biocontext('obo_context'), cu.read_biocontext('monarch_context'),
                      cu.read_biocontext('idot_context'), cu.read_biocontext('semweb_context')]


class ContextGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['json']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='json') -> None:
        super().__init__(schema, fmt)
        self.prefixmap = {
            "id": "@id",
            "type": {
                "@id": "rdf:type",
                "@type": "@id"
            }
        }

    def end_schema(self) -> None:
        comments = f'''Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
Generation date: {self.schema.generation_date}
Schema: {self.schema.name}

id: {self.schema.id}
description: {be(self.schema.description)}
license: {be(self.schema.license)}
'''
        context = {"@context": self.prefixmap,
                   "comments": comments
                   }
        print(json.dumps(context, sort_keys=True, indent=4))

    def visit_class(self, cls: ClassDefinition) -> bool:
        logging.info("Cls: {}".format(cls.name))
        # subClassOf has highest priority
        cn = cls.name
        if cls.subclass_of is not None:
            self.add_mapping(cn, cls.subclass_of)
        self.tr_element(cls, cn)
        return True

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if not slot.alias:
            self.tr_element(slot, slot.name)
        # hold off til we are sure curie_util can handle this
        # rewrite to be an object with id/type fields
        # if n in pm:
        #    iri = pm[n]
        #    pm[n] = { "@id" : iri, "@type" : "@id" }

    def tr_element(self, e: Union[SlotDefinition, ClassDefinition], n: str):
        for m in e.mappings:
            self.add_mapping(n, m)
        # ensure that all declared ID prefixes have an entry in the context
        for px in e.id_prefixes:
            self.add_mapping(px, px+":")
        # anything else, place in bioentity space
        if n not in self.prefixmap:
            self.add_mapping(n, str(BIOENTITY)+n)

    @staticmethod
    def get_uri(shorthand):
        uri = cu.expand_uri(shorthand, default_curie_maps)
        if not uri.startswith('http'):
            return None
        else:
            return uri
        
    def add_mapping(self, shorthand, exp):
        if shorthand in self.prefixmap:
            logging.debug("Ignoring {}->{}".format(shorthand, exp))
            return
        uri = self.get_uri(exp)
        if uri is None:
            logging.error("No expansion for {}".format(exp))
        else:
            logging.info("Adding {} -> {} via {}".format(shorthand, uri, exp))
            self.prefixmap[shorthand] = uri

        # if we expand something like Disease=>MONDO:0000001, ensure MONDO prefix
        # is also added
        if uri is not None and uri != exp:
            parts = exp.split(":", 1)
            pfx = parts[0]
            if pfx not in self.prefixmap and not pfx.startswith("http"):
                pfx_uri = self.get_uri(pfx + ":")
                if pfx_uri is not None:
                    self.prefixmap[pfx] = pfx_uri


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='json', type=click.Choice(['json']), help="Output format")
def cli(yamlfile, format):
    """ Generate jsonld @context definition from biolink model """
    print(ContextGenerator(yamlfile, format).serialize())
