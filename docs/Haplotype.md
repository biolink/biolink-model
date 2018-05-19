---
layout: default
---

## haplotype


A set of zero or more Alleles on a single instance of a Sequence[VMC]

URI: [http://bioentity.io/vocab/Haplotype](http://bioentity.io/vocab/Haplotype)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity|has biological sequence]^-[haplotype|], [haplotype|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [GENO:0000871](http://purl.obolibrary.org/obo/GENO_0000871)
 * [VMC:Haplotype](http://purl.obolibrary.org/obo/VMC_Haplotype)

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children



## Fields

 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * inherited from: [genomic entity](GenomicEntity.html)
 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html) *subsets: translator_minimal*
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
