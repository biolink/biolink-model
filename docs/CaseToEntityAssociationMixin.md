---
parent: Class Mixins
title: biolink:CaseToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: CaseToEntityAssociationMixin


An abstract association for use where the case is the subject

URI: [biolink:CaseToEntityAssociationMixin](https://w3id.org/biolink/CaseToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Case]%3Csubject%201..1-%20[CaseToEntityAssociationMixin],[CaseToPhenotypicFeatureAssociation]uses%20-.-%3E[CaseToEntityAssociationMixin],[CaseToPhenotypicFeatureAssociation],[Case])

---


## Mixin for

 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.

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
