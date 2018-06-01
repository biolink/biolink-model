#!/usr/bin/env python3

import click

from metamodel.generators.ontolgen import write_owl
from metamodel.utils.schemaloader import load_schema

@click.command()
@click.option("--out", "-o", default="target/foo.ttl")
@click.argument("file", type=click.File('r'))
def cli(file, out):
    schema = load_schema(file)
    write_owl(schema, out)


if __name__ == "__main__":
    cli()
    
