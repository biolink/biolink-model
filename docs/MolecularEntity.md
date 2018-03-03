---
layout: default
---

## molecular entity


A gene, gene product, small molecule or macromolecule (including protein complex)

URI: [http://bioentity.io/vocab/MolecularEntity](http://bioentity.io/vocab/MolecularEntity)
## Mappings


## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children

 *  child: [chemical substance](ChemicalSubstance.html)
 *  child: [genomic entity](GenomicEntity.html)
 *  child: [macromolecular complex](MacromolecularComplex.html)
 *  child: [gene family](GeneFamily.html)

## Used in

 *  class: [allele](Allele.html) references: [gene](Gene.html)
 *  class: [genotype to genotype part association](GenotypeToGenotypePartAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to variant association](GenotypeToVariantAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to gene homology association](GeneToGeneHomologyAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [chemical to thing association](ChemicalToThingAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [genotype to thing association](GenotypeToThingAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [gene to go term association](GeneToGoTermAssociation.html) references: [molecular entity](MolecularEntity.html)
 *  class: [genomic sequence localization](GenomicSequenceLocalization.html) references: [genomic entity](GenomicEntity.html)
 *  class: [sequence feature relationship](SequenceFeatureRelationship.html) references: [genomic entity](GenomicEntity.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [transcript](Transcript.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [exon to transcript relationship](ExonToTranscriptRelationship.html) references: [exon](Exon.html)
 *  class: [sequence feature to sequence relationship](SequenceFeatureToSequenceRelationship.html) references: [genomic entity](GenomicEntity.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)

## Fields

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
