---
parent: Class Mixins
title: biolink:ChemicalEntityToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ChemicalEntityToEntityAssociationMixin


An interaction between a chemical entity and another entity

URI: [biolink:ChemicalEntityToEntityAssociationMixin](https://w3id.org/biolink/ChemicalEntityToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DrugToEntityAssociationMixin],[ChemicalToEntityAssociationMixin],[ChemicalEntityOrGeneOrGeneProduct]%3Csubject%201..1-++[ChemicalEntityToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]%5E-[DrugToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]%5E-[ChemicalToEntityAssociationMixin],[ChemicalEntityOrGeneOrGeneProduct])

---


## Children

 * [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)
 * [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) - An interaction between a drug and another entity

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
