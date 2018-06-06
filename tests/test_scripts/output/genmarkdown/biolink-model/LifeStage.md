# Class: life stage


A stage of development or growth of an organism, including post-natal adult stages

URI: [http://bioentity.io/vocab/LifeStage](http://bioentity.io/vocab/LifeStage)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity]^-\[LifeStage|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[LifeStage]-%20related%20to(i)%20%3F>\[NamedThing],%20\[LifeStage]-%20in%20taxon%20%3F>\[OrganismTaxon],%20\[LifeStage]uses%20-.->\[ThingWithTaxon])
## Mappings

 * [UBERON:0000105](http://purl.obolibrary.org/obo/UBERON_0000105)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

## Used in

## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
