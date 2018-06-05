# Class: individual organism




URI: http://bioentity.io/vocab/IndividualOrganism

![img](http://yuml.me/diagram/nofunky/class/\[OrganismalEntity]^-\[IndividualOrganism],%20\[IndividualOrganism]^-\[Case],%20\[IndividualOrganism]-%20in_taxon%20%3F>\[OrganismTaxon],%20\[IndividualOrganism]uses%20-.->\[ThingWithTaxon],%20)
## Mappings

 * [SIO:010000](http://semanticscience.org/resource/SIO_010000)
 * [WD:Q795052](http://purl.obolibrary.org/obo/WD_Q795052)
 * [NCBITaxon:1](http://purl.obolibrary.org/obo/NCBITaxon_1)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md)
## Children

 *  child: [case](Case.md)
## Used in

 *  class: [individual organism](IndividualOrganism.md) references: [case](Case.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
