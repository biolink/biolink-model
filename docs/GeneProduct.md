---
layout: default
---

## gene product


The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

URI: [http://bioentity.io/vocab/GeneProduct](http://bioentity.io/vocab/GeneProduct)


![img](http://yuml.me/diagram/nofunky/class/[gene or gene product|]^-[gene product|], [gene product|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [WD:Q424689](http://purl.obolibrary.org/obo/WD_Q424689)

## Inheritance

 *  is_a: [gene or gene product](GeneOrGeneProduct.html)

## Children

 *  child: [protein](Protein.html)
 *  child: [gene product isoform](GeneProductIsoform.html)
 *  child: [RNA product](RnaProduct.html)

## Used in

 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene product](GeneProduct.html)

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
