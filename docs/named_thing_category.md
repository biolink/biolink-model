
# Slot: category


Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}

URI: [biolink:named_thing_category](https://w3id.org/biolink/vocab/named_thing_category)


## Domain and Range

[NamedThing](NamedThing.md) &#8594;  <sub>1..\*</sub> [CategoryType](types/CategoryType.md)

## Parents

 *  is_a: [category](category.md)

## Children


## Used by

 * [RNAProduct](RNAProduct.md)
 * [RNAProductIsoform](RNAProductIsoform.md)
 * [Activity](Activity.md)
 * [AdministrativeEntity](AdministrativeEntity.md)
 * [Agent](Agent.md)
 * [AnatomicalEntity](AnatomicalEntity.md)
 * [Article](Article.md)
 * [Behavior](Behavior.md)
 * [BehavioralFeature](BehavioralFeature.md)
 * [BiologicalEntity](BiologicalEntity.md)
 * [BiologicalProcess](BiologicalProcess.md)
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)
 * [Book](Book.md)
 * [BookChapter](BookChapter.md)
 * [Case](Case.md)
 * [Cell](Cell.md)
 * [CellLine](CellLine.md)
 * [CellularComponent](CellularComponent.md)
 * [ChemicalEntity](ChemicalEntity.md)
 * [ChemicalMixture](ChemicalMixture.md)
 * [ClinicalEntity](ClinicalEntity.md)
 * [ClinicalFinding](ClinicalFinding.md)
 * [ClinicalIntervention](ClinicalIntervention.md)
 * [ClinicalTrial](ClinicalTrial.md)
 * [CodingSequence](CodingSequence.md)
 * [Cohort](Cohort.md)
 * [ComplexMolecularMixture](ComplexMolecularMixture.md)
 * [ConfidenceLevel](ConfidenceLevel.md)
 * [Dataset](Dataset.md)
 * [DatasetDistribution](DatasetDistribution.md)
 * [DatasetSummary](DatasetSummary.md)
 * [DatasetVersion](DatasetVersion.md)
 * [Device](Device.md)
 * [Disease](Disease.md)
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [Drug](Drug.md)
 * [EnvironmentalFeature](EnvironmentalFeature.md)
 * [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md)
 * [EnvironmentalProcess](EnvironmentalProcess.md)
 * [Event](Event.md)
 * [EvidenceType](EvidenceType.md)
 * [Exon](Exon.md)
 * [Food](Food.md)
 * [FoodAdditive](FoodAdditive.md)
 * [Gene](Gene.md)
 * [GeneFamily](GeneFamily.md)
 * [Genome](Genome.md)
 * [Genotype](Genotype.md)
 * [GeographicLocation](GeographicLocation.md)
 * [GeographicLocationAtTime](GeographicLocationAtTime.md)
 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
 * [Haplotype](Haplotype.md)
 * [Hospitalization](Hospitalization.md)
 * [IndividualOrganism](IndividualOrganism.md)
 * [InformationContentEntity](InformationContentEntity.md)
 * [InformationResource](InformationResource.md)
 * [LifeStage](LifeStage.md)
 * [Macronutrient](Macronutrient.md)
 * [MaterialSample](MaterialSample.md)
 * [MicroRNA](MicroRNA.md)
 * [Micronutrient](Micronutrient.md)
 * [MolecularActivity](MolecularActivity.md)
 * [MolecularEntity](MolecularEntity.md)
 * [MolecularMixture](MolecularMixture.md)
 * [NamedThing](NamedThing.md)
 * [NoncodingRNAProduct](NoncodingRNAProduct.md)
 * [NucleicAcidEntity](NucleicAcidEntity.md)
 * [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md)
 * [Nutrient](Nutrient.md)
 * [OrganismTaxon](OrganismTaxon.md)
 * [OrganismalEntity](OrganismalEntity.md)
 * [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md)
 * [PathologicalProcess](PathologicalProcess.md)
 * [Pathway](Pathway.md)
 * [Phenomenon](Phenomenon.md)
 * [PhenotypicFeature](PhenotypicFeature.md)
 * [PhysicalEntity](PhysicalEntity.md)
 * [PhysiologicalProcess](PhysiologicalProcess.md)
 * [PlanetaryEntity](PlanetaryEntity.md)
 * [Polypeptide](Polypeptide.md)
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [Procedure](Procedure.md)
 * [ProcessedMaterial](ProcessedMaterial.md)
 * [Protein](Protein.md)
 * [ProteinDomain](ProteinDomain.md)
 * [ProteinFamily](ProteinFamily.md)
 * [ProteinIsoform](ProteinIsoform.md)
 * [Publication](Publication.md)
 * [ReagentTargetedGene](ReagentTargetedGene.md)
 * [SequenceVariant](SequenceVariant.md)
 * [Serial](Serial.md)
 * [SiRNA](SiRNA.md)
 * [SmallMolecule](SmallMolecule.md)
 * [Snv](Snv.md)
 * [StudyPopulation](StudyPopulation.md)
 * [Transcript](Transcript.md)
 * [Treatment](Treatment.md)
 * [Vitamin](Vitamin.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |

