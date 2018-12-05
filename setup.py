import sys

from setuptools import setup, find_packages

version = '0.3.0'

requires = [
    "certifi>=2018.4.16",
    "cfgraph>=0.2.1",
    "click>=7.0",
    "graphviz>=0.10.1",
    "idna",
    "jsonasobj>=1.2.1",
    "jsonschema>=2.6.0",
    "prefixcommons>=0.1.7",
    "pyshex>=0.5.12",
    "pyyaml>=3.13",
    "rdflib-jsonld>=0.4.0",
    "rdflib>=4.2.2",
    "requests",
    "shexjsg>=0.5.6"
]

if sys.version_info < (3, 7):
    requires.append("dataclasses")

setup(
    name='BiolinkMG',
    version= version,
    packages=find_packages(exclude=['about', 'contrib', 'docs', 'graphql', 'graphviz', 'images', 'tests']),
    url='https://github.com/biolink/biolink-model',
    license='CC0 1.0 Universal',
    install_requires = requires,
    python_requires='>=3.6',
    description='Schema and generated objects for biolink data model and upper ontology',
    entry_points={
        'console_scripts': [
            'gen-jsonld-context = metamodel.generators.contextgen:cli',
            'gen-csv = metamodel.generators.csvgen:cli',
            'gen-graphviz = metamodel.generators.dotgen:cli',
            'gen-golr-views = metamodel.generators.golrgen:cli',
            'gen-graphql = metamodel.generators.graphqlgen:cli',
            'gen-jsonld = metamodel.generators.jsonldgen:cli',
            'gen-json-schema = metamodel.generators.jsonschemagen:cli',
            'gen-markdown = metamodel.generators.markdowngen:cli',
            'gen-owl = metamodel.generators.owlgen:cli',
            'gen-proto = metamodel.generators.protogen:cli',
            'gen-py-classes = metamodel.generators.pythongen:cli',
            'gen-rdf = metamodel.generators.rdfgen:cli',
            'gen-shex = metamodel.generators.shexgen:cli',
            'gen-yuml = metamodel.generators.yumlgen:cli',
            'comparefiles = metamodel.utils.comparefiles:cli'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
