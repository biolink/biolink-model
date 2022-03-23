# Class: Attribute
_A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material._





URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)




## Inheritance

* [Annotation](Annotation.md)
    * **Attribute** [ ontology class]
        * [BiologicalSex](BiologicalSex.md)
        * [SeverityValue](SeverityValue.md)
        * [OrganismAttribute](OrganismAttribute.md)
        * [Zygosity](Zygosity.md)
        * [ClinicalAttribute](ClinicalAttribute.md)
        * [SocioeconomicAttribute](SocioeconomicAttribute.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name](name.md) | [label_type](label_type.md) | 0..1 | The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.  | . |
| [has_attribute_type](has_attribute_type.md) | [OntologyClass](OntologyClass.md) | 1..1 | connects an attribute to a class that describes it  | . |
| [has_quantitative_value](has_quantitative_value.md) | [QuantityValue](QuantityValue.md) | 0..* | connects an attribute to a value  | . |
| [has_qualitative_value](has_qualitative_value.md) | [NamedThing](NamedThing.md) | 0..1 | connects an attribute to a value  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [source](source.md) | [string](string.md) | 0..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Attribute](Attribute.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [Attribute](Attribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [Attribute](Attribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [BiologicalSex](BiologicalSex.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [BiologicalSex](BiologicalSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [BiologicalSex](BiologicalSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [PhenotypicSex](PhenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [PhenotypicSex](PhenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [GenotypicSex](GenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [GenotypicSex](GenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [GenotypicSex](GenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [SeverityValue](SeverityValue.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [SeverityValue](SeverityValue.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [SeverityValue](SeverityValue.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [Entity](Entity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [NamedThing](NamedThing.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismTaxon](OrganismTaxon.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Event](Event.md) | [has_attribute](has_attribute.md) | range | attribute |
| [AdministrativeEntity](AdministrativeEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Agent](Agent.md) | [has_attribute](has_attribute.md) | range | attribute |
| [InformationContentEntity](InformationContentEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Dataset](Dataset.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DatasetDistribution](DatasetDistribution.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DatasetVersion](DatasetVersion.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DatasetSummary](DatasetSummary.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ConfidenceLevel](ConfidenceLevel.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EvidenceType](EvidenceType.md) | [has_attribute](has_attribute.md) | range | attribute |
| [InformationResource](InformationResource.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Publication](Publication.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Book](Book.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BookChapter](BookChapter.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Serial](Serial.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Article](Article.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PhysicalEntity](PhysicalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Activity](Activity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Procedure](Procedure.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Phenomenon](Phenomenon.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Device](Device.md) | [has_attribute](has_attribute.md) | range | attribute |
| [StudyPopulation](StudyPopulation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MaterialSample](MaterialSample.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PlanetaryEntity](PlanetaryEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeographicLocation](GeographicLocation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BiologicalEntity](BiologicalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MolecularEntity](MolecularEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalEntity](ChemicalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SmallMolecule](SmallMolecule.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalMixture](ChemicalMixture.md) | [has_attribute](has_attribute.md) | range | attribute |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MolecularMixture](MolecularMixture.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MolecularActivity](MolecularActivity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BiologicalProcess](BiologicalProcess.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Pathway](Pathway.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Behavior](Behavior.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ProcessedMaterial](ProcessedMaterial.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Drug](Drug.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [has_attribute](has_attribute.md) | range | attribute |
| [FoodAdditive](FoodAdditive.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Nutrient](Nutrient.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Macronutrient](Macronutrient.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Micronutrient](Micronutrient.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Vitamin](Vitamin.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Food](Food.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [OrganismAttribute](OrganismAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [OrganismAttribute](OrganismAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [Inheritance](Inheritance.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [Inheritance](Inheritance.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [Inheritance](Inheritance.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [OrganismalEntity](OrganismalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [LifeStage](LifeStage.md) | [has_attribute](has_attribute.md) | range | attribute |
| [IndividualOrganism](IndividualOrganism.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Disease](Disease.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PhenotypicFeature](PhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BehavioralFeature](BehavioralFeature.md) | [has_attribute](has_attribute.md) | range | attribute |
| [AnatomicalEntity](AnatomicalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CellularComponent](CellularComponent.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Cell](Cell.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CellLine](CellLine.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Gene](Gene.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Genome](Genome.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Exon](Exon.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Transcript](Transcript.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CodingSequence](CodingSequence.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Polypeptide](Polypeptide.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Protein](Protein.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ProteinIsoform](ProteinIsoform.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ProteinDomain](ProteinDomain.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ProteinFamily](ProteinFamily.md) | [has_attribute](has_attribute.md) | range | attribute |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [has_attribute](has_attribute.md) | range | attribute |
| [RNAProduct](RNAProduct.md) | [has_attribute](has_attribute.md) | range | attribute |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_attribute](has_attribute.md) | range | attribute |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MicroRNA](MicroRNA.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SiRNA](SiRNA.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneFamily](GeneFamily.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Zygosity](Zygosity.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [Zygosity](Zygosity.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [Zygosity](Zygosity.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [Genotype](Genotype.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Haplotype](Haplotype.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SequenceVariant](SequenceVariant.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Snv](Snv.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [ClinicalModifier](ClinicalModifier.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [ClinicalModifier](ClinicalModifier.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [ClinicalCourse](ClinicalCourse.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [ClinicalCourse](ClinicalCourse.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [Onset](Onset.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [Onset](Onset.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [Onset](Onset.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [ClinicalEntity](ClinicalEntity.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ClinicalTrial](ClinicalTrial.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ClinicalIntervention](ClinicalIntervention.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Hospitalization](Hospitalization.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | attribute |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | attribute |
| [Case](Case.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Cohort](Cohort.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PathologicalProcess](PathologicalProcess.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalExposure](ChemicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [DrugExposure](DrugExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | attribute |
| [Treatment](Treatment.md) | [has_attribute](has_attribute.md) | range | attribute |
| [Association](Association.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ContributorAssociation](ContributorAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SequenceAssociation](SequenceAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_attribute](has_attribute.md) | range | attribute |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_attribute](has_attribute.md) | range | attribute |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_attribute](has_attribute.md) | range | attribute |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_attribute](has_attribute.md) | range | attribute |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [has_attribute](has_attribute.md) | range | attribute |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_attribute](has_attribute.md) | range | attribute |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_attribute](has_attribute.md) | range | attribute |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* EDAM-DATA

* EDAM-FORMAT

* EDAM-OPERATION

* EDAM-TOPIC










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
exact_mappings:
- SIO:000614
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://w3id.org/biolink/biolink-model
is_a: annotation
mixins:
- ontology class
slots:
- name
- has attribute type
- has quantitative value
- has qualitative value
- iri
- source
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.

```
</details>

### Induced

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
exact_mappings:
- SIO:000614
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://w3id.org/biolink/biolink-model
is_a: annotation
mixins:
- ontology class
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
attributes:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: attribute
    range: label type
  has attribute type:
    name: has attribute type
    narrow_mappings:
    - LOINC:has_modality_type
    - LOINC:has_view_type
    description: connects an attribute to a class that describes it
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: false
    alias: has_attribute_type
    owner: attribute
    range: ontology class
    required: true
  has quantitative value:
    name: has quantitative value
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: true
    alias: has_quantitative_value
    owner: attribute
    range: quantity value
  has qualitative value:
    name: has qualitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: false
    alias: has_qualitative_value
    owner: attribute
    range: named thing
  iri:
    name: iri
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    alias: iri
    owner: attribute
    range: iri type
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: attribute
    range: string

```
</details>