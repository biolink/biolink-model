---
parent: Class Mixins
title: biolink:VariantToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: VariantToEntityAssociationMixin




URI: [biolink:VariantToEntityAssociationMixin](https://w3id.org/biolink/VariantToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceVariant]%3Csubject%201..1-%20[VariantToEntityAssociationMixin],[VariantToPopulationAssociation]uses%20-.-%3E[VariantToEntityAssociationMixin],[VariantToPhenotypicFeatureAssociation]uses%20-.-%3E[VariantToEntityAssociationMixin],[VariantToGeneAssociation]uses%20-.-%3E[VariantToEntityAssociationMixin],[VariantToDiseaseAssociation]uses%20-.-%3E[VariantToEntityAssociationMixin],[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToGeneAssociation],[VariantToDiseaseAssociation],[SequenceVariant])

---


## Mixin for

 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 
 * [VariantToGeneAssociation](VariantToGeneAssociation.md) (mixin)  - An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) (mixin) 
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Local names:** | | variant annotation (ga4gh) |

