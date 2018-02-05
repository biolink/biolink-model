#!/usr/bin/env python3

import click

import logging
from metamodel.loader import load_schema
from metamodel.markdowngen import MarkdownGenerator

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = MarkdownGenerator(schema=schema)
    print(g.serialize('docs'))



if __name__ == "__main__":
    cli()
    
