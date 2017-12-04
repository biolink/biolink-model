#!/usr/bin/env python3

import click

import logging
from metamodel.golr_yaml_gen import *
from metamodel.loader import load_schema

@click.command()
@click.option("--dir", "-d", nargs=1, default='golr-views')
@click.argument("file", type=click.File('r'))
def cli(file, dir):
    schema = load_schema(file)
    write_golr_yaml_to_dir(schema, dir)


if __name__ == "__main__":
    cli()
    
