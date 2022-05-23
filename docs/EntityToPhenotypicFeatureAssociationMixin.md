---
parent: Class Mixins
title: biolink:EntityToPhenotypicFeatureAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToPhenotypicFeatureAssociationMixin




URI: [biolink:EntityToPhenotypicFeatureAssociationMixin](https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[PhenotypicFeature],[Onset],[PhenotypicFeature]%3Cobject%201..1-%20[EntityToPhenotypicFeatureAssociationMixin%7Cfrequency_qualifier(i):frequency_value%20%3F],[BiologicalSex]%3Csex%20qualifier%200..1-%20[EntityToPhenotypicFeatureAssociationMixin],[VariantToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[GeneToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[ExposureEventToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[DiseaseToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[CaseToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[BehaviorToBehavioralFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociationMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[EntityToPhenotypicFeatureAssociationMixin],[VariantToPhenotypicFeatureAssociation],[GenotypeToPhenotypicFeatureAssociation],[GeneToPhenotypicFeatureAssociation],[ExposureEventToPhenotypicFeatureAssociation],[EntityToFeatureOrDiseaseQualifiersMixin],[DiseaseToPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation],[BiologicalSex],[BehaviorToBehavioralFeatureAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.

## Mixin for

 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) (mixin)  - An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) (mixin)  - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) (mixin) 
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) (mixin)  - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [sex qualifier](sex_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * Range: [BiologicalSex](BiologicalSex.md)

### Inherited from entity to feature or disease qualifiers mixin:

 * [severity qualifier](severity_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * Range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * Range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * Range: [FrequencyValue](types/FrequencyValue.md)

### Domain for slot:

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
