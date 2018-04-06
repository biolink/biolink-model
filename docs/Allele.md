---
layout: default
---

## allele


One of a set of  coexisting sequence variants that exist at a particular genomic locus.

URI: [http://bioentity.io/vocab/Allele](http://bioentity.io/vocab/Allele)
## Mappings

 * [GENO:0000512](http://purl.obolibrary.org/obo/GENO_0000512)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)

## Inheritance

 *  is_a: [genotype](Genotype.html)

## Children



## Fields

 * [has gene](has_gene.html)
    * _connects and entity to a single gene_
    * __range__: [gene](Gene.html)
    * __Local__
 * [has zygosity](has_zygosity.html)
    * __range__: [zygosity](Zygosity.html)
    * inherited from: [genotype](Genotype.html)
 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * inherited from: [genomic entity](GenomicEntity.html)
 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
