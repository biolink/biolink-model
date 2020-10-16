---
parent: Classes
title: biolink:PopulationToPopulationAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Class: PopulationToPopulationAssociation


An association between a two populations

URI: [biolink:PopulationToPopulationAssociation](https://w3id.org/biolink/vocab/PopulationToPopulationAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[PopulationOfIndividualOrganisms]%3Cobject%201..1-%20[PopulationToPopulationAssociation%7Crelation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[PopulationOfIndividualOrganisms]%3Csubject%201..1-%20[PopulationToPopulationAssociation],[Association]%5E-[PopulationToPopulationAssociation],[PopulationOfIndividualOrganisms],[OntologyClass],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [population to population association➞object](population_to_population_association_object.md)  <sub>REQ</sub>
    * Description: the population that form the object of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [population to population association➞relation](population_to_population_association_relation.md)  <sub>REQ</sub>
    * Description: A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [population to population association➞subject](population_to_population_association_subject.md)  <sub>REQ</sub>
    * Description: the population that form the subject of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
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

 * [population to population association➞object](population_to_population_association_object.md)  <sub>REQ</sub>
    * Description: the population that form the object of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [population to population association➞relation](population_to_population_association_relation.md)  <sub>REQ</sub>
    * Description: A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [population to population association➞subject](population_to_population_association_subject.md)  <sub>REQ</sub>
    * Description: the population that form the subject of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
