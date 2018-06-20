"""Generate RDF

"""
import os
from typing import Union, TextIO, Optional

import click
from ShExJSG import ShExC
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, IRIREF, ShapeAnd, EachOf, TripleConstraint, NodeConstraint
from jsonasobj import as_json
from rdflib import Graph, XSD, OWL
from prefixcommons import curie_util as cu

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    SlotDefinitionName
from metamodel.utils.builtins import builtin_names
from metamodel.utils.formatutils import camelcase, underscore
from metamodel.utils.generator import Generator
from metamodel.utils.namespaces import BIOENTITY, META


class ShExGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['shex', 'json', 'rdf']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'shex') -> None:
        super().__init__(schema, fmt)
        self.shex: Schema = None
        self.shape: Shape = None                # Shape being defined

    def visit_schema(self, **_):
        self.shex = Schema()
        self.shex.shapes = []
        if self.format == 'shex':
            raise NotImplementedError("ShExC format is not yet implemented")
        # TODO: Imports

    @staticmethod
    def _shapeIRI(name: ClassDefinitionName) -> IRIREF:
        return IRIREF(BIOENTITY[camelcase(name)])

    def _predicate(self, name: SlotDefinitionName) -> IRIREF:
        slot = self.schema.slots[name]
        if slot.mappings:
            return IRIREF(cu.expand_uri(slot.mappings[0]))
        else:
            # TODO: look at the RDF to figure out what URI's go here
            return IRIREF(BIOENTITY[underscore(name)])

    def visit_class(self, cls: ClassDefinition) -> bool:
        self.shape = Shape()
        # if not cls.mixin and not cls.name in self.synopsis.mixinrefs and not cls.abstract:
        #     self.shapeExpr.closed = jsg.Boolean(True)
        # # TODO: Add this when shex 2.1 is committed
        # if cls.abstract:
        #     self.shapeExpr.abstract = True
        # TODO: Figure out the semantics of union_of
        # TODO: symmetric
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        if cls.is_a or cls.mixins:
            shapeExpr = ShapeAnd(shapeExprs=([self._shapeIRI(cls.is_a)] if cls.is_a else []) +
                                                 [self._shapeIRI(mixin) for mixin in cls.mixins] + [self.shape])
        else:
            shapeExpr = self.shape
        shapeExpr.id = self._shapeIRI(cls.name)
        self.shex.shapes.append(shapeExpr)

    def _type_constraint(self, rnge: Optional[str]) -> NodeConstraint:
        # TODO: missing type - string or '.'?
        if rnge in builtin_names:
            return NodeConstraint(datatype=IRIREF(XSD[rnge]))
        elif rnge in self.schema.types:
            return self._type_constraint(self.schema.types[rnge].typeof)
        else:
            return NodeConstraint()

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        constraint = TripleConstraint()
        if not self.shape.expression:
            self.shape.expression = constraint
        elif isinstance(self.shape.expression, TripleConstraint):
            self.shape.expression = EachOf(expressions=[self.shape.expression])
            self.shape.expression.expressions.append(constraint)
        else:
            self.shape.expression.expressions.append(constraint)
        constraint.predicate = self._predicate(slot.name)
        constraint.min = 1 if slot.primary_key or slot.required else 0
        constraint.max = -1 if slot.multivalued else 1
        if slot.range and slot.range not in self.schema.classes:
            constraint.valueExpr = self._type_constraint(slot.range)
        else:
            constraint.valueExpr = self._shapeIRI(slot.range)

    def end_schema(self, output: Optional[str]) -> None:
        shex = as_json(self.shex)
        if self.format == 'rdf':
            g = Graph()
            g.parse(data=shex, format="json-ld")
            g.bind('owl', OWL)
            g.bind('biolink', BIOENTITY)
            g.bind('meta', META)
            shex = g.serialize(format='turtle').decode()
        elif self.format == 'shex':
            # TODO: wait until the better ShExC emitter is committed
            shex = str(ShExC(self.shex))
        if output:
            with open(output, 'w') as outf:
                outf.write(shex)
        else:
            print(shex)


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='shex', type=click.Choice(ShExGenerator.valid_formats),
              help="Output format")
@click.option("-o", "--output", help="Output file name")
def cli(yamlfile, format, output):
    """ Generate a ShEx Schema for a  biolink model """
    print(ShExGenerator(yamlfile, format).serialize(output=output))
