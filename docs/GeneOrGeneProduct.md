---
layout: default
---

## gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [http://bioentity.io/vocab/GeneOrGeneProduct](http://bioentity.io/vocab/GeneOrGeneProduct)
## Mappings


## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children

 *  child: [gene](Gene.html)
 *  child: [gene product](GeneProduct.html)

## Used in

 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [gene](Gene.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to gene homology association](GeneToGeneHomologyAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [gene](Gene.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [molecular activity to gene product association](MolecularActivityToGeneProductAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _genes are typically designated by a short symbol and a full name. We map the symbol to the default display label and use an additional slot for full name_
    * __range__: symbol type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
