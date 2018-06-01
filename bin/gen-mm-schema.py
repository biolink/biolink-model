#!/usr/bin/env python3

import click

from metamodel.generators.marshmallowgen import MarshmallowGenerator
from metamodel.utils.schemaloader import load_schema

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = MarshmallowGenerator(schema)
    g.serialize()


if __name__ == "__main__":
    cli()
    
