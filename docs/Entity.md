# Class: Entity
_Root Biolink Model class for all things and informational relationships, real or imagined._



* __NOTE__: this is an abstract class and should not be instantiated directly



URI: [biolink:Entity](https://w3id.org/biolink/vocab/Entity)




## Inheritance

* **Entity**
    * [NamedThing](NamedThing.md)
    * [Association](Association.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [id](id.md) | [string](string.md) | 1..1 | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [category_type](category_type.md) | 0..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [label_type](label_type.md) | 0..1 | a lightweight analog to the association class 'provided by' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.  | . |
| [provided_by](provided_by.md) | [Agent](Agent.md) | 0..* | connects an association to the agent (person, organization or group) that provided it  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Entity](Entity.md) | [category](category.md) | domain | entity |
| [Entity](Entity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [NamedThing](NamedThing.md) | [category](category.md) | domain | entity |
| [NamedThing](NamedThing.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismTaxon](OrganismTaxon.md) | [category](category.md) | domain | entity |
| [OrganismTaxon](OrganismTaxon.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Event](Event.md) | [category](category.md) | domain | entity |
| [Event](Event.md) | [has_attribute](has_attribute.md) | domain | entity |
| [AdministrativeEntity](AdministrativeEntity.md) | [category](category.md) | domain | entity |
| [AdministrativeEntity](AdministrativeEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Agent](Agent.md) | [category](category.md) | domain | entity |
| [Agent](Agent.md) | [has_attribute](has_attribute.md) | domain | entity |
| [InformationContentEntity](InformationContentEntity.md) | [category](category.md) | domain | entity |
| [InformationContentEntity](InformationContentEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Dataset](Dataset.md) | [category](category.md) | domain | entity |
| [Dataset](Dataset.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DatasetDistribution](DatasetDistribution.md) | [category](category.md) | domain | entity |
| [DatasetDistribution](DatasetDistribution.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DatasetVersion](DatasetVersion.md) | [category](category.md) | domain | entity |
| [DatasetVersion](DatasetVersion.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DatasetSummary](DatasetSummary.md) | [category](category.md) | domain | entity |
| [DatasetSummary](DatasetSummary.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ConfidenceLevel](ConfidenceLevel.md) | [category](category.md) | domain | entity |
| [ConfidenceLevel](ConfidenceLevel.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EvidenceType](EvidenceType.md) | [category](category.md) | domain | entity |
| [EvidenceType](EvidenceType.md) | [has_attribute](has_attribute.md) | domain | entity |
| [InformationResource](InformationResource.md) | [category](category.md) | domain | entity |
| [InformationResource](InformationResource.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Publication](Publication.md) | [category](category.md) | domain | entity |
| [Publication](Publication.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Book](Book.md) | [category](category.md) | domain | entity |
| [Book](Book.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BookChapter](BookChapter.md) | [category](category.md) | domain | entity |
| [BookChapter](BookChapter.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Serial](Serial.md) | [category](category.md) | domain | entity |
| [Serial](Serial.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Article](Article.md) | [category](category.md) | domain | entity |
| [Article](Article.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PhysicalEntity](PhysicalEntity.md) | [category](category.md) | domain | entity |
| [PhysicalEntity](PhysicalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Activity](Activity.md) | [category](category.md) | domain | entity |
| [Activity](Activity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Procedure](Procedure.md) | [category](category.md) | domain | entity |
| [Procedure](Procedure.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Phenomenon](Phenomenon.md) | [category](category.md) | domain | entity |
| [Phenomenon](Phenomenon.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Device](Device.md) | [category](category.md) | domain | entity |
| [Device](Device.md) | [has_attribute](has_attribute.md) | domain | entity |
| [StudyPopulation](StudyPopulation.md) | [category](category.md) | domain | entity |
| [StudyPopulation](StudyPopulation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MaterialSample](MaterialSample.md) | [category](category.md) | domain | entity |
| [MaterialSample](MaterialSample.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PlanetaryEntity](PlanetaryEntity.md) | [category](category.md) | domain | entity |
| [PlanetaryEntity](PlanetaryEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [category](category.md) | domain | entity |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [category](category.md) | domain | entity |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeographicLocation](GeographicLocation.md) | [category](category.md) | domain | entity |
| [GeographicLocation](GeographicLocation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [category](category.md) | domain | entity |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BiologicalEntity](BiologicalEntity.md) | [category](category.md) | domain | entity |
| [BiologicalEntity](BiologicalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MolecularEntity](MolecularEntity.md) | [category](category.md) | domain | entity |
| [MolecularEntity](MolecularEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalEntity](ChemicalEntity.md) | [category](category.md) | domain | entity |
| [ChemicalEntity](ChemicalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SmallMolecule](SmallMolecule.md) | [category](category.md) | domain | entity |
| [SmallMolecule](SmallMolecule.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalMixture](ChemicalMixture.md) | [category](category.md) | domain | entity |
| [ChemicalMixture](ChemicalMixture.md) | [has_attribute](has_attribute.md) | domain | entity |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [category](category.md) | domain | entity |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MolecularMixture](MolecularMixture.md) | [category](category.md) | domain | entity |
| [MolecularMixture](MolecularMixture.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [category](category.md) | domain | entity |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [category](category.md) | domain | entity |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MolecularActivity](MolecularActivity.md) | [category](category.md) | domain | entity |
| [MolecularActivity](MolecularActivity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BiologicalProcess](BiologicalProcess.md) | [category](category.md) | domain | entity |
| [BiologicalProcess](BiologicalProcess.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Pathway](Pathway.md) | [category](category.md) | domain | entity |
| [Pathway](Pathway.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [category](category.md) | domain | entity |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Behavior](Behavior.md) | [category](category.md) | domain | entity |
| [Behavior](Behavior.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ProcessedMaterial](ProcessedMaterial.md) | [category](category.md) | domain | entity |
| [ProcessedMaterial](ProcessedMaterial.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Drug](Drug.md) | [category](category.md) | domain | entity |
| [Drug](Drug.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [category](category.md) | domain | entity |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [has_attribute](has_attribute.md) | domain | entity |
| [FoodAdditive](FoodAdditive.md) | [category](category.md) | domain | entity |
| [FoodAdditive](FoodAdditive.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Nutrient](Nutrient.md) | [category](category.md) | domain | entity |
| [Nutrient](Nutrient.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Macronutrient](Macronutrient.md) | [category](category.md) | domain | entity |
| [Macronutrient](Macronutrient.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Micronutrient](Micronutrient.md) | [category](category.md) | domain | entity |
| [Micronutrient](Micronutrient.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Vitamin](Vitamin.md) | [category](category.md) | domain | entity |
| [Vitamin](Vitamin.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Food](Food.md) | [category](category.md) | domain | entity |
| [Food](Food.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismalEntity](OrganismalEntity.md) | [category](category.md) | domain | entity |
| [OrganismalEntity](OrganismalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [LifeStage](LifeStage.md) | [category](category.md) | domain | entity |
| [LifeStage](LifeStage.md) | [has_attribute](has_attribute.md) | domain | entity |
| [IndividualOrganism](IndividualOrganism.md) | [category](category.md) | domain | entity |
| [IndividualOrganism](IndividualOrganism.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [category](category.md) | domain | entity |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [category](category.md) | domain | entity |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Disease](Disease.md) | [category](category.md) | domain | entity |
| [Disease](Disease.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PhenotypicFeature](PhenotypicFeature.md) | [category](category.md) | domain | entity |
| [PhenotypicFeature](PhenotypicFeature.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BehavioralFeature](BehavioralFeature.md) | [category](category.md) | domain | entity |
| [BehavioralFeature](BehavioralFeature.md) | [has_attribute](has_attribute.md) | domain | entity |
| [AnatomicalEntity](AnatomicalEntity.md) | [category](category.md) | domain | entity |
| [AnatomicalEntity](AnatomicalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CellularComponent](CellularComponent.md) | [category](category.md) | domain | entity |
| [CellularComponent](CellularComponent.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Cell](Cell.md) | [category](category.md) | domain | entity |
| [Cell](Cell.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CellLine](CellLine.md) | [category](category.md) | domain | entity |
| [CellLine](CellLine.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [category](category.md) | domain | entity |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Gene](Gene.md) | [category](category.md) | domain | entity |
| [Gene](Gene.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Genome](Genome.md) | [category](category.md) | domain | entity |
| [Genome](Genome.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Exon](Exon.md) | [category](category.md) | domain | entity |
| [Exon](Exon.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Transcript](Transcript.md) | [category](category.md) | domain | entity |
| [Transcript](Transcript.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CodingSequence](CodingSequence.md) | [category](category.md) | domain | entity |
| [CodingSequence](CodingSequence.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Polypeptide](Polypeptide.md) | [category](category.md) | domain | entity |
| [Polypeptide](Polypeptide.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Protein](Protein.md) | [category](category.md) | domain | entity |
| [Protein](Protein.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ProteinIsoform](ProteinIsoform.md) | [category](category.md) | domain | entity |
| [ProteinIsoform](ProteinIsoform.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ProteinDomain](ProteinDomain.md) | [category](category.md) | domain | entity |
| [ProteinDomain](ProteinDomain.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ProteinFamily](ProteinFamily.md) | [category](category.md) | domain | entity |
| [ProteinFamily](ProteinFamily.md) | [has_attribute](has_attribute.md) | domain | entity |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [category](category.md) | domain | entity |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [has_attribute](has_attribute.md) | domain | entity |
| [RNAProduct](RNAProduct.md) | [category](category.md) | domain | entity |
| [RNAProduct](RNAProduct.md) | [has_attribute](has_attribute.md) | domain | entity |
| [RNAProductIsoform](RNAProductIsoform.md) | [category](category.md) | domain | entity |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_attribute](has_attribute.md) | domain | entity |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [category](category.md) | domain | entity |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MicroRNA](MicroRNA.md) | [category](category.md) | domain | entity |
| [MicroRNA](MicroRNA.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SiRNA](SiRNA.md) | [category](category.md) | domain | entity |
| [SiRNA](SiRNA.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneFamily](GeneFamily.md) | [category](category.md) | domain | entity |
| [GeneFamily](GeneFamily.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Genotype](Genotype.md) | [category](category.md) | domain | entity |
| [Genotype](Genotype.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Haplotype](Haplotype.md) | [category](category.md) | domain | entity |
| [Haplotype](Haplotype.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SequenceVariant](SequenceVariant.md) | [category](category.md) | domain | entity |
| [SequenceVariant](SequenceVariant.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Snv](Snv.md) | [category](category.md) | domain | entity |
| [Snv](Snv.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [category](category.md) | domain | entity |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ClinicalEntity](ClinicalEntity.md) | [category](category.md) | domain | entity |
| [ClinicalEntity](ClinicalEntity.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ClinicalTrial](ClinicalTrial.md) | [category](category.md) | domain | entity |
| [ClinicalTrial](ClinicalTrial.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ClinicalIntervention](ClinicalIntervention.md) | [category](category.md) | domain | entity |
| [ClinicalIntervention](ClinicalIntervention.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ClinicalFinding](ClinicalFinding.md) | [category](category.md) | domain | entity |
| [ClinicalFinding](ClinicalFinding.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Hospitalization](Hospitalization.md) | [category](category.md) | domain | entity |
| [Hospitalization](Hospitalization.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Case](Case.md) | [category](category.md) | domain | entity |
| [Case](Case.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Cohort](Cohort.md) | [category](category.md) | domain | entity |
| [Cohort](Cohort.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PathologicalProcess](PathologicalProcess.md) | [category](category.md) | domain | entity |
| [PathologicalProcess](PathologicalProcess.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [category](category.md) | domain | entity |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Treatment](Treatment.md) | [category](category.md) | domain | entity |
| [Treatment](Treatment.md) | [has_attribute](has_attribute.md) | domain | entity |
| [Association](Association.md) | [category](category.md) | domain | entity |
| [Association](Association.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ContributorAssociation](ContributorAssociation.md) | [category](category.md) | domain | entity |
| [ContributorAssociation](ContributorAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [category](category.md) | domain | entity |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [category](category.md) | domain | entity |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [category](category.md) | domain | entity |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [category](category.md) | domain | entity |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [category](category.md) | domain | entity |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [category](category.md) | domain | entity |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [category](category.md) | domain | entity |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [category](category.md) | domain | entity |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [category](category.md) | domain | entity |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [category](category.md) | domain | entity |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [category](category.md) | domain | entity |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [category](category.md) | domain | entity |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [category](category.md) | domain | entity |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [category](category.md) | domain | entity |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [category](category.md) | domain | entity |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [category](category.md) | domain | entity |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [category](category.md) | domain | entity |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [category](category.md) | domain | entity |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [category](category.md) | domain | entity |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [category](category.md) | domain | entity |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [category](category.md) | domain | entity |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [category](category.md) | domain | entity |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [category](category.md) | domain | entity |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [category](category.md) | domain | entity |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [category](category.md) | domain | entity |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [category](category.md) | domain | entity |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [FunctionalAssociation](FunctionalAssociation.md) | [category](category.md) | domain | entity |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [category](category.md) | domain | entity |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [category](category.md) | domain | entity |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [category](category.md) | domain | entity |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [category](category.md) | domain | entity |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [category](category.md) | domain | entity |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [category](category.md) | domain | entity |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [category](category.md) | domain | entity |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [category](category.md) | domain | entity |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SequenceAssociation](SequenceAssociation.md) | [category](category.md) | domain | entity |
| [SequenceAssociation](SequenceAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [category](category.md) | domain | entity |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_attribute](has_attribute.md) | domain | entity |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [category](category.md) | domain | entity |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_attribute](has_attribute.md) | domain | entity |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [category](category.md) | domain | entity |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [category](category.md) | domain | entity |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_attribute](has_attribute.md) | domain | entity |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [category](category.md) | domain | entity |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_attribute](has_attribute.md) | domain | entity |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [category](category.md) | domain | entity |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [has_attribute](has_attribute.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [category](category.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [category](category.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [category](category.md) | domain | entity |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [category](category.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [category](category.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [category](category.md) | domain | entity |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_attribute](has_attribute.md) | domain | entity |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [category](category.md) | domain | entity |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_attribute](has_attribute.md) | domain | entity |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: entity
description: Root Biolink Model class for all things and informational relationships,
  real or imagined.
from_schema: https://w3id.org/biolink/biolink-model
abstract: true
slots:
- id
- iri
- category
- type
- name
- description
- source
- provided by
- has attribute

```
</details>

### Induced

<details>
```yaml
name: entity
description: Root Biolink Model class for all things and informational relationships,
  real or imagined.
from_schema: https://w3id.org/biolink/biolink-model
abstract: true
attributes:
  id:
    name: id
    exact_mappings:
    - alliancegenome:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    identifier: true
    alias: id
    owner: entity
    range: string
    required: true
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
    owner: entity
    range: iri type
  category:
    name: category
    description: "Name of the high level ontology class in which this entity is categorized.\
      \ Corresponds to the label for the biolink entity type class.\n * In a neo4j\
      \ database this MAY correspond to the neo4j label tag.\n * In an RDF database\
      \ it should be a biolink model class URI.\nThis field is multi-valued. It should\
      \ include values for ancestors of the biolink class; for example, a protein\
      \ such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`,\
      \ `biolink:MolecularEntity`, ...\nIn an RDF database, nodes will typically have\
      \ an rdf:type triples. This can be to the most specific biolink class, or potentially\
      \ to a class more specific than something in biolink. For example, a sequence\
      \ feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site,\
      \ which is more specific than anything in biolink. Here we would have categories\
      \ {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}"
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: entity
    is_class_field: true
    range: category type
  type:
    name: type
    exact_mappings:
    - alliancegenome:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: entity
    range: string
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: entity
    range: label type
  description:
    name: description
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: dct:description
    alias: description
    owner: entity
    range: narrative text
  source:
    name: source
    description: a lightweight analog to the association class 'provided by' slot,
      which is the string name, or the authoritative (i.e. database) namespace, designating
      the origin of the entity to which the slot belongs.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: entity
    range: label type
  provided by:
    name: provided by
    exact_mappings:
    - pav:providedBy
    description: connects an association to the agent (person, organization or group)
      that provided it
    deprecated: This slot is deprecated and replaced by a set of more precise slots
      for describing the source retrieval provenance of an Association.  These include
      'knowledge source' and its descendants 'primary knowledge source', 'original
      knowledge source', and 'aggregator knowledge source'.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: provided_by
    owner: entity
    range: agent
  has attribute:
    name: has attribute
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - OMIM:has_inheritance_type
    - ORPHA:C016
    - ORPHA:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: entity
    range: attribute

```
</details>