---
layout: default
---

## evidence type


Class of evidence that supports an association

URI: [http://bioentity.io/vocab/EvidenceType](http://bioentity.io/vocab/EvidenceType)


![img](http://yuml.me/diagram/nofunky/class/[information content entity|]^-[evidence type|])
## Mappings

 * [ECO:0000000](http://purl.obolibrary.org/obo/ECO_0000000)

## Inheritance

 *  is_a: [information content entity](InformationContentEntity.html)

## Children



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
