---
parent: Class Mixins
title: biolink:EntityToFeatureOrDiseaseQualifiers
grand_parent: Classes
layout: default
---

# Class: EntityToFeatureOrDiseaseQualifiers


Qualifiers for entity to disease or phenotype associations

URI: [biolink:EntityToFeatureOrDiseaseQualifiers](https://w3id.org/biolink/vocab/EntityToFeatureOrDiseaseQualifiers)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[FrequencyQualifierMixin],[Onset]%3Conset%20qualifier%200..1-%20[EntityToFeatureOrDiseaseQualifiers],[SeverityValue]%3Cseverity%20qualifier%200..1-%20[EntityToFeatureOrDiseaseQualifiers],[EntityToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToFeatureOrDiseaseQualifiers],[EntityToFeatureOrDiseaseQualifiers]%5E-[EntityToDiseaseAssociation],[FrequencyQualifierMixin]%5E-[EntityToFeatureOrDiseaseQualifiers],[EntityToPhenotypicFeatureAssociation],[EntityToDiseaseAssociation])

---


## Parents

 *  is_a: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations

## Children

 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease

## Mixin for

 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
