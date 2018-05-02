---
layout: default
---

## device


A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment

URI: [http://bioentity.io/vocab/Device](http://bioentity.io/vocab/Device)


![img](http://yuml.me/diagram/nofunky/class/[named thing|id;name;category]^-[device|])
## Mappings

 * [UMLSSG:DEVI](http://purl.obolibrary.org/obo/UMLSSG_DEVI)

## Inheritance

 *  is_a: [named thing](NamedThing.html)

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
