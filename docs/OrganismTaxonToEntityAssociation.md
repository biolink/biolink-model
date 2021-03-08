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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]%3Csubject%201..1-++[OrganismTaxonToEntityAssociation],[OrganismTaxonToOrganismTaxonAssociation]uses%20-.-%3E[OrganismTaxonToEntityAssociation],[OrganismTaxonToEnvironmentAssociation]uses%20-.-%3E[OrganismTaxonToEntityAssociation],[OrganismTaxonToOrganismTaxonAssociation],[OrganismTaxonToEnvironmentAssociation],[OrganismTaxon])

---


## Mixin for

 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) (mixin) 
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) (mixin)  - A relationship between two organism taxon nodes

## Referenced by class


## Attributes


### Own

 * [organism taxon to entity association➞subject](organism_taxon_to_entity_association_subject.md)  <sub>REQ</sub>
     * Description: organism taxon that is the subject of the association
     * range: [OrganismTaxon](OrganismTaxon.md)

### Domain for slot:

 * [organism taxon to entity association➞subject](organism_taxon_to_entity_association_subject.md)  <sub>REQ</sub>
     * Description: organism taxon that is the subject of the association
     * range: [OrganismTaxon](OrganismTaxon.md)
