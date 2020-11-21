---
parent: Class Mixins
title: biolink:ThingToDiseaseAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ThingToDiseaseAssociationMixin


mixin class for any association whose object (target node) is a disease

URI: [biolink:ThingToDiseaseAssociationMixin](https://w3id.org/biolink/vocab/ThingToDiseaseAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Disease]%3Cobject%201..1-%20[ThingToDiseaseAssociationMixin],[VariantToDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[VariantAsAModelOfDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[OrganismalEntityAsAModelOfDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[GenotypeToDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[GenotypeAsAModelOfDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[GeneToDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[GeneAsAModelOfDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[CellLineAsAModelOfDiseaseAssociation]uses%20-.-%3E[ThingToDiseaseAssociationMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[ThingToDiseaseAssociationMixin],[VariantToDiseaseAssociation],[VariantAsAModelOfDiseaseAssociation],[SeverityValue],[OrganismalEntityAsAModelOfDiseaseAssociation],[Onset],[GenotypeToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[GeneToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[FrequencyValue],[EntityToFeatureOrDiseaseQualifiersMixin],[Disease],[CellLineAsAModelOfDiseaseAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations

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

 * [thing to disease association mixin➞object](thing_to_disease_association_mixin_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
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

 * [thing to disease association mixin➞object](thing_to_disease_association_mixin_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
    * Example:    
