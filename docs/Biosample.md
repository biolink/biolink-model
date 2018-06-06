# Class: biosample




URI: [http://bioentity.io/vocab/Biosample](http://bioentity.io/vocab/Biosample)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity]^-\[Biosample|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[Biosample]^-\[CellLine],%20\[Biosample]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Biosample]-%20in%20taxon%20%3F>\[OrganismTaxon],%20\[Biosample]uses%20-.->\[ThingWithTaxon])
## Mappings

 * [SIO:001050](http://semanticscience.org/resource/SIO_001050)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [cell line](CellLine.md)
## Used in

 *  class: [biosample](Biosample.md) references: [cell line](CellLine.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
