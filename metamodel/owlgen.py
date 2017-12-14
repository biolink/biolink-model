"""Generate RDFS/OWL definitions


"""

#from prefixcommons import curie_util
#from prefixcommons.curie_util import contract_uri, expand_uri, get_prefixes
from rdflib import Namespace
from rdflib import BNode
from rdflib import Literal
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import OWL
import rdflib
import logging
import uuid

#prefix_context = {key: value for context in curie_util.default_curie_maps + [curie_util.read_biocontext("minerva_context")] for key, value in context.items()}

OBO = Namespace("http://purl.obolibrary.org/obo/")

from .schemautils import *

def write_owl(schema, fn):
    gen = OwlSchemaGenerator()
    gen.tr(schema)
    gen.serialize(fn)

class OwlSchemaGenerator(object):
    
    def __init__(self):
        pass

    def serialize(self, destination=None, format='ttl', **args):
        #self.graph.add((self.base, RDFS.label, Literal(str(destination.name))))
        self.graph.serialize(destination, format, **args)
    
    def tr(self, schema):
        self.schema = schema
        self.base = URIRef("http://bioentity.io/schema/{}".format(get_class_name(schema.name)))
        self.graph = rdflib.Graph(identifier=self.base)
        self.graph.bind("owl", OWL)
        self.graph.bind("obo", "http://purl.obolibrary.org/obo/")
        self.graph.add((self.base, RDF.type, OWL.Ontology))

        for c in schema.classes:
            self.tr_class(c)
        for c in schema.slots:
            self.tr_slot(c)

    def uri(self, id):
        return URIRef("http://bioentity.io/vocab/{}".format(id))

    def class_uri(self, cn):
        cn = get_class_name(cn)
        return self.uri(cn)

    def property_uri(self, pn):
        pn = underscore_style(pn)
        return self.uri(pn)
        
    
    def tr_class(self, c):
        g = self.graph

        ci = self.class_uri(c.name)
        self._tr_element(c, ci)
        g.add((ci, RDF.type, OWL.Class))
        g.add((ci, RDFS.label, Literal(c.name)))
        if c.is_a:
            g.add((ci, RDFS.subClassOf, self.class_uri(c.is_a)))
        if c.mixins:
            for m in c.mixins:
                g.add((ci, RDFS.subClassOf, self.class_uri(m)))
        if c.slots:
            for sn in c.slots:
                srange = get_slot_range(sn, self.schema)
                if srange:
                    restr = BNode()
                    g.add((ci, RDFS.subClassOf, restr))
                    g.add((restr, OWL.onProperty, self.property_uri(sn)))
                    g.add((restr, OWL.someValuesFrom, self.class_uri(sn)))
        
    def tr_slot(self, s):
        g = self.graph

        p = self.property_uri(s.name)
        self._tr_element(s, p)
        g.add((p, RDF.type, OWL.ObjectProperty))
        g.add((p, RDFS.label, Literal(s.name)))
        if s.is_a:
            g.add((p, OWL.subObjectPropertyOf, self.property_uri(s.is_a)))
        if s.domain:
            g.add((p, RDFS.domain, self.class_uri(s.domain)))
        if s.range:
            g.add((p, RDFS.domain, self.class_uri(s.range)))
        

    def _tr_element(self, e, uri):
        g = self.graph
        if e.description:
            g.add((uri, OBO.IAO_0000115, Literal(e.description)))
                  
