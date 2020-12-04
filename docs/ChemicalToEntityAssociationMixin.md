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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalSubstance]%3Csubject%201..1-%20[ChemicalToEntityAssociationMixin],[ChemicalToPathwayAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToGeneAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToChemicalAssociation]uses%20-.-%3E[ChemicalToEntityAssociationMixin],[ChemicalToPathwayAssociation],[ChemicalToGeneAssociation],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalToChemicalAssociation],[ChemicalSubstance])

---


## Mixin for

 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) (mixin)  - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) (mixin)  - An interaction between a chemical entity and a gene or gene product.
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) (mixin)  - An interaction between a chemical entity and a biological process or pathway.

## Referenced by class


## Attributes


### Own

 * [chemical to entity association mixin➞subject](chemical_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: the chemical substance or entity that is an interactor
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Domain for slot:

 * [chemical to entity association mixin➞subject](chemical_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: the chemical substance or entity that is an interactor
    * range: [ChemicalSubstance](ChemicalSubstance.md)
