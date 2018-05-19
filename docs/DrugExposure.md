---
layout: default
---

## drug exposure


A drug exposure is an intake of a particular chemical substance

URI: [http://bioentity.io/vocab/DrugExposure](http://bioentity.io/vocab/DrugExposure)


![img](http://yuml.me/diagram/nofunky/class/[environment|]^-[drug exposure|])
## Mappings

 * [ECTO:0000509](http://purl.obolibrary.org/obo/ECTO_0000509)
 * [SIO:001005](http://semanticscience.org/resource/SIO_001005)

## Inheritance

 *  is_a: [environment](Environment.html)

## Children


## Used in

 *  class: [treatment](Treatment.html) references: [drug exposure](DrugExposure.html)

## Fields

 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
