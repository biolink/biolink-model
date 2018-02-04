"""Generate markdown

"""

import logging

from .manager import *
from .generator import Generator


def write_markdown(schema, fn, classname=None):
    gen = MarkdownGenerator()
    gen.schema = schema
    gen.tr_class(classname)
    gen.serialize(fn)

def write_all_to_directory(schema, dirname):
    for c in schema.classes:
        cn = get_class_name(c.name)
        write_markdown(schema, "{}/{}".format(dirname, cn), c.name)
    
class MarkdownGenerator(Generator):

    def serialize(self, dirname=None, **args):
        self.tr(self.schema, dirname)
    
    def tr(self, schema, dirname):
        self.schema = schema
        self.dirname = dirname
        lines = self.lines
        lines += "## {}\n\n".format(schema.label)
        for c in schema.classes:
            fn = self.class_dir_path(c)
            f = open(fn, 'w')
            self.outfile = f
            self.tr_class(c)
            f.close()
        for s in schema.slots:
            self.tr_slot(s)
        
    def class_dir_path(self, c):
        cn = mgr.class_name(c)
        return '{}/{}.md'.format(self.dirname, cn)

    def cname(self, c):
        if isinstance(c,str):
            cn = c
        else:
            cn = c.name
        return cn

    def tr_slot(self, s):
        pass

    def emit_header(self, level, txt):
        self.w('{} {}\n\n', '#' * level, txt)
    
    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager

        c = mgr.classdef(c)
        
        # header
        cn = mgr.class_name(c)
        self.emit_header(2, cn)
        
        parent = c.is_a
        if parent is not None:
            self.emit_bullet(' is_a: {}', self.link(parent)

        self.emit_header(2, 'Fields')
        slots = mgr.class_slotdefs(c, True, True)
        for s in slots:
            s = mgr.slotdef(s, c)
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
