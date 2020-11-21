---
parent: Associations
title: biolink:PairwiseMolecularInteraction
grand_parent: Classes
layout: default
---

# Class: PairwiseMolecularInteraction


An interaction at the molecular level between two physical entities

URI: [biolink:PairwiseMolecularInteraction](https://w3id.org/biolink/vocab/PairwiseMolecularInteraction)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[MolecularEntity]%3Cobject%201..1-%20[PairwiseMolecularInteraction%7Cid:string;predicate:predicate_type;relation:uriorcurie;negated(i):boolean%20%3F],[MolecularEntity]%3Csubject%201..1-%20[PairwiseMolecularInteraction],[OntologyClass]%3Cinteracting%20molecules%20category%200..1-%20[PairwiseMolecularInteraction],[PairwiseGeneToGeneInteraction]%5E-[PairwiseMolecularInteraction],[PairwiseGeneToGeneInteraction],[OntologyClass],[MolecularEntity],[Agent])

---


## Parents

 *  is_a: [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

## Referenced by class


## Attributes


### Own

 * [interacting molecules category](interacting_molecules_category.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
    * Example: MI:1048 smallmolecule-protein
 * [pairwise molecular interaction➞id](pairwise_molecular_interaction_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database such as IMEX.
    * range: [String](types/String.md)
    * Example:    
 * [pairwise molecular interaction➞object](pairwise_molecular_interaction_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise molecular interaction➞predicate](pairwise_molecular_interaction_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [pairwise molecular interaction➞relation](pairwise_molecular_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
    * Example:    
 * [pairwise molecular interaction➞subject](pairwise_molecular_interaction_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)

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

### Domain for slot:

 * [pairwise molecular interaction➞id](pairwise_molecular_interaction_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database such as IMEX.
    * range: [String](types/String.md)
    * Example:    
 * [pairwise molecular interaction➞object](pairwise_molecular_interaction_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise molecular interaction➞predicate](pairwise_molecular_interaction_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [pairwise molecular interaction➞relation](pairwise_molecular_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
    * Example:    
 * [pairwise molecular interaction➞subject](pairwise_molecular_interaction_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
