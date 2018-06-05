# Class: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: http://bioentity.io/vocab/DiseaseOrPhenotypicFeature

![img](http://yuml.me/diagram/nofunky/class/\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature|treated_by:string%20%3F],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]-%20correlated_with%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20has_biomarker%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20in_taxon%20%3F>\[OrganismTaxon],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon],%20)
## Mappings

## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md)
## Children

 *  child: [phenotypic feature](PhenotypicFeature.md)
 *  child: [disease](Disease.md)
## Used in

 *  class: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) references: [phenotypic feature](PhenotypicFeature.md)
 *  class: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) references: [disease](Disease.md)
## Fields

 * _[correlated with](correlated_with.md) *subsets: translator_minimal*_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [related to](related_to.md)
 * _[has biomarker](has_biomarker.md) *subsets: translator_minimal*_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * __Local__
 * _[treated by](treated_by.md) *subsets: translator_minimal*_
    * _holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition _
    * range: string
    * inherited from: [related to](related_to.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
