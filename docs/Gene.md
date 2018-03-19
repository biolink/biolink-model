---
layout: default
---

## gene


None

URI: [http://bioentity.io/vocab/Gene](http://bioentity.io/vocab/Gene)
## Mappings

 * [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704)
 * [SIO:010035](http://semanticscience.org/resource/SIO_010035)
 * [WD:Q7187](http://purl.obolibrary.org/obo/WD_Q7187)

## Inheritance

 *  is_a: [gene or gene product](GeneOrGeneProduct.html)

## Children


## Used in

 *  class: [allele](Allele.html) references: [gene](Gene.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [gene](Gene.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [gene](Gene.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)

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
