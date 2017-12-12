from .schemautils import *
from .generator import Generator
import json

class JsonSchemaGenerator(Generator):
    """
    A `Generator` for creating JSON Schema from a metamodel schema.
    
    """
    def __init__(self, inline=False, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        self.inline = inline
        
    def serialize(self, destination=None, **args):
        self.tr(self.schema)
        #print("{}".format(self.jsonobj))
        return json.dumps(self.jsonobj, sort_keys=True, indent=4)

    def tr(self, schema, classname=None):
        self.schema = schema

        self.defdict = {}
        self.properties = {}
        schemaobj = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": schema.name,
            "type": "object",
            "properties": self.properties,
            "definitions": self.defdict
        }
        if schema.id:
            schema["$id"] = schema.id

        for c in schema.classes:
            self.tr_class(c)
        for s in schema.slots:
            self.tr_slot(s)
        self.jsonobj = schemaobj


    def type_or_ref(self, c):
        # TODO jref
        return {
            "type": "string"
        }
    
    def tr_class(self, c):
        mgr = self.manager
        schema = self.schema

        c = mgr.classdef(c)

        if c.abstract:
            return
        
        cn = mgr.class_name(c)
        
        props = {}
        obj = {
            "title": cn,
            "type": "object",
            "properties": props,
            "description": c.description,
            "required": []
        }

        # Slots:
        # JSON-Schema does not have inheritance,
        # so we duplicate slots from inherited parents and mixins
        slots = mgr.class_slotdefs(c, True, True)
        for s in slots:
            s = mgr.slotdef(s)
            sn = mgr.slot_name(s)

            if self.inline:
                prop = {
                    "type": {
                        "$ref": "#/definitions/{}".format(sn)
                    }
                }
            else:
                if mgr.class_slot_multivalued(c, s):
                    typedict = self.type_or_ref(c)
                    #r = mgr.class_slot_range(c, s)
                    #if r is None:
                    #    r = 'string'
                    #else:
                    #    r = self.jref(mgr.class_name(r))
                    prop = {
                        "type": "array",
                        "items": typedict
                    }
                else:
                    prop = {
                        "type": "string"
                    }
                    
            if s.description is not None:
                prop['description'] = s.description
            props[sn] = prop

        self.properties[cn] = obj
        return obj
    
    def tr_slot(self, s):
        mgr = self.manager
        schema = self.schema

        s = mgr.slotdef(s)
        sn = mgr.slot_name(s)
        
        obj = None
        range = s.range

        typedict = self.type_or_ref(range)
        # TODO: allow inlining
        if s.multivalued:
            obj = {
                "type" : "array",
                "items" : typedict
            }
        else:
            obj = typedict
        
        self.defdict[sn] = obj
        return obj
    
    def jref(self, n):
        return "#/definitions/{}".format(n)
    
