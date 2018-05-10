"""Generate JSON-LD contexts

"""


import yaml
import logging

from .manager import *
from .generator import Generator
from prefixcommons import curie_util as cu
import json

# highest to lowest priority
default_curie_maps = [cu.read_biocontext('obo_context'), cu.read_biocontext('monarch_context'), cu.read_biocontext('idot_context')]

class ContextGenerator(Generator):
        
    def serialize(self, format='json', **args):
        self.prefixmap = {}
        self.tr(**args)
        c = {"@context": self.prefixmap,
             "comments":
             """
             This JSON-LD context file is generated automatically using the biolink-model yaml spec,
             plus standard prefix expansions from https://github.com/prefixcommons/biocontext
             """}
        return json.dumps(c, sort_keys=True, indent=4)
    
    def tr(self, roots=None):
        schema = self.schema
        mgr = self.manager
        
        # create list of class names
        for c in schema.classes:
            logging.info("Cls: {}".format(c))
            self.tr_element(c, mgr.class_name(c))
        for s in schema.slots:
            self.tr_element(s, mgr.slot_name(s))


    def tr_element(self, e, n):
        schema = self.schema
        mgr = self.manager
        # subClassOf has highest priority
        if isinstance(e, ClassDefinition) and e.subclass_of is not None:
            self.add_mapping(n, e.subclass_of)
        mappings = e.mappings
        if mappings is not None:
            for m in mappings:
                self.add_mapping(n, m)
        # ensure that all declared ID prefixes have an entry in the context
        if e.id_prefixes:
            for px in e.id_prefixes:
                self.add_mapping(px, px+":")

    def get_uri(self, shorthand):
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
            self.prefixmap[shorthand] = uri
