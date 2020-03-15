---
parent: "Mapping to a graph store"
---

# Mapping Biolink Model to a RDF triple store


This is similar to [Mapping to Neo4j](mapping-neo4j). One difference is that Neo4j uses a property-graph model, 
whereas a RDF graph is a triple store, and must employ a technique such as RDF reification or 
named graphs to attach information to a triple.


## Node and node properties

Each node in a graph corresponds to an RDF resource.

BioLink Model defines a typology of nodes, all of which inherit from [biolink:NamedThing](../docs/NamedThing).

Core properties for a node:
 - [biolink:id](../docs/id)
 - [biolink:iri](../docs/iri)
 - [biolink:name](../docs/name)
 - [biolink:category](../docs/category)

The [biolink:id](../docs/id) MUST be provided and MUST be a CURIE, which maps to the resource IRI/URI 
using a standard prefix expansion. The RDF graph MAY include the CURIE short-form represented 
with the predicate `dcterms:identifier` where the CURIE itself is a literal.

The [biolink:name](../docs/name) field SHOULD correspond to a concise label for the entity, and maps 
to `rdfs:label`.

You MAY provide as many additional properties as required.
These SHOULD come from a registered list of properties for that node type.


### Types and Categories

To define the type of a node, you can use the `rdf:type` to link to a specific node type. You MAY use
the predicate [biolink:category](../docs/category) to represent additional categories for that node. 


## Edge and edge properties

An edge maps to an RDF triple where both the subject and object are nodes representing Biolink entities.

See [biolink:Association](../docs/Association) for a taxonomy of associations defined by the model, and 
to see a list of generic properties that are associated with an edge.

Since its not possible attach properties to a triple, we recommend RDF reification where a triple is 
represented as a node. This style of representation allows for attaching one or more properties 
that describes an edge.

There are may strategies for reification,
- [OBAN Reification](https://github.com/EBISPOT/OBAN)
- [Wikidata Reification](https://users.dcc.uchile.cl/~dhernand/research/ssws-2015-reifying.pdf)
- Standard RDF Reification
