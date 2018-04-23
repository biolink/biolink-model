---
layout: default
---

## gene product isoform


This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

URI: [http://bioentity.io/vocab/GeneProductIsoform](http://bioentity.io/vocab/GeneProductIsoform)


![img](http://yuml.me/diagram/nofunky/class/[gene product|]^-[gene product isoform|], [gene product isoform|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings


## Inheritance

 *  is_a: [gene product](GeneProduct.html)

## Children

 *  mixin: [protein isoform](ProteinIsoform.html)
 *  mixin: [RNA product isoform](RnaProductIsoform.html)


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
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
