---
layout: default
---

## life stage


A stage of development or growth of an organism, including post-natal adult stages

URI: [http://bioentity.io/vocab/LifeStage](http://bioentity.io/vocab/LifeStage)


![img](http://yuml.me/diagram/nofunky/class/[organismal entity]^-[life stage], [life stage]-in taxon >[organism taxon], [ontology class]^-[organism taxon])
## Mappings

 * [UBERON:0000105](http://purl.obolibrary.org/obo/UBERON_0000105)

## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children


## Used in

 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [life stage](LifeStage.html)

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
