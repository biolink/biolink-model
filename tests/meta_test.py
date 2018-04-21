import pytest
import yaml
import logging
from metamodel.metaschema import SchemaDefinitionSchema
from metamodel.metamodel import *

def test_foo():
    print("HI")
    path = 'biolink-model.yaml'
    f = open(path,'r')
    obj = yaml.load(f)
    schemadef = SchemaDefinitionSchema()
    schema = schemadef.load(obj)
    errs = schemadef.validate(obj)
    if len(errs) > 0:
        logging.error("CONFIG ERRS: {}".format(errs))
        #raise ValueError('Error loading '+path)
    print('S={}'.format(schema))
    for c in schema.slots:
        print(c.name)
