"""Generate OWL ontology corresponding to information model

model classes are translated to OWL classes, slots to OWL properties.
"""

from rdflib import Namespace
from rdflib import BNode
from rdflib import Literal
from rdflib import URIRef
from rdflib.collection import Collection
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import OWL
from rdflib.namespace import SKOS
from rdflib.namespace import XSD
import rdflib
import logging
import uuid

from .generator import Generator
from .metamodel import ClassDefinition, SlotDefinition

OBO = Namespace("http://purl.obolibrary.org/obo/")
DCTERMS = Namespace("http://purl.org/dc/terms/")
META = Namespace("http://bioentity.io/meta/")
BIOTOP = Namespace("http://purl.org/biotop/biotop.owl#")

from .schemautils import *

def write_owl(schema, fn):
    gen = OwlSchemaGenerator(schema=schema)
    gen.tr()
    gen.serialize(fn)

class OwlSchemaGenerator(Generator):

    def serialize(self, destination=None, format='turtle', **args):
        #self.graph.add((self.base, RDFS.label, Literal(str(destination.name))))
        self.graph.serialize(destination, format, **args)
    
    def tr(self):
        schema = self.schema
        if schema.id:
            self.base = URIRef(schema.id)
        else:
            self.base = URIRef("http://bioentity.io/schema/{}".format(get_class_name(schema.name)))
        self.graph = rdflib.Graph(identifier=self.base)
        self.graph.bind("owl", OWL)
        self.graph.bind("obo", "http://purl.obolibrary.org/obo/")
        self.graph.add((self.base, RDF.type, OWL.Ontology))

        if schema.name:
            self.graph.add((self.base, RDFS.label, Literal(schema.name)))
        if schema.description:
            self.graph.add((self.base, DCTERMS.description, Literal(schema.description)))
        if schema.license:
            self.graph.add((self.base, DCTERMS.license, Literal(schema.license)))
        else:
            logging.warn("No license!")
            
        for c in schema.classes:
            self.tr_class(c)
        for c in schema.slots:
            self.tr_slot(c)

    def uri(self, id):
        return URIRef("http://bioentity.io/vocab/{}".format(id))

    def class_uri(self, cn, create=True):
        if cn is None:
            logging.error("No class name: {}".format(cn))
        c = self.manager.classdef(cn)
        if c is None:
            if not create:
                raise ValueError("no such class {}".format(cn))
            c = ClassDefinition(name=cn)
            logging.error("Created placeholder: {}".format(c))

        cn = self.manager.class_name(c)
        return self.uri(cn)

    def property_uri(self, pn, create=True, c=None):
        p = self.manager.slotdef(pn, c)
        if p is None:
            logging.error("No such slot: {}".format(pn))
            if not create:
                raise ValueError("no such class {}".format(pn))
            p = SlotDefinition(name=pn)

        pn = self.manager.slot_name(p)
        return self.uri(pn)
    
    def tr_class(self, c):
        """
        Translate metamodel class to OWL Class
        """
        mgr = self.manager
        g = self.graph

        ci = self.class_uri(c.name)
        self._tr_element(c, ci)
        g.add((ci, RDF.type, OWL.Class))
        g.add((ci, RDFS.label, Literal(c.name)))
        if c.mixin:
            g.add((ci, RDFS.subClassOf, META.Mixin))
        if c.abstract:
            g.add((ci, RDFS.subClassOf, META.Abstract))
        if c.is_a:
            g.add((ci, RDFS.subClassOf, self.class_uri(c.is_a)))
        if c.mixins:
            for m in c.mixins:
                g.add((ci, RDFS.subClassOf, self.class_uri(m)))
        slots = mgr.class_slotdefs(c, True, True)
        mappings = c.mappings
        if mappings is None:
            if c.subclass_of:
                mappings = [c.subclass_of]
        if mappings:
            # TODO: use geneal
            for m in mappings:
                uri = self.class_uri(m)
                if ':' in m:
                    uri = URIRef(self.id_to_url(m))
                #g.add((ci, BIOTOP.isAbout, uri))                    
                g.add((ci, SKOS.exactMatch, uri))
                #g.add((ci, OWL.equivalentClass, uri))
        for sn in slots:
            s = mgr.slotdef(sn, c)
            slot_range = self.get_range_for_class_slot(c, s)
            if slot_range:
                restr = BNode()
                g.add((ci, RDFS.subClassOf, restr))
                g.add((restr, RDF.type, OWL.Restriction))
                g.add((restr, OWL.onProperty, self.property_uri(sn)))
                g.add((restr, OWL.someValuesFrom, slot_range))

        if c.defining_slots:
            x = BNode()
            g.add((ci, OWL.equivalentClass, x))
            xl = BNode()
            g.add((x, OWL.intersectionOf, xl))
            elts = []
            if c.is_a:
                elts.append(self.class_uri(c.is_a))
            for sn in c.defining_slots:
                logging.info("Defining slot for {} = {}".format(c.name, sn))
                s = mgr.slotdef(sn, c)
                p = self.property_uri(s, False, c)
                slot_range = self.get_range_for_class_slot(c, s)
                if slot_range:
                    restr = BNode()
                    g.add((ci, RDFS.subClassOf, restr))
                    g.add((restr, RDF.type, OWL.Restriction))
                    g.add((restr, OWL.onProperty, self.property_uri(sn)))
                    g.add((restr, OWL.someValuesFrom, slot_range))
                    elts.append(restr)
            c = Collection(g, xl, elts)
            
                
                
    def get_range_for_class_slot(self, c, s):
        mgr = self.manager
        g = self.graph
        srange = mgr.class_slot_range(c, s)
        if srange:
            return self.get_filler(srange)

    def get_filler(self, srange):
        mgr = self.manager
        g = self.graph
        # represent as existential restrictions
        if mgr.typedef(srange):
            t = mgr.typedef(srange)
            typeof = t.typeof
            xtype = XSD.string
            if typeof == 'string':
                xtype = XSD.string
            elif typeof == 'time':
                xtype = XSD.time
            else:
                logging.warn("Unknown type: {}".format(typeof))
            return xtype
        else:
            if srange.startswith('xsd:'):
                return URIRef(srange.replace('xsd:','http://www.w3.org/2001/XMLSchema#'))
            else:
                return self.class_uri(srange)
        
        
    def tr_slot(self, s):
        g = self.graph

        p = self.property_uri(s.name)
        self._tr_element(s, p)
        g.add((p, RDF.type, OWL.ObjectProperty))
        g.add((p, RDFS.label, Literal(s.name)))
        if s.is_a:
            g.add((p, OWL.subObjectPropertyOf, self.property_uri(s.is_a)))
        if s.domain:
            g.add((p, RDFS.domain, self.get_filler(s.domain)))
        if s.range:
            g.add((p, RDFS.range, self.get_filler(s.range)))
        

    def _tr_element(self, e, uri):
        g = self.graph
        if e.description:
            g.add((uri, OBO.IAO_0000115, Literal(e.description)))
                  
