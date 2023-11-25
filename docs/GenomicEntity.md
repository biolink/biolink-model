---
parent: Class Mixins
title: biolink:GenomicEntity
grand_parent: Classes
layout: default
---

# Class: GenomicEntity




URI: [biolink:GenomicEntity](https://w3id.org/biolink/vocab/GenomicEntity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceVariant],[TranscriptionFactorBindingSite]uses%20-.-%3E[GenomicEntity%7Chas_biological_sequence:biological_sequence%20%3F],[SequenceVariant]uses%20-.-%3E[GenomicEntity],[RegulatoryRegion]uses%20-.-%3E[GenomicEntity],[ReagentTargetedGene]uses%20-.-%3E[GenomicEntity],[NucleosomeModification]uses%20-.-%3E[GenomicEntity],[NucleicAcidEntity]uses%20-.-%3E[GenomicEntity],[Haplotype]uses%20-.-%3E[GenomicEntity],[Genotype]uses%20-.-%3E[GenomicEntity],[GenomicBackgroundExposure]uses%20-.-%3E[GenomicEntity],[Genome]uses%20-.-%3E[GenomicEntity],[Gene]uses%20-.-%3E[GenomicEntity],[CodingSequence]uses%20-.-%3E[GenomicEntity],[AccessibleDnaRegion]uses%20-.-%3E[GenomicEntity],[TranscriptionFactorBindingSite],[RegulatoryRegion],[ReagentTargetedGene],[NucleosomeModification],[NucleicAcidEntity],[Haplotype],[Genotype],[GenomicBackgroundExposure],[Genome],[Gene],[CodingSequence],[AccessibleDnaRegion])

---


## Mixin for

 * [AccessibleDnaRegion](AccessibleDnaRegion.md) (mixin)  - A region (or regions) of a chromatinized genome that has been measured to be more accessible to an enzyme such as DNase-I or Tn5 Transpose
 * [CodingSequence](CodingSequence.md) (mixin) 
 * [Gene](Gene.md) (mixin)  - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
 * [Genome](Genome.md) (mixin)  - A genome is the sum of genetic material within a cell or virion.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [Genotype](Genotype.md) (mixin)  - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
 * [Haplotype](Haplotype.md) (mixin)  - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 * [NucleicAcidEntity](NucleicAcidEntity.md) (mixin)  - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
 * [NucleosomeModification](NucleosomeModification.md) (mixin)  - A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A.
 * [ReagentTargetedGene](ReagentTargetedGene.md) (mixin)  - A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
 * [RegulatoryRegion](RegulatoryRegion.md) (mixin)  - A region (or regions) of the genome that contains known or putative regulatory elements that act in cis- or trans- to affect the transcription of gene
 * [SequenceVariant](SequenceVariant.md) (mixin)  - A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.
 * [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) (mixin)  - A region (or regions) of the genome that contains a region of DNA known or predicted to bind a protein that modulates gene transcription

## Referenced by class

 *  **[SequenceVariant](SequenceVariant.md)** *[is frameshift variant of](is_frameshift_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is missense variant of](is_missense_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nearby variant of](is_nearby_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is non coding variant of](is_non_coding_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nonsense variant of](is_nonsense_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is sequence variant of](is_sequence_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is splice site variant of](is_splice_site_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is synonymous variant of](is_synonymous_variant_of.md)*  <sub>0..\*</sub>  **[GenomicEntity](GenomicEntity.md)**

## Attributes


### Inherited from epigenomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Narrow Mappings:** | | STY:T028 |
|  | | GENO:0000897 |

