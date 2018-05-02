---
layout: default
---

## clinical entity


Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities

URI: [http://bioentity.io/vocab/ClinicalEntity](http://bioentity.io/vocab/ClinicalEntity)


![img](http://yuml.me/diagram/nofunky/class/[named thing|id;name;category]^-[clinical entity|])
## Mappings


## Inheritance

 *  is_a: [named thing](NamedThing.html)

## Children

 *  child: [clinical trial](ClinicalTrial.html)
 *  child: [clinical intervention](ClinicalIntervention.html)


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
