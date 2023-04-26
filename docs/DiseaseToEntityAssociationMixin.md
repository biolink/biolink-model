---
parent: Class Mixins
title: biolink:DiseaseToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: DiseaseToEntityAssociationMixin




URI: [biolink:DiseaseToEntityAssociationMixin](https://w3id.org/biolink/DiseaseToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Disease]%3Csubject%201..1-%20[DiseaseToEntityAssociationMixin],[DiseaseToPhenotypicFeatureAssociation]uses%20-.-%3E[DiseaseToEntityAssociationMixin],[DiseaseToExposureEventAssociation]uses%20-.-%3E[DiseaseToEntityAssociationMixin],[DiseaseToPhenotypicFeatureAssociation],[DiseaseToExposureEventAssociation],[Disease])

---


## Mixin for

 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) (mixin)  - An association between an exposure event and a disease.
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.

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
