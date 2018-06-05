# Class: treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: http://bioentity.io/vocab/Treatment

![img](http://yuml.me/diagram/nofunky/class/\[Environment]^-\[Treatment],%20\[Treatment]-%20treats>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20has_exposure_parts%20+>\[DrugExposure],%20)
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://semanticscience.org/resource/SIO_001398)
## Inheritance

 *  is_a: [environment](Environment.md)
## Children

## Used in

## Fields

 * _[treats](treats.md)_
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
 * _[has exposure parts](has_exposure_parts.md)_
    * range: [drug exposure](DrugExposure.md)* [required]
