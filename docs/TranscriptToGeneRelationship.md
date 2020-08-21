---
parent: Classes
title: biolink:TranscriptToGeneRelationship
grand_parent: Browse Biolink Model
layout: default
---

# Type: TranscriptToGeneRelationship


A gene is a collection of transcripts

URI: [biolink:TranscriptToGeneRelationship](https://w3id.org/biolink/vocab/TranscriptToGeneRelationship)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Gene]%3Cobject%201..1-%20[TranscriptToGeneRelationship%7Crelation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[Transcript]%3Csubject%201..1-%20[TranscriptToGeneRelationship],[SequenceFeatureRelationship]%5E-[TranscriptToGeneRelationship],[Transcript],[SequenceFeatureRelationship],[Publication],[Provider],[OntologyClass],[Gene])

---


## Parents

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene

## Referenced by class


## Attributes


### Own

 * [transcript to gene relationship➞object](transcript_to_gene_relationship_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [transcript to gene relationship➞subject](transcript_to_gene_relationship_subject.md)  <sub>REQ</sub>
    * range: [Transcript](Transcript.md)

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

 * [transcript to gene relationship➞object](transcript_to_gene_relationship_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [transcript to gene relationship➞subject](transcript_to_gene_relationship_subject.md)  <sub>REQ</sub>
    * range: [Transcript](Transcript.md)
