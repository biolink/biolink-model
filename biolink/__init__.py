# Biolink model file locations
import os

basedir = os.path.abspath(os.path.join(__file__, '..', '..'))
BIOLINK_MODEL_YAML = os.path.join(basedir, 'biolink-model.yaml')
BIOLINK_MODEL_JSONLD = os.path.join(basedir, 'context.jsonld')
BIOLINK_MODEL_SHEX = os.path.join(basedir, 'shex', 'biolink-model.shex')
BIOLINK_MODEL_RDF = os.path.join(basedir, 'rdf', 'biolink-model.ttl')
BIOLINK_MODEL_OWL = os.path.join(basedir, 'ontology', 'biolink-model.owl')
BIOLINK_MODEL_JSON = os.path.join(basedir, 'biolink-model.json')
BIOLINK_MODEL_JSON_SCHEMA = os.path.join(basedir, 'json-schema', 'biolink-model.json')
BIOLINK_MODEL_JAVA = os.path.join(basedir, 'java')
BIOLINK_MODEL_PYTHON = os.path.join(basedir, 'biolink', 'model.py')
