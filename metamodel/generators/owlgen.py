"""Generate OWL ontology corresponding to information model

model classes are translated to OWL classes, slots to OWL properties.
"""
import logging
import os
from typing import Union, TextIO, Optional

import click
from rdflib import Graph, URIRef, RDF, OWL, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import DCTERMS, RDFS
from rdflib.plugin import plugins as rdflib_plugins, Parser as rdflib_Parser

from metamodel.metamodel import ClassDefinitionName, SchemaDefinition, ClassDefinition, SlotDefinitionName, \
    TypeDefinitionName, SlotDefinition
from metamodel.utils.builtins import builtin_names, builtin_uri
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import BIOENTITY, OBO, META


class OwlSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = [x.name for x in rdflib_plugins(None, rdflib_Parser) if '/' not in str(x.name)]

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'ttl') -> None:
        super().__init__(schema, fmt)
        self.graph: Graph = None

    def visit_schema(self, output: Optional[str]):
        # TODO: Is it even possible to have a schema without an ID?
        base = URIRef(self.schema.id) if self.schema.id else self.class_uri(self.schema.name)
        self.graph = Graph(identifier=base)
        self.graph.bind("obo", str(OBO))
        self.graph.bind("dcterms", str(DCTERMS))
        self.graph.bind("owl", str(OWL))
        self.graph.bind("bioentity", str(BIOENTITY))
        self.graph.bind("meta", str(META))
        self.graph.add((base, RDF.type, OWL.Ontology))
        self.graph.add((base, RDF.type, OWL.Ontology))
        self.graph.add((base, RDFS.label, Literal(self.schema.name)))
        if self.schema.license:
            self.graph.add((base, DCTERMS.license, Literal(self.schema.license)))
        else:
            logging.warning("No license!")

    def end_schema(self, output: Optional[str]) -> None:
        data = lambda: self.graph.serialize(format='turtle' if self.format == 'ttl' else self.format).decode()
        if output:
            with open(output, 'w') as outf:
                outf.write(data())
        else:
            print(data())

    def visit_class(self, cls: ClassDefinition) -> bool:
        cls_uri = self.class_uri(cls.name)
        self.graph.add((cls_uri, RDF.type, OWL.Class))
        self.graph.add((cls_uri, RDFS.label, Literal(cls.name)))
        if cls.description:
            self.graph.add((cls_uri, OBO.IAO_0000115, Literal(cls.description)))

        # Parent classes
        if cls.is_a and not cls.defining_slots:
            self.graph.add((cls_uri, RDFS.subClassOf, self.class_uri(cls.is_a)))
        if cls.mixin:
            self.graph.add((cls_uri, RDFS.subClassOf, META.mixin))
        for mixin in cls.mixins:
            self.graph.add((cls_uri, RDFS.subClassOf, self.class_uri(mixin)))
        # TODO: Add apply_to injections

        if cls.union_of:
            union_node = BNode()
            union_coll = BNode()
            Collection(self.graph, union_coll, [self.class_uri(union_node) for union_node in cls.union_of])
            self.graph.add((union_node, OWL.unionOf, union_coll))
            self.graph.add((cls_uri, RDFS.subClassOf, union_node))

        # Defining slots give us an equivalent class
        if cls.defining_slots:
            equ_node = BNode()
            self.graph.add((cls_uri, OWL.equivalentClass, equ_node))
            self.graph.add((equ_node, RDF.type, OWL.Class))

            elts = []
            if cls.is_a:
                elts.append(self.class_uri(cls.is_a))
            for slotname in cls.defining_slots:
                slot = self.schema.slots[slotname]
                restr_node = BNode()
                self.graph.add((restr_node, RDF.type, OWL.Restriction))
                self.graph.add((restr_node, OWL.onProperty, self.prop_uri(slotname)))
                self.add_cardinality(restr_node, slot)
                self.graph.add((restr_node, OWL.someValuesFrom, self.build_range(slot)))
                elts.append(restr_node)

            coll_bnode = BNode()
            Collection(self.graph, coll_bnode, elts)
            self.graph.add((equ_node, OWL.intersectionOf, coll_bnode))

        for slotname in cls.slots:
            if slotname not in cls.defining_slots:
                subc_node = BNode()
                slot = self.schema.slots[slotname]
                slot_alias = slot.alias if slot.alias else slot.name
                self.graph.add((subc_node, RDF.type, OWL.Restriction))
                self.graph.add((subc_node, OWL.onProperty, self.prop_uri(slot_alias)))
                self.add_cardinality(subc_node, slot)
                self.graph.add((subc_node, OWL.someValuesFrom, self.build_range(slot)))
                self.graph.add((cls_uri, RDFS.subClassOf, subc_node))

        return True

    def add_cardinality(self, subj: Union[BNode, URIRef], slot) -> None:
        if slot.required or slot.primary_key:
            if slot.multivalued:
                self.graph.add((subj, OWL.minCardinality, Literal(1)))
            else:
                self.graph.add((subj, OWL.cardinality, Literal(1)))
        elif not slot.multivalued:
            self.graph.add((subj, OWL.maxCardinality, Literal(1)))

    def build_range(self, slot) -> Union[BNode, URIRef]:
        # if slot.range in builtin_names or slot.range in self.schema.types:
        #     datatype_node = BNode()
        #     self.graph.add((datatype_node, RDF.type, RDFS.DataProperty))
        #     self.graph.add((datatype_node, OWL.onDataType, self.range_uri(slot)))
        #     return datatype_node
        # else:
            return self.range_uri(slot)

    def range_uri(self, slot: SlotDefinition) -> URIRef:
        if slot.range in builtin_names or not slot.range:
            return URIRef(builtin_uri(slot.range, expand=True))
        elif slot.range in self.schema.types:
            return self.type_uri(slot.range)
        else:
            return self.class_uri(slot.range)

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
            self.graph.add((slot_uri, RDFS.subPropertyOf, self.prop_uri(slot.is_a)))
        for mixin in slot.mixins:
            self.graph.add((slot_uri, RDFS.subPropertyOf, self.prop_uri(mixin)))

        # Slot range
        if not slot.range or slot.range in builtin_names:
            self.graph.add((slot_uri, RDF.type,
                            OWL.DatatypeProperty if slot.object_property else OWL.AnnotationProperty))
            self.graph.add((slot_uri, RDFS.range, URIRef(builtin_uri(slot.range, expand=True))))
        elif slot.range in self.schema.types:
            self.graph.add((slot_uri, RDF.type,
                            OWL.DatatypeProperty if slot.object_property else OWL.AnnotationProperty))
            self.graph.add((slot_uri, RDFS.range, self.type_uri(slot.range)))
        else:
            self.graph.add((slot_uri, RDF.type, OWL.ObjectProperty if slot.object_property else OWL.AnnotationProperty))
            self.graph.add((slot_uri, RDFS.range, self.class_uri(slot.range)))

        # Slot domain
        if slot.domain:
            self.graph.add((slot_uri, RDFS.domain, self.class_uri(slot.domain)))

        # Annotations
        self.graph.add((slot_uri, RDFS.label, Literal(slot.name)))
        if slot.description:
            self.graph.add((slot_uri, OBO.IAO_0000115, Literal(slot.description)))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='ttl', type=click.Choice(OwlSchemaGenerator.valid_formats),
              help="Output format")
@click.option("-o", "--output", help="Output file name")
def cli(yamlfile, format, output):
    """ Generate an OWL representation of a biolink model """
    print(OwlSchemaGenerator(yamlfile, format).serialize(output=output))
