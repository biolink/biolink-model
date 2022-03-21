# Biolink-Model

Entity and association taxonomy and datamodel for life-sciences data

URI: https://w3id.org/biolink/biolink-model

## Classes

| Class | Description |
| --- | --- |
| [OntologyClass](OntologyClass.md) | a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type. | 
| [Annotation](Annotation.md) | Biolink Model root class for entity annotations. | 
| [QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value | 
| [Attribute](Attribute.md) | A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material. | 
| [BiologicalSex](BiologicalSex.md) | None | 
| [PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present. | 
| [GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes. | 
| [SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease | 
| [RelationshipQuantifier](RelationshipQuantifier.md) | None | 
| [SensitivityQuantifier](SensitivityQuantifier.md) | None | 
| [SpecificityQuantifier](SpecificityQuantifier.md) | None | 
| [PathognomonicityQuantifier](PathognomonicityQuantifier.md) | A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease | 
| [FrequencyQuantifier](FrequencyQuantifier.md) | None | 
| [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) | None | 
| [Entity](Entity.md) | Root Biolink Model class for all things and informational relationships, real or imagined. | 
| [NamedThing](NamedThing.md) | a databased entity or concept/class | 
| [RelationshipType](RelationshipType.md) | An OWL property used as an edge label | 
| [GeneOntologyClass](GeneOntologyClass.md) | an ontology class that describes a functional aspect of a gene, gene prodoct or complex | 
| [UnclassifiedOntologyClass](UnclassifiedOntologyClass.md) | this is used for nodes that are taken from an ontology but are not typed using an existing biolink class | 
| [TaxonomicRank](TaxonomicRank.md) | A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom) | 
| [OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies. | 
| [Event](Event.md) | Something that happens at a given place and time. | 
| [AdministrativeEntity](AdministrativeEntity.md) | None | 
| [Agent](Agent.md) | person, group, organization or project that provides a piece of information (i.e. a knowledge association) | 
| [InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is used as support. | 
| [Dataset](Dataset.md) | an item that refers to a collection of data from a data source. | 
| [DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset. | 
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset. | 
| [DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset. | 
| [ConfidenceLevel](ConfidenceLevel.md) | Level of confidence in a statement | 
| [EvidenceType](EvidenceType.md) | Class of evidence that supports an association | 
| [InformationResource](InformationResource.md) | A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb. | 
| [Publication](Publication.md) | Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses. | 
| [Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledge graph support its utility. | 
| [BookChapter](BookChapter.md) | None | 
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledge graph support its utility. | 
| [Article](Article.md) | None | 
| [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) | Either a physical or processual entity. | 
| [PhysicalEssence](PhysicalEssence.md) | Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge. | 
| [PhysicalEntity](PhysicalEntity.md) | An entity that has material reality (a.k.a. physical essence). | 
| [Occurrent](Occurrent.md) | A processual entity. | 
| [ActivityAndBehavior](ActivityAndBehavior.md) | Activity or behavior of any independent integral living, organization or mechanical actor in the world | 
| [Activity](Activity.md) | An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities. | 
| [Procedure](Procedure.md) | A series of actions conducted in a certain order or manner | 
| [Phenomenon](Phenomenon.md) | a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question | 
| [Device](Device.md) | A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment | 
| [StudyPopulation](StudyPopulation.md) | A group of people banded together or treated as a group as participants in a research study. | 
| [SubjectOfInvestigation](SubjectOfInvestigation.md) | An entity that has the role of being studied in an investigation, study, or experiment | 
| [MaterialSample](MaterialSample.md) | A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO] | 
| [PlanetaryEntity](PlanetaryEntity.md) | Any entity or process that exists at the level of the whole planet | 
| [EnvironmentalProcess](EnvironmentalProcess.md) | None | 
| [EnvironmentalFeature](EnvironmentalFeature.md) | None | 
| [GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates | 
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular time | 
| [BiologicalEntity](BiologicalEntity.md) | None | 
| [ThingWithTaxon](ThingWithTaxon.md) | A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes | 
| [GenomicEntity](GenomicEntity.md) | None | 
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently bonded atoms. | 
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemistry. | 
| [ChemicalSubstance](ChemicalSubstance.md) | None | 
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion). | 
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular entities. | 
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included. | 
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry. | 
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown concentration and stoichiometry. | 
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system. | 
| [MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromolecular complex. | 
| [BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions | 
| [Pathway](Pathway.md) | None | 
| [PhysiologicalProcess](PhysiologicalProcess.md) | None | 
| [Behavior](Behavior.md) | None | 
| [ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a material entity that is created or changed during material processing. | 
| [Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease | 
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | None | 
| [FoodAdditive](FoodAdditive.md) | None | 
| [Nutrient](Nutrient.md) | None | 
| [Macronutrient](Macronutrient.md) | None | 
| [Micronutrient](Micronutrient.md) | None | 
| [Vitamin](Vitamin.md) | None | 
| [Food](Food.md) | A substance consumed by a living organism as a source of nutrition | 
| [OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity. | 
| [PhenotypicQuality](PhenotypicQuality.md) | A property of a phenotype | 
| [Inheritance](Inheritance.md) | The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc. | 
| [OrganismalEntity](OrganismalEntity.md) | A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities | 
| [LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult stages | 
| [IndividualOrganism](IndividualOrganism.md) | An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576 | 
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes. | 
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate. | 
| [Disease](Disease.md) | None | 
| [PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement. | 
| [BehavioralFeature](BehavioralFeature.md) | A phenotypic feature which is behavioral in nature. | 
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part | 
| [CellularComponent](CellularComponent.md) | A location in or around a cell | 
| [Cell](Cell.md) | None | 
| [CellLine](CellLine.md) | None | 
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | None | 
| [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) | A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities. | 
| [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md) | A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities. | 
| [MacromolecularMachineMixin](MacromolecularMachineMixin.md) | A union of gene locus, gene product, and macromolecular complex mixin. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this. | 
| [GeneOrGeneProduct](GeneOrGeneProduct.md) | A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another | 
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions. | 
| [GeneProductMixin](GeneProductMixin.md) | The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules. | 
| [GeneProductIsoformMixin](GeneProductIsoformMixin.md) | This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms. | 
| [MacromolecularComplexMixin](MacromolecularComplexMixin.md) | A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together. | 
| [Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion. | 
| [Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing. | 
| [Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase. | 
| [CodingSequence](CodingSequence.md) | None | 
| [Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule. | 
| [Protein](Protein.md) | A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA | 
| [ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/ | 
| [ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain. | 
| [ProteinFamily](ProteinFamily.md) | None | 
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences. | 
| [RNAProduct](RNAProduct.md) | None | 
| [RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference RNA | 
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | None | 
| [MicroRNA](MicroRNA.md) | None | 
| [SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules. | 
| [GeneGroupingMixin](GeneGroupingMixin.md) | any grouping of multiple genes or gene products | 
| [GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent | 
| [Zygosity](Zygosity.md) | None | 
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background | 
| [Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] | 
| [SequenceVariant](SequenceVariant.md) | An allele that varies in its sequence from what is considered the reference allele at that locus. | 
| [Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist | 
| [ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi. | 
| [ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation | 
| [ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot. | 
| [ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology, with respect to severity, laterality, and other aspects | 
| [ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual | 
| [Onset](Onset.md) | The age group in which (disease) symptom manifestations appear | 
| [ClinicalEntity](ClinicalEntity.md) | Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities | 
| [ClinicalTrial](ClinicalTrial.md) | None | 
| [ClinicalIntervention](ClinicalIntervention.md) | None | 
| [ClinicalFinding](ClinicalFinding.md) | this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations. | 
| [Hospitalization](Hospitalization.md) | None | 
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation | 
| [Case](Case.md) | An individual (human) organism that has a patient role in some clinical context. | 
| [Cohort](Cohort.md) | A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time. | 
| [ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes | 
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome. | 
| [PathologicalEntityMixin](PathologicalEntityMixin.md) | A pathological (abnormal) structure or process. | 
| [PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level. | 
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease. | 
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level. | 
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome. | 
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer. | 
| [ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity. | 
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug. | 
| [DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug. | 
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome. | 
| [Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures | 
| [BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses). | 
| [GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some impactful entity. | 
| [EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants. | 
| [BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individual. | 
| [SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty). | 
| [Outcome](Outcome.md) | An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes. | 
| [PathologicalProcessOutcome](PathologicalProcessOutcome.md) | An outcome resulting from an exposure event which is the manifestation of a pathological process. | 
| [PathologicalAnatomicalOutcome](PathologicalAnatomicalOutcome.md) | An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure. | 
| [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) | Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype. | 
| [BehavioralOutcome](BehavioralOutcome.md) | An outcome resulting from an exposure event which is the manifestation of human behavior. | 
| [HospitalizationOutcome](HospitalizationOutcome.md) | An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) hospitalization. | 
| [MortalityOutcome](MortalityOutcome.md) | An outcome of death from resulting from an exposure event. | 
| [EpidemiologicalOutcome](EpidemiologicalOutcome.md) | An epidemiological outcome, such as societal disease burden, resulting from an exposure event. | 
| [SocioeconomicOutcome](SocioeconomicOutcome.md) | An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event | 
| [Association](Association.md) | A typed association between two entities, supported by evidence | 
| [ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents that contribute to its realisation | 
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-component of it | 
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality | 
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant. | 
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction. | 
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same) | 
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs. | 
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same conditions. | 
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation) | 
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities | 
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | An relationship between a cell line and another entity | 
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype. | 
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity | 
| [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | An interaction between a drug and another entity | 
| [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity | 
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | An abstract association for use where the case is the subject | 
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another. | 
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | None | 
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | None | 
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
  IF
  R has-input C1 AND
  R has-output C2 AND
  R enabled-by P AND
  R type Reaction
  THEN
  C1 derives-into C2 <<catalyst qualifier P>> | 
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype. | 
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway. | 
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | An interaction between a chemical entity and a gene or gene product. | 
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product. | 
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | An association between a material sample and something. | 
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which it is derived. | 
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype. | 
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | None | 
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | An association between some entity and an exposure event. | 
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease. | 
| [ExposureEventToEntityAssociationMixin](ExposureEventToEntityAssociationMixin.md) | None | 
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | An association between some entity and an outcome | 
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome. | 
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations | 
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations. | 
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | None | 
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property). | 
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease | 
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) | None | 
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site. | 
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | None | 
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) | None | 
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment | 
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype. | 
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way. | 
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype. | 
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior. | 
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) | None | 
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) | None | 
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | None | 
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | None | 
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium) | 
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i.e. e-QTL) | 
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has particular frequency in the population | 
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations | 
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | None | 
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | None | 
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | None | 
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease | 
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | None | 
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | None | 
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | None | 
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | None | 
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | None | 
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | None | 
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | None | 
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | None | 
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and an expression site, possibly qualified by stage/timing info. | 
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used. | 
| [FunctionalAssociation](FunctionalAssociation.md) | An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed. | 
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | an association which has a macromolecular machine mixin as a subject | 
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution. | 
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it. | 
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component. | 
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples | 
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples | 
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | None | 
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | None | 
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | None | 
| [SequenceAssociation](SequenceAssociation.md) | An association between a sequence feature and a nucleic acid entity it is localized to. | 
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig. | 
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene | 
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts | 
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product | 
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons | 
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | A regulatory relationship between two genes | 
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | None | 
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms | 
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship. | 
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | An association between an organism taxon and another entity | 
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes | 
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo | 
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens | 
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | None | 


## Slots

| Slot | Description |
| --- | --- |
| [has_attribute](has_attribute.md) | connects any entity to an attribute | 
| [has_attribute_type](has_attribute_type.md) | connects an attribute to a class that describes it | 
| [has_qualitative_value](has_qualitative_value.md) | connects an attribute to a value | 
| [has_quantitative_value](has_quantitative_value.md) | connects an attribute to a value | 
| [has_numeric_value](has_numeric_value.md) | connects a quantity value to a number | 
| [has_unit](has_unit.md) | connects a quantity value to a unit | 
| [base_coordinate](base_coordinate.md) | A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0. | 
| [node_property](node_property.md) | A grouping for any property that holds between a node and a value | 
| [id](id.md) | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI | 
| [iri](iri.md) | An IRI for an entity. This is determined by the id using expansion rules. | 
| [type](type.md) | None | 
| [category](category.md) | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing} | 
| [name](name.md) | A human-readable name for an attribute or entity. | 
| [source](source.md) | None | 
| [stoichiometry](stoichiometry.md) | the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers. | 
| [reaction_direction](reaction_direction.md) | the direction of a reaction as constrained by the direction_enum (ie: left_to_right, neutral, etc.) | 
| [reaction_balanced](reaction_balanced.md) | None | 
| [reaction_side](reaction_side.md) | the side of a reaction being modeled (ie: left or right) | 
| [symbol](symbol.md) | Symbol for a particular thing | 
| [synonym](synonym.md) | Alternate human-readable names for a thing | 
| [has_topic](has_topic.md) | Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238 | 
| [xref](xref.md) | Alternate CURIEs for a thing | 
| [full_name](full_name.md) | a long-form human readable name for a thing | 
| [description](description.md) | a human-readable description of an entity | 
| [systematic_synonym](systematic_synonym.md) | more commonly used for gene symbols in yeast | 
| [affiliation](affiliation.md) | a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations. | 
| [address](address.md) | the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?). | 
| [latitude](latitude.md) | latitude | 
| [longitude](longitude.md) | longitude | 
| [timepoint](timepoint.md) | a point in time | 
| [creation_date](creation_date.md) | date on which an entity was created. This can be applied to nodes or edges | 
| [update_date](update_date.md) | date on which an entity was updated. This can be applied to nodes or edges | 
| [aggregate_statistic](aggregate_statistic.md) | None | 
| [has_count](has_count.md) | number of things with a particular property | 
| [has_total](has_total.md) | total number of things in a particular reference set | 
| [has_quotient](has_quotient.md) | None | 
| [has_percentage](has_percentage.md) | equivalent to has quotient multiplied by 100 | 
| [has_taxonomic_rank](has_taxonomic_rank.md) | None | 
| [has_dataset](has_dataset.md) | None | 
| [source_web_page](source_web_page.md) | None | 
| [source_logo](source_logo.md) | None | 
| [retrieved_on](retrieved_on.md) | None | 
| [version_of](version_of.md) | None | 
| [version](version.md) | None | 
| [license](license.md) | None | 
| [rights](rights.md) | None | 
| [format](format.md) | None | 
| [created_with](created_with.md) | None | 
| [download_url](download_url.md) | None | 
| [dataset_download_url](dataset_download_url.md) | None | 
| [distribution_download_url](distribution_download_url.md) | None | 
| [ingest_date](ingest_date.md) | None | 
| [has_distribution](has_distribution.md) | None | 
| [published_in](published_in.md) | CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal. | 
| [iso_abbreviation](iso_abbreviation.md) | Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself. | 
| [authors](authors.md) | connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. | 
| [volume](volume.md) | volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication | 
| [chapter](chapter.md) | chapter of a book | 
| [issue](issue.md) | issue of a newspaper, a scientific journal or magazine for reference purpose | 
| [pages](pages.md) | page number of source referenced for statement or publication | 
| [summary](summary.md) | executive  summary of a publication | 
| [keywords](keywords.md) | keywords tagging a publication | 
| [mesh_terms](mesh_terms.md) | mesh terms tagging a publication | 
| [has_biological_sequence](has_biological_sequence.md) | connects a genomic feature to its sequence | 
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | connects an entity with one or more gene or gene products | 
| [has_gene](has_gene.md) | connects an entity associated with one or more genes | 
| [has_zygosity](has_zygosity.md) | None | 
| [has_chemical_formula](has_chemical_formula.md) | description of chemical compound based on element symbols | 
| [is_metabolite](is_metabolite.md) | indicates whether a molecular entity is a metabolite | 
| [has_constituent](has_constituent.md) | one or more molecular entities within a chemical mixture | 
| [has_drug](has_drug.md) | connects an entity to one or more drugs | 
| [has_device](has_device.md) | connects an entity to one or more (medical) devices | 
| [has_procedure](has_procedure.md) | connects an entity to one or more (medical) procedures | 
| [has_receptor](has_receptor.md) | the organism or organism part being exposed | 
| [has_stressor](has_stressor.md) | the process or entity that the receptor is being exposed to | 
| [has_route](has_route.md) | the process that results in the stressor coming into direct contact with the receptor | 
| [has_population_context](has_population_context.md) | a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association. | 
| [has_temporal_context](has_temporal_context.md) | a constraint of time placed upon the truth value of an association. | 
| [is_supplement](is_supplement.md) |  | 
| [trade_name](trade_name.md) |  | 
| [available_from](available_from.md) |  | 
| [is_toxic](is_toxic.md) |  | 
| [max_tolerated_dose](max_tolerated_dose.md) | The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD. | 
| [animal_model_available_from](animal_model_available_from.md) |  | 
| [highest_FDA_approval_status](highest_FDA_approval_status.md) | Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.' | 
| [drug_regulatory_status_world_wide](drug_regulatory_status_world_wide.md) | An agglomeration of drug regulatory status worldwide. Not specific to FDA. | 
| [related_to](related_to.md) | A relationship that is asserted between two named things | 
| [related_to_at_concept_level](related_to_at_concept_level.md) | Represents a relationship held between terminology components that describe the conceptual model of a domain. | 
| [related_to_at_instance_level](related_to_at_instance_level.md) | Represents a relationship held between two instances of a data classes.  Much like an assertion component, in an ABox, these represent facts associated with the conceptual model. | 
| [associated_with](associated_with.md) | Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. | 
| [superclass_of](superclass_of.md) | holds between two classes where the domain class is a super class of the range class | 
| [subclass_of](subclass_of.md) | holds between two classes where the domain class is a specialization of the range class | 
| [same_as](same_as.md) | holds between two entities that are considered equivalent to each other | 
| [close_match](close_match.md) | a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity). | 
| [exact_match](exact_match.md) | holds between two entities that have strictly equivalent meanings, with a high degree of confidence | 
| [broad_match](broad_match.md) | a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree. | 
| [narrow_match](narrow_match.md) | a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree. | 
| [opposite_of](opposite_of.md) | x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased). | 
| [has_real_world_evidence_of_association_with](has_real_world_evidence_of_association_with.md) | this means that the assertion was derived by applying statistical and machine learning models to clinical data such as EHR data, survey data, etc | 
| [active_in](active_in.md) | None | 
| [acts_upstream_of](acts_upstream_of.md) | None | 
| [has_upstream_actor](has_upstream_actor.md) | None | 
| [acts_upstream_of_positive_effect](acts_upstream_of_positive_effect.md) | None | 
| [has_positive_upstream_actor](has_positive_upstream_actor.md) | None | 
| [acts_upstream_of_negative_effect](acts_upstream_of_negative_effect.md) | None | 
| [has_negative_upstream_actor](has_negative_upstream_actor.md) | None | 
| [acts_upstream_of_or_within](acts_upstream_of_or_within.md) | None | 
| [has_upstream_or_within_actor](has_upstream_or_within_actor.md) | None | 
| [acts_upstream_of_or_within_positive_effect](acts_upstream_of_or_within_positive_effect.md) | None | 
| [has_positive_upstream_or_within_actor](has_positive_upstream_or_within_actor.md) | None | 
| [acts_upstream_of_or_within_negative_effect](acts_upstream_of_or_within_negative_effect.md) | None | 
| [has_negative_upstream_or_within_actor](has_negative_upstream_or_within_actor.md) | None | 
| [mentions](mentions.md) | refers to is a relation between one information content entity and the named thing that it makes reference to. | 
| [mentioned_by](mentioned_by.md) | refers to is a relation between one named thing and the information content entity that it makes reference to. | 
| [contributor](contributor.md) | None | 
| [provider](provider.md) | person, group, organization or project that provides a piece of information (e.g. a knowledge association). | 
| [publisher](publisher.md) | organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node). | 
| [editor](editor.md) | editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node). | 
| [author](author.md) | an instance of one (co-)creator primarily responsible for a written work | 
| [interacts_with](interacts_with.md) | holds between any two entities that directly or indirectly interact with each other | 
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interaction | 
| [chemically_interacts_with](chemically_interacts_with.md) | None | 
| [molecularly_interacts_with](molecularly_interacts_with.md) | None | 
| [genetically_interacts_with](genetically_interacts_with.md) | holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality. | 
| [affects](affects.md) | describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be. | 
| [affected_by](affected_by.md) | describes an entity of which the state or quality is affected by another existing entity. | 
| [associated_with_sensitivity_to](associated_with_sensitivity_to.md) | A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical. | 
| [sensitivity_associated_with](sensitivity_associated_with.md) | None | 
| [associated_with_resistance_to](associated_with_resistance_to.md) | A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical. | 
| [resistance_associated_with](resistance_associated_with.md) | None | 
| [diagnoses](diagnoses.md) | a relationship that identifies the nature of (an illness or other problem) by examination of the symptoms. | 
| [is_diagnosed_by](is_diagnosed_by.md) | None | 
| [increases_amount_or_activity_of](increases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that increase the amount or activity of the object. | 
| [decreases_amount_or_activity_of](decreases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that decrease the amount or activity of the object. | 
| [chemical_role_mixin](chemical_role_mixin.md) | A role played by the chemical entity or part thereof within a chemical context. | 
| [biological_role_mixin](biological_role_mixin.md) | A role played by the chemical entity or part thereof within a biological context. | 
| [affects_abundance_of](affects_abundance_of.md) | holds between two chemical or gene/gene product entities where the action or effect of one changes the amount of the other within a system of interest | 
| [abundance_affected_by](abundance_affected_by.md) | None | 
| [increases_abundance_of](increases_abundance_of.md) | holds between two chemical or gene/gene product entities where the action or effect of one increases the amount of the other within a system of interest | 
| [abundance_increased_by](abundance_increased_by.md) | None | 
| [decreases_abundance_of](decreases_abundance_of.md) | holds between two chemical or gene/gene product where the action or effect of one decreases the amount of the other within a system of interest | 
| [abundance_decreased_by](abundance_decreased_by.md) | None | 
| [increases_activity_of](increases_activity_of.md) | holds between two chemical or gene/gene product where the action or effect of one increases the activity of the other within a system of interest | 
| [affects_activity_of](affects_activity_of.md) | holds between two chemical or gene/gene product where the action or effect of one changes the activity of the other within a system of interest | 
| [activity_affected_by](activity_affected_by.md) | holds between two chemical or gene/gene product where the action or effect of one is changed by the activity of the other within a system of interest | 
| [activity_increased_by](activity_increased_by.md) | None | 
| [decreases_activity_of](decreases_activity_of.md) | holds between two chemical or gene/gene product where the action or effect of one decreases the activity of the other within a system of interest | 
| [activity_decreased_by](activity_decreased_by.md) | None | 
| [affects_expression_of](affects_expression_of.md) | holds between a named thing (most often a chemical or gene/gene product, but can also be used to link an environmental affect on expression) and a nucleic acid entity where the action or effect of one changes the level of expression of the other within a system of interest | 
| [expression_affected_by](expression_affected_by.md) | None | 
| [increases_expression_of](increases_expression_of.md) | holds between a chemical or gene/gene product entity and a nucleic acid entity where the action or effect of one increases the level of expression of the other within a system of interest | 
| [expression_increased_by](expression_increased_by.md) | None | 
| [decreases_expression_of](decreases_expression_of.md) | holds between a chemical or gene/gene product entity and a nucleic acid entity where the action or effect of one decreases the level of expression of the other within a system of interest | 
| [expression_decreased_by](expression_decreased_by.md) | None | 
| [affects_folding_of](affects_folding_of.md) | holds between a chemical or gene/gene product entity and a nucleic acid entity where the action or effect of one changes the rate or quality of folding of the other | 
| [folding_affected_by](folding_affected_by.md) | None | 
| [increases_folding_of](increases_folding_of.md) | holds between a chemical or gene/gene product entity and a nucleic acid entity where the action or effect of one increases the rate or quality of folding of the other | 
| [folding_increased_by](folding_increased_by.md) | None | 
| [decreases_folding_of](decreases_folding_of.md) | holds between a chemical or gene or gene product entity and a nucleic acid entity where the action or effect of one decreases the rate or quality of folding of the other | 
| [folding_decreased_by](folding_decreased_by.md) | None | 
| [affects_localization_of](affects_localization_of.md) | holds between two chemical or gene/gene product entities where the action or effect of one changes the localization of the other within a system of interest | 
| [localization_affected_by](localization_affected_by.md) | None | 
| [increases_localization_of](increases_localization_of.md) | holds between two chemical or gene/gene product entities where the action or effect of one increases the proper localization of the other within a system of interest | 
| [localization_increased_by](localization_increased_by.md) | None | 
| [decreases_localization_of](decreases_localization_of.md) | holds between two chemical or gene/gene product entities where the action or effect of one decreases the proper localization of the other within a system of interest | 
| [localization_decreased_by](localization_decreased_by.md) | None | 
| [affects_metabolic_processing_of](affects_metabolic_processing_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one impacts the metabolic processing of the other within a system of interest | 
| [metabolic_processing_affected_by](metabolic_processing_affected_by.md) | None | 
| [increases_metabolic_processing_of](increases_metabolic_processing_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one increases the rate of metabolic processing of the other within a system of interest | 
| [metabolic_processing_increased_by](metabolic_processing_increased_by.md) | None | 
| [decreases_metabolic_processing_of](decreases_metabolic_processing_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest | 
| [metabolic_processing_decreased_by](metabolic_processing_decreased_by.md) | None | 
| [affects_molecular_modification_of](affects_molecular_modification_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons) | 
| [molecular_modification_affected_by](molecular_modification_affected_by.md) | None | 
| [increases_molecular_modification_of](increases_molecular_modification_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons) | 
| [molecular_modification_increased_by](molecular_modification_increased_by.md) | None | 
| [decreases_molecular_modification_of](decreases_molecular_modification_of.md) | holds between two chemical entities  where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons) | 
| [molecular_modification_decreased_by](molecular_modification_decreased_by.md) | None | 
| [affects_synthesis_of](affects_synthesis_of.md) | holds between two chemical entities where the action or effect  of one impacts the rate of chemical synthesis of the other | 
| [synthesis_affected_by](synthesis_affected_by.md) | None | 
| [increases_synthesis_of](increases_synthesis_of.md) | holds between two chemical entities where the action or effect of one increases the rate of chemical synthesis of the other | 
| [synthesis_increased_by](synthesis_increased_by.md) | None | 
| [decreases_synthesis_of](decreases_synthesis_of.md) | holds between two chemical entities where the action or effect of one decreases the rate of chemical synthesis of the other | 
| [synthesis_decreased_by](synthesis_decreased_by.md) | None | 
| [affects_degradation_of](affects_degradation_of.md) | holds between two chemical entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where chemical degradation is defined act or process of simplifying or breaking down a molecule into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995) | 
| [degradation_affected_by](degradation_affected_by.md) | None | 
| [increases_degradation_of](increases_degradation_of.md) | holds between two chemical entities where the action or effect of one increases the rate of degradation of the other within a system of interest | 
| [degradation_increased_by](degradation_increased_by.md) | None | 
| [decreases_degradation_of](decreases_degradation_of.md) | holds between two chemical entities where the action or effect of one decreases the rate of degradation of the other within a system of interest | 
| [degradation_decreased_by](degradation_decreased_by.md) | None | 
| [affects_mutation_rate_of](affects_mutation_rate_of.md) | holds between a chemical entity and a nucleic acid entity where the action or effect of the chemical entity impacts the rate of mutation of the nucleic acid entity within a system of interest | 
| [mutation_rate_affected_by](mutation_rate_affected_by.md) | None | 
| [increases_mutation_rate_of](increases_mutation_rate_of.md) | holds between a chemical entity and a nucleic acid entity where the action or effect of the chemical entity increases the rate of mutation of the nucleic acid entity within a system of interest | 
| [mutation_rate_increased_by](mutation_rate_increased_by.md) | None | 
| [decreases_mutation_rate_of](decreases_mutation_rate_of.md) | holds between a chemical entity and a nucleic acid entity where the action or effect of the chemical entity decreases the rate of mutation of the nucleic acid entity within a system of interest | 
| [mutation_rate_decreased_by](mutation_rate_decreased_by.md) | None | 
| [affects_response_to](affects_response_to.md) | None | 
| [response_affected_by](response_affected_by.md) | holds between two chemical entities where the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) of one is affected by the action of the other. | 
| [increases_response_to](increases_response_to.md) | holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other | 
| [response_increased_by](response_increased_by.md) | None | 
| [decreases_response_to](decreases_response_to.md) | holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other | 
| [response_decreased_by](response_decreased_by.md) | None | 
| [affects_splicing_of](affects_splicing_of.md) | holds between a chemical entity and an mRNA where the action or effect of the chemical entity impacts the splicing of the mRNA | 
| [splicing_affected_by](splicing_affected_by.md) | None | 
| [increases_splicing_of](increases_splicing_of.md) | holds between a chemical entity and an mRNA where the action or effect of the chemical entity increases the proper splicing of the mRNA | 
| [splicing_increased_by](splicing_increased_by.md) | None | 
| [decreases_splicing_of](decreases_splicing_of.md) | holds between a chemical entity and an mRNA where the action or effect of the chemical entity decreases the proper splicing of the mRNA | 
| [splicing_decreased_by](splicing_decreased_by.md) | None | 
| [affects_stability_of](affects_stability_of.md) | holds between two entities where the action or effect of one impacts the stability of the other within a system of interest | 
| [stability_affected_by](stability_affected_by.md) | None | 
| [increases_stability_of](increases_stability_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one increases the stability of the other within a system of interest | 
| [stability_increased_by](stability_increased_by.md) | None | 
| [decreases_stability_of](decreases_stability_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one decreases the stability of the other within a system of interest | 
| [stability_decreased_by](stability_decreased_by.md) | None | 
| [affects_transport_of](affects_transport_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest | 
| [transport_affected_by](transport_affected_by.md) | None | 
| [increases_transport_of](increases_transport_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest | 
| [transport_increased_by](transport_increased_by.md) | None | 
| [decreases_transport_of](decreases_transport_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest | 
| [transport_decreased_by](transport_decreased_by.md) | None | 
| [affects_secretion_of](affects_secretion_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ | 
| [secretion_affected_by](secretion_affected_by.md) | None | 
| [increases_secretion_of](increases_secretion_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ | 
| [secretion_increased_by](secretion_increased_by.md) | None | 
| [decreases_secretion_of](decreases_secretion_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ | 
| [secretion_decreased_by](secretion_decreased_by.md) | None | 
| [affects_uptake_of](affects_uptake_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ | 
| [uptake_affected_by](uptake_affected_by.md) | None | 
| [increases_uptake_of](increases_uptake_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ | 
| [uptake_increased_by](uptake_increased_by.md) | None | 
| [decreases_uptake_of](decreases_uptake_of.md) | holds between two chemical or gene/gene product entities  where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ | 
| [uptake_decreased_by](uptake_decreased_by.md) | None | 
| [regulates](regulates.md) | None | 
| [regulated_by](regulated_by.md) | None | 
| [positively_regulates](positively_regulates.md) | None | 
| [positively_regulated_by](positively_regulated_by.md) | None | 
| [negatively_regulates](negatively_regulates.md) | None | 
| [negatively_regulated_by](negatively_regulated_by.md) | None | 
| [process_regulates_process](process_regulates_process.md) | None | 
| [process_regulated_by_process](process_regulated_by_process.md) | None | 
| [process_positively_regulates_process](process_positively_regulates_process.md) | None | 
| [process_positively_regulated_by_process](process_positively_regulated_by_process.md) | None | 
| [process_negatively_regulates_process](process_negatively_regulates_process.md) | None | 
| [process_negatively_regulated_by_process](process_negatively_regulated_by_process.md) | None | 
| [entity_regulates_entity](entity_regulates_entity.md) | None | 
| [entity_regulated_by_entity](entity_regulated_by_entity.md) | None | 
| [entity_positively_regulates_entity](entity_positively_regulates_entity.md) | None | 
| [entity_positively_regulated_by_entity](entity_positively_regulated_by_entity.md) | None | 
| [entity_negatively_regulates_entity](entity_negatively_regulates_entity.md) | None | 
| [entity_negatively_regulated_by_entity](entity_negatively_regulated_by_entity.md) | None | 
| [disrupts](disrupts.md) | describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another. | 
| [disrupted_by](disrupted_by.md) | describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another. | 
| [gene_product_of](gene_product_of.md) | definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x | 
| [has_gene_product](has_gene_product.md) | holds between a gene and a transcribed and/or translated product generated from it | 
| [transcribed_to](transcribed_to.md) | inverse of transcribed from | 
| [transcribed_from](transcribed_from.md) | x is transcribed from y if and only if x is synthesized from template y | 
| [translates_to](translates_to.md) | x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide) | 
| [translation_of](translation_of.md) | inverse of translates to | 
| [homologous_to](homologous_to.md) | holds between two biological entities that have common evolutionary origin | 
| [paralogous_to](paralogous_to.md) | a homology relationship that holds between entities (typically genes) that diverged after a duplication event. | 
| [orthologous_to](orthologous_to.md) | a homology relationship between entities (typically genes) that diverged after a speciation event. | 
| [xenologous_to](xenologous_to.md) | a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor. | 
| [coexists_with](coexists_with.md) | holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region | 
| [in_pathway_with](in_pathway_with.md) | holds between two genes or gene products that are part of in the same biological pathway | 
| [in_complex_with](in_complex_with.md) | holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex mixin | 
| [in_cell_population_with](in_cell_population_with.md) | holds between two genes or gene products that are expressed in the same cell type or population | 
| [colocalizes_with](colocalizes_with.md) | holds between two entities that are observed to be located in the same place. | 
| [genetic_association](genetic_association.md) | Co-occurrence of a certain allele of a genetic marker and the phenotype of interest in the same individuals at above-chance level | 
| [gene_associated_with_condition](gene_associated_with_condition.md) | holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with | 
| [condition_associated_with_gene](condition_associated_with_gene.md) | holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products | 
| [affects_risk_for](affects_risk_for.md) | holds between two entities where exposure to one entity alters the chance of developing the other | 
| [risk_affected_by](risk_affected_by.md) | None | 
| [predisposes](predisposes.md) | holds between two entities where exposure to one entity increases the chance of developing the other | 
| [contributes_to](contributes_to.md) | holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other | 
| [contribution_from](contribution_from.md) | None | 
| [causes](causes.md) | holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other | 
| [caused_by](caused_by.md) | holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other | 
| [ameliorates](ameliorates.md) | A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition. | 
| [exacerbates](exacerbates.md) | A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition. | 
| [treats](treats.md) | holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat | 
| [treated_by](treated_by.md) | holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition | 
| [approved_to_treat](approved_to_treat.md) | holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature for which it is approved for treatment to some level of clinical trial. Note that in terms of REPODB narrow mappings, terms containing 'suspended', 'terminated' or 'withdrawn' should be mapped onto associations using this term for which 'negated: true' is asserted. | 
| [approved_for_treatment_by](approved_for_treatment_by.md) | holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is approved for treatment of the condition (or not, if negated) to some level of clinical trial | 
| [prevents](prevents.md) | holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature. | 
| [prevented_by](prevented_by.md) | holds between a potential outcome of which the likelihood was reduced by the application or use of an entity. | 
| [correlated_with](correlated_with.md) | holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature. | 
| [positively_correlated_with](positively_correlated_with.md) | holds between any two named thing entities "correlated with" one another in a positive manner. | 
| [negatively_correlated_with](negatively_correlated_with.md) | holds between any two named thing entities "correlated with" one another in a negative manner. | 
| [occurs_together_in_literature_with](occurs_together_in_literature_with.md) | holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider. | 
| [coexpressed_with](coexpressed_with.md) | holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context. | 
| [has_biomarker](has_biomarker.md) | holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature. # metabolite | 
| [biomarker_for](biomarker_for.md) | holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature. | 
| [expressed_in](expressed_in.md) | holds between a gene or gene product and an anatomical entity in which it is expressed | 
| [expresses](expresses.md) | holds between an anatomical entity and gene or gene product that is expressed there | 
| [has_phenotype](has_phenotype.md) | holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate. | 
| [phenotype_of](phenotype_of.md) | holds between a phenotype and a biological entity, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). | 
| [occurs_in](occurs_in.md) | holds between a process and a material entity or site within which the process occurs | 
| [contains_process](contains_process.md) | None | 
| [located_in](located_in.md) | holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part) | 
| [location_of](location_of.md) | holds between material entity or site and a material entity that is located within it (but not considered a part of it) | 
| [disease_has_location](disease_has_location.md) | A relationship between a disease and an anatomical entity where the disease has one or more features that are located in that entity. | 
| [similar_to](similar_to.md) | holds between an entity and some other entity with similar features. | 
| [chemically_similar_to](chemically_similar_to.md) | holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity. | 
| [has_sequence_location](has_sequence_location.md) | holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig. | 
| [sequence_location_of](sequence_location_of.md) | None | 
| [model_of](model_of.md) | holds between a thing and some other thing it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity. | 
| [models](models.md) | None | 
| [overlaps](overlaps.md) | holds between entities that overlap in their extents (materials or processes) | 
| [has_part](has_part.md) | holds between wholes and their parts (material entities or processes) | 
| [has_plasma_membrane_part](has_plasma_membrane_part.md) | Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part. | 
| [composed_primarily_of](composed_primarily_of.md) | x composed_primarily_of_y if:more than half of the mass of x is made from parts of y. | 
| [plasma_membrane_part_of](plasma_membrane_part_of.md) | None | 
| [part_of](part_of.md) | holds between parts and wholes (material entities or processes) | 
| [has_input](has_input.md) | holds between a process and a continuant, where the continuant is an input into the process | 
| [is_input_of](is_input_of.md) | None | 
| [has_output](has_output.md) | holds between a process and a continuant, where the continuant is an output of the process | 
| [is_output_of](is_output_of.md) | None | 
| [has_participant](has_participant.md) | holds between a process and a continuant, where the continuant is somehow involved in the process | 
| [catalyzes](catalyzes.md) | None | 
| [has_catalyst](has_catalyst.md) | None | 
| [has_substrate](has_substrate.md) | None | 
| [is_substrate_of](is_substrate_of.md) | None | 
| [participates_in](participates_in.md) | holds between a continuant and a process, where the continuant is somehow involved in the process | 
| [actively_involved_in](actively_involved_in.md) | holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes | 
| [actively_involves](actively_involves.md) | None | 
| [capable_of](capable_of.md) | holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function. | 
| [capability_of](capability_of.md) | None | 
| [enables](enables.md) | holds between a physical entity and a process, where the physical entity executes the process | 
| [enabled_by](enabled_by.md) | holds between a process and a physical entity, where the physical entity executes the process | 
| [derives_into](derives_into.md) | holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity | 
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity | 
| [is_metabolite_of](is_metabolite_of.md) | holds between two molecular entities in which the first one is derived from the second one as a product of metabolism | 
| [has_metabolite](has_metabolite.md) | holds between two molecular entities in which the second one is derived from the first one as a product of metabolism | 
| [food_component_of](food_component_of.md) | holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive) | 
| [has_food_component](has_food_component.md) | holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive) | 
| [nutrient_of](nutrient_of.md) | holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive) | 
| [has_nutrient](has_nutrient.md) | one or more nutrients which are growth factors for a living organism | 
| [is_active_ingredient_of](is_active_ingredient_of.md) | holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component | 
| [has_active_ingredient](has_active_ingredient.md) | holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component | 
| [is_excipient_of](is_excipient_of.md) | holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component | 
| [has_excipient](has_excipient.md) | holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component | 
| [manifestation_of](manifestation_of.md) | that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome | 
| [has_manifestation](has_manifestation.md) | None | 
| [produces](produces.md) | holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity | 
| [produced_by](produced_by.md) | None | 
| [consumes](consumes.md) | None | 
| [consumed_by](consumed_by.md) | None | 
| [temporally_related_to](temporally_related_to.md) | holds between two entities with a temporal relationship | 
| [precedes](precedes.md) | holds between two processes, where one completes before the other begins | 
| [preceded_by](preceded_by.md) | holds between two processes, where the other is completed before the one begins | 
| [directly_interacts_with](directly_interacts_with.md) | Holds between chemical entities that physically and directly interact with each other | 
| [affects_expression_in](affects_expression_in.md) | Holds between a variant and an anatomical entity where the expression of the variant is located in. | 
| [has_variant_part](has_variant_part.md) | holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it | 
| [variant_part_of](variant_part_of.md) | None | 
| [related_condition](related_condition.md) | None | 
| [is_sequence_variant_of](is_sequence_variant_of.md) | holds between a sequence variant and a nucleic acid entity | 
| [has_sequence_variant](has_sequence_variant.md) | None | 
| [is_missense_variant_of](is_missense_variant_of.md) | holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved. | 
| [has_missense_variant](has_missense_variant.md) | None | 
| [is_synonymous_variant_of](is_synonymous_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence | 
| [has_synonymous_variant](has_synonymous_variant.md) | None | 
| [is_nonsense_variant_of](is_nonsense_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon | 
| [has_nonsense_variant](has_nonsense_variant.md) | None | 
| [is_frameshift_variant_of](is_frameshift_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three. | 
| [has_frameshift_variant](has_frameshift_variant.md) | None | 
| [is_splice_site_variant_of](is_splice_site_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons. | 
| [has_splice_site_variant](has_splice_site_variant.md) | None | 
| [is_nearby_variant_of](is_nearby_variant_of.md) | holds between a sequence variant and a gene sequence that the variant is genomically close to. | 
| [has_nearby_variant](has_nearby_variant.md) | None | 
| [is_non_coding_variant_of](is_non_coding_variant_of.md) | holds between a sequence variant and a gene, where the variant does not affect the coding sequence | 
| [has_non_coding_variant](has_non_coding_variant.md) | None | 
| [disease_has_basis_in](disease_has_basis_in.md) | A relation that holds between a disease and an entity where the state of the entity has contribution to the disease. | 
| [causes_adverse_event](causes_adverse_event.md) | holds between a drug and a disease or phenotype that can be caused by the drug | 
| [adverse_event_caused_by](adverse_event_caused_by.md) | None | 
| [contraindicated_for](contraindicated_for.md) | Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug. | 
| [has_contraindication](has_contraindication.md) | None | 
| [has_not_completed](has_not_completed.md) | holds between an entity and a process that the entity is capable of, but has not completed | 
| [not_completed_by](not_completed_by.md) | None | 
| [has_completed](has_completed.md) | holds between an entity and a process that the entity is capable of and has completed | 
| [completed_by](completed_by.md) | None | 
| [decreases_molecular_interaction](decreases_molecular_interaction.md) | indicates that the source decreases the molecular interaction between the target and some other chemical entity | 
| [molecular_interaction_decreased_by](molecular_interaction_decreased_by.md) | None | 
| [increases_molecular_interaction](increases_molecular_interaction.md) | indicates that the source increases the molecular interaction between the target and some other chemical entity | 
| [molecular_interaction_increased_by](molecular_interaction_increased_by.md) | None | 
| [in_linkage_disequilibrium_with](in_linkage_disequilibrium_with.md) | holds between two sequence variants, the presence of which are correlated in a population | 
| [has_increased_amount](has_increased_amount.md) | None | 
| [increased_amount_of](increased_amount_of.md) | None | 
| [has_decreased_amount](has_decreased_amount.md) | None | 
| [decreased_amount_in](decreased_amount_in.md) | None | 
| [lacks_part](lacks_part.md) | None | 
| [missing_from](missing_from.md) | None | 
| [develops_from](develops_from.md) | None | 
| [develops_into](develops_into.md) | None | 
| [in_taxon](in_taxon.md) | connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon' | 
| [taxon_of](taxon_of.md) | None | 
| [has_molecular_consequence](has_molecular_consequence.md) | connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583 | 
| [is_molecular_consequence_of](is_molecular_consequence_of.md) | None | 
| [association_slot](association_slot.md) | any slot that relates an association to another entity | 
| [original_subject](original_subject.md) | used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification. | 
| [original_object](original_object.md) | used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification. | 
| [original_predicate](original_predicate.md) | used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification. | 
| [subject](subject.md) | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. | 
| [object](object.md) | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object. | 
| [predicate](predicate.md) | A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes. | 
| [logical_interpretation](logical_interpretation.md) | None | 
| [relation](relation.md) | None | 
| [negated](negated.md) | if set to true, then the association is negated i.e. is not true | 
| [has_confidence_level](has_confidence_level.md) | connects an association to a qualitative term denoting the level of confidence | 
| [has_evidence](has_evidence.md) | connects an association to an instance of supporting evidence | 
| [mechanism_of_action](mechanism_of_action.md) | a boolean flag to indicate if the edge is part of a path or subgraph of a knowledge graph that constitutes the mechanism of action for a result. | 
| [knowledge_source](knowledge_source.md) | An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property. | 
| [provided_by](provided_by.md) | The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. | 
| [primary_knowledge_source](primary_knowledge_source.md) | The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source). | 
| [original_knowledge_source](original_knowledge_source.md) | The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data). | 
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form. | 
| [supporting_data_source](supporting_data_source.md) | An Information Resource from which data was retrieved and subsequently used as evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference over the retrieved data). | 
| [association_type](association_type.md) | connects an association to the category of association (e.g. gene to phenotype) | 
| [chi_squared_statistic](chi_squared_statistic.md) | represents the chi-squared statistic computed from observations | 
| [p_value](p_value.md) | A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone. | 
| [interacting_molecules_category](interacting_molecules_category.md) | None | 
| [quantifier_qualifier](quantifier_qualifier.md) | A measurable quantity for the object of the association | 
| [catalyst_qualifier](catalyst_qualifier.md) | a qualifier that connects an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change. | 
| [expression_site](expression_site.md) | location in which gene or protein expression takes place. May be cell, tissue, or organ. | 
| [stage_qualifier](stage_qualifier.md) | stage during which gene or protein expression of takes place. | 
| [phenotypic_state](phenotypic_state.md) | in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX. | 
| [qualifiers](qualifiers.md) | connects an association to qualifiers that modify or qualify the meaning of that association | 
| [frequency_qualifier](frequency_qualifier.md) | a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject | 
| [severity_qualifier](severity_qualifier.md) | a qualifier used in a phenotypic association to state how severe the phenotype is in the subject | 
| [sex_qualifier](sex_qualifier.md) | a qualifier used in a phenotypic association to state whether the association is specific to a particular sex. | 
| [onset_qualifier](onset_qualifier.md) | a qualifier used in a phenotypic association to state when the phenotype appears is in the subject | 
| [clinical_modifier_qualifier](clinical_modifier_qualifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects | 
| [sequence_variant_qualifier](sequence_variant_qualifier.md) | a qualifier used in an association with the variant | 
| [publications](publications.md) | connects an association to publications supporting the association | 
| [associated_environmental_context](associated_environmental_context.md) | An attribute that can be applied to an association where the association holds between two entities located or occurring in a particular environment. For example, two microbial taxa may interact in the context of a human gut; a disease may give rise to a particular phenotype in a particular environmental exposure. | 
| [sequence_localization_attribute](sequence_localization_attribute.md) | An attribute that can be applied to a genome sequence localization edge. These edges connect a nucleic acid entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line. | 
| [interbase_coordinate](interbase_coordinate.md) | A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge. | 
| [start_interbase_coordinate](start_interbase_coordinate.md) | The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0). | 
| [end_interbase_coordinate](end_interbase_coordinate.md) | The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on. | 
| [start_coordinate](start_coordinate.md) | The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1). | 
| [end_coordinate](end_coordinate.md) | The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on. | 
| [genome_build](genome_build.md) | The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens. | 
| [strand](strand.md) | The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand). | 
| [phase](phase.md) | The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2. | 
| [FDA_approval_status](FDA_approval_status.md) |  | 


## Enums

| Enums | Description |
| --- | --- |
| [LogicalInterpretationEnum](LogicalInterpretationEnum.md) | None | 
| [ReactionDirectionEnum](ReactionDirectionEnum.md) | None | 
| [ReactionSideEnum](ReactionSideEnum.md) | None | 
| [PhaseEnum](PhaseEnum.md) | phase | 
| [StrandEnum](StrandEnum.md) | strand | 
| [SequenceEnum](SequenceEnum.md) | type of sequence | 
| [PredicateQualifierEnum](PredicateQualifierEnum.md) | constrained list of qualifying terms that soften or expand the definition of the predicate used. can be used to constrain or qualify any predicate (any child of related_to). | 
| [DrugAvailabilityEnum](DrugAvailabilityEnum.md) |  | 
| [FDAApprovalStatusEnum](FDAApprovalStatusEnum.md) |  | 

