---
layout: default
---

## haplotype


A set of zero or more Alleles on a single instance of a Sequence[VMC]

URI: [http://bioentity.io/vocab/Haplotype](http://bioentity.io/vocab/Haplotype)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity]^-[haplotype], [haplotype]-in taxon >[organism taxon], [ontology class]^-[organism taxon])
## Mappings

 * [VMC:Haplotype](http://purl.obolibrary.org/obo/VMC_Haplotype)

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children



## Fields

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
