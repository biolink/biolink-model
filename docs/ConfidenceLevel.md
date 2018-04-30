---
layout: default
---

## confidence level


Level of confidence in a statement

URI: [http://bioentity.io/vocab/ConfidenceLevel](http://bioentity.io/vocab/ConfidenceLevel)


![img](http://yuml.me/diagram/nofunky/class/[information content entity|]^-[confidence level|])
## Mappings

 * [CIO:0000028](http://purl.obolibrary.org/obo/CIO_0000028)

## Inheritance

 *  is_a: [information content entity](InformationContentEntity.html)

## Children



## Fields

 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
