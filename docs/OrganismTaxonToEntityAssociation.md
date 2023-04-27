---
parent: Class Mixins
title: biolink:OrganismTaxonToEntityAssociation
grand_parent: Classes
layout: default
---

# Class: OrganismTaxonToEntityAssociation


An association between an organism taxon and another entity

URI: [biolink:OrganismTaxonToEntityAssociation](https://w3id.org/biolink/vocab/OrganismTaxonToEntityAssociation)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]%3Csubject%201..1-%20[OrganismTaxonToEntityAssociation],[OrganismTaxonToOrganismTaxonAssociation]uses%20-.-%3E[OrganismTaxonToEntityAssociation],[OrganismTaxonToEnvironmentAssociation]uses%20-.-%3E[OrganismTaxonToEntityAssociation],[OrganismTaxonToOrganismTaxonAssociation],[OrganismTaxonToEnvironmentAssociation],[OrganismTaxon])

---


## Mixin for

 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) (mixin) 
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) (mixin)  - A relationship between two organism taxon nodes

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
