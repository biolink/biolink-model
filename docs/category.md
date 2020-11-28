---
parent: Node Properties
title: biolink:category
grand_parent: Slots
layout: default
---

# Slot: category

translator_minimal
{: .translator_minimal-subset-label }


Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}

URI: [biolink:category](https://w3id.org/biolink/vocab/category)

## Domain and Range

[NamedThing](NamedThing.md) ->  <sub>1..*</sub> [CategoryType](types/CategoryType.md)

## Parents

 *  is_a: [type](type.md)

## Children


## Used by

 * [RNAProduct](RNAProduct.md)
 * [RNAProductIsoform](RNAProductIsoform.md)
 * [AdministrativeEntity](AdministrativeEntity.md)
 * [Agent](Agent.md)
 * [AnatomicalEntity](AnatomicalEntity.md)
 * [Article](Article.md)
 * [Behavior](Behavior.md)
 * [BiologicalEntity](BiologicalEntity.md)
 * [BiologicalProcess](BiologicalProcess.md)
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)
 * [Book](Book.md)
 * [BookChapter](BookChapter.md)
 * [Carbohydrate](Carbohydrate.md)
 * [Case](Case.md)
 * [Cell](Cell.md)
 * [CellLine](CellLine.md)
 * [CellularComponent](CellularComponent.md)
 * [ChemicalExposure](ChemicalExposure.md)
 * [ChemicalSubstance](ChemicalSubstance.md)
 * [ClinicalEntity](ClinicalEntity.md)
 * [ClinicalIntervention](ClinicalIntervention.md)
 * [ClinicalTrial](ClinicalTrial.md)
 * [CodingSequence](CodingSequence.md)
 * [ConfidenceLevel](ConfidenceLevel.md)
 * [DataFile](DataFile.md)
 * [DataSet](DataSet.md)
 * [DataSetSummary](DataSetSummary.md)
 * [DataSetVersion](DataSetVersion.md)
 * [Device](Device.md)
 * [Disease](Disease.md)
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [DistributionLevel](DistributionLevel.md)
 * [Drug](Drug.md)
 * [DrugExposure](DrugExposure.md)
 * [EnvironmentalFeature](EnvironmentalFeature.md)
 * [EnvironmentalProcess](EnvironmentalProcess.md)
 * [EvidenceType](EvidenceType.md)
 * [Exon](Exon.md)
 * [ExposureEvent](ExposureEvent.md)
 * [Food](Food.md)
 * [Gene](Gene.md)
 * [GeneFamily](GeneFamily.md)
 * [GeneOntologyClass](GeneOntologyClass.md)
 * [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [GeneProduct](GeneProduct.md)
 * [Genome](Genome.md)
 * [GenomicEntity](GenomicEntity.md)
 * [Genotype](Genotype.md)
 * [GeographicLocation](GeographicLocation.md)
 * [GeographicLocationAtTime](GeographicLocationAtTime.md)
 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
 * [Haplotype](Haplotype.md)
 * [IndividualOrganism](IndividualOrganism.md)
 * [InformationContentEntity](InformationContentEntity.md)
 * [LifeStage](LifeStage.md)
 * [MacromolecularComplex](MacromolecularComplex.md)
 * [MacromolecularMachine](MacromolecularMachine.md)
 * [MaterialSample](MaterialSample.md)
 * [Metabolite](Metabolite.md)
 * [MicroRNA](MicroRNA.md)
 * [MolecularActivity](MolecularActivity.md)
 * [MolecularEntity](MolecularEntity.md)
 * [NamedThing](NamedThing.md)
 * [NoncodingRNAProduct](NoncodingRNAProduct.md)
 * [OntologyClass](OntologyClass.md)
 * [OrganismTaxon](OrganismTaxon.md)
 * [OrganismalEntity](OrganismalEntity.md)
 * [Pathway](Pathway.md)
 * [Phenomenon](Phenomenon.md)
 * [PhenotypicFeature](PhenotypicFeature.md)
 * [PhysicalEntity](PhysicalEntity.md)
 * [PhysiologicalProcess](PhysiologicalProcess.md)
 * [PlanetaryEntity](PlanetaryEntity.md)
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [Procedure](Procedure.md)
 * [ProcessedMaterial](ProcessedMaterial.md)
 * [Protein](Protein.md)
 * [ProteinIsoform](ProteinIsoform.md)
 * [Publication](Publication.md)
 * [ReagentTargetedGene](ReagentTargetedGene.md)
 * [RelationshipType](RelationshipType.md)
 * [SequenceVariant](SequenceVariant.md)
 * [Serial](Serial.md)
 * [Snv](Snv.md)
 * [SourceFile](SourceFile.md)
 * [Transcript](Transcript.md)
 * [Treatment](Treatment.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |

