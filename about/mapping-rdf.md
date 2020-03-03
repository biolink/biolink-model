---
parent: "Mapping to a graph store"
---

# Mapping BioLink Model to a RDF triple store


This is similar to the [Neo4J mapping](mapping-neo4j.html). One
difference is that Neo4J uses a property-graph model, whereas a RDF
graph is a triple store, and must employ a technique such as
reification or named graphs to attach information to the triple.

## Nodes

Each node in a graph corresponds to an RDF resource. See [named
thing](../docs/NamedThing.html) for the base class.

The `id` field is a CURIE, which maps to the resource IRI/URI using a
standard prefix expansion. The RDF graph MAY include the CURIE
shortform using a triple with `dcterms:identifier` as predicate and the
CURIE as a literal.

The `name` field maps to `rdfs:label`.

## Types and Categories

TBD: use rdf:type or include additional category

## Mapping Edges

An edge maps to an RDF triple.

See [named thing](../docs/Association.html) for a list of generic
properties that are associated with an edge.

### OBAN Reification

### Wikidata Reification

### Standard RDF Reification

### Use of NamedGraphs

Examples: nanopubs
