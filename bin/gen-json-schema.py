#!/usr/bin/env python3

import click

import logging
from metamodel.schemaloader import load_schema
from metamodel.jsonschemagen import JsonSchemaGenerator

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = JsonSchemaGenerator(schema=schema)
    print(g.serialize())



if __name__ == "__main__":
    cli()
    
