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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Drug]%3Csubject%201..1-%20[DrugToEntityAssociationMixin],[DrugToGeneAssociation]uses%20-.-%3E[DrugToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]%5E-[DrugToEntityAssociationMixin],[DrugToGeneAssociation],[Drug],[ChemicalEntityToEntityAssociationMixin])

---


## Parents

 *  is_a: [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) - An interaction between a chemical entity and another entity

## Mixin for

 * [DrugToGeneAssociation](DrugToGeneAssociation.md) (mixin)  - An interaction between a drug and a gene or gene product.

## Referenced by class


## Attributes


### Own

 * [drug to entity association mixin➞subject](drug_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
     * Description: the drug that is an interactor
     * Range: [Drug](Drug.md)

### Domain for slot:

 * [drug to entity association mixin➞subject](drug_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
     * Description: the drug that is an interactor
     * Range: [Drug](Drug.md)
