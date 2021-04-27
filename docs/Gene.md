---
parent: Entities
title: biolink:Gene
grand_parent: Classes
layout: default
---

# Class: Gene


A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.

URI: [biolink:Gene](https://w3id.org/biolink/vocab/Gene)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToGeneAssociation],[TranscriptToGeneRelationship],[Transcript],[SequenceVariant],[OrganismTaxon],[NamedThing],[GenotypeToGeneAssociation],[GenomicEntity],[GeneToGeneProductRelationship],[GeneProductMixin],[GeneOrGeneProduct],[GeneToGeneProductRelationship]-%20subject%201..1%3E[Gene%7Csymbol:string%20%3F;synonym:label_type%20%2A;xref:iri_type%20%2A;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeToGeneAssociation]-%20object%201..1%3E[Gene],[SequenceVariant]-%20has%20gene(i)%200..%2A%3E[Gene],[GeneGroupingMixin]-%20has%20gene%20or%20gene%20product%200..%2A%3E[Gene],[SequenceVariant]-%20has%20gene%200..%2A%3E[Gene],[TranscriptToGeneRelationship]-%20object%201..1%3E[Gene],[VariantToGeneAssociation]-%20object%201..1%3E[Gene],[Gene]uses%20-.-%3E[GeneOrGeneProduct],[GenomicEntity]%5E-[Gene],[GeneGroupingMixin],[DiseaseOrPhenotypicFeature],[Attribute],[Agent])

---


## Identifier prefixes

 * NCBIGene
 * ENSEMBL
 * HGNC
 * MGI
 * ZFIN
 * dictyBase
 * WB
 * WormBase
 * FB
 * FB
 * RGD
 * SGD
 * POMBASE
 * OMIM
 * KEGG.GENE
 * UMLS

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Uses Mixins

 *  mixin: [GeneOrGeneProduct](GeneOrGeneProduct.md) - A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another

## Referenced by class

 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[condition associated with gene](condition_associated_with_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GeneProductMixin](GeneProductMixin.md)** *[gene product of](gene_product_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞object](genotype_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[NamedThing](NamedThing.md)** *[has gene](has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[NamedThing](NamedThing.md)** *[has gene or gene product](has_gene_or_gene_product.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is frameshift variant of](is_frameshift_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is missense variant of](is_missense_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nearby variant of](is_nearby_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is non coding variant of](is_non_coding_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nonsense variant of](is_nonsense_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is splice site variant of](is_splice_site_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is synonymous variant of](is_synonymous_variant_of.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[sequence variant➞has gene](sequence_variant_has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[Transcript](Transcript.md)** *[transcribed from](transcribed_from.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship➞object](transcript_to_gene_relationship_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[VariantToGeneAssociation](VariantToGeneAssociation.md)** *[variant to gene association➞object](variant_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
     * Description: connects any entity to an attribute
     * range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
     * Description: connects a genomic feature to its sequence
     * range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
     * range: [NamedThing](NamedThing.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | locus |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | SO:0000704 |
|  | | SIO:010035 |
|  | | WIKIDATA:Q7187 |

