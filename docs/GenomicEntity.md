---
parent: Class Mixins
title: biolink:GenomicEntity
grand_parent: Classes
layout: default
---

# Class: GenomicEntity




URI: [biolink:GenomicEntity](https://w3id.org/biolink/vocab/GenomicEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismTaxon],[NucleicAcidEntity]uses%20-.-%3E[GenomicEntity],[Haplotype]uses%20-.-%3E[GenomicEntity],[Genotype]uses%20-.-%3E[GenomicEntity],[GenomicBackgroundExposure]uses%20-.-%3E[GenomicEntity],[Genome]uses%20-.-%3E[GenomicEntity],[ThingWithTaxon]%5E-[GenomicEntity],[NucleicAcidEntity],[Haplotype],[Genotype],[GenomicBackgroundExposure],[Genome])

---


## Parents

 *  is_a: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

## Mixin for

 * [Genome](Genome.md) (mixin)  - A genome is the sum of genetic material within a cell or virion.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [Genotype](Genotype.md) (mixin)  - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
 * [Haplotype](Haplotype.md) (mixin)  - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 * [NucleicAcidEntity](NucleicAcidEntity.md) (mixin)  - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.

## Referenced by class


## Attributes


### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |

