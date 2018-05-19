---
layout: default
---

## macromolecular machine


A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: [http://bioentity.io/vocab/MacromolecularMachine](http://bioentity.io/vocab/MacromolecularMachine)


![img](http://yuml.me/diagram/nofunky/class/[genomic entity|has biological sequence]^-[macromolecular machine|], [macromolecular machine|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings


## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children

 *  child: [gene or gene product](GeneOrGeneProduct.html)
 *  child: [macromolecular complex](MacromolecularComplex.html)

## Used in

 *  class: [sequence variant](SequenceVariant.html) references: [gene](Gene.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [gene](Gene.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to gene homology association](GeneToGeneHomologyAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [functional association](FunctionalAssociation.html) references: [macromolecular machine](MacromolecularMachine.html)
 *  class: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.html) references: [macromolecular machine](MacromolecularMachine.html)
 *  class: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.html) references: [macromolecular machine](MacromolecularMachine.html)
 *  class: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.html) references: [macromolecular machine](MacromolecularMachine.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [gene](Gene.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)

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
    * _genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name_
    * __range__: symbol type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html) *subsets: translator_minimal*
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
