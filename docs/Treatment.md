---
layout: default
---

## treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [http://bioentity.io/vocab/Treatment](http://bioentity.io/vocab/Treatment)
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://purl.obolibrary.org/obo/SIO_001398)

## Inheritance

 *  is_a: [environment](Environment.html)

## Children


## Used in

 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [treatment](Treatment.html)

## Fields

 * [treats](treats.html)
    * __range__: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) [required]
    * __Local__
 * [has exposure parts](has_exposure_parts.html)
    * __range__: [drug exposure](DrugExposure.html) [required]
    * __Local__
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
