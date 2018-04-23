---
layout: default
---

## population of individual organisms


None

URI: [http://bioentity.io/vocab/PopulationOfIndividualOrganisms](http://bioentity.io/vocab/PopulationOfIndividualOrganisms)


![img](http://yuml.me/diagram/nofunky/class/[organismal entity|]^-[population of individual organisms|in taxon], [population of individual organisms|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SIO:001061](http://semanticscience.org/resource/SIO_001061)

## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children


## Used in

 *  class: [variant to population association](VariantToPopulationAssociation.html) references: [population of individual organisms](PopulationOfIndividualOrganisms.html)

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
