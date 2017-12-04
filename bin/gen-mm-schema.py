#!/usr/bin/env python3

import click

import logging
from metamodel.marshmallow.schemagen import write_schema
from metamodel.loader import load_schema

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    write_schema(schema)


if __name__ == "__main__":
    cli()
    
