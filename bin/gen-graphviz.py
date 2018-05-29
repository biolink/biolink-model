#!/usr/bin/env python3

import click

import logging
from metamodel.dotgen import *
from metamodel.schemaloader import load_schema

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option("--directory", "-d")
@click.option("--out", "-o", default="target/foo.ttl")
@click.option("--classname", "-c", default="target/foo.ttl")
@click.argument("file", type=click.File('r'))
def cli(file, classname, out, directory):
    schema = load_schema(file)
    if directory is not None:
        write_all_to_directory(schema, directory)
    else:
        write_dot(schema, out, classname=classname)

    

if __name__ == "__main__":
    cli()
    
