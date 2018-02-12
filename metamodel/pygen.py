"""Generate python OO-class definitions

These can be automatically serialized and de-serialized using
marshmallow, given accompanying schema defs.

For examples, see the biolinkmodel directory in this repo.

"""


from .schemautils import *
import yaml
import logging
from .manager import *
from .generator import Generator

class PythonGenerator(Generator):
        
    def serialize(self, dirname=None, **args):
        self.dirname = dirname
        self.tr()
    
    def tr(self):
        schema = self.schema
        mgr = self.manager
        print('')
        print('')
        print('## CLASSES')
        print('')

        # create list of class names
        clist = [c.name for c in schema.classes]
        
        while len(clist) > 0:

            # find root
            c = mgr.classdef(clist[0])
            while c.is_a and c.is_a in clist:
                c = mgr.classdef(c.is_a)
            clist.remove(c.name)

            self.tr_class(c)

    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager
        cn = c.name
        parent = c.is_a
        if parent is None:
            parent = 'object'
        else:
            parent = self.get_class_name(parent)
        print('class {}({}):'.format(self.get_class_name(cn), parent))
        print('    """')
        print('    {}'.format(c.description))
        print('    """')

        slots = mgr.class_slotdefs(c, True, True)

        snames = []
        init_args = ['self']
        for sn in slots:
            s = mgr.slotdef(sn, c)
            if s is None:
                logging.error("No slotdef: {}".format(sn))
                continue
            sn = self.get_slot_name(s)
            snames.append(sn)
            init_args.append('{}=None'.format(sn))

        print('    def __init__({}):'.format(',\n                 '.join(init_args)))
        if snames:
            for sn in snames:
                print('        self.{}={}'.format(sn,sn))
        else:
            print('        pass')
        print('')

        fmtstr = ""
        for sn in snames:
            fmtstr = fmtstr + '{}={} '.format(sn,'{}')
        print('    def __str__(self):')
        print('        return "{}".format({})'.format(fmtstr,",".join(['self.{}'.format(s) for s in snames])))
        print('    def __repr__(self):')
        print('        return self.__str__()')
        print('')
        print('')
    
    def get_class_name(self, cn):
        return self.manager.class_name(self.manager.classdef(cn))
    
    def get_slot_name(self, sn):
        s = self.manager.slotdef(sn)
        if s is None:
            logging.warning("No slotdef for {}".format(sn))
            return sn
        else:
            return self.manager.slot_name(s)
