---
parent: Class Mixins
title: biolink:MaterialSampleToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: MaterialSampleToEntityAssociationMixin


An association between a material sample and something.

URI: [biolink:MaterialSampleToEntityAssociationMixin](https://w3id.org/biolink/MaterialSampleToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MaterialSample]%3Csubject%201..1-%20[MaterialSampleToEntityAssociationMixin],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[MaterialSampleToEntityAssociationMixin],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[MaterialSample])

---


## Mixin for

 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An association between a material sample and a disease or phenotype.

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
