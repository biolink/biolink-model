#!/usr/bin/env python3

import click

import logging
from metamodel.marshmallow.schemagen import write_schema
from metamodel.schemaloader import load_schema
from marshmallow_jsonschema import JSONSchema

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    json_schema = JSONSchema()
    json_schema.dump(schema).data



if __name__ == "__main__":
    cli()
    
