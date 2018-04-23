---
layout: default
---

## coding sequence


None

URI: [http://bioentity.io/vocab/CodingSequence](http://bioentity.io/vocab/CodingSequence)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity|has biological sequence]^-[coding sequence|], [coding sequence|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SO:0000316](http://purl.obolibrary.org/obo/SO_0000316)
 * [SIO:001390](http://semanticscience.org/resource/SIO_001390)

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
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
