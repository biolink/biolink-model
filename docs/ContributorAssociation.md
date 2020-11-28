---
parent: Associations
title: biolink:ContributorAssociation
grand_parent: Classes
layout: default
---

# Class: ContributorAssociation


Any association between an entity (such as a publication) and various agents that contribute to its realisation

URI: [biolink:ContributorAssociation](https://w3id.org/biolink/vocab/ContributorAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[InformationContentEntity],[OntologyClass]%3Cqualifiers%200..%2A-%20[ContributorAssociation%7Cpredicate:predicate_type;id(i):string;relation(i):uriorcurie;negated(i):boolean%20%3F],[Agent]%3Cobject%201..1-%20[ContributorAssociation],[InformationContentEntity]%3Csubject%201..1-%20[ContributorAssociation],[Association]%5E-[ContributorAssociation],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [contributor association➞object](contributor_association_object.md)  <sub>REQ</sub>
    * Description: agent helping to realise the given entity (e.g. such as a publication)
    * range: [Agent](Agent.md)
 * [contributor association➞predicate](contributor_association_predicate.md)  <sub>REQ</sub>
    * Description: generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'
    * range: [PredicateType](types/PredicateType.md)
 * [contributor association➞qualifiers](contributor_association_qualifiers.md)  <sub>0..*</sub>
    * Description: this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'
    * range: [OntologyClass](OntologyClass.md)
 * [contributor association➞subject](contributor_association_subject.md)  <sub>REQ</sub>
    * Description: information content entity which an agent has helped realise
    * range: [InformationContentEntity](InformationContentEntity.md)

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
    * range: [Agent](Agent.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Domain for slot:

 * [contributor association➞object](contributor_association_object.md)  <sub>REQ</sub>
    * Description: agent helping to realise the given entity (e.g. such as a publication)
    * range: [Agent](Agent.md)
 * [contributor association➞predicate](contributor_association_predicate.md)  <sub>REQ</sub>
    * Description: generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'
    * range: [PredicateType](types/PredicateType.md)
 * [contributor association➞qualifiers](contributor_association_qualifiers.md)  <sub>0..*</sub>
    * Description: this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'
    * range: [OntologyClass](OntologyClass.md)
 * [contributor association➞subject](contributor_association_subject.md)  <sub>REQ</sub>
    * Description: information content entity which an agent has helped realise
    * range: [InformationContentEntity](InformationContentEntity.md)
