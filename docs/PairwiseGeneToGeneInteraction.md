---
parent: Classes
title: biolink:PairwiseGeneToGeneInteraction
grand_parent: Browse Biolink Model
layout: default
---

# Type: PairwiseGeneToGeneInteraction


An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

URI: [biolink:PairwiseGeneToGeneInteraction](https://w3id.org/biolink/vocab/PairwiseGeneToGeneInteraction)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[PairwiseInteractionAssociation],[PairwiseGeneToGeneInteraction%7Crelation:uriorcurie;id(i):string;negated(i):boolean%20%3F]uses%20-.-%3E[PairwiseInteractionAssociation],[GeneToGeneAssociation]%5E-[PairwiseGeneToGeneInteraction],[OntologyClass],[GeneToGeneAssociation],[GeneOrGeneProduct])

---


## Parents

 *  is_a: [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.

## Uses Mixins

 *  mixin: [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities

## Referenced by class


## Attributes


### Own

 * [pairwise gene to gene interaction➞relation](pairwise_gene_to_gene_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)

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

### Inherited from gene to gene association:

 * [gene to gene association➞subject](gene_to_gene_association_subject.md)  <sub>REQ</sub>
    * Description: the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [gene to gene association➞object](gene_to_gene_association_object.md)  <sub>REQ</sub>
    * Description: the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

### Inherited from pairwise interaction association:

 * [pairwise interaction association➞subject](pairwise_interaction_association_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise interaction association➞id](pairwise_interaction_association_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database such as IMEX.
    * range: [String](types/String.md)
 * [pairwise interaction association➞relation](pairwise_interaction_association_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [pairwise interaction association➞object](pairwise_interaction_association_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise interaction association➞interacting molecules category](pairwise_interaction_association_interacting_molecules_category.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)

### Domain for slot:

 * [pairwise gene to gene interaction➞relation](pairwise_gene_to_gene_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
