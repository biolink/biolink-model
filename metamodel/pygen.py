"""Generate python OO-class definitions

These can be automatically serialized and de-serialized using
marshmallow, given accompanying schema defs.

For examples, see the biolinkmodel directory in this repo.

"""

import logging
from .schemautils import *

def write_python_module(schema):
    print('')
    print('')
    print('## CLASSES')
    print('')

    # copy
    clist = [c.name for c in schema.classes]
    
    while len(clist) > 0:
        cn = clist[0]
        c = get_cls(cn, schema)
        #logging.error("SELECTED: {}".format(c.name))
        while c.is_a and c.is_a in clist:
            #logging.error("REP {} -> {}".format(c.name, c.is_a))
            c = get_cls(c.is_a, schema)
        #logging.error("REMOVING: {}".format(c.name))
        clist.remove(c.name)
        
        cn = c.name
        parent = c.is_a
        if parent is None:
            parent = 'object'
        else:
            parent = get_class_name(parent)
        print('class {}({}):'.format(get_class_name(cn), parent))
        print('    """')
        print('    {}'.format(c.description))
        print('    """')
        
        pyslots = []
        slots = c.slots
        if slots is None:
              slots = []
        for x in get_parents_refl(c, schema):
            if x.slots:
                pyslots += x.slots
        for f in slots:
            slotname = None
            if isinstance(f,str):
                slotname = f
            elif isinstance(f,dict):
                # TODO
                slotname = f['name']
            else:
                slotname = f.name
            pyslotname = get_slot_name(slotname)
            pyslots.append(pyslotname)

        pyslots = get_slots_inf(c, schema)
        trail=','
        if len(pyslots) == 0:
            trail="):{}        pass".format("\n")
        print('    def __init__(self{}'.format(trail))
        for i in range(0,len(pyslots)):
            pyslot = pyslots[i]
            trail=','
            if i == len(pyslots)-1:
                trail='):'
            print('                 {}=None{}'.format(pyslot,trail))
        for pyslot in pyslots:
            print('        self.{}={}'.format(pyslot,pyslot))
        print('')

        fmtstr = ""
        for pyslot in pyslots:
            fmtstr = fmtstr + '{}={} '.format(pyslot,'{}')
        print('    def __str__(self):')
        print('        return "{}".format({})'.format(fmtstr,",".join(['self.{}'.format(s) for s in pyslots])))
        print('    def __repr__(self):')
        print('        return self.__str__()')
        print('')
        print('')
