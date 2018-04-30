---
layout: default
---

## transcript


An RNA synthesized on a DNA or RNA template by an RNA polymerase

URI: [http://bioentity.io/vocab/Transcript](http://bioentity.io/vocab/Transcript)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity|has biological sequence]^-[transcript|], [transcript|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SO:0000673](http://purl.obolibrary.org/obo/SO_0000673)
 * [SIO:010450](http://semanticscience.org/resource/SIO_010450)

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children


## Used in

 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [transcript](Transcript.html)
 *  class: [exon to transcript relationship](ExonToTranscriptRelationship.html) references: [transcript](Transcript.html)

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
