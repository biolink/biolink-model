---
parent: "Mapping to a graph store"
---

# Mapping BioLink Model to a Neo4j property graph

This document describes how a Neo4j database is mapped to the BioLink
model. Although specific to Neo4j, this should hold for any Property
Graph (PG) model, e.g a Python networkx graph (specifically a [MultiDiGraph](https://networkx.github.io/documentation/networkx-1.10/reference/classes.multidigraph.html)).

For mapping to RDF graphs refer to [mapping-rdf](mapping-rdf.md).


## Nodes

All nodes in the Neo4j database should correspond to [named thing](../docs/NamedThing.html).
BioLink model defines a typology of nodes, all of which inherit from [named thing](../docs/NamedThing.html).

Nodes in Neo4j (and property graphs in general) may have *node properties*.
The [named thing](../docs/NamedThing.html) class defines core properties for a node, plus additional optional ones.

See [named thing](../docs/NamedThing.html) for a canonical documentation, while the core properties are summarized here:

 - id
 - iri
 - name
 - category

The `id` field MUST be provided and MUST be a CURIE or an IRI.

**Note**: this is distinct from the internal 'id' in Neo4j.

The `name` field SHOULD correspond to a concise display label for the
entity. For example `asthma` or `Wnt signaling pathway`. If the node
is an ontology class then this will correspond to the `rdf:label` of that class.

Any Neo4j instance MAY provide as many additional properties as required.
These SHOULD come from a registered list of properties for that node type.

For example, the [genotype](../docs/Genotype.html) class provides a
property [has zygosity](../docs/has_zygosity.html), which is specific to that class (and its sub-class, if any).


### Use of Neo4J labels

Neo4j nodes can be tagged with `labels` indicating a grouping to which the node belongs.
The `category` field in the model MUST map to a Neo4j label.
The BioLink class name in CamelCase MUST be used.

Additionally, the Neo4j implementation MAY use superclasses of the category.
For example, if a node representing a particular type of neuron has category [Cell](../docs/Cell.html),
then the Neo4j graph may also tag the node with [anatomical entity](../docs/AnatomicalEntity.html) as label, in
addition to [cell](../docs/Cell.html).


Consequently, any number of additional local labels MAY also be used.


**Implementation Note:** Cypher queries that use labels are optimized for speed, under the assumption that
an index has already been generated in Neo4j for said label(s).

**Terminology note:** The term 'label' is overloaded. In RDF it usually denotes the name of an entity (`rdf:label`).
For this reason we use [category](../docs/category.html) instead as the property name in BioLink.

Note that in addition to Neo4j labels, additional 'type' edges may be used to connect a node
to an ontology class node (see below).

## Edges

Each edge in the Neo4j graph should have an edge label or relationship type that is a
sub-property of [related to](../docs/related_to.html).

For example, two protein nodes may be related via
[physically_interacts_with](../docs/physically_interacts_with.html) relationship types.

**Note:** Always use snake_case to represent edge labels.

The set of edge labels is deliberately kept minimal. This is partly for practical reasons.
Neo4j has no easy way to automatically use sub-property relationship types in Cypher queries.
For example, if we have a deep hierarchy of interaction relationships including specific
physical interactions such as 'phosphorylates', then queries for *any* kind of interaction must
be expanded to include all sub-property relationship types.

More precise relationship types are allowed through the use of *edge properties* via [relation](../docs/relation.html).

### Edge properties

Note that Neo4J uses a property-graph model, where any number of properties
can be attached to an edge. Some properties may be generic, while some may
only pertain to particular kinds of relationship type.

Edges SHOULD have a [relation](relation.html) property which encodes the most specific relationship type
for the relationship. This MAY correspond to the edge label, or it MAY be more specific.
The relation property MUST be encoded as a CURIE or IRI.

An example of a generic property is [negated](negated.html), which
logically negates the assertion defined by the edge.

### Association types

BioLink includes a hierarchy of association types. See [Association](../docs/Association.html)

Note that this is distinct from the relation hierarchy, although in some cases they parallel one another.

For example, the relation hierarchy has a generic relation [part of](../docs/part_of.html).
This can be used in different contexts - for example, connecting two anatomical entities, or
connecting a pathway to a sub-pathway.

Formally, the [Association](../docs/Association.html) hierarchy is a classification of edge objects.
Any edge SHOULD be mappable to an [association type](../docs/association_type.html),
using the subject's category, edge's relation and object's category.

Different association types may have different properties associated with them.

The core ones are:

 - [subject](../docs/subject.html)*
 - [object](../docs/object.html)*
 - [edge label](../docs/edge_label.html)*
 - relation

*Note that 3 of these are builtin, so these do not correspond to edge properties.

The edge label is a snake_case human-readable high-level grouping relation.
In contrast, [relation](../docs/relation.html) is a CURIE from a more refined relationship ontology like RO or SIO.


