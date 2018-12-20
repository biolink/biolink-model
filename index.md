---
layout: default
---

[![Build Status](https://travis-ci.org/biolink/biolink-model.svg?branch=master)](https://travis-ci.org/biolink/biolink-model)

# Biolink Model

A high level datamodel of biological entities (genes, diseases,
phenotypes, pathways, individuals, substances, etc) and their
associations.

## Datamodel

The datamodel consists of classes that represent nodes and edges, in a property graph sense.

### Nodes

 * [named thing](docs/NamedThing.html) - all nodes are a sub class of 'named thing'

### Edges

 * [association](docs/Association.html) - all edges are a sub class of 'association'

### Slots

 * [Slots](docs#slots) - slots are used to collectively refer to, both, node and edge properties.
    * [node property](docs/node_property.html) - all node properties are a sub class of 'node property'
    * [association slot](docs/association_slot.html) - all edge properties are a sub class of 'association slot'
 

See the [Datamodel index](docs/) for a list nodes, edges, and slots.


# Identifiers

See [biolink json-ld context](context.jsonld) to see CURIE prefix mappings.


# BioLink model representation

## Neo4J representation

See [mapping to neo4j](about/mapping-neo4j.html)

## RDF representation

See [mapping to RDF](about/mapping-rdf.html)
