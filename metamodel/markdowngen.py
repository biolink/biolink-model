"""Generate markdown

"""

import logging

from .manager import *
from .generator import Generator


def write_markdown(schema, fn, classname=None):
    gen = MarkdownGenerator()
    gen.tr(schema, classname=classname)
    gen.serialize(fn)

def write_all_to_directory(schema, dirname):
    for c in schema.classes:
        cn = get_class_name(c.name)
        write_markdown(schema, "{}/{}".format(dirname, cn), c.name)
    
class MarkdownGenerator(Generator):
    
    def __init__(self):
        self.schema = None

    def serialize(self, destination=None, format='png', view=False, **args):
        markdown = self.markdown
        markdown.format = format
        markdown.render(destination, view=view) 
    
    def tr(self, schema, classname=None):
        self.schema = schema
        markdown = Digraph(comment=schema.name)
        self.markdown = markdown

        for c in schema.classes:
            if classname == None or c.name == classname:
                self.tr_class(c)
        for s in schema.slots:
            self.tr_slot(s)
        
        return markdown

    def cname(self, c):
        if isinstance(c,str):
            cn = c
        else:
            cn = c.name
        return cn

    def tr_slot(self, s):
        pass
    
    def tr_class(self, c):
        schema = self.schema
        markdown = self.markdown
        
        cid = self.cname(c)
        markdown.node(cid, c.name)
        
        parent = c.is_a
        if parent is not None:
            markdown.edge(cid, self.cname(parent), label='is_a')

        slots = get_slot_names_inf(c, schema)
        for sn in slots:
            srange = get_slot_range(sn, self.schema, classdef=c)
            if not srange:
                logging.warn("No range for {} in cls {}".format(sn, c.name))
                srange = 'Thing'
            if srange:
                markdown.edge(cid, self.cname(srange), label=sn)
