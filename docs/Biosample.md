# Class: biosample




URI: http://bioentity.io/vocab/Biosample

![img](http://yuml.me/diagram/nofunky/class/\[OrganismalEntity]^-\[Biosample],%20\[Biosample]^-\[CellLine],%20\[Biosample]-%20in_taxon%20%3F>\[OrganismTaxon],%20\[Biosample]uses%20-.->\[ThingWithTaxon],%20)
## Mappings

 * [SIO:001050](http://semanticscience.org/resource/SIO_001050)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md)
## Children

 *  child: [cell line](CellLine.md)
## Used in

 *  class: [biosample](Biosample.md) references: [cell line](CellLine.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
