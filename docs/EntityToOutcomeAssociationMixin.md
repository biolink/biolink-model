---
parent: Class Mixins
title: biolink:EntityToOutcomeAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToOutcomeAssociationMixin


An association between some entity and an outcome

URI: [biolink:EntityToOutcomeAssociationMixin](https://w3id.org/biolink/vocab/EntityToOutcomeAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Outcome],[Outcome]%3Cobject%201..1-++[EntityToOutcomeAssociationMixin],[ExposureEventToOutcomeAssociation]uses%20-.-%3E[EntityToOutcomeAssociationMixin],[ExposureEventToOutcomeAssociation])

---


## Mixin for

 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) (mixin)  - An association between an exposure event and an outcome.

## Referenced by class


## Attributes


### Own

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
