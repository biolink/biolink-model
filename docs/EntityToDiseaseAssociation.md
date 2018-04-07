---
layout: default
---

## entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [http://bioentity.io/vocab/EntityToDiseaseAssociation](http://bioentity.io/vocab/EntityToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky/class/[entity to disease association]-frequency qualifier >[frequency value], [attribute]^-[frequency value], [entity to disease association]-severity qualifier >[severity value], [attribute]^-[severity value], [entity to disease association]-onset qualifier >[onset], [attribute]^-[onset])
## Mappings


## Inheritance


## Children

 *  mixin: [gene to disease association](GeneToDiseaseAssociation.html)
 *  mixin: [variant to disease association](VariantToDiseaseAssociation.html)
 *  mixin: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html)


## Fields

 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * __Local__
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * __Local__
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * __Local__
