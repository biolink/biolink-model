---
parent: Associations
title: biolink:GeneToGeneProductRelationship
grand_parent: Classes
layout: default
---

# Class: GeneToGeneProductRelationship


A gene is transcribed and potentially translated to a gene product

URI: [biolink:GeneToGeneProductRelationship](https://w3id.org/biolink/vocab/GeneToGeneProductRelationship)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SequenceFeatureRelationship],[Publication],[Provider],[OntologyClass],[GeneProduct]%3Cobject%201..1-%20[GeneToGeneProductRelationship%7Crelation:uriorcurie;id(i):string;predicate(i):predicate_type;negated(i):boolean%20%3F],[Gene]%3Csubject%201..1-%20[GeneToGeneProductRelationship],[SequenceFeatureRelationship]%5E-[GeneToGeneProductRelationship],[GeneProduct],[Gene])

---


## Parents

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene

## Referenced by class


## Attributes


### Own

 * [gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)  <sub>REQ</sub>
    * range: [GeneProduct](GeneProduct.md)
 * [gene to gene product relationship➞relation](gene_to_gene_product_relationship_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)

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

 * [gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)  <sub>REQ</sub>
    * range: [GeneProduct](GeneProduct.md)
 * [gene to gene product relationship➞relation](gene_to_gene_product_relationship_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
