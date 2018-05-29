from .schemautils import *
from .schemamanager import NameStyle
from .generator import Generator

class ProtoGenerator(Generator):
    """
    A `Generator` for creating Protobuf schemas from a metamodel schema.
    
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

        cn = mgr.class_name(c)
        desc = c.description

        if c.mixin:
            return
        if c.abstract:
            return

        # Slots:
        # proto does not have object inheritance,
        # so we duplicate slots from inherited parents and mixins
        slots = mgr.class_slotdefs(c, True, True)
        if len(slots) == 0:
            return
        
        if desc:
            dlines = desc.split("\n")
            for dline in dlines:
                lines.append('// {}'.format(dline))
        line1 = "message {}".format(cn)
        line1 += " {"
        lines.append(line1)

        counter = 0
        for s in slots:
            counter += 1
            s = mgr.slotdef(s, c)
            sn = self.slot_name(s)

            r = mgr.class_slot_range(c, s)
            if mgr.classdef(r):
                r = mgr.class_name(r)
            else:
                # TODO: check types
                r = 'String'

            qual = 'optional '
            if mgr.class_slot_multivalued(c, s):
                qual = 'repeated '
            elif mgr.class_slot_getattr(c, s, 'required', False):
                qual = ''
            lines.append("  {}{} {} = {}".format(qual, sn, r, counter))

        lines.append("}\n");
    
    
