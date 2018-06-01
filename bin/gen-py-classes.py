#!/usr/bin/env python3

import click

import logging
from metamodel.pygen import PythonGenerator
from metamodel.utils.schemaloader import load_schema

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = PythonGenerator(schema=schema)
    g.serialize()


if __name__ == "__main__":
    cli()
    
