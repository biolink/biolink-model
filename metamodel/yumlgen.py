"""Generate yuml 

https://yuml.me/diagram/scruffy/class/samples

"""


from .schemautils import *
import yaml
import logging
from .manager import *
from .generator import Generator

class YumlGenerator(Generator):

    """
    A `Generator` for making yuml
    
    """
    def __init__(self, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        self.arcs = []
        self.visited = {}
        
    def serialize(self, **args):
        self.tr()
        return self.url()

    def url(self, **args):
        p = ", ".join(self.arcs)
        url = 'http://yuml.me/diagram/nofunky/class/{}'.format(p)
        return url
        
    
    def tr(self):
        schema = self.schema
        mgr = self.manager

        # create list of class names
        clist = [c.name for c in schema.classes]
        
        while len(clist) > 0:

            # find root
            c = mgr.classdef(clist[0])
            while c.is_a and c.is_a in clist:
                c = mgr.classdef(c.is_a)
            clist.remove(c.name)

            self.tr_class(c)

    def add_arc(self, sc, oc, sym):
        scbox = self.box(sc)
        ocbox = self.box(oc)
        self.arcs.append('[{}]{}[{}]'.format(scbox,sym,ocbox))

    def box(self, cn):
        mgr = self.manager
        c = mgr.classdef(cn)
        slots = mgr.class_slotdefs(c, False, True)
        rows = []
        for sn in slots:
            rows.append(sn)
        return '{}|{}'.format(cn, ";".join(rows))
        
    
    def tr_class(self, c, recurse=False):
        if c in self.visited:
            return
        self.visited[c] = True
        
        mgr = self.manager
        cn = c.name
        parent = c.is_a
        if parent is not None:
            self.add_arc(parent, cn, '^-')
            
        slots = mgr.class_slotdefs(c, True, True)

        for sn in slots:
            s = mgr.slotdef(sn, c)
            r = mgr.class_slot_range(c, s)
            rc = mgr.classdef(r)
            if rc:
                sym = '-{} >'.format(sn)
                self.add_arc(cn, r, sym)
                if recurse:
                    self.tr_class(rc, recurse=True)
            else:
                pass



