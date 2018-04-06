---
layout: default
---

## RNA product isoform


Represents a protein that is a specific isoform of the canonical or reference RNA

URI: [http://bioentity.io/vocab/RnaProductIsoform](http://bioentity.io/vocab/RnaProductIsoform)
## Mappings


## Inheritance

 *  is_a: [RNA product](RnaProduct.html)
 *  mixin: [gene product isoform](GeneProductIsoform.html)

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
