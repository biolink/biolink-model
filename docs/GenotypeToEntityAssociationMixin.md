---
parent: Class Mixins
title: biolink:GenotypeToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: GenotypeToEntityAssociationMixin




URI: [biolink:GenotypeToEntityAssociationMixin](https://w3id.org/biolink/GenotypeToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Genotype]%3Csubject%201..1-%20[GenotypeToEntityAssociationMixin],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[GenotypeToEntityAssociationMixin],[GenotypeToDiseaseAssociation]uses%20-.-%3E[GenotypeToEntityAssociationMixin],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToDiseaseAssociation],[Genotype])

---


## Mixin for

 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) (mixin) 
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) (mixin)  - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment

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
