import yaml
import logging

from metamodel.metaschema import SchemaDefinitionSchema

def load_schema(file):
    obj = yaml.load(file)
    schemadef = SchemaDefinitionSchema()
    errs = schemadef.validate(obj)
    if len(errs) > 0:
        logging.error("CONFIG ERRS: {}".format(errs))
    schema = schemadef.load(obj).data
    return schema
    
