---
parent: Classes
title: biolink:Gene
grand_parent: Browse Biolink Model
layout: default
---

# Type: Gene




URI: [biolink:Gene](https://w3id.org/biolink/vocab/Gene)

SO:0000704
{: .mapping-label }

SIO:010035
{: .mapping-label }

WIKIDATA:Q7187
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TranscriptToGeneRelationship],[SequenceVariant],[OrganismTaxon],[NamedThing],[GenotypeToGeneAssociation],[GeneToGeneProductRelationship],[GeneOrGeneProduct],[GeneToGeneProductRelationship]-%20subject%201..1%3E[Gene%7Cname(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B],[GenotypeToGeneAssociation]-%20object%201..1%3E[Gene],[SequenceVariant]-%20has%20gene(i)%200..1%3E[Gene],[SequenceVariant]-%20has%20gene%200..%2A%3E[Gene],[TranscriptToGeneRelationship]-%20object%201..1%3E[Gene],[GeneOrGeneProduct]%5E-[Gene])

---


## Identifier prefixes

 * NCBIGene
 * ENSEMBL
 * HGNC
 * UniProtKB
 * MGI
 * ZFIN
 * dictyBase
 * WB
 * WormBase
 * FlyBase
 * FB
 * RGD
 * SGD
 * PomBase

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞object](genotype_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[NamedThing](NamedThing.md)** *[has gene](has_gene.md)*  <sub>OPT</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[sequence variant➞has gene](sequence_variant_has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship➞object](transcript_to_gene_relationship_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from macromolecular machine:

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
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
| **Aliases:** | | locus |
| **Mappings:** | | SO:0000704 |
|  | | SIO:010035 |
|  | | WIKIDATA:Q7187 |

