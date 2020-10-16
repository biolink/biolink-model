---
parent: Associations
title: biolink:GenotypeToGenotypePartAssociation
grand_parent: Classes
layout: default
---

# Class: GenotypeToGenotypePartAssociation


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [biolink:GenotypeToGenotypePartAssociation](https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[Genotype]%3Cobject%201..1-%20[GenotypeToGenotypePartAssociation%7Crelation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[Genotype]%3Csubject%201..1-%20[GenotypeToGenotypePartAssociation],[Association]%5E-[GenotypeToGenotypePartAssociation],[Genotype],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * Description: child genotype
    * range: [Genotype](Genotype.md)
 * [genotype to genotype part association➞relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * Description: parent genotype
    * range: [Genotype](Genotype.md)

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

 * [genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * Description: child genotype
    * range: [Genotype](Genotype.md)
 * [genotype to genotype part association➞relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * Description: parent genotype
    * range: [Genotype](Genotype.md)
