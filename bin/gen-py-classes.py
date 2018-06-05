#!/usr/bin/env python3
import logging

from metamodel.generators.pythongen import cli

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cli()
