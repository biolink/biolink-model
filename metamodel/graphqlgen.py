from .schemautils import *
from .manager import NameStyle
from .generator import Generator

class GraphqlGenerator(Generator):
    """
    A `Generator` for creating Graphql from a metamodel schema.
    
    """
    def __init__(self, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        
    def serialize(self, destination=None, **args):
        self.lines = []
        self.tr(self.schema)
        return "\n".join(self.lines)

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

        etype = 'type'
        if c.abstract or c.mixin:
            type = 'interface'
        
        cn = mgr.class_name(c)

        line1 = "{} {}".format(etype,cn)
        if c.mixins:
            inh = [mgr.class_name(m) for m in c.mixins]
            line1 += " implements "+ ", ".join(inh)
        line1 += ' {'
        lines.append(line1)
        

        # Slots:
        # graphql does not have object inheritance,
        # so we duplicate slots from inherited parents and mixins
        slots = mgr.class_slotdefs(c, True, True)
        for s in slots:
            s = mgr.slotdef(s)
            sn = self.slot_name(s)

            r = mgr.class_slot_range(c, s)
            if mgr.classdef(r):
                r = mgr.class_name(r)
            else:
                # TODO: check types
                r = 'String'

            if mgr.class_slot_multivalued(c, s):
                r = "[{}]".format(r)
            reqd = mgr.class_slot_getattr(c, s, 'required', False)
            if reqd:
                r += '!'
            lines.append("  {}: {}".format(sn, r))

        lines.append("}\n");
    
    
