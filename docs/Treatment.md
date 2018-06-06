# Class: treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [http://bioentity.io/vocab/Treatment](http://bioentity.io/vocab/Treatment)

![img](images/Treatment.png)
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://semanticscience.org/resource/SIO_001398)
## Inheritance

 *  is_a: [environment](Environment.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
## Children

## Used in

## Fields

 * _[treats](treats.md)_
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * __Local__
 * _[has exposure parts](has_exposure_parts.md)_
    * range: [drug exposure](DrugExposure.md)* [required]
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
