---
parent: Class Mixins
title: biolink:GeneToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: GeneToEntityAssociationMixin




URI: [biolink:GeneToEntityAssociationMixin](https://w3id.org/biolink/vocab/GeneToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneOrGeneProduct]%3Csubject%201..1-++[GeneToEntityAssociationMixin],[GeneToPhenotypicFeatureAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[GeneToPathwayAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[GeneToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[GeneToDiseaseAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[DruggableGeneToDiseaseAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[CorrelatedGeneToDiseaseAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[CausalGeneToDiseaseAssociation]uses%20-.-%3E[GeneToEntityAssociationMixin],[GeneToPhenotypicFeatureAssociation],[GeneToPathwayAssociation],[GeneToDiseaseOrPhenotypicFeatureAssociation],[GeneToDiseaseAssociation],[GeneOrGeneProduct],[DruggableGeneToDiseaseAssociation],[CorrelatedGeneToDiseaseAssociation],[CausalGeneToDiseaseAssociation])

---


## Mixin for

 * [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) (mixin) 
 * [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) (mixin) 
 * [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) (mixin) 
 * [GeneToPathwayAssociation](GeneToPathwayAssociation.md) (mixin)  - An interaction between a gene or gene product and a biological process or pathway.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) (mixin) 

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