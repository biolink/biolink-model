#!/usr/bin/env python3

import click

import logging
from metamodel.schemaloader import load_schema
from metamodel.graphqlgen import GraphqlGenerator

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = GraphqlGenerator(schema=schema)
    print(g.serialize())



if __name__ == "__main__":
    cli()
    
