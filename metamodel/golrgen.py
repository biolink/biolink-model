"""
Generate GOlr YAML schema definitions.

These can be converted to solr schema-xml, and used in amigo-bbop tools

See the golr-views directory in this repo for examples

"""

from .schemautils import *
import yaml
import logging
from .schemamanager import *
from .generator import Generator

class GolrSchemaGenerator(Generator):
        
    def serialize(self, dirname=None, **args):
        self.dirname = dirname
        self.tr()
    
    def tr(self):
        schema = self.schema
        dirname = self.dirname
        mgr = self.manager
        for c in schema.classes:
            if c.abstract:
                continue
            cn = mgr.get_name(c.name, NameStyle.UNDERSCORE)
            obj = self.tr_class(c)
            fn = "{}/{}-config.yaml".format(dirname, cn)
            f = open(fn,'w')
            f.write(yaml.dump(obj))
            f.close()

    def tr_class(self, c):
        mgr = self.manager
        c = mgr.classdef(c)
        obj = {
            'id': c.name,
            'schema_generating': True,
            'description' : c.description,
            'display_name': c.name,
            'document_category': c.name,
            'weight': 20
            }
        fields = []
        slots = mgr.class_slotdefs(c, True, True)
        for s in slots:
            s = mgr.slotdef(s, c)
            slot_id = mgr.slot_name(s)
            field = {}
            field = {
                'id': slot_id,
                'description': s.description,
                'display_name': s.name,
            }
            if s.multivalued:
                field['cardinality'] = 'multi'
            field['property'] = []
            fields.append(field)
        obj['fields'] = fields
        return obj

        
