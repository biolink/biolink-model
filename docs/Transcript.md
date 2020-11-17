---
parent: Entities
title: biolink:Transcript
grand_parent: Classes
layout: default
---

# Class: Transcript


An RNA synthesized on a DNA or RNA template by an RNA polymerase

URI: [biolink:Transcript](https://w3id.org/biolink/vocab/Transcript)

SO:0000673
{: .mapping-label }

SIO:010450
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TranscriptToGeneRelationship],[ExonToTranscriptRelationship]-%20object%201..1%3E[Transcript%7Cname(i):label_type;description(i):narrative_text%20%3F;synonym(i):label_type%20%2A;xref(i):iri_type%20%2A;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B],[TranscriptToGeneRelationship]-%20subject%201..1%3E[Transcript],[GeneProduct]%5E-[Transcript],[OrganismTaxon],[MolecularEntity],[GeneProduct],[ExonToTranscriptRelationship])

---


## Parents

 *  is_a: [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

## Referenced by class

 *  **[MolecularEntity](MolecularEntity.md)** *[affects splicing of](affects_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases splicing of](decreases_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)** *[exon to transcript relationship➞object](exon_to_transcript_relationship_object.md)*  <sub>REQ</sub>  **[Transcript](Transcript.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases splicing of](increases_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship➞subject](transcript_to_gene_relationship_subject.md)*  <sub>REQ</sub>  **[Transcript](Transcript.md)**

## Attributes


### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SO:0000673 |
|  | | SIO:010450 |

