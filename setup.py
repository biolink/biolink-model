import sys

from setuptools import setup, find_packages

version = '0.0.2'

requires = [
    "click>=6.7",
    "PyYAML>=3.12",
    "jsonasobj>=1.2.1",
    "jsonschema>=2.6.0",
    "rdflib>=4.2.2",
    "graphviz>=0.8.3",
    "prefixcommons>=0.1.7"
    "rdflib-jsonld>=0.4.0"
    ]

if sys.version_info < (3, 7):
    requires.append("dataclasses")

setup(
    name='Biolink Model Generator',
    version= version,
    packages=find_packages(exclude=['about', 'contrib', 'docs', 'graphql', 'graphviz', 'images', 'tests']),
    url='https://github.com/biolink/biolink-model',
    license='CC0 1.0 Universal',
    description='Schema and generated objects for biolink data model and upper ontology',
    scripts=['bin/gen-csv.py', 'bin/gen-golr-views.py', 'bin/gen-graphql.py', 'bin/gen-graphviz.py',
             'bin/gen-json-schema-via-mm.py', 'bin/gen-json-schema.py', 'bin/gen-jsonld-context.py',
             'bin/gen-markdown.py', 'bin/gen-mm-schema.py', 'bin/gen-proto.py', 'bin/gen-py-classes.py',
             'bin/gen-rdf.py', 'bin/gen-shex.py', 'bin/gen-yuml.py'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry"
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
