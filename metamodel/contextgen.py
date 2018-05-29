"""Generate JSON-LD contexts

"""

import json
import logging
from typing import Union

from prefixcommons import curie_util as cu

from metamodel.metamodel import SchemaDefinition, SlotDefinition, ClassDefinition
from metamodel.utils.formatutils import camelcase, underscore

# highest to lowest priority
default_curie_maps = [cu.read_biocontext('obo_context'), cu.read_biocontext('monarch_context'),
                      cu.read_biocontext('idot_context'), cu.read_biocontext('semweb_context')]


class ContextGenerator:
    def __init__(self, schema: SchemaDefinition) -> None:
        self.schema = schema
        self.prefixmap = None
        
    def serialize(self, _='json', **args):
        self.prefixmap = {
            "id": "@id",
            "type": {
                "@id": "rdf:type",
                "@type": "@id"
            }
        }
        self.tr(**args)
        c = {"@context": self.prefixmap,
             "comments":
             """
             This JSON-LD context file is generated automatically using the biolink-model yaml spec,
             plus standard prefix expansions from https://github.com/prefixcommons/biocontext
             """}
        return json.dumps(c, sort_keys=True, indent=4)
    
    def tr(self, _=None):
        # create list of class names
        for cn, cls in self.schema.classes.items():
            logging.info("Cls: {}".format(cn))
            self.tr_element(cls, camelcase(cn))
        for sn, slot in self.schema.slots.items():
            self.tr_element(slot, underscore(sn))
            # hold off til we are sure curie_util can handle this
            # rewrite to be an object with id/type fields
            # if n in pm:
            #    iri = pm[n]
            #    pm[n] = { "@id" : iri, "@type" : "@id" }

    def tr_element(self, e: Union[SlotDefinition, ClassDefinition], n: str):
        # subClassOf has highest priority
        if isinstance(e, ClassDefinition) and e.subclass_of is not None:
            self.add_mapping(n, e.subclass_of)
        for m in e.mappings:
            self.add_mapping(n, m)
        # ensure that all declared ID prefixes have an entry in the context
        for px in e.id_prefixes:
            self.add_mapping(px, px+":")
        # anything else, place in bioentity space
        if n not in self.prefixmap:
            self.add_mapping(n, "http://bioentity.io/vocab/"+n)

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
