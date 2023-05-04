---
parent: Edge Properties
title: biolink:object_category_closure
grand_parent: Slots
layout: default
---

# Slot: object_category_closure


Used to hold the object category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.

URI: [biolink:object_category_closure](https://w3id.org/biolink/vocab/object_category_closure)

## Domain and Range

[Association](Association.md) ->  <sub>0..\*</sub> [OntologyClass](OntologyClass.md)

## Parents

 *  is_a: [association slot](association_slot.md)

## Children


## Used by

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)
 * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)
 * [Association](Association.md)
 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md)
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md)
 * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md)
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)
 * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
 * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md)
 * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)
 * [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)
 * [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)
 * [ContributorAssociation](ContributorAssociation.md)
 * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md)
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md)
 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md)
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md)
 * [DrugToGeneAssociation](DrugToGeneAssociation.md)
 * [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md)
 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md)
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md)
 * [FunctionalAssociation](FunctionalAssociation.md)
 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)
 * [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)
 * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)
 * [GeneToGeneAssociation](GeneToGeneAssociation.md)
 * [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md)
 * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md)
 * [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md)
 * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)
 * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
 * [GeneToPathwayAssociation](GeneToPathwayAssociation.md)
 * [GeneToPhenotypeAssociation](GeneToPhenotypeAssociation.md)
 * [GenomicSequenceLocalization](GenomicSequenceLocalization.md)
 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)
 * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md)
 * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md)
 * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)
 * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md)
 * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)
 * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)
 * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md)
 * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md)
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md)
 * [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md)
 * [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md)
 * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md)
 * [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)
 * [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md)
 * [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md)
 * [SequenceAssociation](SequenceAssociation.md)
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)
 * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
 * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)
 * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToGeneAssociation](VariantToGeneAssociation.md)
 * [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='[\'biolink:Disease", "biolink:NamedThing\']', description='The object category closure of the association between the gene \'BRCA1\' and the disease \'breast cancer\' is the set of all biolink classes that are ancestors of \'biolink:Disease\' in the biolink model.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.') |

