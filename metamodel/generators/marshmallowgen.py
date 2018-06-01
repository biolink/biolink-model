"""Generate python OO-class definitions

These can be automatically serialized and de-serialized using
marshmallow, given accompanying schema defs.

For examples, see the biolinkmodel directory in this repo.

"""


from metamodel.schemautils import *
from metamodel.schemamanager import *
from metamodel.utils.generator import Generator

class MarshmallowGenerator(Generator):
        
    def serialize(self, dirname=None, **args):
        self.dirname = dirname
        self.tr()
    
    def tr(self):
        schema = self.schema
        mgr = self.manager
        print('## SCHEMA')
        print('')
        print('from marshmallow import Schema, fields, pprint, post_load')
        print('')

        for c in schema.classes:
            self.tr_class(c)

    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager
        cn = c.name
        parent = c.is_a
        if parent is None:
            parent = 'Schema'
        else:
            parent = self.get_schema_class_name(parent)
            
        print('class {}({}):'.format(self.get_schema_class_name(cn), parent))
        print('    """')
        print('    {}'.format(c.description))
        print('    """')

        slots = mgr.class_slotdefs(c, use_isa=False, use_mixins=True)

        snames = []
        init_args = ['self']
        for sn in slots:
            s = mgr.slotdef(sn, c)
            if s is None:
                logging.error('No such slot: {}'.format(sn))
                continue
            sn = self.get_slot_name(s)

            # TODO: support other types
            stype = 'Str'
            print('    {n} = fields.{type}()'.format(n=sn, type=stype))

        # generate post-load annotations that vivify objects from json
        # or equivalent dict representations
        print('')
        print('    @post_load')
        print('    def make_object(self, data):')
        print('        {}(**data)'.format(get_class_name(cn)))
        print('')
    
    def get_schema_class_name(self, cn):
        return self.manager.class_name(self.manager.classdef(cn)) + 'Schema'
    
    def get_slot_name(self, sn):
        return self.manager.slot_name(self.manager.slotdef(sn))
