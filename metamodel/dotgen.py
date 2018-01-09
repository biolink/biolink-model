"""Generate dotfiles

"""

import logging
import os

from .generator import Generator
from graphviz import Digraph


def write_dot(schema, fn, classname=None):
    gen = DotGenerator(schema=schema)
    gen.tr(classname=classname)
    gen.serialize(fn)

def write_all_to_directory(schema, dirname):
    gen = DotGenerator(schema=schema)
    for c in schema.classes:
        cn = gen.manager.class_name(c)
        basepath = "{}/{}".format(dirname, cn)
        write_dot(schema, basepath, c.name)
        # graphviz will generate basepath.png, tidy up remaining dot file
        os.remove(basepath)
    
class DotGenerator(Generator):

    def serialize(self, destination=None, format='png', view=False, **args):
        dot = self.dot
        dot.format = format
        dot.render(destination, view=view) 
    
    def tr(self, classname=None):
        schema = self.schema
        mgr = self.manager
        dot = Digraph(comment=schema.name)
        self.dot = dot

        for c in schema.classes:
            if classname == None or c.name == classname or mgr.class_name(c.name) == classname:
                self.tr_class(c)
        for s in schema.slots:
            self.tr_slot(s)
        
        return dot

    def tr_slot(self, s):
        pass
    
    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager
        dot = self.dot

        c = mgr.classdef(c)
        
        cid = c.name
        dot.node(cid, c.name)
        
        parent = c.is_a
        if parent is not None:
            dot.edge(cid, parent, label='is_a')
        if c.mixins:
            for m in c.mixins:
                dot.edge(cid, m, label='uses')

        slots_direct = mgr.class_slotdefs(c, False, False)
        slots = mgr.class_slotdefs(c, True, True)

        stmt_subj = None
        stmt_obj = None
        stmt_pred = None
        for s in slots:
            s = mgr.slotdef(s, c)

            # todo: handle reification generically
            if s.name == 'subject':
                stmt_subj = s
            if s.name == 'object':
                stmt_obj = s

            srange = mgr.class_slot_range(c, s)
            logging.debug("RANGE Getting range for {}.{} = {}".format(c.name, s.name, srange))
            subp = mgr.class_slot_getattr(c, s, 'subproperty_of')
            if not srange:
                logging.warn("No range for {} in cls {}".format(s.name, c.name))
                srange = 'Thing'
            if srange:
                color = 'blue'
                if s.name in slots_direct:
                    color = 'blue'
                else:
                    color = 'black'
                dot.edge(cid, s.name, label=s.name, color=color)
                if subp:
                    srange += " [{}]".format(subp)
                dot.node(s.name, srange, color=color)
        if stmt_subj and stmt_obj:
            rnode = 'relation'
            dot.edge(stmt_subj.name,
                     stmt_obj.name,
                     label=rnode)
            dot.edge(stmt_subj.name,
                     rnode,
                     style='dotted')
            dot.edge(stmt_obj.name,
                     rnode,
                     style='dotted')
            #dot.node(hnode, '', size='0', shape='diamond')
            #dot.edge(stmt_subj.name,
            #         hnode,
            #         arrowhead='none')
            #dot.edge(hnode,
            #         stmt_obj.name,
            #         label='relation')
            #dot.edge(hnode,
            #         'relation',
            #         style='dotted')
