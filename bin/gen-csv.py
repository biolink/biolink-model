#!/usr/bin/env python3

import click

import logging
from metamodel.csvgen import CsvGenerator
from metamodel.loader import load_schema

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument("file", type=click.File('r'))
@click.option("--root", "-r")
def cli(file, root):
    schema = load_schema(file)
    g = CsvGenerator(schema=schema)
    roots = []
    if root:
        roots = [root]
    g.serialize(roots=roots)


if __name__ == "__main__":
    cli()
    
