---
parent: Classes
title: biolink:Exon
grand_parent: Browse Biolink Model
---

# Type: Exon


A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing

URI: [biolink:Exon](https://w3id.org/biolink/vocab/Exon)

SO:0000147
{: .mapping-label }

SIO:010445
{: .mapping-label }

WD:Q373027
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Exon&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExonToTranscriptRelationship]-%20subject%201..1>\[Exon],%20\[GenomicEntity]^-\[Exon])

---


## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)** *[exon to transcript relationship➞subject](exon_to_transcript_relationship_subject.md)*  <sub>REQ</sub>  **[Exon](Exon.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SO:0000147 |
|  | | SIO:010445 |
|  | | WD:Q373027 |

