---
layout: default
---

## biological process or activity


Either an individual molecular activity, or a collection of causally connected molecular activities

URI: [http://bioentity.io/vocab/BiologicalProcessOrActivity](http://bioentity.io/vocab/BiologicalProcessOrActivity)


![img](http://yuml.me/diagram/nofunky/class/[biological entity|]^-[biological process or activity|])
## Mappings


## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)

## Children

 *  child: [molecular activity](MolecularActivity.html)
 *  child: [biological process](BiologicalProcess.html)

## Used in

 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [pathway](Pathway.html)
 *  class: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.html) references: [molecular activity](MolecularActivity.html)
 *  class: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.html) references: [biological process](BiologicalProcess.html)

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
