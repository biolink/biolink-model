---
title: "Frequently Asked Questions"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 6
---

## FAQ

### How do I type nodes in a graph with concepts that are not in the Biolink Model?

Each node in a knowledge graph can be typed using the slot `category`.

In addition to `category`, one can type a node using the `rdf:type` and `rdfs:subClassOf` predicates.


### How do I type edges in a graph with concepts that are not in the Biolink Model?

Each edge in a knowledge graph can be typed using the slot `category`.

In addition to `category`, one can type a node using the `rdf:type`.


### How do I add properties that are not in the Biolink Model

Each node and/or edge can have properties that are outside of Biolink Model. 

Alternatively, for a more structured representation it is recommended to use the class `Attribute` to represent the property and link a node/edge using the `has attribute` slot.

### What is the serialized form of Biolink Model?

Refer to [Working with the Model](working-with-the-model.md) for an example on how a Biolink Model graph can be represented as labelled property graphs and RDF graphs.

### What is the difference between `predicate`, `relation`, `category`?

- `predicate` is an association slot and must have a value from the [`related to` hierarchy](https://biolink.github.io/biolink-model/docs/related_to)
- `relation` is an association slot and can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- `category` (or `rdf:type`) is a slot and must have a value from the [`named thing`](https://biolink.github.io/biolink-model/docs/NamedThing)
or the [`association`](https://biolink.github.io/biolink-model/docs/Association) hierarchy.

