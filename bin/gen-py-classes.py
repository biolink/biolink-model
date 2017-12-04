#!/usr/bin/env python3

import click

import logging
from metamodel.pygen import write_python_module
from metamodel.loader import load_schema

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    write_python_module(schema)


if __name__ == "__main__":
    cli()
    
