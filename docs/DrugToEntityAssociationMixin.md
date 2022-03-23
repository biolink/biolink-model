---
parent: Class Mixins
title: biolink:DrugToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: DrugToEntityAssociationMixin


An interaction between a drug and another entity

URI: [biolink:DrugToEntityAssociationMixin](https://w3id.org/biolink/vocab/DrugToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Drug]%3Csubject%201..1-%20[DrugToEntityAssociationMixin],[DrugToGeneAssociation]uses%20-.-%3E[DrugToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]%5E-[DrugToEntityAssociationMixin],[DrugToGeneAssociation],[Drug],[ChemicalEntityToEntityAssociationMixin])

---


## Parents

 *  is_a: [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) - An interaction between a chemical entity and another entity

## Mixin for

 * [DrugToGeneAssociation](DrugToGeneAssociation.md) (mixin)  - An interaction between a drug and a gene or gene product.

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
