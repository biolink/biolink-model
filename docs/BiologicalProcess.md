---
layout: default
---

## biological process


One or more causally connected executions of molecular functions

URI: [http://bioentity.io/vocab/BiologicalProcess](http://bioentity.io/vocab/BiologicalProcess)


![img](http://yuml.me/diagram/nofunky/class/[biological process or activity|]^-[biological process|])
## Mappings

 * [GO:0008150](http://purl.obolibrary.org/obo/GO_0008150)
 * [SIO:000006](http://semanticscience.org/resource/SIO_000006)
 * [WD:Q2996394](http://purl.obolibrary.org/obo/WD_Q2996394)

## Inheritance

 *  is_a: [biological process or activity](BiologicalProcessOrActivity.html)
 *  mixin: [occurrent](Occurrent.html)

## Children

 *  child: [pathway](Pathway.html)
 *  child: [physiological process](PhysiologicalProcess.html)

## Used in

 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [pathway](Pathway.html)
 *  class: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.html) references: [biological process](BiologicalProcess.html)

## Fields

 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
