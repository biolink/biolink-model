import yaml
import logging

from .metaschema import SchemaDefinitionSchema
from .manager import Manager

def load_schema(file):
    mgr = Manager()
    schema = mgr.load_schema(file)
    return schema
    
