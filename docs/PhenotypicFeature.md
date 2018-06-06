# Class: phenotypic feature




URI: [http://bioentity.io/vocab/PhenotypicFeature](http://bioentity.io/vocab/PhenotypicFeature)

![img](images/PhenotypicFeature.png)
## Mappings

 * [UPHENO:0001001](http://purl.obolibrary.org/obo/UPHENO_0001001)
 * [SIO:010056](http://semanticscience.org/resource/SIO_010056)
 * [WD:Q169872](http://purl.obolibrary.org/obo/WD_Q169872)
## Inheritance

 *  is_a: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
## Children

## Used in

 *  class: [phenotypic feature](PhenotypicFeature.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[correlated with](correlated_with.md) *subsets: translator_minimal*_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 * _[has biomarker](has_biomarker.md) *subsets: translator_minimal*_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
