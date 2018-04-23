---
layout: default
---

## protein isoform


Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

URI: [http://bioentity.io/vocab/ProteinIsoform](http://bioentity.io/vocab/ProteinIsoform)


![img](http://yuml.me/diagram/nofunky/class/[protein|]^-[protein isoform|has biological sequence;id;label;in taxon], [protein isoform|has biological sequence;id;label;in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings


## Inheritance

 *  is_a: [protein](Protein.html)
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
