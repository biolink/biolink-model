"""Generate OWL ontology corresponding to information model

model classes are translated to OWL classes, slots to OWL properties.
"""
import logging
import os
from typing import List, Union, TextIO

import click
from rdflib import Graph, URIRef, RDF, OWL, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import DCTERMS, RDFS, XSD
from rdflib.plugin import plugins as rdflib_plugins, Parser as rdflib_Parser

from metamodel.metamodel import ClassDefinitionName, SchemaDefinition, ClassDefinition, SlotDefinitionName, \
    TypeDefinitionName, SlotDefinition
from metamodel.utils.builtins import builtin_names
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import BIOENTITY, OBO, META


class OwlSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = List(x.name for x in rdflib_plugins(None, rdflib_Parser) if '/' not in str(x.name))

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'turtle') -> None:
        super().__init__(schema, fmt)
        self.graph: Graph = None

    def visit_schema(self):
        # TODO: Is it even possible to have a schema without an ID?
        base = URIRef(self.schema.id) if self.schema.id else self.class_uri(self.schema.name)
        self.graph = Graph(identifier=base)
        self.graph.bind("obo", str(OBO))
        self.graph.add((base, RDF.type, OWL.Ontology))
        self.graph.add((base, RDF.type, OWL.Ontology))
        self.graph.label(base, Literal(self.schema.name))
        if self.schema.description:
            self.graph.add((base, DCTERMS.description, Literal(self.schema.description)))
        if self.schema.license:
            self.graph.add((base, DCTERMS.license, Literal(self.schema.license)))
        else:
            logging.warning("No license!")

    def visit_class(self, cls: ClassDefinition) -> bool:
        cls_uri = self.class_uri(cls.name)
        self.graph.add((cls_uri, RDF.type, OWL.Class))
        self.graph.label(cls_uri, cls.name)

        # Parent classes
        if cls.is_a and not cls.defining_slots:
            self.graph.add((cls_uri, RDFS.subClassOf, self.class_uri(cls.is_a)))
        if cls.abstract:
            self.graph.add((cls_uri, RDFS.subClassOf, META.abstract))
        if cls.mixin:
            self.graph.add((cls_uri, RDFS.subClassOf, META.mixin))
        for mixin in cls.mixins:
            self.graph.add((cls_uri, RDFS.subClassOf, self.class_uri(mixin)))
        # TODO: Add apply_to injections

        # Defining slots give us an equivalent class
        if cls.defining_slots:
            x = BNode()
            self.graph.add((cls_uri, OWL.equivalentClass, x))
            xl = BNode()
            self.graph.add((x, OWL.intersectionOf, xl))

            elts = []
            if cls.is_a:
                elts.append(self.class_uri(cls.is_a))
            for slotname in cls.defining_slots:
                slot = self.schema.slots[slotname]
                if slot.range in builtin_names:
                    prop_type = XSD[slot]
                elif slot.range in self.schema.types:
                    prop_type = self.type_uri(slot.range)
                else:
                    prop_type = self.class_uri(slot.range)
                restr = BNode()
                self.graph.add((cls_uri, RDFS.subClassOf, restr))
                self.graph.add((restr, RDF.type, OWL.Restriction))
                self.graph.add((restr, OWL.onProperty, self.prop_uri(slot.name)))
                # TODO: Look up data values restriction
                self.graph.add((restr, OWL.someValuesFrom, prop_type))
                elts.append(restr)
            equ_bnode = BNode()
            self.graph.add((cls_uri, OWL.equivalentClass, equ_bnode))
            Collection(self.graph, equ_bnode, elts)

        return True

    @staticmethod
    def class_uri(cn: ClassDefinitionName) -> URIRef:
        return BIOENTITY[camelcase(cn)]

    @staticmethod
    def prop_uri(pn: SlotDefinitionName) -> URIRef:
        return BIOENTITY[underscore(pn)]
    
    @staticmethod
    def type_uri(tn: TypeDefinitionName) -> URIRef:
        return BIOENTITY[underscore(tn)]

    def visit_slot(self, slot_name: str, slot: SlotDefinition) -> None:
        """ Add a slot definition per slot

        @param slot_name:
        @param slot:
        @return:
        """
        # Note: We use the raw name in OWL and add a subProperty arc
        slot_uri = self.prop_uri(slot.name)

        # Parent slots
        if slot.is_a:
            self.graph.add((slot_uri, RDFS.subPropertyOf, self.class_uri(slot.is_a)))
        if slot.abstract:
            self.graph.add((slot_uri, RDFS.subPropertyOf, META.abstract))
        if slot.mixin:
            self.graph.add((slot_uri, RDFS.subPropertyOf, META.mixin))
        for mixin in slot.mixins:
            self.graph.add((slot_uri, RDFS.subPropertyOf, self.class_uri(mixin)))

        # Slot range
        if slot.range in builtin_names:
            self.graph.add((slot_uri, RDF.type, OWL.DatatypeProperty))
            self.graph.add((slot_uri, RDFS.range, XSD[slot.range]))
        elif slot.range in self.schema.types:
            self.graph.add((slot_uri, RDF.type, OWL.DatatypeProperty))
            self.graph.add((slot_uri, RDFS.range, self.type_uri(slot.range)))
        else:
            self.graph.add((slot_uri, RDF.type, OWL.ObjectProperty))
            self.graph.add((slot_uri, RDFS.range, self.class_uri(slot.range)))

        # Slot domain
        self.graph.add((slot_uri, RDFS.domain, self.class_uri(slot.domain)))

        # Annotations
        self.graph.label(slot_uri, slot.name)
        if slot.description:
            self.graph.add((slot_uri, DCTERMS.description, Literal(slot.description)))
            self.graph.add((slot_uri, OBO.IAO_0000115, Literal(slot.description)))


@click.command()
@click.argument("yamlfile", type=click.File('r'))
@click.option("--format", "-f", default='rdf', type=click.Choice(OwlSchemaGenerator.valid_formats),
              help="Output format")
def cli(yamlfile, format):
    """ Generate an OWL representation of a biolink model """
    print(OwlSchemaGenerator(yamlfile, format).serialize())
