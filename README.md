[![](https://img.shields.io/github/license/biolink/biolink-model)](https://img.shields.io/github/license/biolink/biolink-model)
[![Biolink Model](https://img.shields.io/github/v/release/biolink/biolink-model?style=flat-square)](https://img.shields.io/github/v/release/biolink/biolink-model?style=flat-square)
[![Python 3.7](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)](https://www.python.org/downloads/release/python-370/)
[![DOI](https://zenodo.org/badge/112995625.svg)](https://zenodo.org/badge/latestdoi/112995625)
![Regenerate Biolink Model Artifacts](https://github.com/biolink/biolink-model/workflows/Regenerate%20Biolink%20Model%20Artifacts/badge.svg)
![Deploy Documentation](https://github.com/biolink/biolink-model/workflows/Deploy%20Documentation/badge.svg)

<img src="images/biolink-logo.png" width="20%">

# Biolink Model

Quickstart docs:

For a good overview of the biolink-model, [watch Chris Mungall's talk](https://www.youtube.com/watch?v=RE1hFm8lvJA&t=2s) at ICBO 2020.

- Browse the model: [https://biolink.github.io/biolink-model](https://biolink.github.io/biolink-model)
  - [named thing](https://biolink.github.io/biolink-model/docs/NamedThing.html)
  - [association](https://biolink.github.io/biolink-model/docs/Association.html)
  - [predicate](https://biolink.github.io/biolink-model/docs/predicates.html)


Refer to the following resources for a quick introduction to the Biolink Model:
- [Introduction to the Biolink Datamodel](https://www.slideshare.net/cmungall/introduction-to-the-biolink-datamodel)
- [Biolink Model - A community driven data model for life sciences](https://bit.ly/biolink-model-workshop-biocuration-2020) (Biocuration 2020)
    - Slides: https://bit.ly/biolink-model-workshop-biocuration-2020
    - Video: https://www.youtube.com/watch?v=RE1hFm8lvJA

See also [Biolink Model Guidelines](guidelines/README.md) for understanding, curating, and working with the model.


## Introduction

The purpose of the Biolink Model is to provide a high-level datamodel of
biological entities (genes, diseases, phenotypes, pathways, individuals, substances, etc),
their properties, relationships, and enumerate ways in which they can be associated.

The representation is independent of storage technology or metamodel (Solr documents, neo4j/property graphs,
RDF/OWL, JSON, CSVs, etc). Different mappings to each of these are provided.

The specification of the Biolink Model is a [single YAML file](biolink-model.yaml) built using [linkml](https://github.com/linkml).
The basic elements of the YAML are:

 - Class Definitions: definitions of upper level *classes* representing both 'named thing' and 'association'
 - Slot Definitions: definitions of *slots* (aka properties) that can be used to relate members of these classes to other classes or data types. Slots collectively refer to predicates, node properties, and edge properties

The model itself is being used in the following projects:
- [NCATS Biomedical Data Translator](https://ncats.nih.gov/translator)
- [Monarch Initiative](https://monarchinitiative.org/)
- [KG-COVID-19](https://github.com/Knowledge-Graph-Hub/kg-covid-19/wiki)
- [KG Microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe)
- [Illuminating the Druggable Genome](https://github.com/Knowledge-Graph-Hub/kg-idg)

## Organization

The main source of truth is [biolink-model.yaml](biolink-model.yaml). This is a YAML file that is intended to
be relatively simple to view and edit in its native form.

The yaml definition is currently used to derive:

  - [JSON Schema](json-schema)
  - [Python dataclasses](biolink/model.py)
  - [Java code gen](java)
  - [ProtoBuf definitions](biolink-model.proto)
  - [RDF](biolink-model.ttl)
  - [OWL](biolink-model.owl.ttl)
  - [RDF Shape Expressions](biolink-model.shex)
  - [JSON-LD context](context.jsonld)
  - [Markdown documentation](docs)


## Make and build instructions

Prerequisites: Python 3.7+ and poetry

To install poetry,

```sh
pip3 install poetry
```

To install the project,
```sh
poetry shell
poetry install
```

To make model changes, edit biolink-model.yaml then regenerate the python and 
json-schema artifacts and run the tests.

```sh
make 
make test 
```


Artifacts are generated automatically via GitHub actions. 

## How do I use Biolink Model YAML programatically?

For operations such as CURIE lookup, finding class by synonyms, get parents, get ancestors, etc. please make use of [biolink-model-toolkit](https://github.com/biolink/biolink-model-toolkit/). It provides a convenience methods for traversing Biolink Model.
