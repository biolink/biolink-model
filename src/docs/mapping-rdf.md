---
title: "Mapping Biolink Model to a RDF and RDF*"
parent: "Mapping to a graph store"
layout: default
---

# Mapping Biolink Model to a RDF and RDF*

This document describes how Biolink is to be used in the context of
RDF, either in storage in a triplestore, or in serialization to one of
the RDF syntaxes, such as turtle.

In RDF, a graph is a collection of triples `<S P O>` (subject
predicate object). The S and P must be RDF _resources_ (nodes). The O
can be a literal or a resource.

Graphs are organized into collections of Named Graphs. Each triple can be conceived of as a quad `<S P O G>`.

## Node and node properties

Each node in a graph corresponds to an RDF resource.

Biolink Model defines a typology of nodes, all of which inherit from [biolink:NamedThing](NamedThing).

Core properties for a node:
 - [biolink:id](id)
 - [biolink:iri](iri)
 - [biolink:name](name)
 - [biolink:category](category)

The [biolink:id](id) MUST be provided and MUST be a CURIE, which maps to the resource IRI/URI 
using a standard prefix expansion. The RDF graph MAY include the CURIE short-form represented 
with the predicate `dcterms:identifier` where the CURIE itself is a literal.

The [biolink:name](name) field SHOULD correspond to a concise label for the entity, and maps 
to `rdfs:label`.

For example, the biolink node with ID `MONDO:0001083` and name
`Fanconi syndrome` will be expressed in RDF (turtle syntax) as:

```turtle
PREFIX MONDO: <http://purl.obolibrary.org/obo/MONDO_>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

MONDO:0001083 rdfs:label "Fanconi syndrome"
```

When the CURIEs are expanded this will be rendered as:

```turtle
<http://purl.obolibrary.org/obo/MONDO_0001083> <http://www.w3.org/2000/01/rdf-schema#label> "Fanconi syndrome" .
```


### Types and Categories

To define the type of a node, you can use the `rdf:type` to link to a specific node type. You MAY use
the predicate [biolink:category](category) to represent additional categories for that node. 

The rdf:type triples MAY be partitioned into separate named
graphs. For example, it can be convenient to put the direct rdf:type
assertion in the main graph and the inferred/index (ie asserted plus
inferred) in a separate 'inferred' graph.

### Additional node properties

You MAY provide as many additional properties as required.
These SHOULD come from a registered list of properties for that node type.

## Edge and edge properties

An edge maps to an RDF triple where both the subject and object are nodes representing Biolink entities.

RDF reification is used for representing edge properties. RDF*
provides a convenient syntax for abstracting over this.

So for example, an edge between x and y with edge label p and an
additional edge property `publication=PMID:123` would be represented
in RDF* as:

```
<<:x :p :y>> bl:publication <http://identifiers.org/pmid/123>.
```

This is syntactic sugar for the more verbose reification triples:

```
:x :p :y .
[a rdf:Statement ;
   rdf:subject :x ;
   rdf:predicate :p ;
   rdf:object :y ;
   bl:publication http://identifiers.org/pmid/123 ].
```

The jury is still out on the question whether referring to an RDF* triple also asserts the triple. Therefore in some 
RDF* implementations you need to assert it explicitly if you need to have it as a direct triple, similar to the 
RDF Reification example below:

```
:x :p :y.
<<:x :p :y>> bl:publication <http://identifiers.org/pmid/123>.
```

(For example, GraphDB's RDF* does not assert automatically.)

See [biolink:Association](Association) for a taxonomy of associations defined by the model, and 
to see a list of generic properties that are associated with an edge.


## Comparison to Neo4J mapping

The mapping is similar to [Mapping to Neo4j](mapping-neo4j.md). Differences include:

 * Neo4j uses a Property Graph (LPG) model. In RDF reification is used. RDF* is a developing convention that outputs a LPG.
 * In the Neo4J mapping, ids are represented as CURIEs. In RDF URIs are first class entities.
 * There is a built-in concept of category in Neo4j, called labels. In RDF this is modeled as another node property (rdf:type)
