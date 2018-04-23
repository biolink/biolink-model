---
layout: default
---

## biological process


One or more causally connected executions of molecular functions

URI: [http://bioentity.io/vocab/BiologicalProcess](http://bioentity.io/vocab/BiologicalProcess)


![img](http://yuml.me/diagram/nofunky/class/[biological entity|]^-[biological process|])
## Mappings

 * [GO:0008150](http://purl.obolibrary.org/obo/GO_0008150)
 * [SIO:000006](http://semanticscience.org/resource/SIO_000006)
 * [WD:Q2996394](http://purl.obolibrary.org/obo/WD_Q2996394)

## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)
 *  mixin: [occurrent](Occurrent.html)

## Children

 *  child: [pathway](Pathway.html)
 *  child: [physiology](Physiology.html)

## Used in

 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [pathway](Pathway.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
