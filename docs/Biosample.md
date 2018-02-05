---
layout: default
---

## biosample


None

URI: [http://bioentity.io/vocab/Biosample](http://bioentity.io/vocab/Biosample)
## Mappings


## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children


## Used in

 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
