---
parent: Associations
title: biolink:GenotypeToVariantAssociation
grand_parent: Classes
layout: default
---

# Class: GenotypeToVariantAssociation


Any association between a genotype and a sequence variant.

URI: [biolink:GenotypeToVariantAssociation](https://w3id.org/biolink/vocab/GenotypeToVariantAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SequenceVariant],[Publication],[OntologyClass],[SequenceVariant]%3Cobject%201..1-%20[GenotypeToVariantAssociation%7Cpredicate:predicate_type;id(i):string;relation(i):uriorcurie;negated(i):boolean%20%3F],[Genotype]%3Csubject%201..1-%20[GenotypeToVariantAssociation],[Association]%5E-[GenotypeToVariantAssociation],[Genotype],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [genotype to variant association➞object](genotype_to_variant_association_object.md)  <sub>REQ</sub>
    * Description: gene implicated in genotype
    * range: [SequenceVariant](SequenceVariant.md)
 * [genotype to variant association➞predicate](genotype_to_variant_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect genotype to gene
    * range: [PredicateType](types/PredicateType.md)
 * [genotype to variant association➞subject](genotype_to_variant_association_subject.md)  <sub>REQ</sub>
    * Description: parent genotype
    * range: [Genotype](Genotype.md)

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

 * [genotype to variant association➞object](genotype_to_variant_association_object.md)  <sub>REQ</sub>
    * Description: gene implicated in genotype
    * range: [SequenceVariant](SequenceVariant.md)
 * [genotype to variant association➞predicate](genotype_to_variant_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect genotype to gene
    * range: [PredicateType](types/PredicateType.md)
 * [genotype to variant association➞subject](genotype_to_variant_association_subject.md)  <sub>REQ</sub>
    * Description: parent genotype
    * range: [Genotype](Genotype.md)
