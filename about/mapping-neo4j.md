# Mapping to Neo4J

## Mapping Nodes

See [named thing](../docs/NamedThing.html) for a list of generic properties that are associated with a node

These are repeated here for summary purposes, but the generated markdown is canonical

 - id (required)
 - iri
 - name
 - category

The `id` field MUST be provided and MUST be a CURIE or an IRI.

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
may also tag the node with AnatomicalEntity, etc.

Additionally, any number of additional local labels MAY be used.

## Mapping Edges

Note that Neo4J uses a property-graph model, any number of properties
can be attached to an edge.

See [named thing](../docs/Association.html) for a list of generic
properties that are associated with an edge.

These are repeated here for summary purposes, but the generated markdown is canonical

 - subject [builtin]
 - object [builtin]
 - edge label [builtin]
 - relation

Note that 3 of these are builtin, so these do not correspond to edge
properties. The edge label is a snake-case human-readable high-level
grouping relation. In contrast, [relation](../docs/relation.html) is a
CURIE from a more refined relationship ontology like RO or SIO.


