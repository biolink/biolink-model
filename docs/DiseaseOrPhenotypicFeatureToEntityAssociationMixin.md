---
parent: Class Mixins
title: biolink:DiseaseOrPhenotypicFeatureToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: DiseaseOrPhenotypicFeatureToEntityAssociationMixin




URI: [biolink:DiseaseOrPhenotypicFeatureToEntityAssociationMixin](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]%3Csubject%201..1-%20[DiseaseOrPhenotypicFeatureToEntityAssociationMixin],[DiseaseOrPhenotypicFeatureToLocationAssociation]uses%20-.-%3E[DiseaseOrPhenotypicFeatureToEntityAssociationMixin],[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation]uses%20-.-%3E[DiseaseOrPhenotypicFeatureToEntityAssociationMixin],[DiseaseOrPhenotypicFeatureToLocationAssociation],[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation],[DiseaseOrPhenotypicFeature])

---


## Mixin for

 * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) (mixin)  - An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance.
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) (mixin)  - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.

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
