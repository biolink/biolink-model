#!/usr/bin/env python3

import click

import logging
from metamodel.csvgen import CsvGenerator
from metamodel.schemaloader import load_schema

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument("file", type=click.File('r'))
@click.option("--root", "-r", default=None)
@click.option("--format", "-f", default='csv')
def cli(file, root, format):
    schema = load_schema(file)
    g = CsvGenerator(schema=schema)
    roots = None
    if root:
        roots = [root]
    g.serialize(roots=roots, format=format)


if __name__ == "__main__":
    cli()
    
