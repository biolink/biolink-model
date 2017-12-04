## SCHEMA

from marshmallow import Schema, fields, pprint, post_load
from metamodel.metamodel import *

class DefinitionSchema(Schema):
    name = fields.Str()
    singular_name = fields.Str()
    is_a = fields.Str()
    description = fields.Str()
    abstract = fields.Boolean()
    mappings = fields.List(fields.Str)

    @post_load
    def make_object(self, data):
        return Definition(**data)

class SlotDefinitionSchema(DefinitionSchema):
    identifier = fields.Boolean()
    domain = fields.Str()
    range = fields.Str()
    multivalued = fields.Boolean()
    path = fields.Str()

    @post_load
    def make_object(self, data):
        if isinstance(data,str):
            return SlotDefinition(name=data)
        return SlotDefinition(**data)

class SlotUsageDefinitionSchema(SlotDefinitionSchema):

    @post_load
    def make_object(self, data):
        if isinstance(data,str):
            return SlotUsageDefinition(name=data)
        return SlotUsageDefinition(**data)
    
class ClassDefinitionSchema(DefinitionSchema):
    mixins = fields.List(fields.Str())
    slots = fields.List(fields.Str)
    slot_usage = fields.List(fields.Nested(SlotUsageDefinitionSchema))

    @post_load
    def make_object(self, data):
        return ClassDefinition(**data)

class TypeDefinitionSchema(DefinitionSchema):
    mixins = fields.Str()

    @post_load
    def make_object(self, data):
        return TypeDefinition(**data)

class SchemaDefinitionSchema(DefinitionSchema):
    slots = fields.List(fields.Nested(SlotDefinitionSchema))
    classes = fields.List(fields.Nested(ClassDefinitionSchema))
    types = fields.List(fields.Nested(TypeDefinitionSchema))

    @post_load
    def make_object(self, data):
        return SchemaDefinition(**data)


