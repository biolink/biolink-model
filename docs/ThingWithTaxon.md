---
layout: default
---

## thing with taxon


A mixin that can be used on any entity with a taxon

URI: [http://bioentity.io/vocab/ThingWithTaxon](http://bioentity.io/vocab/ThingWithTaxon)
## Mappings


## Inheritance


## Children

 *  mixin: [individual organism](IndividualOrganism.html)
 *  mixin: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  mixin: [biosample](Biosample.html)
 *  mixin: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  mixin: [molecular entity](MolecularEntity.html)
 *  mixin: [anatomical entity](AnatomicalEntity.html)
 *  mixin: [life stage](LifeStage.html)

## Used in

 *  class: [allele](Allele.html) references: [gene](Gene.html)
 *  class: [treatment](Treatment.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [genotype to genotype part association](GenotypeToGenotypePartAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to variant association](GenotypeToVariantAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [molecular interaction](MolecularInteraction.html) references: [molecular entity](MolecularEntity.html)
 *  class: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.html) references: [molecular entity](MolecularEntity.html)
 *  class: [chemical to thing association](ChemicalToThingAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [disease to thing association](DiseaseToThingAssociation.html) references: [disease](Disease.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [genotype](Genotype.html)
 *  class: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [genotype to thing association](GenotypeToThingAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [life stage](LifeStage.html)
 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [gene to go term association](GeneToGoTermAssociation.html) references: [molecular entity](MolecularEntity.html)
 *  class: [genomic sequence localization](GenomicSequenceLocalization.html) references: [genomic entity](GenomicEntity.html)
 *  class: [sequence feature relationship](SequenceFeatureRelationship.html) references: [genomic entity](GenomicEntity.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [transcript](Transcript.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [exon to transcript relationship](ExonToTranscriptRelationship.html) references: [exon](Exon.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity part of anatomical entity association](AnatomicalEntityPartOfAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)

## Fields

 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * __Local__
