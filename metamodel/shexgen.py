from .schemautils import *
from .manager import NameStyle
from .generator import Generator

class ShexGenerator(Generator):
    """
    A `Generator` for creating Shex from a metamodel schema.
    
    """
    def __init__(self, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        
    def serialize(self, destination=None, **args):
        self.lines = []
        self.tr(self.schema)
        return "".join(self.lines)

    def tr(self, schema, classname=None):
        self.schema = schema

        for c in schema.classes:
            self.tr_class(c)

    def slot_name(self, s):
        return self.manager.slot_name(s, NameStyle.LCAMELCASE)
    
    def tr_class(self, c):
        mgr = self.manager
        schema = self.schema
        lines = self.lines
        
        c = mgr.classdef(c)

        
        cn = mgr.class_name(c)

        line1 = ":{} ".format(cn)
        extends = []
        if c.is_a:
            extends.append('@:'+mgr.class_name(c.is_a))
        if c.mixins:
            extends += ['@:'+mgr.class_name(m) for m in c.mixins]
        if len(extends) > 0:
            line1 += " AND ".join(extends) + " AND "
        line1 += "{\n"
        lines.append(line1)

        # Slots:
        slots = mgr.class_slotdefs(c, True, True)

        nl = "\n  "
        for s in slots:
            s = mgr.slotdef(s, c)
            sn = self.slot_name(s)

            r = mgr.class_slot_range(c, s)
            if mgr.classdef(r):
                r = ':' + mgr.class_name(r)
            else:
                # TODO: check types
                r = 'xsd:string'

            cardinality = '?'
            reqd = mgr.class_slot_getattr(c, s, 'required', False)
            if reqd:
                cardinality = ''
            if mgr.class_slot_multivalued(c, s):
                if reqd:
                    cardinality = '+'
                else:
                    cardinality = '*'
                    
            lines.append(nl+"  schema:{}   {}".format(sn, r))
            nl = " ;\n  "

        lines.append("\n}\n\n");
    
    
