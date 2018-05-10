#!/usr/bin/env python3

import click

import logging
from metamodel.contextgen import ContextGenerator
from metamodel.loader import load_schema

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument("file", type=click.File('r'))
@click.option("--format", "-f", default='json')
def cli(file, format):
    schema = load_schema(file)
    g = ContextGenerator(schema=schema)
    print(g.serialize())


if __name__ == "__main__":
    cli()
    
