"""Generate dotfiles

"""

import logging

from .schemautils import *
from graphviz import Digraph


def write_dot(schema, fn, classname=None):
    gen = DotGenerator()
    gen.tr(schema, classname=classname)
    gen.serialize(fn)

def write_all_to_directory(schema, dirname):
    for c in schema.classes:
        cn = get_class_name(c.name)
        write_dot(schema, "{}/{}".format(dirname, cn), c.name)
    
class DotGenerator(object):
    
    def __init__(self):
        self.schema = None

    def serialize(self, destination=None, format='png', view=False, **args):
        dot = self.dot
        dot.format = format
        dot.render(destination, view=view) 
    
    def tr(self, schema, classname=None):
        self.schema = schema
        dot = Digraph(comment=schema.name)
        self.dot = dot

        for c in schema.classes:
            if classname == None or c.name == classname:
                self.tr_class(c)
        for s in schema.slots:
            self.tr_slot(s)
        
        return dot

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
        dot = self.dot
        
        cid = self.cname(c)
        dot.node(cid, c.name)
        
        parent = c.is_a
        if parent is not None:
            dot.edge(cid, self.cname(parent), label='is_a')

        slots = get_slot_names_inf(c, schema)
        for sn in slots:
            srange = get_slot_range(sn, self.schema, classdef=c)
            if not srange:
                logging.warn("No range for {} in cls {}".format(sn, c.name))
                srange = 'Thing'
            if srange:
                dot.edge(cid, self.cname(srange), label=sn)
