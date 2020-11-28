---
parent: Associations
title: biolink:ChemicalToChemicalDerivationAssociation
grand_parent: Classes
layout: default
---

# Class: ChemicalToChemicalDerivationAssociation


A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
  IF
  R has-input C1 AND
  R has-output C2 AND
  R enabled-by P AND
  R type Reaction
  THEN
  C1 derives-into C2 <<change is catalyzed by P>>

URI: [biolink:ChemicalToChemicalDerivationAssociation](https://w3id.org/biolink/vocab/ChemicalToChemicalDerivationAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[MacromolecularMachine],[ChemicalSubstance]%3Cobject%201..1-%20[ChemicalToChemicalDerivationAssociation%7Cpredicate:predicate_type;id(i):string;relation(i):uriorcurie;negated(i):boolean%20%3F],[ChemicalSubstance]%3Csubject%201..1-%20[ChemicalToChemicalDerivationAssociation],[MacromolecularMachine]%3Cchange%20is%20catalyzed%20by%200..%2A-%20[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation]%5E-[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation],[ChemicalSubstance],[Attribute],[Agent])

---


## Parents

 *  is_a: [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.

## Referenced by class


## Attributes


### Own

 * [chemical to chemical derivation association➞change is catalyzed by](chemical_to_chemical_derivation_association_change_is_catalyzed_by.md)  <sub>0..*</sub>
    * Description: this connects the derivation edge to the molecular entity that catalyzes the reaction that causes the subject chemical to transform into the object chemical
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)  <sub>REQ</sub>
    * Description: the downstream chemical entity
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [chemical to chemical derivation association➞predicate](chemical_to_chemical_derivation_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)  <sub>REQ</sub>
    * Description: the upstream chemical entity
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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

 * [chemical to chemical derivation association➞change is catalyzed by](chemical_to_chemical_derivation_association_change_is_catalyzed_by.md)  <sub>0..*</sub>
    * Description: this connects the derivation edge to the molecular entity that catalyzes the reaction that causes the subject chemical to transform into the object chemical
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)  <sub>REQ</sub>
    * Description: the downstream chemical entity
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [chemical to chemical derivation association➞predicate](chemical_to_chemical_derivation_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)  <sub>REQ</sub>
    * Description: the upstream chemical entity
    * range: [ChemicalSubstance](ChemicalSubstance.md)
