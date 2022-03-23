---
parent: Class Mixins
title: biolink:ChemicalToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ChemicalToEntityAssociationMixin


An interaction between a chemical entity and another entity

URI: [biolink:ChemicalToEntityAssociationMixin](https://w3id.org/biolink/vocab/ChemicalToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntityOrGeneOrGeneProduct]%3Csubject%201..1-++[ChemicalToEntityAssociationMixin],[ChemicalToPathwayAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToGeneAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToChemicalAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]%5E-[ChemicalToEntityAssociationMixin],[ChemicalToPathwayAssociation],[ChemicalToGeneAssociation],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalToChemicalAssociation],[ChemicalEntityToEntityAssociationMixin],[ChemicalEntityOrGeneOrGeneProduct])

---


## Parents

 *  is_a: [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) - An interaction between a chemical entity and another entity

## Mixin for

 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) (mixin)  - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) (mixin)  - An interaction between a chemical entity and a gene or gene product.
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) (mixin)  - An interaction between a chemical entity and a biological process or pathway.

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
