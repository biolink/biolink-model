---
title: Browse Biolink Model
has_children: true
nav_order: 2
layout: default
has_toc: false
---

Entity and association taxonomy and datamodel for life-sciences data


## Classes


### Entities

 * [NamedThing](NamedThing.md) - a databased entity or concept/class
    * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
    * [AdministrativeEntity](AdministrativeEntity.md)
       * [Agent](Agent.md) - person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    * [BiologicalEntity](BiologicalEntity.md)
       * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities
          * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
             * [Pathway](Pathway.md)
             * [PhysiologicalProcess](PhysiologicalProcess.md)
          * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.
       * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
          * [Disease](Disease.md)
          * [PhenotypicFeature](PhenotypicFeature.md)
       * [ExposureEvent](ExposureEvent.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
          * [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical substance
             * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular chemical substance
          * [Treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
       * [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
          * [ChemicalSubstance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
             * [Carbohydrate](Carbohydrate.md)
             * [Metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
             * [ProcessedMaterial](ProcessedMaterial.md) - A chemical substance (often a mixture) processed for consumption for nutritional, medical or technical use.
          * [Drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
          * [Food](Food.md) - A substance consumed by a living organism as a source of nutrition
          * [GeneFamily](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
          * [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
             * [CodingSequence](CodingSequence.md)
             * [Exon](Exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
             * [Genome](Genome.md) - A genome is the sum of genetic material within a cell or virion.
             * [Genotype](Genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
             * [Haplotype](Haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
             * [MacromolecularMachine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
                * [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
                   * [Gene](Gene.md)
                   * [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
                      * [RNAProduct](RNAProduct.md)
                         * [RNAProductIsoform](RNAProductIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference RNA
                         * [NoncodingRNAProduct](NoncodingRNAProduct.md)
                            * [MicroRNA](MicroRNA.md)
                      * [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
                         * [ProteinIsoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
                      * [Transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase
                * [MacromolecularComplex](MacromolecularComplex.md)
             * [ReagentTargetedGene](ReagentTargetedGene.md) - A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi
             * [SequenceVariant](SequenceVariant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.
                * [Snv](Snv.md) - SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
       * [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
          * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
             * [Cell](Cell.md)
             * [CellularComponent](CellularComponent.md) - A location in or around a cell
             * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
          * [CellLine](CellLine.md)
          * [IndividualOrganism](IndividualOrganism.md)
             * [Case](Case.md) - An individual organism that has a patient role in some clinical context.
          * [LifeStage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
          * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
    * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
       * [ClinicalIntervention](ClinicalIntervention.md)
       * [ClinicalTrial](ClinicalTrial.md)
    * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
       * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
       * [DataFile](DataFile.md)
          * [SourceFile](SourceFile.md)
       * [DataSet](DataSet.md)
          * [DataSetVersion](DataSetVersion.md)
             * [DataSetSummary](DataSetSummary.md)
             * [DistributionLevel](DistributionLevel.md)
       * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
       * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.
          * [Article](Article.md)
          * [Book](Book.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
          * [BookChapter](BookChapter.md)
          * [Serial](Serial.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
       * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
       * [OrganismTaxon](OrganismTaxon.md) - A classification of a set of organisms. Examples: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
       * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
    * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    * [PhysicalEntity](PhysicalEntity.md) - An entity that has material reality (a.k.a. physical essence).
       * [MaterialSample](MaterialSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
       * [EnvironmentalFeature](EnvironmentalFeature.md)
       * [EnvironmentalProcess](EnvironmentalProcess.md)
       * [GeographicLocation](GeographicLocation.md) - a location that can be described in lat/long coordinates
          * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
    * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner

### Associations

 * [Association](Association.md) - A typed association between two entities, supported by evidence
    * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
       * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
       * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
    * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
    * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
       * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md)
    * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
       * [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) - A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
    * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
    * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
    * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
    * [ChemicalToThingAssociation](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
    * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
    * [DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
       * [DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
    * [DiseaseToExposureAssociation](DiseaseToExposureAssociation.md) - An association between an exposure event and a disease
    * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
    * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
       * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
       * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
       * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
       * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
    * [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
    * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
       * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)
       * [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)
    * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
    * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
       * [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
       * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
          * [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) - An interaction at the molecular level between two physical entities
    * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
    * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
       * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)
    * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
    * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
    * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity it is derived from
    * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype
    * [MaterialSampleToThingAssociation](MaterialSampleToThingAssociation.md) - An association between a material sample and something
    * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
    * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
    * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a genomic entity it is localized to.
       * [GenomicSequenceLocalization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and a genomic entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
    * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
       * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
       * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
       * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts
    * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
    * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
       * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)
    * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
    * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population

### Class Mixins

 * [CaseToThingAssociationMixin](CaseToThingAssociationMixin.md) - An abstract association for use where the case is the subject
 * [CellLineToThingAssociationMixin](CellLineToThingAssociationMixin.md) - An relationship between a cell line and another entity
 * [DiseaseToThingAssociationMixin](DiseaseToThingAssociationMixin.md)
 * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations
    * [ThingToDiseaseAssociationMixin](ThingToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
    * [ThingToPhenotypicFeatureAssociationMixin](ThingToPhenotypicFeatureAssociationMixin.md)
 * [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations
    * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations
       * [ThingToDiseaseAssociationMixin](ThingToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
       * [ThingToPhenotypicFeatureAssociationMixin](ThingToPhenotypicFeatureAssociationMixin.md)
 * [FrequencyQuantifier](FrequencyQuantifier.md)
 * [GeneGrouping](GeneGrouping.md) - any grouping of multiple genes or gene products
 * [GeneProductIsoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
 * [GeneToThingAssociationMixin](GeneToThingAssociationMixin.md)
 * [GenotypeToThingAssociationMixin](GenotypeToThingAssociationMixin.md)
 * [Mixture](Mixture.md) - The physical combination of two or more molecular entities in which the identities are retained and are mixed in the form of solutions, suspensions and colloids.
 * [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 * [Occurrent](Occurrent.md) - A processual entity
 * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
 * [RelationshipQuantifier](RelationshipQuantifier.md)
    * [FrequencyQuantifier](FrequencyQuantifier.md)
    * [SensitivityQuantifier](SensitivityQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
       * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [SubjectOfInvestigation](SubjectOfInvestigation.md) - An entity that has the role of being studied in an investigation, study, or experiment
 * [ThingToDiseaseOrPhenotypicFeatureAssociationMixin](ThingToDiseaseOrPhenotypicFeatureAssociationMixin.md)
 * [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
 * [VariantToThingAssociationMixin](VariantToThingAssociationMixin.md)

### Other Classes

 * [AbstractEntity](AbstractEntity.md) - Any thing that is not a process or a physical mass-bearing entity
    * [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
       * [BiologicalSex](BiologicalSex.md)
          * [GenotypicSex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
          * [PhenotypicSex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
       * [ClinicalCourse](ClinicalCourse.md) - The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
          * [Onset](Onset.md) - The age group in which manifestations appear
       * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, and other aspects
       * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
       * [Inheritance](Inheritance.md) - The pattern in which a particular genetic trait or disorder is passed from one generation to the next
       * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
       * [Zygosity](Zygosity.md)
    * [QuantityValue](QuantityValue.md) - A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value

## Slots


### Predicates

 * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
    * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * [affects abundance of](affects_abundance_of.md) - holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
       * [decreases abundance of](decreases_abundance_of.md) - holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
       * [increases abundance of](increases_abundance_of.md) - holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
    * [affects activity of](affects_activity_of.md) - holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
       * [decreases activity of](decreases_activity_of.md) - holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
       * [increases activity of](increases_activity_of.md) - holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
    * [affects degradation of](affects_degradation_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where chemical degradation is defined act or process of simplifying or breaking down a molecule into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
       * [decreases degradation of](decreases_degradation_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
       * [increases degradation of](increases_degradation_of.md) - holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
    * [affects expression in](affects_expression_in.md) - Holds between a variant and an anatomical entity where the expression of the variant is located in.
    * [affects expression of](affects_expression_of.md) - holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
       * [decreases expression of](decreases_expression_of.md) - holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
       * [increases expression of](increases_expression_of.md) - holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
    * [affects folding of](affects_folding_of.md) - holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
       * [decreases folding of](decreases_folding_of.md) - holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
       * [increases folding of](increases_folding_of.md) - holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
    * [affects localization of](affects_localization_of.md) - holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
       * [decreases localization of](decreases_localization_of.md) - holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
       * [increases localization of](increases_localization_of.md) - holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
    * [affects metabolic processing of](affects_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
       * [decreases metabolic processing of](decreases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
       * [increases metabolic processing of](increases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
    * [affects molecular modification of](affects_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
       * [decreases molecular modification of](decreases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
       * [increases molecular modification of](increases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * [affects mutation rate of](affects_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
       * [decreases mutation rate of](decreases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
       * [increases mutation rate of](increases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
    * [affects response to](affects_response_to.md) - holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
       * [decreases response to](decreases_response_to.md) - holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
       * [increases response to](increases_response_to.md) - holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * [affects secretion of](affects_secretion_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
       * [decreases secretion of](decreases_secretion_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
       * [increases secretion of](increases_secretion_of.md) - holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
    * [affects splicing of](affects_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
       * [decreases splicing of](decreases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
       * [increases splicing of](increases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
    * [affects stability of](affects_stability_of.md) - holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
       * [decreases stability of](decreases_stability_of.md) - holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
       * [increases stability of](increases_stability_of.md) - holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
    * [affects synthesis of](affects_synthesis_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
       * [decreases synthesis of](decreases_synthesis_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
       * [increases synthesis of](increases_synthesis_of.md) - holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
    * [affects transport of](affects_transport_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
       * [decreases transport of](decreases_transport_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
       * [increases transport of](increases_transport_of.md) - holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
    * [affects uptake of](affects_uptake_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
       * [decreases uptake of](decreases_uptake_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
       * [increases uptake of](increases_uptake_of.md) - holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
    * [ameliorates](ameliorates.md) - hA relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
       * [treats](treats.md) - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
    * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
    * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
    * [regulates, entity to entity](regulates_entity_to_entity.md)
       * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
       * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
    * [regulates, process to process](regulates_process_to_process.md)
       * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
       * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [affects abundance of](affects_abundance_of.md) - holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
    * [decreases abundance of](decreases_abundance_of.md) - holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
    * [increases abundance of](increases_abundance_of.md) - holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
 * [affects activity of](affects_activity_of.md) - holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
    * [decreases activity of](decreases_activity_of.md) - holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
    * [increases activity of](increases_activity_of.md) - holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
 * [affects degradation of](affects_degradation_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where chemical degradation is defined act or process of simplifying or breaking down a molecule into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
    * [decreases degradation of](decreases_degradation_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
    * [increases degradation of](increases_degradation_of.md) - holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
 * [affects expression in](affects_expression_in.md) - Holds between a variant and an anatomical entity where the expression of the variant is located in.
 * [affects expression of](affects_expression_of.md) - holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
    * [decreases expression of](decreases_expression_of.md) - holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
    * [increases expression of](increases_expression_of.md) - holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
 * [affects folding of](affects_folding_of.md) - holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
    * [decreases folding of](decreases_folding_of.md) - holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
    * [increases folding of](increases_folding_of.md) - holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
 * [affects localization of](affects_localization_of.md) - holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
    * [decreases localization of](decreases_localization_of.md) - holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
    * [increases localization of](increases_localization_of.md) - holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
 * [affects metabolic processing of](affects_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
    * [decreases metabolic processing of](decreases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
    * [increases metabolic processing of](increases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
 * [affects molecular modification of](affects_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * [decreases molecular modification of](decreases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * [increases molecular modification of](increases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
 * [affects mutation rate of](affects_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
    * [decreases mutation rate of](decreases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
    * [increases mutation rate of](increases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
 * [affects response to](affects_response_to.md) - holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * [decreases response to](decreases_response_to.md) - holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * [increases response to](increases_response_to.md) - holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
 * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
    * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
    * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
 * [affects secretion of](affects_secretion_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
    * [decreases secretion of](decreases_secretion_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
    * [increases secretion of](increases_secretion_of.md) - holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
 * [affects splicing of](affects_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
    * [decreases splicing of](decreases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
    * [increases splicing of](increases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
 * [affects stability of](affects_stability_of.md) - holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
    * [decreases stability of](decreases_stability_of.md) - holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
    * [increases stability of](increases_stability_of.md) - holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
 * [affects synthesis of](affects_synthesis_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
    * [decreases synthesis of](decreases_synthesis_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
    * [increases synthesis of](increases_synthesis_of.md) - holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
 * [affects transport of](affects_transport_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
    * [decreases transport of](decreases_transport_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
    * [increases transport of](increases_transport_of.md) - holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
 * [affects uptake of](affects_uptake_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
    * [decreases uptake of](decreases_uptake_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
    * [increases uptake of](increases_uptake_of.md) - holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
 * [ameliorates](ameliorates.md) - hA relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
    * [treats](treats.md) - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
 * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
 * [biomarker for](biomarker_for.md) - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
 * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
 * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
    * [causes adverse event](causes_adverse_event.md) - holds between a drug and a disease or phenotype that can be caused by the drug
 * [causes adverse event](causes_adverse_event.md) - holds between a drug and a disease or phenotype that can be caused by the drug
 * [chemically similar to](chemically_similar_to.md) - holds between one chemical substances and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [close match](close_match.md) - holds between two entities that are considered a skos:closeMatch to one another
    * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
       * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
    * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
    * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
    * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
 * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
 * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
 * [contraindicated for](contraindicated_for.md) - Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug.
 * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
    * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
       * [causes adverse event](causes_adverse_event.md) - holds between a drug and a disease or phenotype that can be caused by the drug
 * [contributor](contributor.md)
    * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
    * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
    * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
    * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [correlated with](correlated_with.md) - holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * [biomarker for](biomarker_for.md) - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
    * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
 * [decreases abundance of](decreases_abundance_of.md) - holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
 * [decreases activity of](decreases_activity_of.md) - holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
 * [decreases degradation of](decreases_degradation_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
 * [decreases expression of](decreases_expression_of.md) - holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
 * [decreases folding of](decreases_folding_of.md) - holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
 * [decreases localization of](decreases_localization_of.md) - holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
 * [decreases metabolic processing of](decreases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
 * [decreases molecular interaction](decreases_molecular_interaction.md) - indicates that the source decreases the molecular interaction between the target and some other molecular entity
 * [decreases molecular modification of](decreases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
 * [decreases mutation rate of](decreases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
 * [decreases response to](decreases_response_to.md) - holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
 * [decreases secretion of](decreases_secretion_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
 * [decreases splicing of](decreases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
 * [decreases stability of](decreases_stability_of.md) - holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
 * [decreases synthesis of](decreases_synthesis_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
 * [decreases transport of](decreases_transport_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
 * [decreases uptake of](decreases_uptake_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
 * [derives from](derives_from.md) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
 * [derives into](derives_into.md) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
 * [develops from](develops_from.md)
 * [directly interacts with](directly_interacts_with.md) - Holds between molecular entities that physically and directly interact with each other
 * [disease has basis in](disease_has_basis_in.md) - A relation that holds between a disease and an entity where the state of the entity has contribution to the disease.
 * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
 * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
 * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
 * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
 * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
 * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
    * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
 * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
 * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
 * [genetic association](genetic_association.md) - Co-occurrence of a certain allele of a genetic marker and the phenotype of interest in the same individuals at above-chance level
    * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
    * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
 * [genetically interacts with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
 * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
 * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
 * [has decreased amount](has_decreased_amount.md)
 * [has gene product](has_gene_product.md) - holds between a gene and a transcribed and/or translated product generated from it
 * [has increased amount](has_increased_amount.md)
 * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
 * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
 * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
 * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
    * [has variant part](has_variant_part.md) - holds between a genomic entity and a genotypic entity that is a sub-component of it
 * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
    * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
    * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
    * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has phenotype](has_phenotype.md) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
 * [has sequence location](has_sequence_location.md) - holds between two genomic entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
 * [has variant part](has_variant_part.md) - holds between a genomic entity and a genotypic entity that is a sub-component of it
 * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
    * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
    * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
    * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
 * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
 * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
 * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
 * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
 * [in taxon](in_taxon.md) - connects a thing to a class representing a taxon
 * [increases abundance of](increases_abundance_of.md) - holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
 * [increases activity of](increases_activity_of.md) - holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
 * [increases degradation of](increases_degradation_of.md) - holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
 * [increases expression of](increases_expression_of.md) - holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
 * [increases folding of](increases_folding_of.md) - holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
 * [increases localization of](increases_localization_of.md) - holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
 * [increases metabolic processing of](increases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
 * [increases molecular interaction](increases_molecular_interaction.md) - indicates that the source increases the molecular interaction between the target and some other molecular entity
 * [increases molecular modification of](increases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
 * [increases mutation rate of](increases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
 * [increases response to](increases_response_to.md) - holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
 * [increases secretion of](increases_secretion_of.md) - holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
 * [increases splicing of](increases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
 * [increases stability of](increases_stability_of.md) - holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
 * [increases synthesis of](increases_synthesis_of.md) - holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
 * [increases transport of](increases_transport_of.md) - holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
 * [increases uptake of](increases_uptake_of.md) - holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
 * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
    * [directly interacts with](directly_interacts_with.md) - Holds between molecular entities that physically and directly interact with each other
    * [genetically interacts with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    * [physically interacts with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction
       * [molecularly interacts with](molecularly_interacts_with.md)
          * [decreases molecular interaction](decreases_molecular_interaction.md) - indicates that the source decreases the molecular interaction between the target and some other molecular entity
          * [increases molecular interaction](increases_molecular_interaction.md) - indicates that the source increases the molecular interaction between the target and some other molecular entity
 * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
 * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
 * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
 * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
 * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
 * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a genomic entity
    * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
    * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
    * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
    * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
    * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
    * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
    * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
 * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
 * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
 * [lacks part](lacks_part.md)
 * [located in](located_in.md) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
 * [location of](location_of.md) - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
 * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
 * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [molecularly interacts with](molecularly_interacts_with.md)
    * [decreases molecular interaction](decreases_molecular_interaction.md) - indicates that the source decreases the molecular interaction between the target and some other molecular entity
    * [increases molecular interaction](increases_molecular_interaction.md) - indicates that the source increases the molecular interaction between the target and some other molecular entity
 * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
 * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
 * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
 * [occurs in](occurs_in.md) - holds between a process and a material entity or site within which the process occurs
 * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
 * [overlaps](overlaps.md) - holds between entities that overlap in their extents (materials or processes)
    * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
       * [has variant part](has_variant_part.md) - holds between a genomic entity and a genotypic entity that is a sub-component of it
    * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
 * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
 * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
 * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
    * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
       * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
    * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
 * [physically interacts with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction
    * [molecularly interacts with](molecularly_interacts_with.md)
       * [decreases molecular interaction](decreases_molecular_interaction.md) - indicates that the source decreases the molecular interaction between the target and some other molecular entity
       * [increases molecular interaction](increases_molecular_interaction.md) - indicates that the source increases the molecular interaction between the target and some other molecular entity
 * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
 * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
 * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
 * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
 * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
 * [produced by](produced_by.md)
 * [produces](produces.md) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
 * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
 * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [regulates, entity to entity](regulates_entity_to_entity.md)
    * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
    * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
 * [regulates, process to process](regulates_process_to_process.md)
    * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
    * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [related condition](related_condition.md)
 * [related to](related_to.md) - A relationship that is asserted between two named things
    * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
       * [affects abundance of](affects_abundance_of.md) - holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
          * [decreases abundance of](decreases_abundance_of.md) - holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
          * [increases abundance of](increases_abundance_of.md) - holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
       * [affects activity of](affects_activity_of.md) - holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
          * [decreases activity of](decreases_activity_of.md) - holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
          * [increases activity of](increases_activity_of.md) - holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
       * [affects degradation of](affects_degradation_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where chemical degradation is defined act or process of simplifying or breaking down a molecule into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
          * [decreases degradation of](decreases_degradation_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
          * [increases degradation of](increases_degradation_of.md) - holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
       * [affects expression in](affects_expression_in.md) - Holds between a variant and an anatomical entity where the expression of the variant is located in.
       * [affects expression of](affects_expression_of.md) - holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
          * [decreases expression of](decreases_expression_of.md) - holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
          * [increases expression of](increases_expression_of.md) - holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
       * [affects folding of](affects_folding_of.md) - holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
          * [decreases folding of](decreases_folding_of.md) - holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
          * [increases folding of](increases_folding_of.md) - holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
       * [affects localization of](affects_localization_of.md) - holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
          * [decreases localization of](decreases_localization_of.md) - holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
          * [increases localization of](increases_localization_of.md) - holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
       * [affects metabolic processing of](affects_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
          * [decreases metabolic processing of](decreases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
          * [increases metabolic processing of](increases_metabolic_processing_of.md) - holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
       * [affects molecular modification of](affects_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
          * [decreases molecular modification of](decreases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
          * [increases molecular modification of](increases_molecular_modification_of.md) - holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
       * [affects mutation rate of](affects_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
          * [decreases mutation rate of](decreases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
          * [increases mutation rate of](increases_mutation_rate_of.md) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
       * [affects response to](affects_response_to.md) - holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
          * [decreases response to](decreases_response_to.md) - holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
          * [increases response to](increases_response_to.md) - holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
       * [affects secretion of](affects_secretion_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
          * [decreases secretion of](decreases_secretion_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
          * [increases secretion of](increases_secretion_of.md) - holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
       * [affects splicing of](affects_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
          * [decreases splicing of](decreases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
          * [increases splicing of](increases_splicing_of.md) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
       * [affects stability of](affects_stability_of.md) - holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
          * [decreases stability of](decreases_stability_of.md) - holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
          * [increases stability of](increases_stability_of.md) - holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
       * [affects synthesis of](affects_synthesis_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
          * [decreases synthesis of](decreases_synthesis_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
          * [increases synthesis of](increases_synthesis_of.md) - holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
       * [affects transport of](affects_transport_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
          * [decreases transport of](decreases_transport_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
          * [increases transport of](increases_transport_of.md) - holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
       * [affects uptake of](affects_uptake_of.md) - holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
          * [decreases uptake of](decreases_uptake_of.md) - holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
          * [increases uptake of](increases_uptake_of.md) - holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
       * [ameliorates](ameliorates.md) - hA relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
          * [treats](treats.md) - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
       * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
       * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
       * [regulates, entity to entity](regulates_entity_to_entity.md)
          * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
          * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
       * [regulates, process to process](regulates_process_to_process.md)
          * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
          * [positively regulates, process to process](positively_regulates_process_to_process.md)
    * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
       * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
       * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
    * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
    * [close match](close_match.md) - holds between two entities that are considered a skos:closeMatch to one another
       * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
          * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
    * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
       * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
       * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
       * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
       * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
    * [contraindicated for](contraindicated_for.md) - Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug.
    * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
       * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
          * [causes adverse event](causes_adverse_event.md) - holds between a drug and a disease or phenotype that can be caused by the drug
    * [contributor](contributor.md)
       * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
       * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
       * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
       * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
    * [correlated with](correlated_with.md) - holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * [biomarker for](biomarker_for.md) - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
       * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
       * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
    * [derives from](derives_from.md) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [derives into](derives_into.md) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [develops from](develops_from.md)
    * [disease has basis in](disease_has_basis_in.md) - A relation that holds between a disease and an entity where the state of the entity has contribution to the disease.
    * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
    * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
    * [genetic association](genetic_association.md) - Co-occurrence of a certain allele of a genetic marker and the phenotype of interest in the same individuals at above-chance level
       * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
       * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
    * [has decreased amount](has_decreased_amount.md)
    * [has gene product](has_gene_product.md) - holds between a gene and a transcribed and/or translated product generated from it
    * [has increased amount](has_increased_amount.md)
    * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
    * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
    * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
       * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
       * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
       * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
    * [has phenotype](has_phenotype.md) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * [has sequence location](has_sequence_location.md) - holds between two genomic entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
    * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
    * [in taxon](in_taxon.md) - connects a thing to a class representing a taxon
    * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
       * [directly interacts with](directly_interacts_with.md) - Holds between molecular entities that physically and directly interact with each other
       * [genetically interacts with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
       * [physically interacts with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction
          * [molecularly interacts with](molecularly_interacts_with.md)
             * [decreases molecular interaction](decreases_molecular_interaction.md) - indicates that the source decreases the molecular interaction between the target and some other molecular entity
             * [increases molecular interaction](increases_molecular_interaction.md) - indicates that the source increases the molecular interaction between the target and some other molecular entity
    * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a genomic entity
       * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
       * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
       * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
       * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
       * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
       * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
       * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
    * [lacks part](lacks_part.md)
    * [located in](located_in.md) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
    * [location of](location_of.md) - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
    * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
    * [occurs in](occurs_in.md) - holds between a process and a material entity or site within which the process occurs
    * [overlaps](overlaps.md) - holds between entities that overlap in their extents (materials or processes)
       * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
          * [has variant part](has_variant_part.md) - holds between a genomic entity and a genotypic entity that is a sub-component of it
       * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
    * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
       * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
          * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
       * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
    * [produced by](produced_by.md)
    * [produces](produces.md) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
    * [related condition](related_condition.md)
    * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
       * [chemically similar to](chemically_similar_to.md) - holds between one chemical substances and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
       * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
          * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
          * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
          * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
       * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
    * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
    * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
    * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
       * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
       * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
    * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
 * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
    * [chemically similar to](chemically_similar_to.md) - holds between one chemical substances and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
    * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
       * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
       * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
       * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
    * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
 * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
 * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
    * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
    * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
 * [treats](treats.md) - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
 * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.

### Node Properties

 * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
 * [affiliation](affiliation.md) - a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
 * [aggregate statistic](aggregate_statistic.md)
    * [has count](has_count.md) - number of things with a particular property
    * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
    * [has quotient](has_quotient.md)
    * [has total](has_total.md) - total number of things in a particular reference set
 * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
 * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * [chapter](chapter.md) - chapter of a book
 * [created_with](created_with.md)
 * [creation date](creation_date.md) - date on which thing was created. This can be applied to nodes or edges
 * [description](description.md) - a human-readable description of a thing
 * [distribution](distribution.md)
 * [download url](download_url.md)
 * [filler](filler.md) - The value in a property-value tuple
 * [format](format.md)
 * [full name](full_name.md) - a long-form human readable name for a thing
 * [has active ingredient](has_active_ingredient.md) - one or more chemical substance which are the active ingredient(s) of a drug
 * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
 * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
 * [has constituent](has_constituent.md) - one or more chemical substances within a mixture
 * [has count](has_count.md) - number of things with a particular property
 * [has drug](has_drug.md) - connects an entity to a single drug
 * [has excipient](has_excipient.md) - one or more (generally inert) chemical substances which are formulated alongside the active ingredient of a drug
 * [has gene](has_gene.md) - connects an entity to a single gene
 * [has nutrient](has_nutrient.md) - one or more chemical substance which are growth factors for a living organism
 * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
 * [has quotient](has_quotient.md)
 * [has receptor](has_receptor.md) - the organism or organism part being exposed
 * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the receptor
 * [has stressor](has_stressor.md) - the process or entity that the receptor is being exposed to
 * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238
 * [has total](has_total.md) - total number of things in a particular reference set
 * [has zygosity](has_zygosity.md)
 * [id](id.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
 * [iri](iri.md) - An IRI for the node. This is determined by the id using expansion rules.
 * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
 * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
 * [keywords](keywords.md) - keywords tagging a publication
 * [latitude](latitude.md) - latitude
 * [license](license.md)
 * [longitude](longitude.md) - longitude
 * [mesh terms](mesh_terms.md) - mesh terms tagging a publication
 * [name](name.md) - A human-readable name for a thing
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
    * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * [affiliation](affiliation.md) - a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * [aggregate statistic](aggregate_statistic.md)
       * [has count](has_count.md) - number of things with a particular property
       * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
       * [has quotient](has_quotient.md)
       * [has total](has_total.md) - total number of things in a particular reference set
    * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * [chapter](chapter.md) - chapter of a book
    * [created_with](created_with.md)
    * [creation date](creation_date.md) - date on which thing was created. This can be applied to nodes or edges
    * [description](description.md) - a human-readable description of a thing
    * [distribution](distribution.md)
    * [download url](download_url.md)
    * [filler](filler.md) - The value in a property-value tuple
    * [format](format.md)
    * [full name](full_name.md) - a long-form human readable name for a thing
    * [has active ingredient](has_active_ingredient.md) - one or more chemical substance which are the active ingredient(s) of a drug
    * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
    * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
    * [has constituent](has_constituent.md) - one or more chemical substances within a mixture
    * [has drug](has_drug.md) - connects an entity to a single drug
    * [has excipient](has_excipient.md) - one or more (generally inert) chemical substances which are formulated alongside the active ingredient of a drug
    * [has gene](has_gene.md) - connects an entity to a single gene
    * [has nutrient](has_nutrient.md) - one or more chemical substance which are growth factors for a living organism
    * [has receptor](has_receptor.md) - the organism or organism part being exposed
    * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the receptor
    * [has stressor](has_stressor.md) - the process or entity that the receptor is being exposed to
    * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238
    * [has zygosity](has_zygosity.md)
    * [id](id.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * [iri](iri.md) - An IRI for the node. This is determined by the id using expansion rules.
    * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
    * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
    * [keywords](keywords.md) - keywords tagging a publication
    * [latitude](latitude.md) - latitude
    * [license](license.md)
    * [longitude](longitude.md) - longitude
    * [mesh terms](mesh_terms.md) - mesh terms tagging a publication
    * [name](name.md) - A human-readable name for a thing
    * [pages](pages.md) - page number of source referenced for statement or publication
    * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
    * [retrieved on](retrieved_on.md)
    * [rights](rights.md)
    * [source data file](source_data_file.md)
    * [source version](source_version.md)
    * [source web page](source_web_page.md)
    * [summary](summary.md) - executive  summary of a publication
    * [symbol](symbol.md) - Symbol for a particular thing
    * [synonym](synonym.md) - Alternate human-readable names for a thing
    * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
    * [timepoint](timepoint.md) - a point in time
    * [type](type.md)
       * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
    * [update date](update_date.md) - date on which thing was updated. This can be applied to nodes or edges
    * [version of](version_of.md)
    * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
    * [xref](xref.md) - Alternate CURIEs for a thing
 * [pages](pages.md) - page number of source referenced for statement or publication
 * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
 * [retrieved on](retrieved_on.md)
 * [rights](rights.md)
 * [source data file](source_data_file.md)
 * [source version](source_version.md)
 * [source web page](source_web_page.md)
 * [summary](summary.md) - executive  summary of a publication
 * [symbol](symbol.md) - Symbol for a particular thing
 * [synonym](synonym.md) - Alternate human-readable names for a thing
 * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
 * [timepoint](timepoint.md) - a point in time
 * [type](type.md)
    * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * [update date](update_date.md) - date on which thing was updated. This can be applied to nodes or edges
 * [version of](version_of.md)
 * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
 * [xref](xref.md) - Alternate CURIEs for a thing

### Edge Properties

 * [association slot](association_slot.md) - any slot that relates an association to another entity
    * [association type](association_type.md) - connects an association to the type of association (e.g. gene to phenotype)
    * [change is catalyzed by](change_is_catalyzed_by.md) - hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
    * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
    * [clinical modifier qualifier](clinical_modifier_qualifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [edge label](edge_label.md)
    * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
    * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
    * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
    * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
    * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * [provided by](provided_by.md) - connects an association to the agent (person, organization or group) that provided it
    * [publications](publications.md) - connects an association to publications supporting the association
    * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
    * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
    * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a genome sequence localization edge. These edges connect a genomic entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
       * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
       * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
          * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
          * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on.
       * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
       * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
    * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
    * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * [stage qualifier](stage_qualifier.md) - stage at which expression takes place
    * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
 * [association type](association_type.md) - connects an association to the type of association (e.g. gene to phenotype)
 * [change is catalyzed by](change_is_catalyzed_by.md) - hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
 * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
 * [clinical modifier qualifier](clinical_modifier_qualifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 * [edge label](edge_label.md)
 * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
 * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
 * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
 * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
 * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
 * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
    * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
    * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on.
 * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
 * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
 * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
 * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
 * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
 * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
 * [provided by](provided_by.md) - connects an association to the agent (person, organization or group) that provided it
 * [publications](publications.md) - connects an association to publications supporting the association
 * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
 * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
 * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
 * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a genome sequence localization edge. These edges connect a genomic entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
    * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
    * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
       * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
       * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on.
    * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
    * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
 * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
 * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
 * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
 * [stage qualifier](stage_qualifier.md) - stage at which expression takes place
 * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on.
 * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
 * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.

### Slot Mixins

 * [negatively regulates](negatively_regulates.md)
 * [positively regulates](positively_regulates.md)
 * [regulates](regulates.md)

### Other Slots

 * [has attribute](has_attribute.md) - connects any named thing to an attribute
 * [has attribute type](has_attribute_type.md) - connects an attribute to a class that describes it
 * [has numeric value](has_numeric_value.md) - connects a quantity value to a number
 * [has qualitative value](has_qualitative_value.md) - connects an attribute to a value
 * [has quantitative value](has_quantitative_value.md) - connects an attribute to a value
 * [has unit](has_unit.md) - connects a quantity value to a unit
 * [interacting molecules category](interacting_molecules_category.md)

## Types


### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

### Defined

 * [BiologicalSequence](types/BiologicalSequence.md)  ([String](types/String.md)) 
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [CategoryType](types/CategoryType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A primitive type in which the value denotes a class within the biolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the biolink class, for example biolink:Gene. For an RDF representation, the value should be a URI such as https://w3id.org/biolink/vocab/Gene
 * [ChemicalFormulaValue](types/ChemicalFormulaValue.md)  (**str**)  - A chemical formula
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Frequency](types/Frequency.md)  ([String](types/String.md)) 
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [IriType](types/IriType.md)  ([Uriorcurie](types/Uriorcurie.md))  - An IRI
 * [LabelType](types/LabelType.md)  ([String](types/String.md))  - A string that provides a human-readable name for a thing
 * [NarrativeText](types/NarrativeText.md)  ([String](types/String.md))  - A string that provides a human-readable description of something
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [PercentageFrequencyValue](types/PercentageFrequencyValue.md)  ([Double](types/Double.md)) 
 * [PredicateType](types/PredicateType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A CURIE from the biolink related_to hierarchy. For example, biolink:related_to, biolink:causes, biolink:treats.
 * [Quotient](types/Quotient.md)  ([Double](types/Double.md)) 
 * [String](types/String.md)  (**str**)  - A character string
 * [SymbolType](types/SymbolType.md)  ([String](types/String.md)) 
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [TimeType](types/TimeType.md)  ([Time](types/Time.md)) 
 * [Unit](types/Unit.md)  ([String](types/String.md)) 
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
