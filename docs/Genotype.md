---
layout: default
---

## genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background

URI: [http://bioentity.io/vocab/Genotype](http://bioentity.io/vocab/Genotype)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity|has biological sequence]^-[genotype|has zygosity], [genotype|has zygosity]-has zygosity >[zygosity|], [attribute|]^-[zygosity|], [genotype|has zygosity]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [GENO:0000536](http://purl.obolibrary.org/obo/GENO_0000536)
 * [SIO:001079](http://semanticscience.org/resource/SIO_001079)

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children


## Used in

 *  class: [genotype to genotype part association](GenotypeToGenotypePartAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to variant association](GenotypeToVariantAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to thing association](GenotypeToThingAssociation.html) references: [genotype](Genotype.html)

## Fields

 * [has zygosity](has_zygosity.html)
    * __range__: [zygosity](Zygosity.html)
    * __Local__
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
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
