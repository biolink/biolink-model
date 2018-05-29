#!/usr/bin/env python3

import click

import logging
from metamodel.golrgen import *
from metamodel.schemaloader import load_schema

@click.command()
@click.option("--dir", "-d", nargs=1, default='golr-views')
@click.argument("file", type=click.File('r'))
def cli(file, dir):
    schema = load_schema(file)
    g = GolrSchemaGenerator(schema=schema)
    print(g.serialize(dir))
    #write_golr_yaml_to_dir(schema, dir)


if __name__ == "__main__":
    cli()
    
