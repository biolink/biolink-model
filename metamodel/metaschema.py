## SCHEMA

from marshmallow import Schema, fields, pprint, post_load
from metamodel.metamodel import *

class ExampleSchema(Schema):
    value = fields.Str()
    description = fields.Str()

    @post_load
    def make_object(self, data):
        return Example(**data)

class DefinitionSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    singular_name = fields.Str()
    is_a = fields.Str()
    description = fields.Str()
    apply_to = fields.Str()
    abstract = fields.Boolean()
    mappings = fields.List(fields.Str)
    id_prefixes = fields.List(fields.Str)
    in_subset = fields.List(fields.Str)

    @post_load
    def make_object(self, data):
        return Definition(**data)

class SlotDefinitionSchema(DefinitionSchema):
    identifier = fields.Boolean()
    domain = fields.Str()
    range = fields.Str()
    multivalued = fields.Boolean()
    required = fields.Boolean()
    path = fields.Str()
    subproperty_of = fields.Str()
    examples = fields.List(fields.Nested(ExampleSchema))

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
    subclass_of = fields.Str()
    mixin = fields.Bool()
    abstract = fields.Bool()
    mixins = fields.List(fields.Str())
    slots = fields.List(fields.Str)
    defining_slots = fields.List(fields.Str)
    slot_usage = fields.List(fields.Nested(SlotUsageDefinitionSchema))

    @post_load
    def make_object(self, data):
        return ClassDefinition(**data)

class TypeDefinitionSchema(DefinitionSchema):
    mixins = fields.Str()
    typeof = fields.Str()

    @post_load
    def make_object(self, data):
        return TypeDefinition(**data)

class SchemaDefinitionSchema(DefinitionSchema):
    slots = fields.List(fields.Nested(SlotDefinitionSchema))
    classes = fields.List(fields.Nested(ClassDefinitionSchema))
    types = fields.List(fields.Nested(TypeDefinitionSchema))
    imports = fields.List(fields.Str)
    license = fields.Str()

    @post_load
    def make_object(self, data):
        return SchemaDefinition(**data)
