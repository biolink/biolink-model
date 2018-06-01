from typing import Optional, Dict, Union

from ShExJSG import ShExJ
from jsonasobj import as_json
from prefixcommons.curie_util import read_biocontext
from rdflib import Namespace, XSD

from metamodel.metamodel import ClassDefinition, TypeDefinition
from metamodel.utils.generator import Generator
from metamodel.schemamanager import NameStyle

SCHEMA = Namespace("http://bioentity.io/vocab/")
BASE = Namespace("http://namespace.org/base/")

XSDMap: Dict[str, str] = {'integer': 'integer', 'double': 'decimal'}

# TODO: Extend PrefixLibrary to allow libraries to be merged
biocontext = read_biocontext('commons_context')


class ShexGenerator(Generator):
    """
    A `Generator` for creating Shex from a metamodel schema.
    """
    def __init__(self, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        self.shex = None

    @staticmethod
    def as_iriref(ns: Namespace, id_: str) -> ShExJ.IRIREF:
        return ShExJ.IRIREF(ns[id_.replace(':', '_').replace(' ', '_')])

    @staticmethod
    def as_shapref(id_: str) -> ShExJ.ShapeExternal:
        return ShExJ.ShapeExternal(ShexGenerator.as_iriref(BASE, id_))
        
    def serialize(self, _=None, classname: Optional[str] = None):
        self.shex = ShExJ.Schema()
        self.shex.shapes = []
        self.tr(classname)
        return as_json(self.shex)

    def tr(self, classname=None):
        for cn in self.schema.classes:
            if not classname or cn == classname:
                cls = self.manager.classdef(cn)
                shape = ShExJ.Shape(id=self.as_iriref(BASE, cls.name))
                self.tr_class(shape, cls)
        for tn in self.schema.types:
            typ = self.manager.typedef(tn)
            shape = ShExJ.Shape(id=self.as_iriref(BASE, typ.name))
            self.tr_type(shape, typ)

    def slot_name(self, s):
        return self.manager.slot_name(s, NameStyle.LCAMELCASE)

    def tr_type(self, shape: ShExJ.Shape, typ: TypeDefinition) -> None:
        pass
    
    def tr_class(self, shape: ShExJ.Shape, cls_or_typ: Union[ClassDefinition, TypeDefinition]) -> None:
        if cls_or_typ.is_a or cls_or_typ.mixins:
            expr = ShExJ.ShapeAnd()
            expr.shapeExprs = [shape]
            if cls_or_typ.is_a:
                expr.shapeExprs.append(self.as_shapref(self.manager.class_name(cls_or_typ.is_a)))
            if cls_or_typ.mixins:
                expr.shapeExprs += [self.as_shapref(self.manager.class_name(mixin)) for mixin in cls_or_typ.mixins]
        else:
            expr = shape
        self.shex.shapes.append(expr)

        # Slots:
        for slot in self.manager.class_slotdefs(cls_or_typ.name, use_isa=False, use_mixins=False):
            slot_def = self.manager.slotdef(slot, cls_or_typ)
            shape.expression = ShExJ.TripleConstraint(predicate=self.as_iriref(SCHEMA, slot_def.name))
            if slot_def.range:
                if self.manager.classdef(slot_def.range):
                    shape.expression.valueExpr = self.as_shapref(self.manager.class_name(slot_def.range))
                elif self.manager.typedef(slot_def.range):
                    shape.expression.valueExpr = self.as_shapref(slot_def.range)
                elif ':' in slot_def.range:
                    ns, name = slot_def.range.split(':')
                    if ns in biocontext:
                        shape.expression.valueExpr = \
                            ShExJ.NodeConstraint(datatype=ShExJ.IRIREF(biocontext[ns] + name))
                    else:
                        print(f"Unknown ref: {slot_def.range}")
                elif slot_def.range in XSDMap:
                    shape.expression.valueExpr = \
                        ShExJ.NodeConstraint(datatype=self.as_iriref(XSD, XSDMap[slot_def.range]))
                else:
                    ...
        ...

        #
        #
        # nl = "\n  "
        # for s in slots:
        #     s = mgr.slotdef(s, c)
        #     sn = self.slot_name(s)
        #
        #     r = mgr.class_slot_range(c, s)
        #     if mgr.classdef(r):
        #         r = ':' + mgr.class_name(r)
        #     else:
        #         # TODO: check types
        #         r = 'xsd:string'
        #
        #     cardinality = '?'
        #     reqd = mgr.class_slot_getattr(c, s, 'required', False)
        #     if reqd:
        #         cardinality = ''
        #     if mgr.class_slot_multivalued(c, s):
        #         if reqd:
        #             cardinality = '+'
        #         else:
        #             cardinality = '*'
        #
        #     lines.append(nl+"  schema:{}   {}".format(sn, r))
        #     nl = " ;\n  "
        #
        # lines.append("\n}\n\n");
        #
