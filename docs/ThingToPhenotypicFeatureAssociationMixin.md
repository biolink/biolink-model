---
parent: Class Mixins
title: biolink:ThingToPhenotypicFeatureAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ThingToPhenotypicFeatureAssociationMixin




URI: [biolink:ThingToPhenotypicFeatureAssociationMixin](https://w3id.org/biolink/vocab/ThingToPhenotypicFeatureAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature]%3Cobject%201..1-%20[ThingToPhenotypicFeatureAssociationMixin%7Cdescription:narrative_text%20%3F],[BiologicalSex]%3Csex%20qualifier%200..1-++[ThingToPhenotypicFeatureAssociationMixin],[VariantToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[GeneToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[ExposureEventToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[DiseaseToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[CaseToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[ThingToPhenotypicFeatureAssociationMixin],[VariantToPhenotypicFeatureAssociation],[SeverityValue],[PhenotypicFeature],[Onset],[GenotypeToPhenotypicFeatureAssociation],[GeneToPhenotypicFeatureAssociation],[FrequencyValue],[ExposureEventToPhenotypicFeatureAssociation],[EntityToFeatureOrDiseaseQualifiersMixin],[DiseaseToPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation],[BiologicalSex])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.

## Mixin for

 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) (mixin)  - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) (mixin) 
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) (mixin)  - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)
 * [thing to phenotypic feature association mixin➞description](thing_to_phenotypic_feature_association_mixin_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [thing to phenotypic feature association mixin➞object](thing_to_phenotypic_feature_association_mixin_object.md)  <sub>REQ</sub>
    * Description: phenotypic class
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * Example:    
    * Example:    
    * Example:    

### Inherited from entity to feature or disease qualifiers mixin:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)

### Domain for slot:

 * [thing to phenotypic feature association mixin➞description](thing_to_phenotypic_feature_association_mixin_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [thing to phenotypic feature association mixin➞object](thing_to_phenotypic_feature_association_mixin_object.md)  <sub>REQ</sub>
    * Description: phenotypic class
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * Example:    
    * Example:    
    * Example:    
