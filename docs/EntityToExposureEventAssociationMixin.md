---
parent: Class Mixins
title: biolink:EntityToExposureEventAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToExposureEventAssociationMixin


An association between some entity and an exposure event.

URI: [biolink:EntityToExposureEventAssociationMixin](https://w3id.org/biolink/EntityToExposureEventAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEvent],[ExposureEvent]%3Cobject%201..1-%20[EntityToExposureEventAssociationMixin],[DiseaseToExposureEventAssociation]uses%20-.-%3E[EntityToExposureEventAssociationMixin],[DiseaseToExposureEventAssociation])

---


## Mixin for

 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) (mixin)  - An association between an exposure event and a disease.

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
