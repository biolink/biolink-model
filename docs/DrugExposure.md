---
layout: default
---

## drug exposure


A drug exposure is an intake of a particular chemical substance

URI: [http://bioentity.io/vocab/DrugExposure](http://bioentity.io/vocab/DrugExposure)
## Mappings

 * [ECTO:0000509](http://purl.obolibrary.org/obo/ECTO_0000509)
 * [SIO:001005](http://semanticscience.org/resource/SIO_001005)

## Inheritance

 *  is_a: [environment](Environment.html)

## Children


## Used in

 *  class: [treatment](Treatment.html) references: [drug exposure](DrugExposure.html)

## Fields

 * [drug](drug.html)
    * __range__: [chemical substance](ChemicalSubstance.html) [required]
    * __Local__
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
