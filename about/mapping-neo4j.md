---
parent: "Mapping to a graph store"
---

# Mapping BioLink Model to a Neo4j property graph

This document describes how a Neo4j database is mapped to the Biolink Model. 

Although specific to Neo4j, this should hold for any Property Graph (PG) model, 
e.g a Python networkx graph (specifically a [MultiDiGraph](https://networkx.github.io/documentation/stable/reference/classes/multidigraph.html)).

For mapping to RDF graphs refer to [Mapping to RDF](mapping-rdf).


## Nodes

All nodes in the Neo4j database should correspond to [biolink:NamedThing](../docs/NamedThing).

BioLink Model defines a typology of nodes, all of which inherit from [biolink:NamedThing](../docs/NamedThing).

Nodes in Neo4j (and property graphs in general) may have *node properties*.

The [biolink:NamedThing](../docs/NamedThing) class defines core properties for a node, plus additional (optional) ones. 

Core properties for a node:
 - `id`
 - `iri`
 - `name`
 - `category`

The `id` field MUST be provided and MUST be a CURIE.

**Note:** this is distinct from the internal numerical 'id' in Neo4j.

The `name` field SHOULD correspond to a concise display label for the
entity. For example `asthma` or `Wnt signaling pathway`. If the node
is an ontology class then name will correspond to the `rdfs:label` of that class.

Any Neo4j instance MAY provide as many additional properties as required.
These SHOULD come from a registered list of properties for that node type.

For example, the [biolink:Genotype](../docs/Genotype) class provides a
property [biolink:has_zygosity](../docs/has_zygosity), which is specific to that class 
(and its sub-class, if any).


> **Note:** While the name of a property is `biolink:has_zygosity` that does not necessarily mean the property
> name to be `biolink:has_zygosity` in Neo4j. Instead, the prefix part of the property can be omitted such that
> the property name is `has_zygosity`.


### Use of Neo4j labels

Neo4j nodes can be tagged with labels indicating a grouping to which the node belongs.
The `category` field in the model MUST map to a Neo4j label.
The Biolink class name in CamelCase MUST be used.

Additionally, the Neo4j implementation MAY use superclasses of the category.
For example, if a node representing a particular type of neuron has category [biolink:Cell](../docs/Cell),
then the Neo4j graph may also tag the node with [biolink:AnatomicalEntity](../docs/AnatomicalEntity) as label, 
in addition to [biolink:Cell](../docs/Cell).


Consequently, any number of additional local labels MAY also be used.


**Implementation Note:** Cypher queries that use labels are optimized for speed, under the assumption that
an index has already been generated in Neo4j for said label(s).

**Terminology note:** The term 'label' is overloaded. In RDF it usually denotes the name of an entity (`rdfs:label`).
For this reason we use [biolink:category](../docs/category) instead as the property name in Biolink Model.

Note that in addition to Neo4j labels, additional 'type' edges may be used to connect a node
to an ontology class node (see below).

## Edges

Each edge in the Neo4j graph should have an edge label or relationship type that is a
sub-property of [biolink:related_to](../docs/related_to).

For example, two protein nodes may be related via
[biolink:physically_interacts_with](../docs/physically_interacts_with) relationship types.

**Note:** Always use snake_case to represent edge labels.

The set of edge labels is deliberately kept minimal. This is partly for practical reasons.
Neo4j has no easy way to automatically use sub-property relationship types in Cypher queries.
For example, if we have a deep hierarchy of interaction relationships including specific
physical interactions such as 'phosphorylates', then queries for *any* kind of interaction must
be expanded to include all sub-property relationship types.

More precise relationship types are allowed through the use of [biolink:relation](../docs/relation) property. 
 

### Edge properties

Neo4j uses a property graph model, where any number of properties can be attached to an edge. 
Some properties may be generic, while some may only pertain to particular kinds of relationship type.

Edges SHOULD have a [biolink:relation](../docs/relation) property which encodes the most specific relationship type
for the relationship. This MAY correspond to the edge label, or it MAY be more specific.
The relation property MUST be encoded as a CURIE or IRI.

Edges can also have generic properties that changes the meaning of the edge itself. 
For example, the generic property [biolink:negated](../docs/negated), which logically negates the assertion defined by the edge.


### Association types

BioLink includes a hierarchy of [biolink:Association](../docs/Association.html)

> Note that this is distinct from the relation hierarchy, although in some cases they parallel one another.

For example, the relation hierarchy has a generic relation [biolink:part_of](../docs/part_of). 
This can be used in different contexts. For example, connecting two anatomical entities, or
connecting a pathway to a sub-pathway.

Formally, the [biolink:Association](../docs/Association) hierarchy is a classification of edge objects.
Any edge SHOULD be mappable to an [biolink:association_type](../docs/association_type),
using the subject's category, edge's relation and object's category.

Different association types may have different properties associated with them.

The core properties are:
 - [biolink:subject](../docs/subject)*
 - [biolink:object](../docs/object)*
 - [biolink:edge_label](../docs/edge_label)*
 - [biolink:relation](../docs/relation)

*Note that 3 of these are builtin, so these do not correspond to edge properties.

The `edge_label` is a snake_case human-readable high-level grouping relationship.

In contrast, [biolink:relation](../docs/relation) is a CURIE from a more refined relationship ontology like RO or SIO.

