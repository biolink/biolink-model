---
parent: Associations
title: biolink:MaterialSampleToThingAssociation
grand_parent: Classes
layout: default
---

# Class: MaterialSampleToThingAssociation


An association between a material sample and something

URI: [biolink:MaterialSampleToThingAssociation](https://w3id.org/biolink/vocab/MaterialSampleToThingAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[NamedThing],[MaterialSample]%3Csubject%201..1-%20[MaterialSampleToThingAssociation%7Cid(i):string;predicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[MaterialSampleToThingAssociation],[Association]%5E-[MaterialSampleToThingAssociation],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[MaterialSample],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Mixin for

 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An association between a material sample and a disease or phenotype

## Referenced by class


## Attributes


### Own

 * [material sample to thing association➞subject](material_sample_to_thing_association_subject.md)  <sub>REQ</sub>
    * Description: the material sample being described
    * range: [MaterialSample](MaterialSample.md)

### Inherited from association:

 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)

### Domain for slot:

 * [material sample to thing association➞subject](material_sample_to_thing_association_subject.md)  <sub>REQ</sub>
    * Description: the material sample being described
    * range: [MaterialSample](MaterialSample.md)
