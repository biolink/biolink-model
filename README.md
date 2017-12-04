# biolink-models

A high level datamodel of biological entities (genes, diseases,
phenotypes, pathways, individuals, substances, etc) and their
associations.

The immediate goal is to provide a reference datamodel that is
independent of storage technology (solr, neo4j, csvs, etc) which can
be used for documentation and alignment purposes. The datamodel
provides:

 - definitions of upper level *classes* representing both named things
(genes, phenotypes, etc) and associations between them
 - definitions of *slots* (aka properties) that can be used to relate
   members of these classes to other classes or datatypes

Minimally this can be used for purposes like schema and datamodel
mapping. For example a CSV or Solr schema could map columns in a
column header (or fields in a document) to slots.

An additional goal is to provide a means to automatically generate and
automatically map to code and schemas in a variety of languages and
modalities.

For example

 - solr schemas and other flat denormalized forms, e.g. csvs
 - JSON-Schema (from whence it can be used for codegen)
 - Generation of python bindings
 - SHACL/Shex shapes
 - JSON-LD

## Organization

The datamodel source is [biolink-model.yaml](biolink-model.yaml). This
is a yaml file that is intended to be relatively simple to view and
edit in its native form.

The yaml definition is currently used to derive:

 - [golr-yaml schemas](golr-views)
    - these can be compiled down to solr xml schemas
    - these are also intermediate targets used within the bbop/amigo framework
 - [json-schema](json-schema) TODO
 - [python object model](biolinkmodel/datamodel.py)
 - [marshmallow schema definitions](biolinkmodel/schema.py)
    - can be used to serialize/deserialize python object model to json and yaml
 - [ontology](ontology)

We leverage existing frameworks where possible. E.g json-schema allows
codegen to other languages

TODO:

 - JSON-LD
 - SHACL
 - POJOs+Jackson

Additionally, this repo contains the metamodel definition of itself in
yaml, together with code for working with datamodels. In theory this
could be used in other domains but there is no plan for this at the
moment.

See [metamodel](metamodel) for details of the metamodel.

## Why not use X as the modeling framework?

Why invent our own yaml and not use JSON-Schema, SQL, UML, ProtoBuf,
OWL, ...

each of these is tied to a particular formalisms. E.g. JSON-Schema to
trees. OWL to open world logic. There are various impedance mismatches
in converting between these. The goal was to develop something simple
and more general that is not tied to any one serialization format or
set of assumptions.

There are other projects with similar goals, e.g
https://github.com/common-workflow-language/schema_salad

It may be possible to align with these.

## Why not use X as the datamodel

Here X may be bioschemas, some upper ontology (BioTop), UMLS
metathesaurus, bio*, various other attempts to model all of biology in
an object model.

Currently as far as we know there is no existing reference datamodel
that is flexible enough to be used here.


