---
layout: default
---

## protein


A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

URI: [http://bioentity.io/vocab/Protein](http://bioentity.io/vocab/Protein)


![img](http://yuml.me/diagram/nofunky/class/[gene product|]^-[protein|], [protein|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001)
 * [SIO:010043](http://semanticscience.org/resource/SIO_010043)
 * [WD:Q8054](http://purl.obolibrary.org/obo/WD_Q8054)

## Inheritance

 *  is_a: [gene product](GeneProduct.html)

## Children

 *  child: [protein isoform](ProteinIsoform.html)


## Fields

 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * inherited from: [genomic entity](GenomicEntity.html)
 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
