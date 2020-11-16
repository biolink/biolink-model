---
parent: Mixins
title: biolink:EntityToDiseaseAssociation
grand_parent: Classes
layout: default
---

# Class: EntityToDiseaseAssociation


mixin class for any association whose object (target node) is a disease

URI: [biolink:EntityToDiseaseAssociation](https://w3id.org/biolink/vocab/EntityToDiseaseAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[EntityToFeatureOrDiseaseQualifiers],[Disease]%3Cobject%201..1-%20[EntityToDiseaseAssociation],[VariantToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[VariantAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[GenotypeToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[GeneToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[CellLineAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],[EntityToFeatureOrDiseaseQualifiers]%5E-[EntityToDiseaseAssociation],[VariantToDiseaseAssociation],[VariantAsAModelOfDiseaseAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[GenotypeToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[GeneToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[Disease],[CellLineAsAModelOfDiseaseAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) (mixin) 
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) (mixin) 
 * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) (mixin) 
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [entity to disease association➞object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
    * Example:    

### Inherited from entity to feature or disease qualifiers:

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

 * [entity to disease association➞object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
    * Example:    
