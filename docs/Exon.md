---
parent: Classes
title: biolink:Exon
grand_parent: Browse Biolink Model
layout: default
---

# Class: Exon


A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing

URI: [biolink:Exon](https://w3id.org/biolink/vocab/Exon)

SO:0000147
{: .mapping-label }

SIO:010445
{: .mapping-label }

WIKIDATA:Q373027
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[GenomicEntity],[ExonToTranscriptRelationship],[ExonToTranscriptRelationship]-%20subject%201..1%3E[Exon%7Chas_biological_sequence(i):biological_sequence%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[GenomicEntity]%5E-[Exon])

---


## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)** *[exon to transcript relationship➞subject](exon_to_transcript_relationship_subject.md)*  <sub>REQ</sub>  **[Exon](Exon.md)**

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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
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
| **Mappings:** | | SO:0000147 |
|  | | SIO:010445 |
|  | | WIKIDATA:Q373027 |

