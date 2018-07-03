# Mapping to Neo4J

This document describes how a neo4j database is mapped to the biolink
model. Although specific to neo4j, this should hold for any Property
Graph (PG) model, e.g a Python networkx object.

For mapping to RDF graphs see [mapping-rdf](mapping-rdf.md).


## Nodes

All nodes in the neo4j database should correspond to [named thing](../docs/NamedThing.html)s. Biolink defines a typology of nodes, all of which inherit from NamedThing.

Nodes in neo4j (and property graphs in general) may have *node properties*. The NamedThink biolink class defines core properties for a node, plus additional optional ones.

See [named thing](../docs/NamedThing.html) docs for canonical documentation, these are summarized here:

 - id
 - iri
 - name
 - category

The `id` field MUST be provided and MUST be a CURIE or an IRI. Note
this is distinct from the internal id in neo4j.

The `name` field SHOULD correspond to a concise display label for the
entity. For example `asthma` or `Wnt signaling pathway`. If the node
is an ontology class then this will correspond to the rdf:label.

Any neo4j instance MAY provide as many additional properties as is
required. These SHOULD come from a registered list of properties for
that node type.

For example, the [genotype](../docs/Genotype.html) class provides a
property [has zygosity](../docs/has_zygosity.html).

## Use of Neo4J labels

Neo4j nodes can be tagged with `labels` indicating a grouping to which
the node belongs. The `category` field in the model MUST map to a
neo4j label. The biolink class name in camelcase MUST be used.

Additionally, the neo4j implementation MAY use superclasses of the
category. For example, if a node representing a particular type of
neuron has category [Cell](../docs/Cell.html), then the neo4j graph
may also tag the node with [AnatomicalEntity](../docs/AnatomicalEntity.html), etc.

Additionally, any number of additional local labels MAY be used.

Implementation Note: Cypher queries that use labels are optimized for speed.

Terminology note: the term "label" is overloaded. In RDF it usually denotes the name of an entity. For this reason we use [category](../docs/category.html) as the property name in biolink.

Note that in addition to neo4j labels, additional 'type' edges may be
used to connect a node to an ontology class node (see Mapping Edges, below)

## Edges

Each edge in the neo4j graph should have an edge label / relationship type that is a subproperty of [related to](../docs/related_to.html)

For example, two protein nodes may be related via [physically_interacts_with](../docs/physically_interacts_with.html) relationship types.

snake_case is always used for edge labels.

The set of edge labels is deliberately kept minimal. This is partly for practical reasons. Neo4j has no easy way to automatically use sub-property relationship types in Cypher queries. For example, if we have a deep hierarchy of interaction relationships including specific physical interactions such as 'phosphorylates', then queries for *any* kind of interaction must be expanded to include all sub-properties.

More precise relationship types are allowed through the use of *edge properties*.

### Edge properties

Note that Neo4J uses a property-graph model, any number of properties
can be attached to an edge. Some properties may be generic, some may
only pertain to particular kinds of relationship type.

Edges SHOULD have a [relation](relation.html) property which encodes the most specific relationship type for the relationship. This MAY correspond to the edge label, or it MAY be more specific. The relation property MUST be encoded as a CURIE or IRI.

An example of a generic property is [negated](negated.html), which
logically negates the assertion coded by the edge.

### Association types

Biolink includes a hierarchy of association types. See [Association](../docs/Association.html)

Note that this is distinct from the relation hierarchy, although in some cases they parallel one another.

For example, the relation hierarchy has a generic relation [part of](../docs/part_of.html). This can be used in different contexts - for example, connecting two anatomical entities, or connecting a pathway to a sub-pathway.

Formally, the Association hierarchy is a classification of edge objects. Any edge SHOULD be mappable to an association type, using the source category, relation and target category of the edge.

Different association types may have different properties associated. The core ones are:

 - subject [builtin]
 - object [builtin]
 - edge label [builtin]
 - relation

Note that 3 of these are builtin, so these do not correspond to edge
properties. The edge label is a snake-case human-readable high-level
grouping relation. In contrast, [relation](../docs/relation.html) is a
CURIE from a more refined relationship ontology like RO or SIO.

# Examples


