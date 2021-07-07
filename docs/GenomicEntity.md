---
parent: Class Mixins
title: biolink:GenomicEntity
grand_parent: Classes
layout: default
---

# Class: GenomicEntity




URI: [biolink:GenomicEntity](https://w3id.org/biolink/vocab/GenomicEntity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismTaxon],[SequenceVariant]uses%20-.-%3E[GenomicEntity%7Chas_biological_sequence:biological_sequence%20%3F],[ReagentTargetedGene]uses%20-.-%3E[GenomicEntity],[NucleicAcidEntity]uses%20-.-%3E[GenomicEntity],[Haplotype]uses%20-.-%3E[GenomicEntity],[Genotype]uses%20-.-%3E[GenomicEntity],[GenomicBackgroundExposure]uses%20-.-%3E[GenomicEntity],[Genome]uses%20-.-%3E[GenomicEntity],[Gene]uses%20-.-%3E[GenomicEntity],[ThingWithTaxon]%5E-[GenomicEntity],[SequenceVariant],[ReagentTargetedGene],[NucleicAcidEntity],[Haplotype],[Genotype],[GenomicBackgroundExposure],[Genome],[Gene])

---


## Parents

 *  is_a: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

## Mixin for

 * [Gene](Gene.md) (mixin)  - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
 * [Genome](Genome.md) (mixin)  - A genome is the sum of genetic material within a cell or virion.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [Genotype](Genotype.md) (mixin)  - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
 * [Haplotype](Haplotype.md) (mixin)  - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 * [NucleicAcidEntity](NucleicAcidEntity.md) (mixin)  - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
 * [ReagentTargetedGene](ReagentTargetedGene.md) (mixin)  - A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
 * [SequenceVariant](SequenceVariant.md) (mixin)  - An allele that varies in its sequence from what is considered the reference allele at that locus.

## Referenced by class


## Attributes


### Own

 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Narrow Mappings:** | | UMLSSC:T028 |
|  | | GENO:0000897 |

