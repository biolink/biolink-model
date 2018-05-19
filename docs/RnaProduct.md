---
layout: default
---

## RNA product


None

URI: [http://bioentity.io/vocab/RnaProduct](http://bioentity.io/vocab/RnaProduct)


![img](http://yuml.me/diagram/nofunky/class/[gene product|]^-[RNA product|], [RNA product|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [CHEBI:33697](http://purl.obolibrary.org/obo/CHEBI_33697)
 * [SIO:010450](http://semanticscience.org/resource/SIO_010450)
 * [WD:Q11053](http://purl.obolibrary.org/obo/WD_Q11053)

## Inheritance

 *  is_a: [gene product](GeneProduct.html)

## Children

 *  child: [RNA product isoform](RnaProductIsoform.html)
 *  child: [noncoding RNA product](NoncodingRnaProduct.html)


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
