#!/usr/bin/env python3

import click

import logging
from metamodel.loader import load_schema
from metamodel.shexgen import ShexGenerator

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = ShexGenerator(schema=schema)
    print(g.serialize())



if __name__ == "__main__":
    cli()
    
