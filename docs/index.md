---
title: Browse Biolink Model
has_children: true
nav_order: 2
layout: default
has_toc: false
---

Entity and association taxonomy and datamodel for life-sciences data


## Classes


### Entity

 * [Entity](Entity.md) - Root Biolink Model class for all things and informational relationships, real or imagined.

### Named Things

 * [NamedThing](NamedThing.md) - a databased entity or concept/class
     * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
         * [Study](Study.md) - a detailed investigation and/or analysis
     * [AdministrativeEntity](AdministrativeEntity.md)
         * [Agent](Agent.md) - person, group, organization or project that provides a piece of information (i.e. a knowledge association)
     * [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
         * [BehavioralExposure](BehavioralExposure.md) - A behavioral exposure is a factor relating to behavior impacting an individual.
         * [BiologicalSex](BiologicalSex.md)
             * [GenotypicSex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
             * [PhenotypicSex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
         * [BioticExposure](BioticExposure.md) - An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
         * [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical entity.
             * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular drug.
                 * [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) - drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
         * [ChemicalRole](ChemicalRole.md) - 	A role played by the molecular entity or part thereof within a chemical context.
         * [ClinicalAttribute](ClinicalAttribute.md) - Attributes relating to a clinical manifestation
             * [ClinicalCourse](ClinicalCourse.md) - The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
                 * [Onset](Onset.md) - The age group in which (disease) symptom manifestations appear
             * [ClinicalMeasurement](ClinicalMeasurement.md) - A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
             * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology, with respect to severity, laterality, and other aspects
         * [ComplexChemicalExposure](ComplexChemicalExposure.md) - A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
         * [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) - A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.
         * [EnvironmentalExposure](EnvironmentalExposure.md) - A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.
             * [GeographicExposure](GeographicExposure.md) - A geographic exposure is a factor relating to geographic proximity to some impactful entity.
         * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
         * [OrganismAttribute](OrganismAttribute.md) - describes a characteristic of an organismal entity.
             * [PhenotypicQuality](PhenotypicQuality.md) - A property of a phenotype
         * [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) - An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
         * [PathologicalProcessExposure](PathologicalProcessExposure.md) - A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
         * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
         * [SocioeconomicAttribute](SocioeconomicAttribute.md) - Attributes relating to a socioeconomic manifestation
         * [SocioeconomicExposure](SocioeconomicExposure.md) - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
         * [Zygosity](Zygosity.md)
     * [BiologicalEntity](BiologicalEntity.md)
         * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
             * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
                 * [Behavior](Behavior.md)
                 * [PathologicalProcess](PathologicalProcess.md) - A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
                 * [Pathway](Pathway.md)
                 * [PhysiologicalProcess](PhysiologicalProcess.md)
             * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.
         * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.  Please see definitions of phenotypic feature and disease in this model for their independent descriptions.  This class is helpful to enforce domains and ranges   that may involve either a disease or a phenotypic feature.
             * [Disease](Disease.md) - A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism.
             * [PhenotypicFeature](PhenotypicFeature.md) - A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an  individual resulting from the interaction of its genotype with its molecular and physical environment.
                 * [BehavioralFeature](BehavioralFeature.md) - A phenotypic feature which is behavioral in nature.
                 * [ClinicalFinding](ClinicalFinding.md) - this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
         * [Gene](Gene.md) - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
         * [GeneFamily](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
         * [GeneticInheritance](GeneticInheritance.md) - The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc.
         * [Genome](Genome.md) - A genome is the sum of genetic material within a cell or virion.
         * [Genotype](Genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
         * [Haplotype](Haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
         * [MacromolecularComplex](MacromolecularComplex.md) - A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.
         * [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) - A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences.
         * [NucleosomeModification](NucleosomeModification.md) - A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A.
         * [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities
             * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
                 * [Cell](Cell.md)
                 * [CellularComponent](CellularComponent.md) - A location in or around a cell
                 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
                 * [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) - An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
             * [Bacterium](Bacterium.md) - A member of a group of unicellular microorganisms lacking a nuclear membrane, that reproduce by binary fission and are often motile.
             * [CellLine](CellLine.md)
             * [CellularOrganism](CellularOrganism.md)
                 * [Fungus](Fungus.md) - A kingdom of eukaryotic, heterotrophic organisms that live as saprobes or parasites,  including mushrooms, yeasts, smuts, molds, etc. They reproduce either sexually or asexually, and have life cycles that range from simple to complex. Filamentous  fungi refer to those that grow as multicellular colonies (mushrooms and molds).
                 * [Invertebrate](Invertebrate.md) - An animal lacking a vertebral column. This group consists of 98% of all animal species.
                 * [Mammal](Mammal.md) - A member of the class Mammalia, a clade of endothermic amniotes distinguished from reptiles and birds by the possession of hair, three middle ear bones, mammary glands, and a neocortex
                     * [Human](Human.md) - A member of the the species Homo sapiens.
                 * [Plant](Plant.md)
                 * [Vertebrate](Vertebrate.md) - A sub-phylum of animals consisting of those having a bony or cartilaginous vertebral column.
             * [IndividualOrganism](IndividualOrganism.md) - An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
                 * [Case](Case.md) - An individual (human) organism that has a patient role in some clinical context.
             * [LifeStage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
             * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.
                 * [StudyPopulation](StudyPopulation.md) - A group of people banded together or treated as a group as participants in a research study.
                     * [Cohort](Cohort.md) - A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
             * [Virus](Virus.md) - A virus is a microorganism that replicates itself as a microRNA and infects the host cell.
         * [Polypeptide](Polypeptide.md) - A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
             * [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
                 * [ProteinIsoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
         * [PosttranslationalModification](PosttranslationalModification.md) - A chemical modification of a polypeptide or protein that occurs after translation.  e.g. polypeptide cleavage to form separate proteins, methylation or acetylation of histone tail amino acids,  protein ubiquitination.
         * [ProteinDomain](ProteinDomain.md) - A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
         * [ProteinFamily](ProteinFamily.md)
         * [ReagentTargetedGene](ReagentTargetedGene.md) - A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
         * [RegulatoryRegion](RegulatoryRegion.md) - A region (or regions) of the genome that contains known or putative regulatory elements that act in cis- or trans- to affect the transcription of gene
             * [AccessibleDnaRegion](AccessibleDnaRegion.md) - A region (or regions) of a chromatinized genome that has been measured to be more accessible to an enzyme such as DNase-I or Tn5 Transpose
             * [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) - A region (or regions) of the genome that contains a region of DNA known or predicted to bind a protein that modulates gene transcription
         * [SequenceVariant](SequenceVariant.md) - A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.
             * [Snv](Snv.md) - SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
     * [ChemicalEntity](ChemicalEntity.md) - A chemical entity is a physical entity that pertains to chemistry or biochemistry.
         * [ChemicalMixture](ChemicalMixture.md) - A chemical mixture is a chemical entity composed of two or more molecular entities.
             * [ComplexMolecularMixture](ComplexMolecularMixture.md) - A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown concentration and stoichiometry.
             * [Food](Food.md) - A substance consumed by a living organism as a source of nutrition
             * [MolecularMixture](MolecularMixture.md) - A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry.
                 * [Drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
             * [ProcessedMaterial](ProcessedMaterial.md) - A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a material entity that is created or changed during material processing.
         * [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md)
         * [FoodAdditive](FoodAdditive.md)
         * [MolecularEntity](MolecularEntity.md) - A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
             * [NucleicAcidEntity](NucleicAcidEntity.md) - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
                 * [CodingSequence](CodingSequence.md)
                 * [Exon](Exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing.
                 * [Transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase.
                     * [RNAProduct](RNAProduct.md)
                         * [RNAProductIsoform](RNAProductIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference RNA
                         * [NoncodingRNAProduct](NoncodingRNAProduct.md)
                             * [MicroRNA](MicroRNA.md)
                             * [SiRNA](SiRNA.md) - A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
             * [SmallMolecule](SmallMolecule.md) - A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).
     * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
         * [ClinicalIntervention](ClinicalIntervention.md)
             * [Hospitalization](Hospitalization.md)
         * [ClinicalTrial](ClinicalTrial.md)
     * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
     * [DiagnosticAid](DiagnosticAid.md) - A device or substance used to help diagnose disease or injury
     * [Event](Event.md) - Something that happens at a given place and time.
     * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
         * [CommonDataElement](CommonDataElement.md) - A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable  responses, used systematically across different sites, studies, or clinical trials to ensure consistent  data collection. Multiple CDEs (from one or more Collections) can be curated into Forms.  (https://cde.nlm.nih.gov/home)
         * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
         * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
         * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
         * [DatasetSummary](DatasetSummary.md) - an item that holds summary level information about a dataset.
         * [DatasetVersion](DatasetVersion.md) - an item that holds version level information about a dataset.
         * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
         * [Publication](Publication.md) - Any ‘published’ piece of information. Publications are considered broadly  to include any document or document part made available in print or on the  web - which may include scientific journal issues, individual articles, and  books - as well as things like pre-prints, white papers, patents, drug  labels, web pages, protocol documents,  and even a part of a publication if  of significant knowledge scope (e.g. a figure, figure legend, or section  highlighted by NLP). 
             * [Article](Article.md) - a piece of writing on a particular topic presented as a stand-alone  section of a larger publication	  
                 * [JournalArticle](JournalArticle.md) - an article, typically presenting results of research, that is published  in an issue of a scientific journal.
             * [Book](Book.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
             * [BookChapter](BookChapter.md)
             * [DrugLabel](DrugLabel.md) - a document accompanying a drug or its container that provides written, printed or graphic information about the drug, including drug contents, specific instructions  or warnings for administration, storage and disposal instructions, etc. 
             * [Patent](Patent.md) - a legal document granted by a patent issuing authority which confers upon  the patenter the sole right to make, use and sell an invention for a set period of time. 
             * [PreprintPublication](PreprintPublication.md) - a document reresenting an early version of an author's original scholarly work,  such as a research paper or a review, prior to formal peer review and publication  in a peer-reviewed scholarly or scientific journal.
             * [Serial](Serial.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
             * [WebPage](WebPage.md) - a document that is published according to World Wide Web standards, which  may incorporate text, graphics, sound, and/or other features.
         * [RetrievalSource](RetrievalSource.md) - Provides information about how a particular InformationResource served as a source from which knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved.
         * [StudyResult](StudyResult.md) - A collection of data items from a study that are about a particular study subject or experimental unit (the  'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of this data as evidence.
             * [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) - A result of a chi squared analysis.
             * [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) - A result of a concept count analysis.
             * [LogOddsAnalysisResult](LogOddsAnalysisResult.md) - A result of a log odds ratio analysis.
             * [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) - A result of a observed expected frequency analysis.
             * [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) - A result of a relative frequency analysis.
             * [TextMiningResult](TextMiningResult.md) - A result of text mining.
         * [StudyVariable](StudyVariable.md) - a variable that is used as a measure in the investigation of a study
     * [OrganismTaxon](OrganismTaxon.md) - A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
     * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
     * [PhysicalEntity](PhysicalEntity.md) - An entity that has material reality (a.k.a. physical essence).
         * [MaterialSample](MaterialSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
     * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
         * [EnvironmentalFeature](EnvironmentalFeature.md)
         * [EnvironmentalProcess](EnvironmentalProcess.md)
         * [GeographicLocation](GeographicLocation.md) - a location that can be described in lat/long coordinates
             * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
     * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
     * [Treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures

### Associations

 * [Association](Association.md) - A typed association between two entities, supported by evidence
     * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
         * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship.
         * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
     * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
     * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
     * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
         * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md)
     * [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) - Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.)
     * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
     * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) - A regulatory relationship between two genes
     * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) - describes a physical interaction between a chemical entity and a gene or gene product. Any biological or chemical effect resulting from such an interaction are out of scope, and covered by the ChemicalAffectsGeneAssociation type (e.g. impact of a chemical on the abundance, activity, structure, etc, of either participant in the interaction)
     * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) - This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary undesirable effect.
         * [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) - This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary, typically (but not always) undesirable effect.
     * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
         * [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) - A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
         * [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md)
             * [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md)
     * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
     * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway.
     * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
     * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) - An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance.
     * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
     * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) - An association between an exposure event and a disease.
     * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
     * [DrugToGeneAssociation](DrugToGeneAssociation.md) - An interaction between a drug and a gene or gene product.
     * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
     * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
     * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
     * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
     * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.
         * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
         * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it.
         * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component.
         * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution.
     * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)
         * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
             * [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md)
             * [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md)
             * [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md)
             * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)
             * [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)
         * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
     * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and a gene expression site, possibly qualified by stage/timing info.
     * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
         * [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) - Indicates that two genes are co-expressed, generally under the same conditions.
         * [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
         * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
             * [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) - An interaction at the molecular level between two physical entities
     * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) - Set membership of a gene in a family of genes related by common evolutionary ancestry usually inferred by sequence comparisons. The genes in a given family generally share common sequence motifs which generally map onto shared gene product structure-function relationships.
     * [GeneToPathwayAssociation](GeneToPathwayAssociation.md) - An interaction between a gene or gene product and a biological process or pathway.
     * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
         * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)
     * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
     * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
     * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
     * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
     * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) - association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).
     * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity from which it is derived.
     * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype.
     * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) - Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
     * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) - Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
     * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) - Association that holds the relationship between a reaction and the pathway it participates in.
     * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
     * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md)
     * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) - A relationship between two organism taxon nodes
         * [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) - An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens
         * [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) - A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo
     * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
     * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
     * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
     * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a nucleic acid entity it is localized to.
         * [GenomicSequenceLocalization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig.
     * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
         * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
         * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
         * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts
     * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
     * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
     * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
         * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)
     * [VariantToGeneAssociation](VariantToGeneAssociation.md) - An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
         * [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) - An association between a variant and expression of a gene (i.e. e-QTL)
     * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
     * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population

### Class Mixins

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) - An abstract association for use where the case is the subject
 * [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) - An relationship between a cell line and another entity
 * [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) - A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
 * [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md) - A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
 * [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) - An interaction between a chemical entity and another entity
     * [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)
     * [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) - An interaction between a drug and another entity
 * [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)
 * [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)
 * [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md)
 * [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
 * [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)
 * [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) - An association between some entity and an exposure event.
 * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.
     * [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
     * [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)
 * [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) - An association between some entity and an outcome
 * [EpigenomicEntity](EpigenomicEntity.md)
 * [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 * [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations
     * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.
         * [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
         * [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)
 * [FrequencyQuantifier](FrequencyQuantifier.md)
 * [GeneExpressionMixin](GeneExpressionMixin.md) - Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.
 * [GeneGroupingMixin](GeneGroupingMixin.md) - any grouping of multiple genes or gene products
 * [GeneOrGeneProduct](GeneOrGeneProduct.md) - A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
     * [GeneProductMixin](GeneProductMixin.md) - The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.
         * [GeneProductIsoformMixin](GeneProductIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
 * [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)
 * [GenomicEntity](GenomicEntity.md)
 * [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md)
 * [MacromolecularMachineMixin](MacromolecularMachineMixin.md) - A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
     * [GeneOrGeneProduct](GeneOrGeneProduct.md) - A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
         * [GeneProductMixin](GeneProductMixin.md) - The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.
             * [GeneProductIsoformMixin](GeneProductIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
 * [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) - an association which has a macromolecular machine mixin as a subject
 * [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) - An association between a material sample and something.
 * [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 * [Occurrent](Occurrent.md) - A processual entity.
     * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
     * [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
     * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
 * [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) - An association between an organism taxon and another entity
 * [Outcome](Outcome.md) - An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes.
 * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [PathologicalEntityMixin](PathologicalEntityMixin.md) - A pathological (abnormal) structure or process.
 * [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
 * [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) - Either a physical or processual entity.
     * [Occurrent](Occurrent.md) - A processual entity.
         * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
     * [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
 * [RelationshipQuantifier](RelationshipQuantifier.md)
     * [FrequencyQuantifier](FrequencyQuantifier.md)
     * [SensitivityQuantifier](SensitivityQuantifier.md)
     * [SpecificityQuantifier](SpecificityQuantifier.md)
         * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [SubjectOfInvestigation](SubjectOfInvestigation.md) - An entity that has the role of being studied in an investigation, study, or experiment
 * [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
 * [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)

### Other Classes

 * [Annotation](Annotation.md) - Biolink Model root class for entity annotations.
     * [QuantityValue](QuantityValue.md) - A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
 * [BehavioralOutcome](BehavioralOutcome.md) - An outcome resulting from an exposure event which is the manifestation of human behavior.
 * [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) - Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype.
 * [EpidemiologicalOutcome](EpidemiologicalOutcome.md) - An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
 * [HospitalizationOutcome](HospitalizationOutcome.md) - An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) hospitalization.
 * [MappingCollection](MappingCollection.md) - A collection of deprecated mappings.
 * [MortalityOutcome](MortalityOutcome.md) - An outcome of death from resulting from an exposure event.
 * [PathologicalAnatomicalOutcome](PathologicalAnatomicalOutcome.md) - An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure.
 * [PathologicalProcessOutcome](PathologicalProcessOutcome.md) - An outcome resulting from an exposure event which is the manifestation of a pathological process.
 * [PredicateMapping](PredicateMapping.md) - A deprecated predicate mapping object contains the deprecated predicate and an example of the rewiring that should be done to use a qualified statement in its place.
 * [SocioeconomicOutcome](SocioeconomicOutcome.md) - An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event

## Slots


### Predicates

 * [active in](active_in.md)
 * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
     * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [actively involves](actively_involves.md)
     * [can be carried out by](can_be_carried_out_by.md)
 * [acts upstream of](acts_upstream_of.md)
     * [acts upstream of negative effect](acts_upstream_of_negative_effect.md)
     * [acts upstream of or within](acts_upstream_of_or_within.md)
         * [acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)
         * [acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)
     * [acts upstream of positive effect](acts_upstream_of_positive_effect.md)
 * [acts upstream of negative effect](acts_upstream_of_negative_effect.md)
 * [acts upstream of or within](acts_upstream_of_or_within.md)
     * [acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)
     * [acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)
 * [acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)
 * [acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)
 * [acts upstream of positive effect](acts_upstream_of_positive_effect.md)
 * [adverse event of](adverse_event_of.md)
 * [affected by](affected_by.md) - describes an entity of which the state or quality is affected by another existing entity.
     * [adverse event of](adverse_event_of.md)
     * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
     * [is ameliorated by](is_ameliorated_by.md)
         * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition
     * [is exacerbated by](is_exacerbated_by.md)
     * [is side effect of](is_side_effect_of.md)
     * [regulated by](regulated_by.md)
     * [response affected by](response_affected_by.md) - holds between two chemical entities where the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) of one is affected by the action of the other.
         * [response decreased by](response_decreased_by.md)
         * [response increased by](response_increased_by.md)
 * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * [affects response to](affects_response_to.md)
         * [decreases response to](decreases_response_to.md) - holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
         * [increases response to](increases_response_to.md) - holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
     * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure, clinical intervention) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
         * [treats](treats.md) - holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat
     * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
     * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
     * [has adverse event](has_adverse_event.md) - An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment  with a therapeutic agent. Adverse events may be caused by something  other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or  diseases temporally associated with the treatment, whether or not considered related to the treatment.  Adverse events are unintended effects that occur when a medication is administered correctly.
     * [has side effect](has_side_effect.md) - An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of  the medication.
     * [regulates](regulates.md) - A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction.
 * [affects response to](affects_response_to.md)
     * [decreases response to](decreases_response_to.md) - holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
     * [increases response to](increases_response_to.md) - holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
 * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
     * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
     * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
 * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure, clinical intervention) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
     * [treats](treats.md) - holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat
 * [amount or activity decreased by](amount_or_activity_decreased_by.md)
 * [amount or activity increased by](amount_or_activity_increased_by.md)
 * [assesses](assesses.md) - The effect of a thing on a target was interrogated in some assay. A relationship between some perturbing agent (usually a chemical compound) and some target entity, where the affect of the perturbing agent on the target entity was interrogated in a particular assay. The target might be a particular protein, tissue, phenotype, whole organism, cell line, or other type of biological entity.
 * [associated with](associated_with.md) - Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. This relationship holds between two concepts represented by variables for which a statistical  dependence is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with Myocardial  Infraction (MI)” asserts that having Afib is not statistically independent from whether a patient  will also have MI. Note that in Translator associations, the subject and object concepts may map exactly to  the statistical variables, or represent related entities for which the variables serve as proxies in an  Association (e.g. diseases, chemical entities or processes).
     * [associated with likelihood of](associated_with_likelihood_of.md) - A a relationship that holds between two concepts represented by variables for which a statistical  dependence is demonstrated, wherein the state or value of one variable predicts the future state  or value of the other.  E.g. the statement “An Atrial Fibrillation (Afib) diagnosis is associated  with likelihood of a Myocardial Infraction (MI) diagnosis” asserts that the state of having Afib  is associated with an increased or decreased likelihood that a patient will later exhibit MI.
         * [associated with decreased likelihood of](associated_with_decreased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is less probable.
         * [associated with increased likelihood of](associated_with_increased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is more probable.
     * [associated with resistance to](associated_with_resistance_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical.
     * [associated with sensitivity to](associated_with_sensitivity_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical.
     * [correlated with](correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical dependence is  demonstrated using a correlation analysis method.
         * [biomarker for](biomarker_for.md) - holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
         * [coexpressed with](coexpressed_with.md) - holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context.
         * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature.
         * [negatively correlated with](negatively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move in opposite directions (i.e. increased in one or presence of  one correlates with a decrease or absence of the other).
         * [occurs together in literature with](occurs_together_in_literature_with.md) - holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider.
         * [positively correlated with](positively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other).
     * [genetic association](genetic_association.md)
     * [genetically associated with](genetically_associated_with.md)
         * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
         * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * [likelihood associated with](likelihood_associated_with.md)
         * [decreased likelihood associated with](decreased_likelihood_associated_with.md)
         * [increased likelihood associated with](increased_likelihood_associated_with.md)
     * [resistance associated with](resistance_associated_with.md)
     * [sensitivity associated with](sensitivity_associated_with.md)
 * [associated with decreased likelihood of](associated_with_decreased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is less probable.
 * [associated with increased likelihood of](associated_with_increased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is more probable.
 * [associated with likelihood of](associated_with_likelihood_of.md) - A a relationship that holds between two concepts represented by variables for which a statistical  dependence is demonstrated, wherein the state or value of one variable predicts the future state  or value of the other.  E.g. the statement “An Atrial Fibrillation (Afib) diagnosis is associated  with likelihood of a Myocardial Infraction (MI) diagnosis” asserts that the state of having Afib  is associated with an increased or decreased likelihood that a patient will later exhibit MI.
     * [associated with decreased likelihood of](associated_with_decreased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is less probable.
     * [associated with increased likelihood of](associated_with_increased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is more probable.
 * [associated with resistance to](associated_with_resistance_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical.
 * [associated with sensitivity to](associated_with_sensitivity_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical.
 * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
 * [binds](binds.md) - A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity,  which form a stable physical interaction.
 * [biomarker for](biomarker_for.md) - holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
 * [broad match](broad_match.md) - a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
 * [can be carried out by](can_be_carried_out_by.md)
 * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [catalyzes](catalyzes.md)
 * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
 * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
 * [chemically similar to](chemically_similar_to.md) - holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [close match](close_match.md) - a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity).
     * [exact match](exact_match.md) - holds between two entities that have strictly equivalent meanings, with a high degree of confidence
         * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
     * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
     * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
     * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
     * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
 * [coexpressed with](coexpressed_with.md) - holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context.
 * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
 * [completed by](completed_by.md)
 * [composed primarily of](composed_primarily_of.md) - x composed_primarily_of_y if:more than half of the mass of x is made from parts of y.
 * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
 * [consumed by](consumed_by.md)
 * [consumes](consumes.md)
 * [contains process](contains_process.md)
 * [contraindicated for](contraindicated_for.md) - Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug.
 * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one contributes to the occurrence or generation of the other
     * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
 * [contribution from](contribution_from.md)
     * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
 * [contributor](contributor.md)
     * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
     * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
     * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
     * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [correlated with](correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical dependence is  demonstrated using a correlation analysis method.
     * [biomarker for](biomarker_for.md) - holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * [coexpressed with](coexpressed_with.md) - holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context.
     * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature.
     * [negatively correlated with](negatively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move in opposite directions (i.e. increased in one or presence of  one correlates with a decrease or absence of the other).
     * [occurs together in literature with](occurs_together_in_literature_with.md) - holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider.
     * [positively correlated with](positively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other).
 * [decreased amount in](decreased_amount_in.md)
 * [decreased likelihood associated with](decreased_likelihood_associated_with.md)
 * [decreases response to](decreases_response_to.md) - holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
 * [derives from](derives_from.md) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * [is metabolite of](is_metabolite_of.md) - holds between two molecular entities in which the first one is derived from the second one as a product of metabolism
 * [derives into](derives_into.md) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * [has metabolite](has_metabolite.md) - holds between two molecular entities in which the second one is derived from the first one as a product of metabolism
 * [develops from](develops_from.md)
 * [develops into](develops_into.md)
 * [diagnoses](diagnoses.md) - a relationship that identifies the nature of (an illness or other problem) by examination  of the symptoms.
 * [directly physically interacts with](directly_physically_interacts_with.md) - A causal mechanism mediated by a direct contact between the effector and target entities (this contact may  be weak or strong, transient or stable).
     * [binds](binds.md) - A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity,  which form a stable physical interaction.
 * [disease has basis in](disease_has_basis_in.md) - A relation that holds between a disease and an entity where the state of the entity has contribution to the disease.
 * [disease has location](disease_has_location.md) - A relationship between a disease and an anatomical entity where the disease has one or more features that are located in that entity.
 * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
 * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
 * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
 * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
 * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
 * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
 * [exact match](exact_match.md) - holds between two entities that have strictly equivalent meanings, with a high degree of confidence
     * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
 * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
 * [food component of](food_component_of.md) - holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)
     * [nutrient of](nutrient_of.md)
 * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
 * [gene product of](gene_product_of.md) - definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x
 * [gene_fusion_with](gene_fusion_with.md) - holds between two independent genes that have fused through  translocation, interstitial deletion, or chromosomal inversion to  form a new, hybrid gene. Fusion genes are often implicated in various neoplasms and cancers.
 * [genetic association](genetic_association.md)
 * [genetic_neighborhood_of](genetic_neighborhood_of.md) - holds between two genes located nearby one another on a chromosome. 
 * [genetically associated with](genetically_associated_with.md)
     * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
     * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
 * [genetically interacts with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * [gene_fusion_with](gene_fusion_with.md) - holds between two independent genes that have fused through  translocation, interstitial deletion, or chromosomal inversion to  form a new, hybrid gene. Fusion genes are often implicated in various neoplasms and cancers.
     * [genetic_neighborhood_of](genetic_neighborhood_of.md) - holds between two genes located nearby one another on a chromosome. 
 * [has active component](has_active_component.md)
 * [has active ingredient](has_active_ingredient.md) - holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component
 * [has adverse event](has_adverse_event.md) - An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment  with a therapeutic agent. Adverse events may be caused by something  other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or  diseases temporally associated with the treatment, whether or not considered related to the treatment.  Adverse events are unintended effects that occur when a medication is administered correctly.
 * [has author](has_author.md)
 * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature.
 * [has catalyst](has_catalyst.md)
 * [has chemical role](has_chemical_role.md) - A role is particular behaviour which a chemical entity may exhibit.
 * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
 * [has contraindication](has_contraindication.md)
 * [has contributor](has_contributor.md)
     * [has author](has_author.md)
     * [has editor](has_editor.md)
     * [has provider](has_provider.md)
     * [has publisher](has_publisher.md)
 * [has decreased amount](has_decreased_amount.md)
 * [has editor](has_editor.md)
 * [has excipient](has_excipient.md) - holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component
 * [has food component](has_food_component.md) - holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
     * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
 * [has frameshift variant](has_frameshift_variant.md)
 * [has gene product](has_gene_product.md) - holds between a gene and a transcribed and/or translated product generated from it
 * [has increased amount](has_increased_amount.md)
 * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
     * [consumes](consumes.md)
 * [has manifestation](has_manifestation.md)
     * [has mode of inheritance](has_mode_of_inheritance.md) - Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome).
 * [has member](has_member.md) - Defines a mereological relation between a collection and an item.
 * [has metabolite](has_metabolite.md) - holds between two molecular entities in which the second one is derived from the first one as a product of metabolism
 * [has missense variant](has_missense_variant.md)
 * [has mode of inheritance](has_mode_of_inheritance.md) - Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome).
 * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
 * [has nearby variant](has_nearby_variant.md)
 * [has negative upstream actor](has_negative_upstream_actor.md)
 * [has negative upstream or within actor](has_negative_upstream_or_within_actor.md)
 * [has non coding variant](has_non_coding_variant.md)
 * [has nonsense variant](has_nonsense_variant.md)
 * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
 * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
 * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
     * [has active ingredient](has_active_ingredient.md) - holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component
     * [has excipient](has_excipient.md) - holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component
     * [has food component](has_food_component.md) - holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
         * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
     * [has plasma membrane part](has_plasma_membrane_part.md) - Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part.
     * [has variant part](has_variant_part.md) - holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it
 * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
     * [actively involves](actively_involves.md)
         * [can be carried out by](can_be_carried_out_by.md)
     * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
     * [has catalyst](has_catalyst.md)
     * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
         * [consumes](consumes.md)
     * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
     * [has substrate](has_substrate.md)
 * [has phenotype](has_phenotype.md) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate.
 * [has plasma membrane part](has_plasma_membrane_part.md) - Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part.
 * [has positive upstream actor](has_positive_upstream_actor.md)
 * [has positive upstream or within actor](has_positive_upstream_or_within_actor.md)
 * [has predisposing factor](has_predisposing_factor.md)
 * [has provider](has_provider.md)
 * [has publisher](has_publisher.md)
 * [has sequence location](has_sequence_location.md) - holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
 * [has sequence variant](has_sequence_variant.md)
     * [has frameshift variant](has_frameshift_variant.md)
     * [has missense variant](has_missense_variant.md)
     * [has nearby variant](has_nearby_variant.md)
     * [has non coding variant](has_non_coding_variant.md)
     * [has nonsense variant](has_nonsense_variant.md)
     * [has splice site variant](has_splice_site_variant.md)
     * [has synonymous variant](has_synonymous_variant.md)
 * [has side effect](has_side_effect.md) - An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of  the medication.
 * [has splice site variant](has_splice_site_variant.md)
 * [has substrate](has_substrate.md)
 * [has synonymous variant](has_synonymous_variant.md)
 * [has target](has_target.md)
 * [has upstream actor](has_upstream_actor.md)
     * [has negative upstream actor](has_negative_upstream_actor.md)
     * [has positive upstream actor](has_positive_upstream_actor.md)
     * [has upstream or within actor](has_upstream_or_within_actor.md)
         * [has negative upstream or within actor](has_negative_upstream_or_within_actor.md)
         * [has positive upstream or within actor](has_positive_upstream_or_within_actor.md)
 * [has upstream or within actor](has_upstream_or_within_actor.md)
     * [has negative upstream or within actor](has_negative_upstream_or_within_actor.md)
     * [has positive upstream or within actor](has_positive_upstream_or_within_actor.md)
 * [has variant part](has_variant_part.md) - holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it
 * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
     * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
     * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
     * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
 * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
 * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
 * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
 * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
 * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
 * [increased amount of](increased_amount_of.md)
 * [increased likelihood associated with](increased_likelihood_associated_with.md)
 * [increases response to](increases_response_to.md) - holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
 * [indirectly physically interacts with](indirectly_physically_interacts_with.md)
 * [is active ingredient of](is_active_ingredient_of.md) - holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component
 * [is ameliorated by](is_ameliorated_by.md)
     * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition
 * [is assessed by](is_assessed_by.md)
 * [is diagnosed by](is_diagnosed_by.md)
 * [is exacerbated by](is_exacerbated_by.md)
 * [is excipient of](is_excipient_of.md) - holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component
 * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
 * [is input of](is_input_of.md)
     * [consumed by](consumed_by.md)
 * [is metabolite of](is_metabolite_of.md) - holds between two molecular entities in which the first one is derived from the second one as a product of metabolism
 * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
 * [is molecular consequence of](is_molecular_consequence_of.md)
 * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
 * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
 * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
 * [is output of](is_output_of.md)
 * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a nucleic acid entity
     * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
     * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
     * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
     * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
     * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
     * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
     * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
 * [is side effect of](is_side_effect_of.md)
 * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
 * [is substrate of](is_substrate_of.md)
 * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
 * [lacks part](lacks_part.md)
 * [likelihood associated with](likelihood_associated_with.md)
     * [decreased likelihood associated with](decreased_likelihood_associated_with.md)
     * [increased likelihood associated with](increased_likelihood_associated_with.md)
 * [located in](located_in.md) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
     * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
 * [location of](location_of.md) - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
     * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
 * [location of disease](location_of_disease.md)
 * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
     * [mode of inheritance of](mode_of_inheritance_of.md)
 * [member of](member_of.md) - Defines a mereological relation between a item and a collection.
 * [mentioned by](mentioned_by.md) - refers to is a relation between one named thing and the information content entity that it makes reference to.
 * [mentions](mentions.md) - refers to is a relation between one information content entity and the named thing that it makes reference to.
 * [missing from](missing_from.md)
 * [mode of inheritance of](mode_of_inheritance_of.md)
 * [model of](model_of.md) - holds between a thing and some other thing it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [models](models.md)
 * [narrow match](narrow_match.md) - a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
 * [negatively correlated with](negatively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move in opposite directions (i.e. increased in one or presence of  one correlates with a decrease or absence of the other).
 * [not completed by](not_completed_by.md)
 * [nutrient of](nutrient_of.md)
 * [occurs in](occurs_in.md) - holds between a process and a material entity or site within which the process occurs
 * [occurs in disease](occurs_in_disease.md)
 * [occurs together in literature with](occurs_together_in_literature_with.md) - holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider.
 * [opposite of](opposite_of.md) - x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased).
 * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
 * [overlaps](overlaps.md) - holds between entities that overlap in their extents (materials or processes)
     * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
         * [has active ingredient](has_active_ingredient.md) - holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component
         * [has excipient](has_excipient.md) - holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component
         * [has food component](has_food_component.md) - holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
         * [has plasma membrane part](has_plasma_membrane_part.md) - Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part.
         * [has variant part](has_variant_part.md) - holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it
     * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
         * [food component of](food_component_of.md) - holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [nutrient of](nutrient_of.md)
         * [is active ingredient of](is_active_ingredient_of.md) - holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component
         * [is excipient of](is_excipient_of.md) - holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component
         * [plasma membrane part of](plasma_membrane_part_of.md)
         * [variant part of](variant_part_of.md)
 * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
 * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
     * [food component of](food_component_of.md) - holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)
         * [nutrient of](nutrient_of.md)
     * [is active ingredient of](is_active_ingredient_of.md) - holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component
     * [is excipient of](is_excipient_of.md) - holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component
     * [plasma membrane part of](plasma_membrane_part_of.md)
     * [variant part of](variant_part_of.md)
 * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
     * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
         * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
     * [catalyzes](catalyzes.md)
     * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
     * [is input of](is_input_of.md)
         * [consumed by](consumed_by.md)
     * [is output of](is_output_of.md)
     * [is substrate of](is_substrate_of.md)
 * [phenotype of](phenotype_of.md)
 * [physically interacts with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction.  does not imply a causal relationship.
     * [directly physically interacts with](directly_physically_interacts_with.md) - A causal mechanism mediated by a direct contact between the effector and target entities (this contact may  be weak or strong, transient or stable).
         * [binds](binds.md) - A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity,  which form a stable physical interaction.
     * [indirectly physically interacts with](indirectly_physically_interacts_with.md)
 * [plasma membrane part of](plasma_membrane_part_of.md)
 * [positively correlated with](positively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other).
 * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
 * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
 * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the application or use of an entity.
 * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
 * [primarily composed of](primarily_composed_of.md)
 * [produced by](produced_by.md)
 * [produces](produces.md) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
 * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
 * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [regulated by](regulated_by.md)
 * [regulates](regulates.md) - A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction.
 * [related condition](related_condition.md)
 * [related to](related_to.md) - A relationship that is asserted between two named things
     * [composed primarily of](composed_primarily_of.md) - x composed_primarily_of_y if:more than half of the mass of x is made from parts of y.
     * [disease has location](disease_has_location.md) - A relationship between a disease and an anatomical entity where the disease has one or more features that are located in that entity.
     * [location of disease](location_of_disease.md)
     * [primarily composed of](primarily_composed_of.md)
     * [related to at concept level](related_to_at_concept_level.md) - Represents a relationship held between terminology components that describe the conceptual model of a domain.
         * [broad match](broad_match.md) - a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
         * [close match](close_match.md) - a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity).
             * [exact match](exact_match.md) - holds between two entities that have strictly equivalent meanings, with a high degree of confidence
                 * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
         * [has chemical role](has_chemical_role.md) - A role is particular behaviour which a chemical entity may exhibit.
         * [has member](has_member.md) - Defines a mereological relation between a collection and an item.
         * [member of](member_of.md) - Defines a mereological relation between a item and a collection.
         * [narrow match](narrow_match.md) - a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
         * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
         * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
     * [related to at instance level](related_to_at_instance_level.md) - Represents a relationship held between two instances of a data classes.  Much like an assertion component, in an ABox, these represent facts associated with the conceptual model.
         * [active in](active_in.md)
         * [acts upstream of](acts_upstream_of.md)
             * [acts upstream of negative effect](acts_upstream_of_negative_effect.md)
             * [acts upstream of or within](acts_upstream_of_or_within.md)
                 * [acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)
                 * [acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)
             * [acts upstream of positive effect](acts_upstream_of_positive_effect.md)
         * [affected by](affected_by.md) - describes an entity of which the state or quality is affected by another existing entity.
             * [adverse event of](adverse_event_of.md)
             * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
             * [is ameliorated by](is_ameliorated_by.md)
                 * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition
             * [is exacerbated by](is_exacerbated_by.md)
             * [is side effect of](is_side_effect_of.md)
             * [regulated by](regulated_by.md)
             * [response affected by](response_affected_by.md) - holds between two chemical entities where the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) of one is affected by the action of the other.
                 * [response decreased by](response_decreased_by.md)
                 * [response increased by](response_increased_by.md)
         * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
             * [affects response to](affects_response_to.md)
                 * [decreases response to](decreases_response_to.md) - holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
                 * [increases response to](increases_response_to.md) - holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
             * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure, clinical intervention) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
                 * [treats](treats.md) - holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat
             * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
             * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
             * [has adverse event](has_adverse_event.md) - An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment  with a therapeutic agent. Adverse events may be caused by something  other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or  diseases temporally associated with the treatment, whether or not considered related to the treatment.  Adverse events are unintended effects that occur when a medication is administered correctly.
             * [has side effect](has_side_effect.md) - An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of  the medication.
             * [regulates](regulates.md) - A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction.
         * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
             * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
             * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
         * [amount or activity decreased by](amount_or_activity_decreased_by.md)
         * [amount or activity increased by](amount_or_activity_increased_by.md)
         * [assesses](assesses.md) - The effect of a thing on a target was interrogated in some assay. A relationship between some perturbing agent (usually a chemical compound) and some target entity, where the affect of the perturbing agent on the target entity was interrogated in a particular assay. The target might be a particular protein, tissue, phenotype, whole organism, cell line, or other type of biological entity.
         * [associated with](associated_with.md) - Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. This relationship holds between two concepts represented by variables for which a statistical  dependence is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with Myocardial  Infraction (MI)” asserts that having Afib is not statistically independent from whether a patient  will also have MI. Note that in Translator associations, the subject and object concepts may map exactly to  the statistical variables, or represent related entities for which the variables serve as proxies in an  Association (e.g. diseases, chemical entities or processes).
             * [associated with likelihood of](associated_with_likelihood_of.md) - A a relationship that holds between two concepts represented by variables for which a statistical  dependence is demonstrated, wherein the state or value of one variable predicts the future state  or value of the other.  E.g. the statement “An Atrial Fibrillation (Afib) diagnosis is associated  with likelihood of a Myocardial Infraction (MI) diagnosis” asserts that the state of having Afib  is associated with an increased or decreased likelihood that a patient will later exhibit MI.
                 * [associated with decreased likelihood of](associated_with_decreased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is less probable.
                 * [associated with increased likelihood of](associated_with_increased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is more probable.
             * [associated with resistance to](associated_with_resistance_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical.
             * [associated with sensitivity to](associated_with_sensitivity_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical.
             * [correlated with](correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical dependence is  demonstrated using a correlation analysis method.
                 * [biomarker for](biomarker_for.md) - holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
                 * [coexpressed with](coexpressed_with.md) - holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context.
                 * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature.
                 * [negatively correlated with](negatively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move in opposite directions (i.e. increased in one or presence of  one correlates with a decrease or absence of the other).
                 * [occurs together in literature with](occurs_together_in_literature_with.md) - holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider.
                 * [positively correlated with](positively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other).
             * [genetic association](genetic_association.md)
             * [genetically associated with](genetically_associated_with.md)
                 * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
                 * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
             * [likelihood associated with](likelihood_associated_with.md)
                 * [decreased likelihood associated with](decreased_likelihood_associated_with.md)
                 * [increased likelihood associated with](increased_likelihood_associated_with.md)
             * [resistance associated with](resistance_associated_with.md)
             * [sensitivity associated with](sensitivity_associated_with.md)
         * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
             * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
             * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
             * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
             * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
         * [completed by](completed_by.md)
         * [contains process](contains_process.md)
         * [contraindicated for](contraindicated_for.md) - Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug.
         * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one contributes to the occurrence or generation of the other
             * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
         * [contribution from](contribution_from.md)
             * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
         * [contributor](contributor.md)
             * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
             * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
             * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
             * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
         * [decreased amount in](decreased_amount_in.md)
         * [derives from](derives_from.md) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
             * [is metabolite of](is_metabolite_of.md) - holds between two molecular entities in which the first one is derived from the second one as a product of metabolism
         * [derives into](derives_into.md) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
             * [has metabolite](has_metabolite.md) - holds between two molecular entities in which the second one is derived from the first one as a product of metabolism
         * [develops from](develops_from.md)
         * [develops into](develops_into.md)
         * [diagnoses](diagnoses.md) - a relationship that identifies the nature of (an illness or other problem) by examination  of the symptoms.
         * [disease has basis in](disease_has_basis_in.md) - A relation that holds between a disease and an entity where the state of the entity has contribution to the disease.
         * [gene product of](gene_product_of.md) - definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x
         * [has active component](has_active_component.md)
         * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
         * [has contraindication](has_contraindication.md)
         * [has contributor](has_contributor.md)
             * [has author](has_author.md)
             * [has editor](has_editor.md)
             * [has provider](has_provider.md)
             * [has publisher](has_publisher.md)
         * [has decreased amount](has_decreased_amount.md)
         * [has gene product](has_gene_product.md) - holds between a gene and a transcribed and/or translated product generated from it
         * [has increased amount](has_increased_amount.md)
         * [has manifestation](has_manifestation.md)
             * [has mode of inheritance](has_mode_of_inheritance.md) - Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome).
         * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
         * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
         * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
             * [actively involves](actively_involves.md)
                 * [can be carried out by](can_be_carried_out_by.md)
             * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
             * [has catalyst](has_catalyst.md)
             * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
                 * [consumes](consumes.md)
             * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
             * [has substrate](has_substrate.md)
         * [has phenotype](has_phenotype.md) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate.
         * [has sequence location](has_sequence_location.md) - holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
         * [has sequence variant](has_sequence_variant.md)
             * [has frameshift variant](has_frameshift_variant.md)
             * [has missense variant](has_missense_variant.md)
             * [has nearby variant](has_nearby_variant.md)
             * [has non coding variant](has_non_coding_variant.md)
             * [has nonsense variant](has_nonsense_variant.md)
             * [has splice site variant](has_splice_site_variant.md)
             * [has synonymous variant](has_synonymous_variant.md)
         * [has target](has_target.md)
         * [has upstream actor](has_upstream_actor.md)
             * [has negative upstream actor](has_negative_upstream_actor.md)
             * [has positive upstream actor](has_positive_upstream_actor.md)
             * [has upstream or within actor](has_upstream_or_within_actor.md)
                 * [has negative upstream or within actor](has_negative_upstream_or_within_actor.md)
                 * [has positive upstream or within actor](has_positive_upstream_or_within_actor.md)
         * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
         * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
         * [increased amount of](increased_amount_of.md)
         * [is assessed by](is_assessed_by.md)
         * [is diagnosed by](is_diagnosed_by.md)
         * [is molecular consequence of](is_molecular_consequence_of.md)
         * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a nucleic acid entity
             * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
             * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
             * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
             * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
             * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
             * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
             * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
         * [lacks part](lacks_part.md)
         * [located in](located_in.md) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
             * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
         * [location of](location_of.md) - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
             * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
         * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
             * [mode of inheritance of](mode_of_inheritance_of.md)
         * [mentioned by](mentioned_by.md) - refers to is a relation between one named thing and the information content entity that it makes reference to.
         * [mentions](mentions.md) - refers to is a relation between one information content entity and the named thing that it makes reference to.
         * [missing from](missing_from.md)
         * [model of](model_of.md) - holds between a thing and some other thing it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
         * [models](models.md)
         * [not completed by](not_completed_by.md)
         * [occurs in](occurs_in.md) - holds between a process and a material entity or site within which the process occurs
         * [occurs in disease](occurs_in_disease.md)
         * [opposite of](opposite_of.md) - x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased).
         * [overlaps](overlaps.md) - holds between entities that overlap in their extents (materials or processes)
             * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
                 * [has active ingredient](has_active_ingredient.md) - holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component
                 * [has excipient](has_excipient.md) - holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component
                 * [has food component](has_food_component.md) - holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
                     * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
                 * [has plasma membrane part](has_plasma_membrane_part.md) - Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part.
                 * [has variant part](has_variant_part.md) - holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it
             * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
                 * [food component of](food_component_of.md) - holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)
                     * [nutrient of](nutrient_of.md)
                 * [is active ingredient of](is_active_ingredient_of.md) - holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component
                 * [is excipient of](is_excipient_of.md) - holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component
                 * [plasma membrane part of](plasma_membrane_part_of.md)
                 * [variant part of](variant_part_of.md)
         * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
             * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
                 * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
             * [catalyzes](catalyzes.md)
             * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
             * [is input of](is_input_of.md)
                 * [consumed by](consumed_by.md)
             * [is output of](is_output_of.md)
             * [is substrate of](is_substrate_of.md)
         * [phenotype of](phenotype_of.md)
         * [produced by](produced_by.md)
         * [produces](produces.md) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
         * [related condition](related_condition.md)
         * [risk affected by](risk_affected_by.md)
             * [has predisposing factor](has_predisposing_factor.md)
             * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the application or use of an entity.
         * [sequence location of](sequence_location_of.md)
         * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
             * [chemically similar to](chemically_similar_to.md) - holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
             * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
                 * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
                 * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
                 * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
         * [target for](target_for.md) - A gene is a target of a disease when its products are druggable and when a drug interaction with the gene product could have a therapeutic effect
         * [taxon of](taxon_of.md)
         * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
             * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
             * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
         * [transcribed from](transcribed_from.md) - x is transcribed from y if and only if x is synthesized from template y
         * [transcribed to](transcribed_to.md) - inverse of transcribed from
         * [translates to](translates_to.md) - x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)
         * [translation of](translation_of.md) - inverse of translates to
 * [related to at concept level](related_to_at_concept_level.md) - Represents a relationship held between terminology components that describe the conceptual model of a domain.
     * [broad match](broad_match.md) - a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
     * [close match](close_match.md) - a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity).
         * [exact match](exact_match.md) - holds between two entities that have strictly equivalent meanings, with a high degree of confidence
             * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
     * [has chemical role](has_chemical_role.md) - A role is particular behaviour which a chemical entity may exhibit.
     * [has member](has_member.md) - Defines a mereological relation between a collection and an item.
     * [member of](member_of.md) - Defines a mereological relation between a item and a collection.
     * [narrow match](narrow_match.md) - a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
     * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
     * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
 * [related to at instance level](related_to_at_instance_level.md) - Represents a relationship held between two instances of a data classes.  Much like an assertion component, in an ABox, these represent facts associated with the conceptual model.
     * [active in](active_in.md)
     * [acts upstream of](acts_upstream_of.md)
         * [acts upstream of negative effect](acts_upstream_of_negative_effect.md)
         * [acts upstream of or within](acts_upstream_of_or_within.md)
             * [acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)
             * [acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)
         * [acts upstream of positive effect](acts_upstream_of_positive_effect.md)
     * [affected by](affected_by.md) - describes an entity of which the state or quality is affected by another existing entity.
         * [adverse event of](adverse_event_of.md)
         * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
         * [is ameliorated by](is_ameliorated_by.md)
             * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition
         * [is exacerbated by](is_exacerbated_by.md)
         * [is side effect of](is_side_effect_of.md)
         * [regulated by](regulated_by.md)
         * [response affected by](response_affected_by.md) - holds between two chemical entities where the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) of one is affected by the action of the other.
             * [response decreased by](response_decreased_by.md)
             * [response increased by](response_increased_by.md)
     * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
         * [affects response to](affects_response_to.md)
             * [decreases response to](decreases_response_to.md) - holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
             * [increases response to](increases_response_to.md) - holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other
         * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure, clinical intervention) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition.
             * [treats](treats.md) - holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat
         * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
         * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition.
         * [has adverse event](has_adverse_event.md) - An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment  with a therapeutic agent. Adverse events may be caused by something  other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or  diseases temporally associated with the treatment, whether or not considered related to the treatment.  Adverse events are unintended effects that occur when a medication is administered correctly.
         * [has side effect](has_side_effect.md) - An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of  the medication.
         * [regulates](regulates.md) - A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction.
     * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
         * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
         * [prevents](prevents.md) - holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
     * [amount or activity decreased by](amount_or_activity_decreased_by.md)
     * [amount or activity increased by](amount_or_activity_increased_by.md)
     * [assesses](assesses.md) - The effect of a thing on a target was interrogated in some assay. A relationship between some perturbing agent (usually a chemical compound) and some target entity, where the affect of the perturbing agent on the target entity was interrogated in a particular assay. The target might be a particular protein, tissue, phenotype, whole organism, cell line, or other type of biological entity.
     * [associated with](associated_with.md) - Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. This relationship holds between two concepts represented by variables for which a statistical  dependence is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with Myocardial  Infraction (MI)” asserts that having Afib is not statistically independent from whether a patient  will also have MI. Note that in Translator associations, the subject and object concepts may map exactly to  the statistical variables, or represent related entities for which the variables serve as proxies in an  Association (e.g. diseases, chemical entities or processes).
         * [associated with likelihood of](associated_with_likelihood_of.md) - A a relationship that holds between two concepts represented by variables for which a statistical  dependence is demonstrated, wherein the state or value of one variable predicts the future state  or value of the other.  E.g. the statement “An Atrial Fibrillation (Afib) diagnosis is associated  with likelihood of a Myocardial Infraction (MI) diagnosis” asserts that the state of having Afib  is associated with an increased or decreased likelihood that a patient will later exhibit MI.
             * [associated with decreased likelihood of](associated_with_decreased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is less probable.
             * [associated with increased likelihood of](associated_with_increased_likelihood_of.md) - Expresses a relationship between two named things where the relationship is typically generated statistically and the state or fact of something is more probable.
         * [associated with resistance to](associated_with_resistance_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical.
         * [associated with sensitivity to](associated_with_sensitivity_to.md) - A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical.
         * [correlated with](correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical dependence is  demonstrated using a correlation analysis method.
             * [biomarker for](biomarker_for.md) - holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
             * [coexpressed with](coexpressed_with.md) - holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context.
             * [has biomarker](has_biomarker.md) - holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature.
             * [negatively correlated with](negatively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move in opposite directions (i.e. increased in one or presence of  one correlates with a decrease or absence of the other).
             * [occurs together in literature with](occurs_together_in_literature_with.md) - holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider.
             * [positively correlated with](positively_correlated_with.md) - A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other).
         * [genetic association](genetic_association.md)
         * [genetically associated with](genetically_associated_with.md)
             * [condition associated with gene](condition_associated_with_gene.md) - holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products
             * [gene associated with condition](gene_associated_with_condition.md) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
         * [likelihood associated with](likelihood_associated_with.md)
             * [decreased likelihood associated with](decreased_likelihood_associated_with.md)
             * [increased likelihood associated with](increased_likelihood_associated_with.md)
         * [resistance associated with](resistance_associated_with.md)
         * [sensitivity associated with](sensitivity_associated_with.md)
     * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
         * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
         * [in cell population with](in_cell_population_with.md) - holds between two genes or gene products that are expressed in the same cell type or population
         * [in complex with](in_complex_with.md) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
         * [in pathway with](in_pathway_with.md) - holds between two genes or gene products that are part of in the same biological pathway
     * [completed by](completed_by.md)
     * [contains process](contains_process.md)
     * [contraindicated for](contraindicated_for.md) - Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug.
     * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one contributes to the occurrence or generation of the other
         * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
     * [contribution from](contribution_from.md)
         * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
     * [contributor](contributor.md)
         * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
         * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
         * [provider](provider.md) - person, group, organization or project that provides a piece of information (e.g. a knowledge association).
         * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
     * [decreased amount in](decreased_amount_in.md)
     * [derives from](derives_from.md) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
         * [is metabolite of](is_metabolite_of.md) - holds between two molecular entities in which the first one is derived from the second one as a product of metabolism
     * [derives into](derives_into.md) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
         * [has metabolite](has_metabolite.md) - holds between two molecular entities in which the second one is derived from the first one as a product of metabolism
     * [develops from](develops_from.md)
     * [develops into](develops_into.md)
     * [diagnoses](diagnoses.md) - a relationship that identifies the nature of (an illness or other problem) by examination  of the symptoms.
     * [disease has basis in](disease_has_basis_in.md) - A relation that holds between a disease and an entity where the state of the entity has contribution to the disease.
     * [gene product of](gene_product_of.md) - definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x
     * [has active component](has_active_component.md)
     * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
     * [has contraindication](has_contraindication.md)
     * [has contributor](has_contributor.md)
         * [has author](has_author.md)
         * [has editor](has_editor.md)
         * [has provider](has_provider.md)
         * [has publisher](has_publisher.md)
     * [has decreased amount](has_decreased_amount.md)
     * [has gene product](has_gene_product.md) - holds between a gene and a transcribed and/or translated product generated from it
     * [has increased amount](has_increased_amount.md)
     * [has manifestation](has_manifestation.md)
         * [has mode of inheritance](has_mode_of_inheritance.md) - Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome).
     * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
     * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
     * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
         * [actively involves](actively_involves.md)
             * [can be carried out by](can_be_carried_out_by.md)
         * [enabled by](enabled_by.md) - holds between a process and a physical entity, where the physical entity executes the process
         * [has catalyst](has_catalyst.md)
         * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
             * [consumes](consumes.md)
         * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
         * [has substrate](has_substrate.md)
     * [has phenotype](has_phenotype.md) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate.
     * [has sequence location](has_sequence_location.md) - holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
     * [has sequence variant](has_sequence_variant.md)
         * [has frameshift variant](has_frameshift_variant.md)
         * [has missense variant](has_missense_variant.md)
         * [has nearby variant](has_nearby_variant.md)
         * [has non coding variant](has_non_coding_variant.md)
         * [has nonsense variant](has_nonsense_variant.md)
         * [has splice site variant](has_splice_site_variant.md)
         * [has synonymous variant](has_synonymous_variant.md)
     * [has target](has_target.md)
     * [has upstream actor](has_upstream_actor.md)
         * [has negative upstream actor](has_negative_upstream_actor.md)
         * [has positive upstream actor](has_positive_upstream_actor.md)
         * [has upstream or within actor](has_upstream_or_within_actor.md)
             * [has negative upstream or within actor](has_negative_upstream_or_within_actor.md)
             * [has positive upstream or within actor](has_positive_upstream_or_within_actor.md)
     * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
     * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * [increased amount of](increased_amount_of.md)
     * [is assessed by](is_assessed_by.md)
     * [is diagnosed by](is_diagnosed_by.md)
     * [is molecular consequence of](is_molecular_consequence_of.md)
     * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a nucleic acid entity
         * [is frameshift variant of](is_frameshift_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.
         * [is missense variant of](is_missense_variant_of.md) - holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved.
         * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a gene sequence that the variant is genomically close to.
         * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a gene, where the variant does not affect the coding sequence
         * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon
         * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the canonical splice site of one of the gene's exons.
         * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a gene, such the sequence variant is in the coding sequence of the gene, but results in the same amino acid sequence
     * [lacks part](lacks_part.md)
     * [located in](located_in.md) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
         * [expressed in](expressed_in.md) - holds between a gene or gene product and an anatomical entity in which it is expressed
     * [location of](location_of.md) - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
         * [expresses](expresses.md) - holds between an anatomical entity and gene or gene product that is expressed there
     * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
         * [mode of inheritance of](mode_of_inheritance_of.md)
     * [mentioned by](mentioned_by.md) - refers to is a relation between one named thing and the information content entity that it makes reference to.
     * [mentions](mentions.md) - refers to is a relation between one information content entity and the named thing that it makes reference to.
     * [missing from](missing_from.md)
     * [model of](model_of.md) - holds between a thing and some other thing it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
     * [models](models.md)
     * [not completed by](not_completed_by.md)
     * [occurs in](occurs_in.md) - holds between a process and a material entity or site within which the process occurs
     * [occurs in disease](occurs_in_disease.md)
     * [opposite of](opposite_of.md) - x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased).
     * [overlaps](overlaps.md) - holds between entities that overlap in their extents (materials or processes)
         * [has part](has_part.md) - holds between wholes and their parts (material entities or processes)
             * [has active ingredient](has_active_ingredient.md) - holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component
             * [has excipient](has_excipient.md) - holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component
             * [has food component](has_food_component.md) - holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
                 * [has nutrient](has_nutrient.md) - one or more nutrients which are growth factors for a living organism
             * [has plasma membrane part](has_plasma_membrane_part.md) - Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part.
             * [has variant part](has_variant_part.md) - holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it
         * [part of](part_of.md) - holds between parts and wholes (material entities or processes)
             * [food component of](food_component_of.md) - holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)
                 * [nutrient of](nutrient_of.md)
             * [is active ingredient of](is_active_ingredient_of.md) - holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component
             * [is excipient of](is_excipient_of.md) - holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component
             * [plasma membrane part of](plasma_membrane_part_of.md)
             * [variant part of](variant_part_of.md)
     * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
         * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
             * [capable of](capable_of.md) - holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
         * [catalyzes](catalyzes.md)
         * [enables](enables.md) - holds between a physical entity and a process, where the physical entity executes the process
         * [is input of](is_input_of.md)
             * [consumed by](consumed_by.md)
         * [is output of](is_output_of.md)
         * [is substrate of](is_substrate_of.md)
     * [phenotype of](phenotype_of.md)
     * [produced by](produced_by.md)
     * [produces](produces.md) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
     * [related condition](related_condition.md)
     * [risk affected by](risk_affected_by.md)
         * [has predisposing factor](has_predisposing_factor.md)
         * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the application or use of an entity.
     * [sequence location of](sequence_location_of.md)
     * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
         * [chemically similar to](chemically_similar_to.md) - holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
         * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
             * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
             * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
             * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
     * [target for](target_for.md) - A gene is a target of a disease when its products are druggable and when a drug interaction with the gene product could have a therapeutic effect
     * [taxon of](taxon_of.md)
     * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
         * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
         * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
     * [transcribed from](transcribed_from.md) - x is transcribed from y if and only if x is synthesized from template y
     * [transcribed to](transcribed_to.md) - inverse of transcribed from
     * [translates to](translates_to.md) - x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)
     * [translation of](translation_of.md) - inverse of translates to
 * [resistance associated with](resistance_associated_with.md)
 * [response affected by](response_affected_by.md) - holds between two chemical entities where the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) of one is affected by the action of the other.
     * [response decreased by](response_decreased_by.md)
     * [response increased by](response_increased_by.md)
 * [response decreased by](response_decreased_by.md)
 * [response increased by](response_increased_by.md)
 * [risk affected by](risk_affected_by.md)
     * [has predisposing factor](has_predisposing_factor.md)
     * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the application or use of an entity.
 * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [sensitivity associated with](sensitivity_associated_with.md)
 * [sequence location of](sequence_location_of.md)
 * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
     * [chemically similar to](chemically_similar_to.md) - holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
     * [homologous to](homologous_to.md) - holds between two biological entities that have common evolutionary origin
         * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically genes) that diverged after a speciation event.
         * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
         * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
 * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
 * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
 * [target for](target_for.md) - A gene is a target of a disease when its products are druggable and when a drug interaction with the gene product could have a therapeutic effect
 * [taxon of](taxon_of.md)
 * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
     * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
     * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [transcribed from](transcribed_from.md) - x is transcribed from y if and only if x is synthesized from template y
 * [transcribed to](transcribed_to.md) - inverse of transcribed from
 * [translates to](translates_to.md) - x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)
 * [translation of](translation_of.md) - inverse of translates to
 * [treated by](treated_by.md) - holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition
 * [treats](treats.md) - holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat
 * [variant part of](variant_part_of.md)
 * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.

### Node Properties

 * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
 * [affiliation](affiliation.md) - a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
 * [aggregate statistic](aggregate_statistic.md)
     * [has count](has_count.md) - number of things with a particular property
     * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
     * [has quotient](has_quotient.md)
     * [has total](has_total.md) - total number of things in a particular reference set
 * [animal model available from](animal_model_available_from.md)
 * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
 * [available from](available_from.md)
 * [broad synonym](broad_synonym.md)
 * [chapter](chapter.md) - chapter of a book
 * [created with](created_with.md)
 * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
 * [dataset download url](dataset_download_url.md)
 * [distribution download url](distribution_download_url.md)
 * [download url](download_url.md)
 * [exact synonym](exact_synonym.md)
 * [format](format.md)
 * [full name](full_name.md) - a long-form human readable name for a thing
 * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
 * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
 * [has constituent](has_constituent.md) - one or more molecular entities within a chemical mixture
 * [has count](has_count.md) - number of things with a particular property
 * [has dataset](has_dataset.md)
 * [has device](has_device.md) - connects an entity to one or more (medical) devices
 * [has distribution](has_distribution.md)
 * [has drug](has_drug.md) - connects an entity to one or more drugs
 * [has gene](has_gene.md) - connects an entity associated with one or more genes
 * [has gene or gene product](has_gene_or_gene_product.md) - connects an entity with one or more gene or gene products
     * [has gene](has_gene.md) - connects an entity associated with one or more genes
 * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
 * [has procedure](has_procedure.md) - connects an entity to one or more (medical) procedures
 * [has quotient](has_quotient.md)
 * [has receptor](has_receptor.md) - the organism or organism part being exposed
 * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the receptor
 * [has stressor](has_stressor.md) - the process or entity that the receptor is being exposed to
 * [has taxonomic rank](has_taxonomic_rank.md)
 * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238
 * [has total](has_total.md) - total number of things in a particular reference set
 * [has zygosity](has_zygosity.md)
 * [in_taxon_label](in_taxon_label.md) - The human readable scientific name for the taxon of the entity.
 * [ingest date](ingest_date.md)
 * [is metabolite](is_metabolite.md) - indicates whether a molecular entity is a metabolite
 * [is supplement](is_supplement.md)
 * [is toxic](is_toxic.md)
 * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
 * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
 * [keywords](keywords.md) - keywords tagging a publication
 * [latitude](latitude.md) - latitude
 * [license](license.md)
 * [longitude](longitude.md) - longitude
 * [max tolerated dose](max_tolerated_dose.md) - The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.
 * [mesh terms](mesh_terms.md) - mesh terms tagging a publication
 * [narrow synonym](narrow_synonym.md)
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
     * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
     * [affiliation](affiliation.md) - a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
     * [aggregate statistic](aggregate_statistic.md)
         * [has count](has_count.md) - number of things with a particular property
         * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
         * [has quotient](has_quotient.md)
         * [has total](has_total.md) - total number of things in a particular reference set
     * [animal model available from](animal_model_available_from.md)
     * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
     * [available from](available_from.md)
     * [chapter](chapter.md) - chapter of a book
     * [created with](created_with.md)
     * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
     * [dataset download url](dataset_download_url.md)
     * [distribution download url](distribution_download_url.md)
     * [download url](download_url.md)
     * [format](format.md)
     * [full name](full_name.md) - a long-form human readable name for a thing
     * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
     * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
     * [has constituent](has_constituent.md) - one or more molecular entities within a chemical mixture
     * [has dataset](has_dataset.md)
     * [has device](has_device.md) - connects an entity to one or more (medical) devices
     * [has distribution](has_distribution.md)
     * [has drug](has_drug.md) - connects an entity to one or more drugs
     * [has gene or gene product](has_gene_or_gene_product.md) - connects an entity with one or more gene or gene products
         * [has gene](has_gene.md) - connects an entity associated with one or more genes
     * [has procedure](has_procedure.md) - connects an entity to one or more (medical) procedures
     * [has receptor](has_receptor.md) - the organism or organism part being exposed
     * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the receptor
     * [has stressor](has_stressor.md) - the process or entity that the receptor is being exposed to
     * [has taxonomic rank](has_taxonomic_rank.md)
     * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238
     * [has zygosity](has_zygosity.md)
     * [in_taxon_label](in_taxon_label.md) - The human readable scientific name for the taxon of the entity.
     * [ingest date](ingest_date.md)
     * [is metabolite](is_metabolite.md) - indicates whether a molecular entity is a metabolite
     * [is supplement](is_supplement.md)
     * [is toxic](is_toxic.md)
     * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
     * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
     * [keywords](keywords.md) - keywords tagging a publication
     * [latitude](latitude.md) - latitude
     * [license](license.md)
     * [longitude](longitude.md) - longitude
     * [max tolerated dose](max_tolerated_dose.md) - The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.
     * [mesh terms](mesh_terms.md) - mesh terms tagging a publication
     * [pages](pages.md) - page number of source referenced for statement or publication
     * [provided by](provided_by.md) - The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
     * [resource id](resource_id.md) - The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
     * [resource role](resource_role.md) - The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.
     * [retrieved on](retrieved_on.md)
     * [rights](rights.md)
     * [source logo](source_logo.md)
     * [source web page](source_web_page.md)
     * [summary](summary.md) - executive  summary of a publication
     * [symbol](symbol.md) - Symbol for a particular thing
     * [synonym](synonym.md) - Alternate human-readable names for a thing
         * [broad synonym](broad_synonym.md)
         * [exact synonym](exact_synonym.md)
         * [narrow synonym](narrow_synonym.md)
         * [related synonym](related_synonym.md)
     * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
     * [trade name](trade_name.md)
     * [update date](update_date.md) - date on which an entity was updated. This can be applied to nodes or edges
     * [upstream resource ids](upstream_resource_ids.md) - An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.
     * [version](version.md)
     * [version of](version_of.md)
     * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
 * [pages](pages.md) - page number of source referenced for statement or publication
 * [provided by](provided_by.md) - The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
 * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
 * [related synonym](related_synonym.md)
 * [resource id](resource_id.md) - The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
 * [resource role](resource_role.md) - The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.
 * [retrieved on](retrieved_on.md)
 * [rights](rights.md)
 * [source logo](source_logo.md)
 * [source web page](source_web_page.md)
 * [summary](summary.md) - executive  summary of a publication
 * [symbol](symbol.md) - Symbol for a particular thing
 * [synonym](synonym.md) - Alternate human-readable names for a thing
     * [broad synonym](broad_synonym.md)
     * [exact synonym](exact_synonym.md)
     * [narrow synonym](narrow_synonym.md)
     * [related synonym](related_synonym.md)
 * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
 * [trade name](trade_name.md)
 * [update date](update_date.md) - date on which an entity was updated. This can be applied to nodes or edges
 * [upstream resource ids](upstream_resource_ids.md) - An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.
 * [version](version.md)
 * [version of](version_of.md)
 * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication

### Edge Properties

 * [adjusted p value](adjusted_p_value.md) - The adjusted p-value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct, adjusted for multiple comparisons.   P is always italicized and capitalized. The actual P value* should be expressed (P=. 04)  rather than expressing a statement of inequality (P<. 05), unless P<.
     * [bonferonni adjusted p value](bonferonni_adjusted_p_value.md) - The Bonferroni correction is an adjustment made to P values when several dependent or independent  statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni  correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and  capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality  (P<. 05), unless P<.
 * [aggregator knowledge source](aggregator_knowledge_source.md) - An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
 * [anatomical context qualifier](anatomical_context_qualifier.md) - A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).
 * [aspect qualifier](aspect_qualifier.md) - Composes with the core concept to describe new concepts of a different ontological type. e.g. a process in which the core concept participates, a function/activity/role held by the core concept, or a characteristic/quality that inheres in the core concept.  The purpose of the aspect slot is to indicate what aspect is being affected in an  'affects' association.
     * [object aspect qualifier](object_aspect_qualifier.md)
     * [subject aspect qualifier](subject_aspect_qualifier.md)
 * [associated environmental context](associated_environmental_context.md) - An attribute that can be applied to an association where the association holds between two entities located or occurring in a particular environment. For example, two microbial taxa may interact in the context of a human gut; a disease may give rise to a particular phenotype in a particular environmental exposure.
 * [association slot](association_slot.md) - any slot that relates an association to another entity
     * [FDA adverse event level](FDA_adverse_event_level.md)
     * [FDA approval status](FDA_approval_status.md)
     * [associated environmental context](associated_environmental_context.md) - An attribute that can be applied to an association where the association holds between two entities located or occurring in a particular environment. For example, two microbial taxa may interact in the context of a human gut; a disease may give rise to a particular phenotype in a particular environmental exposure.
     * [catalyst qualifier](catalyst_qualifier.md) - a qualifier that connects an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
     * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
     * [clinical modifier qualifier](clinical_modifier_qualifier.md) - the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.
     * [concept count object](concept_count_object.md) - The number of instances in a dataset/cohort whose records contain the concept in the object slot of an association.
     * [concept count subject](concept_count_subject.md) - The number of instances in a dataset/cohort whose records contain the concept in the subject slot of an association.
     * [concept pair count](concept_pair_count.md) - The number of instances in a dataset/cohort whose records contain both the subject and object concept of an association.
     * [dataset count](dataset_count.md) - The total number of instances (e.g., number of patients, number of rows, etc) in a dataset/cohort.
         * [total sample size](total_sample_size.md) - The total number of patients or participants within a sample population.
     * [evidence count](evidence_count.md) - The number of evidence instances that are connected to an association.
     * [expected count](expected_count.md) - The expected (calculated) number of instances in a dataset/cohort whose records contain both the subject and  object concept of an association if the subject and object concepts are independent.
     * [expression site](expression_site.md) - location in which gene or protein expression takes place. May be cell, tissue, or organ.
     * [extraction confidence score](extraction_confidence_score.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
     * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
     * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
     * [has supporting study result](has_supporting_study_result.md) - connects an association to an instance of supporting study result
     * [interacting molecules category](interacting_molecules_category.md)
     * [knowledge source](knowledge_source.md) - An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
         * [aggregator knowledge source](aggregator_knowledge_source.md) - An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
         * [primary knowledge source](primary_knowledge_source.md) - The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.
     * [ln ratio](ln_ratio.md) - the natural log of the ratio of co-occurrence to expected
     * [ln ratio confidence interval](ln_ratio_confidence_interval.md) - The 99% confidence interval for the ln_ratio calculation (i.e. the range of values within which the true value has a 99% chance of falling)
     * [log odds ratio](log_odds_ratio.md) - The logarithm of the odds ratio, or the ratio of the odds of event Y occurring in an exposed group versus the  odds of event Y occurring in a non-exposed group.
     * [log odds ration 95 ci](log_odds_ration_95_ci.md) - The ninety-five percent confidence range in which the true log odds ratio for the sample population falls.
     * [logical interpretation](logical_interpretation.md)
     * [mechanism of action](mechanism_of_action.md) - a boolean flag to indicate if the edge is part of a path or subgraph of a knowledge graph that constitutes the mechanism of action for a result.
     * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
     * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * [object category](object_category.md) - Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [object category closure](object_category_closure.md) - Used to hold the object category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [object closure](object_closure.md) - Used to hold the object closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [object label closure](object_label_closure.md) - Used to hold the object label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [object location in text](object_location_in_text.md) - Character offsets for the text span(s) in the supporting text corresponding to the object concept of the extracted assertion
     * [object namespace](object_namespace.md) - Used to hold the object namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [original object](original_object.md) - used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * [original predicate](original_predicate.md) - used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.
     * [original subject](original_subject.md) - used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
         * [adjusted p value](adjusted_p_value.md) - The adjusted p-value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct, adjusted for multiple comparisons.   P is always italicized and capitalized. The actual P value* should be expressed (P=. 04)  rather than expressing a statement of inequality (P<. 05), unless P<.
             * [bonferonni adjusted p value](bonferonni_adjusted_p_value.md) - The Bonferroni correction is an adjustment made to P values when several dependent or independent  statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni  correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and  capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality  (P<. 05), unless P<.
     * [phenotypic state](phenotypic_state.md) - in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.
     * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * [publications](publications.md) - One or more publications that report the statement expressed in an  Association, or provide information used as evidence supporting this statement.
     * [qualifier](qualifier.md) - grouping slot for all qualifiers on an edge.  useful for testing compliance with association classes
         * [aspect qualifier](aspect_qualifier.md) - Composes with the core concept to describe new concepts of a different ontological type. e.g. a process in which the core concept participates, a function/activity/role held by the core concept, or a characteristic/quality that inheres in the core concept.  The purpose of the aspect slot is to indicate what aspect is being affected in an  'affects' association.
             * [object aspect qualifier](object_aspect_qualifier.md)
             * [subject aspect qualifier](subject_aspect_qualifier.md)
         * [context qualifier](context_qualifier.md) - Restricts the setting/context/location where the core concept (or qualified core concept) resides or occurs.
             * [object context qualifier](object_context_qualifier.md)
             * [subject context qualifier](subject_context_qualifier.md)
         * [derivative qualifier](derivative_qualifier.md) - A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’.
             * [object derivative qualifier](object_derivative_qualifier.md)
             * [subject derivative qualifier](subject_derivative_qualifier.md)
         * [direction qualifier](direction_qualifier.md) - Composes with the core concept (+ aspect if provided) to describe a change in its direction or degree.
             * [object direction qualifier](object_direction_qualifier.md)
             * [subject direction qualifier](subject_direction_qualifier.md)
         * [form or variant qualifier](form_or_variant_qualifier.md) - A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’.
             * [object form or variant qualifier](object_form_or_variant_qualifier.md)
             * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)
         * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
         * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
         * [part qualifier](part_qualifier.md) - defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it, e.g. 'ESR1 transcript' q: polyA tail).
             * [object part qualifier](object_part_qualifier.md)
             * [subject part qualifier](subject_part_qualifier.md)
         * [population context qualifier](population_context_qualifier.md) - a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
         * [qualified predicate](qualified_predicate.md) - Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
         * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
         * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
         * [statement qualifier](statement_qualifier.md)
             * [anatomical context qualifier](anatomical_context_qualifier.md) - A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).
             * [causal mechanism qualifier](causal_mechanism_qualifier.md) - A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
             * [species context qualifier](species_context_qualifier.md) - A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
         * [temporal context qualifier](temporal_context_qualifier.md) - a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier.
             * [temporal interval qualifier](temporal_interval_qualifier.md) - a constraint of a time interval placed upon the truth value of an association.
     * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
     * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
     * [reaction balanced](reaction_balanced.md)
     * [reaction direction](reaction_direction.md) - the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)
     * [reaction side](reaction_side.md) - the side of a reaction being modeled (ie: left or right)
     * [relative frequency object](relative_frequency_object.md) - The frequency at which subject and object concepts co-occur in  records within a dataset/cohort, relative to the frequency at which the object concept appears in these same records.
     * [relative frequency object confidence interval](relative_frequency_object_confidence_interval.md) - The 99% confidence interval for the relative_frequency_object calculation (i.e. the range of values within which the true value has a 99% chance of falling)
     * [relative frequency subject](relative_frequency_subject.md) - The frequency at which subject and object concepts co-occur in  records within a dataset/cohort, relative to the frequency at which the subject concept appears in these same records.
     * [relative frequency subject confidence interval](relative_frequency_subject_confidence_interval.md) - The 99% confidence interval for the relative_frequency_subject calculation (i.e. the range of values within which the true value has a 99% chance of falling)
     * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a genome sequence localization edge. These edges connect a nucleic acid entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
         * [base coordinate](base_coordinate.md) - A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0.
             * [end coordinate](end_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
             * [start coordinate](start_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1).
         * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
         * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge.
             * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
             * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
         * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
         * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
     * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
     * [stage qualifier](stage_qualifier.md) - stage during which gene or protein expression of takes place.
     * [stoichiometry](stoichiometry.md) - the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.
     * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * [subject category](subject_category.md) - Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [subject category closure](subject_category_closure.md) - Used to hold the subject category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [subject closure](subject_closure.md) - Used to hold the subject closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [subject label closure](subject_label_closure.md) - Used to hold the subject label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [subject location in text](subject_location_in_text.md) - Character offsets for the text span(s) in the supporting text corresponding to the subject concept of the extracted assertion.
     * [subject namespace](subject_namespace.md) - Used to hold the subject namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * [supporting data set](supporting_data_set.md) - A set of data used as evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference over the retrieved data).
     * [supporting data source](supporting_data_source.md) - An Information Resource from which data was retrieved and subsequently used as evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference over the retrieved data).
     * [supporting document type](supporting_document_type.md) - The document type (e.g., Journal Article, Case Study, Preprint) for the supporting document used in a Text Mining Result.
     * [supporting document year](supporting_document_year.md) - The document year (typically the publication year) for the supporting document used in a Text Mining Result.
     * [supporting documents](supporting_documents.md) - One or more referenceable documents that report the statement expressed in an Association, or provide  information used as evidence supporting this statement.
     * [supporting study metadata](supporting_study_metadata.md) - Information about a study used to generate information used as evidence to support the knowledge expressed in an  Association. In practice, data creators should use one of the more specific subtypes of this property.
         * [supporting study cohort](supporting_study_cohort.md) - A description of a study population/cohort that was interrogated to provide evidence for the association  (e.g. the inclusion and exclusion criteria).
         * [supporting study context](supporting_study_context.md) - A term or terms describing the experimental setting/context in which evidence supporting the Association was  generated ('context' may be defined by many factors, including taxon, model system (e.g. cell line type), tissue  type, disease, etc.).
         * [supporting study date range](supporting_study_date_range.md) - The date range over which data was collected in a study that provided evidence for an Association.
         * [supporting study method description](supporting_study_method_description.md) - A uri or curie pointing to information about the methodology used to generate data supporting an Association.
         * [supporting study method type](supporting_study_method_type.md) - A type of method that was applied in a study used to generate the information used as evidence (e.g. a type of  experimental assay, or statistical calculation, or computational analysis).
         * [supporting study size](supporting_study_size.md) - The sample size used in a study that provided evidence for the association (e.g. 'n' of a cohort for a  clinical study).
     * [supporting text](supporting_text.md) - The segment of text from a document that supports the mined assertion.
     * [supporting text section type](supporting_text_section_type.md) - The section of the supporting text of a Text Mining Result within the supporting document. This is in the form of the name of the document section (e.g., Abstract, Introduction) that contains the supporting text.
 * [base coordinate](base_coordinate.md) - A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0.
     * [end coordinate](end_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
     * [start coordinate](start_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1).
 * [bonferonni adjusted p value](bonferonni_adjusted_p_value.md) - The Bonferroni correction is an adjustment made to P values when several dependent or independent  statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni  correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and  capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality  (P<. 05), unless P<.
 * [catalyst qualifier](catalyst_qualifier.md) - a qualifier that connects an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
 * [causal mechanism qualifier](causal_mechanism_qualifier.md) - A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
 * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
 * [clinical modifier qualifier](clinical_modifier_qualifier.md) - the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.
 * [concept count object](concept_count_object.md) - The number of instances in a dataset/cohort whose records contain the concept in the object slot of an association.
 * [concept count subject](concept_count_subject.md) - The number of instances in a dataset/cohort whose records contain the concept in the subject slot of an association.
 * [concept pair count](concept_pair_count.md) - The number of instances in a dataset/cohort whose records contain both the subject and object concept of an association.
 * [context qualifier](context_qualifier.md) - Restricts the setting/context/location where the core concept (or qualified core concept) resides or occurs.
     * [object context qualifier](object_context_qualifier.md)
     * [subject context qualifier](subject_context_qualifier.md)
 * [dataset count](dataset_count.md) - The total number of instances (e.g., number of patients, number of rows, etc) in a dataset/cohort.
     * [total sample size](total_sample_size.md) - The total number of patients or participants within a sample population.
 * [derivative qualifier](derivative_qualifier.md) - A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’.
     * [object derivative qualifier](object_derivative_qualifier.md)
     * [subject derivative qualifier](subject_derivative_qualifier.md)
 * [direction qualifier](direction_qualifier.md) - Composes with the core concept (+ aspect if provided) to describe a change in its direction or degree.
     * [object direction qualifier](object_direction_qualifier.md)
     * [subject direction qualifier](subject_direction_qualifier.md)
 * [end coordinate](end_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
 * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
 * [evidence count](evidence_count.md) - The number of evidence instances that are connected to an association.
 * [expected count](expected_count.md) - The expected (calculated) number of instances in a dataset/cohort whose records contain both the subject and  object concept of an association if the subject and object concepts are independent.
 * [expression site](expression_site.md) - location in which gene or protein expression takes place. May be cell, tissue, or organ.
 * [extraction confidence score](extraction_confidence_score.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
 * [FDA adverse event level](FDA_adverse_event_level.md)
 * [FDA approval status](FDA_approval_status.md)
 * [form or variant qualifier](form_or_variant_qualifier.md) - A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’.
     * [object form or variant qualifier](object_form_or_variant_qualifier.md)
     * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)
 * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
 * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
 * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
 * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
 * [has supporting study result](has_supporting_study_result.md) - connects an association to an instance of supporting study result
 * [interacting molecules category](interacting_molecules_category.md)
 * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge.
     * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
     * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
 * [knowledge source](knowledge_source.md) - An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
     * [aggregator knowledge source](aggregator_knowledge_source.md) - An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
     * [primary knowledge source](primary_knowledge_source.md) - The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.
 * [ln ratio](ln_ratio.md) - the natural log of the ratio of co-occurrence to expected
 * [ln ratio confidence interval](ln_ratio_confidence_interval.md) - The 99% confidence interval for the ln_ratio calculation (i.e. the range of values within which the true value has a 99% chance of falling)
 * [log odds ratio](log_odds_ratio.md) - The logarithm of the odds ratio, or the ratio of the odds of event Y occurring in an exposed group versus the  odds of event Y occurring in a non-exposed group.
 * [log odds ration 95 ci](log_odds_ration_95_ci.md) - The ninety-five percent confidence range in which the true log odds ratio for the sample population falls.
 * [logical interpretation](logical_interpretation.md)
 * [mechanism of action](mechanism_of_action.md) - a boolean flag to indicate if the edge is part of a path or subgraph of a knowledge graph that constitutes the mechanism of action for a result.
 * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
 * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
 * [object aspect qualifier](object_aspect_qualifier.md)
 * [object category](object_category.md) - Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [object category closure](object_category_closure.md) - Used to hold the object category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [object closure](object_closure.md) - Used to hold the object closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [object context qualifier](object_context_qualifier.md)
 * [object derivative qualifier](object_derivative_qualifier.md)
 * [object direction qualifier](object_direction_qualifier.md)
 * [object form or variant qualifier](object_form_or_variant_qualifier.md)
 * [object label closure](object_label_closure.md) - Used to hold the object label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [object location in text](object_location_in_text.md) - Character offsets for the text span(s) in the supporting text corresponding to the object concept of the extracted assertion
 * [object namespace](object_namespace.md) - Used to hold the object namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [object part qualifier](object_part_qualifier.md)
 * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
 * [original object](original_object.md) - used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
 * [original predicate](original_predicate.md) - used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.
 * [original subject](original_subject.md) - used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
 * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
     * [adjusted p value](adjusted_p_value.md) - The adjusted p-value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct, adjusted for multiple comparisons.   P is always italicized and capitalized. The actual P value* should be expressed (P=. 04)  rather than expressing a statement of inequality (P<. 05), unless P<.
         * [bonferonni adjusted p value](bonferonni_adjusted_p_value.md) - The Bonferroni correction is an adjustment made to P values when several dependent or independent  statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni  correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and  capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality  (P<. 05), unless P<.
 * [part qualifier](part_qualifier.md) - defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it, e.g. 'ESR1 transcript' q: polyA tail).
     * [object part qualifier](object_part_qualifier.md)
     * [subject part qualifier](subject_part_qualifier.md)
 * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
 * [phenotypic state](phenotypic_state.md) - in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.
 * [population context qualifier](population_context_qualifier.md) - a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
 * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
 * [primary knowledge source](primary_knowledge_source.md) - The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.
 * [publications](publications.md) - One or more publications that report the statement expressed in an  Association, or provide information used as evidence supporting this statement.
 * [qualified predicate](qualified_predicate.md) - Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
 * [qualifier](qualifier.md) - grouping slot for all qualifiers on an edge.  useful for testing compliance with association classes
     * [aspect qualifier](aspect_qualifier.md) - Composes with the core concept to describe new concepts of a different ontological type. e.g. a process in which the core concept participates, a function/activity/role held by the core concept, or a characteristic/quality that inheres in the core concept.  The purpose of the aspect slot is to indicate what aspect is being affected in an  'affects' association.
         * [object aspect qualifier](object_aspect_qualifier.md)
         * [subject aspect qualifier](subject_aspect_qualifier.md)
     * [context qualifier](context_qualifier.md) - Restricts the setting/context/location where the core concept (or qualified core concept) resides or occurs.
         * [object context qualifier](object_context_qualifier.md)
         * [subject context qualifier](subject_context_qualifier.md)
     * [derivative qualifier](derivative_qualifier.md) - A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’.
         * [object derivative qualifier](object_derivative_qualifier.md)
         * [subject derivative qualifier](subject_derivative_qualifier.md)
     * [direction qualifier](direction_qualifier.md) - Composes with the core concept (+ aspect if provided) to describe a change in its direction or degree.
         * [object direction qualifier](object_direction_qualifier.md)
         * [subject direction qualifier](subject_direction_qualifier.md)
     * [form or variant qualifier](form_or_variant_qualifier.md) - A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’.
         * [object form or variant qualifier](object_form_or_variant_qualifier.md)
         * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)
     * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * [part qualifier](part_qualifier.md) - defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it, e.g. 'ESR1 transcript' q: polyA tail).
         * [object part qualifier](object_part_qualifier.md)
         * [subject part qualifier](subject_part_qualifier.md)
     * [population context qualifier](population_context_qualifier.md) - a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
     * [qualified predicate](qualified_predicate.md) - Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
     * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * [statement qualifier](statement_qualifier.md)
         * [anatomical context qualifier](anatomical_context_qualifier.md) - A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).
         * [causal mechanism qualifier](causal_mechanism_qualifier.md) - A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
         * [species context qualifier](species_context_qualifier.md) - A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
     * [temporal context qualifier](temporal_context_qualifier.md) - a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier.
         * [temporal interval qualifier](temporal_interval_qualifier.md) - a constraint of a time interval placed upon the truth value of an association.
 * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
 * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
 * [reaction balanced](reaction_balanced.md)
 * [reaction direction](reaction_direction.md) - the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)
 * [reaction side](reaction_side.md) - the side of a reaction being modeled (ie: left or right)
 * [relative frequency object](relative_frequency_object.md) - The frequency at which subject and object concepts co-occur in  records within a dataset/cohort, relative to the frequency at which the object concept appears in these same records.
 * [relative frequency object confidence interval](relative_frequency_object_confidence_interval.md) - The 99% confidence interval for the relative_frequency_object calculation (i.e. the range of values within which the true value has a 99% chance of falling)
 * [relative frequency subject](relative_frequency_subject.md) - The frequency at which subject and object concepts co-occur in  records within a dataset/cohort, relative to the frequency at which the subject concept appears in these same records.
 * [relative frequency subject confidence interval](relative_frequency_subject_confidence_interval.md) - The 99% confidence interval for the relative_frequency_subject calculation (i.e. the range of values within which the true value has a 99% chance of falling)
 * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a genome sequence localization edge. These edges connect a nucleic acid entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
     * [base coordinate](base_coordinate.md) - A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0.
         * [end coordinate](end_coordinate.md) - The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
         * [start coordinate](start_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1).
     * [genome build](genome_build.md) - The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
     * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge.
         * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
         * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
     * [phase](phase.md) - The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
     * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
 * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
 * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
 * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
 * [species context qualifier](species_context_qualifier.md) - A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
 * [stage qualifier](stage_qualifier.md) - stage during which gene or protein expression of takes place.
 * [start coordinate](start_coordinate.md) - The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1).
 * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
 * [statement qualifier](statement_qualifier.md)
     * [anatomical context qualifier](anatomical_context_qualifier.md) - A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).
     * [causal mechanism qualifier](causal_mechanism_qualifier.md) - A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
     * [species context qualifier](species_context_qualifier.md) - A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
 * [stoichiometry](stoichiometry.md) - the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.
 * [strand](strand.md) - The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
 * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
 * [subject aspect qualifier](subject_aspect_qualifier.md)
 * [subject category](subject_category.md) - Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [subject category closure](subject_category_closure.md) - Used to hold the subject category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [subject closure](subject_closure.md) - Used to hold the subject closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [subject context qualifier](subject_context_qualifier.md)
 * [subject derivative qualifier](subject_derivative_qualifier.md)
 * [subject direction qualifier](subject_direction_qualifier.md)
 * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)
 * [subject label closure](subject_label_closure.md) - Used to hold the subject label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [subject location in text](subject_location_in_text.md) - Character offsets for the text span(s) in the supporting text corresponding to the subject concept of the extracted assertion.
 * [subject namespace](subject_namespace.md) - Used to hold the subject namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
 * [subject part qualifier](subject_part_qualifier.md)
 * [supporting data set](supporting_data_set.md) - A set of data used as evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference over the retrieved data).
 * [supporting data source](supporting_data_source.md) - An Information Resource from which data was retrieved and subsequently used as evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference over the retrieved data).
 * [supporting document type](supporting_document_type.md) - The document type (e.g., Journal Article, Case Study, Preprint) for the supporting document used in a Text Mining Result.
 * [supporting document year](supporting_document_year.md) - The document year (typically the publication year) for the supporting document used in a Text Mining Result.
 * [supporting documents](supporting_documents.md) - One or more referenceable documents that report the statement expressed in an Association, or provide  information used as evidence supporting this statement.
 * [supporting study cohort](supporting_study_cohort.md) - A description of a study population/cohort that was interrogated to provide evidence for the association  (e.g. the inclusion and exclusion criteria).
 * [supporting study context](supporting_study_context.md) - A term or terms describing the experimental setting/context in which evidence supporting the Association was  generated ('context' may be defined by many factors, including taxon, model system (e.g. cell line type), tissue  type, disease, etc.).
 * [supporting study date range](supporting_study_date_range.md) - The date range over which data was collected in a study that provided evidence for an Association.
 * [supporting study metadata](supporting_study_metadata.md) - Information about a study used to generate information used as evidence to support the knowledge expressed in an  Association. In practice, data creators should use one of the more specific subtypes of this property.
     * [supporting study cohort](supporting_study_cohort.md) - A description of a study population/cohort that was interrogated to provide evidence for the association  (e.g. the inclusion and exclusion criteria).
     * [supporting study context](supporting_study_context.md) - A term or terms describing the experimental setting/context in which evidence supporting the Association was  generated ('context' may be defined by many factors, including taxon, model system (e.g. cell line type), tissue  type, disease, etc.).
     * [supporting study date range](supporting_study_date_range.md) - The date range over which data was collected in a study that provided evidence for an Association.
     * [supporting study method description](supporting_study_method_description.md) - A uri or curie pointing to information about the methodology used to generate data supporting an Association.
     * [supporting study method type](supporting_study_method_type.md) - A type of method that was applied in a study used to generate the information used as evidence (e.g. a type of  experimental assay, or statistical calculation, or computational analysis).
     * [supporting study size](supporting_study_size.md) - The sample size used in a study that provided evidence for the association (e.g. 'n' of a cohort for a  clinical study).
 * [supporting study method description](supporting_study_method_description.md) - A uri or curie pointing to information about the methodology used to generate data supporting an Association.
 * [supporting study method type](supporting_study_method_type.md) - A type of method that was applied in a study used to generate the information used as evidence (e.g. a type of  experimental assay, or statistical calculation, or computational analysis).
 * [supporting study size](supporting_study_size.md) - The sample size used in a study that provided evidence for the association (e.g. 'n' of a cohort for a  clinical study).
 * [supporting text](supporting_text.md) - The segment of text from a document that supports the mined assertion.
 * [supporting text section type](supporting_text_section_type.md) - The section of the supporting text of a Text Mining Result within the supporting document. This is in the form of the name of the document section (e.g., Abstract, Introduction) that contains the supporting text.
 * [temporal context qualifier](temporal_context_qualifier.md) - a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier.
     * [temporal interval qualifier](temporal_interval_qualifier.md) - a constraint of a time interval placed upon the truth value of an association.
 * [temporal interval qualifier](temporal_interval_qualifier.md) - a constraint of a time interval placed upon the truth value of an association.
 * [total sample size](total_sample_size.md) - The total number of patients or participants within a sample population.

### Slot Mixins

 * [biological role mixin](biological_role_mixin.md) - A role played by the chemical entity or part thereof within a biological context.
 * [chemical role mixin](chemical_role_mixin.md) - A role played by the chemical entity or part thereof within a chemical context.
 * [decreases amount or activity of](decreases_amount_or_activity_of.md) - A grouping mixin to help with searching for all the predicates that decrease the amount or activity of the object.
 * [increases amount or activity of](increases_amount_or_activity_of.md) - A grouping mixin to help with searching for all the predicates that increase the amount or activity of the object.
 * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
     * [genetically interacts with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
         * [gene_fusion_with](gene_fusion_with.md) - holds between two independent genes that have fused through  translocation, interstitial deletion, or chromosomal inversion to  form a new, hybrid gene. Fusion genes are often implicated in various neoplasms and cancers.
         * [genetic_neighborhood_of](genetic_neighborhood_of.md) - holds between two genes located nearby one another on a chromosome. 
     * [physically interacts with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction.  does not imply a causal relationship.
         * [directly physically interacts with](directly_physically_interacts_with.md) - A causal mechanism mediated by a direct contact between the effector and target entities (this contact may  be weak or strong, transient or stable).
             * [binds](binds.md) - A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity,  which form a stable physical interaction.
         * [indirectly physically interacts with](indirectly_physically_interacts_with.md)

### Other Slots

 * [broad matches](broad_matches.md) - A list of terms from different schemas or terminology systems that have a broader meaning. Such terms often describe a more general concept from different ontological perspectives.
 * [description](description.md) - a human-readable description of an entity
 * [drug regulatory status world wide](drug_regulatory_status_world_wide.md) - An agglomeration of drug regulatory status worldwide. Not specific to FDA.
 * [exact matches](exact_matches.md) - A list of terms from different schemas or terminology systems that have an identical meaning. Such terms often describe the same concept from different ontological perspectives.
 * [has attribute](has_attribute.md) - connects any entity to an attribute
 * [has attribute type](has_attribute_type.md) - connects an attribute to a class that describes it
 * [has numeric value](has_numeric_value.md) - connects a quantity value to a number
 * [has qualitative value](has_qualitative_value.md) - connects an attribute to a value
 * [has quantitative value](has_quantitative_value.md) - connects an attribute to a value
 * [has unit](has_unit.md) - connects a quantity value to a unit
 * [highest FDA approval status](highest_FDA_approval_status.md) - Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'
 * [id](id.md) - A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
 * [iri](iri.md) - An IRI for an entity. This is determined by the id using expansion rules.
 * [mapped predicate](mapped_predicate.md) - The predicate that is being replaced by the fully qualified representation of predicate + subject and object  qualifiers.  Only to be used in test data and mapping data to help with the transition to the fully qualified predicate model. Not to be used in knowledge graphs.
 * [name](name.md) - A human-readable name for an attribute or entity.
 * [narrow matches](narrow_matches.md) - A list of terms from different schemas or terminology systems that have a narrower meaning. Such terms often describe a more specific concept from different ontological perspectives.
 * [predicate mappings](predicate_mappings.md) - A collection of relationships that are not used in biolink, but have biolink patterns that can  be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3.
 * [publication type](publication_type.md) - Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
 * [relation](relation.md)
 * [retrieval source ids](retrieval_source_ids.md) - A list of retrieval sources that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
 * [routes of delivery](routes_of_delivery.md) - the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.
 * [support graphs](support_graphs.md) - A list of knowledge graphs that support the existence of this node.
 * [timepoint](timepoint.md) - a point in time
 * [type](type.md)
     * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * [xref](xref.md) - A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.

## Subsets

 * [ModelOrganismDatabase](ModelOrganismDatabase.md) - Subset that is relevant for a typical Model Organism Database (MOD)
 * [Samples](Samples.md) - Sample/biosample datamodel
 * [Testing](Testing.md) - TBD
 * [TranslatorMinimal](TranslatorMinimal.md) - Minimum subset of translator work

## Types


### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
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
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [FrequencyValue](types/FrequencyValue.md)  ([String](types/String.md)) 
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [IriType](types/IriType.md)  ([Uriorcurie](types/Uriorcurie.md))  - An IRI
 * [LabelType](types/LabelType.md)  ([String](types/String.md))  - A string that provides a human-readable name for an entity
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

## Enums

 * [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md)
 * [ChemicalEntityDerivativeEnum](ChemicalEntityDerivativeEnum.md)
 * [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md)
 * [DirectionQualifierEnum](DirectionQualifierEnum.md)
 * [DrugAvailabilityEnum](DrugAvailabilityEnum.md)
 * [DrugDeliveryEnum](DrugDeliveryEnum.md)
 * [DruggableGeneCategoryEnum](DruggableGeneCategoryEnum.md)
 * [FDAApprovalStatusEnum](FDAApprovalStatusEnum.md)
 * [FDAIDAAdverseEventEnum](FDAIDAAdverseEventEnum.md) - please consult with the FDA guidelines as proposed in this document: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=312.32
 * [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md)
 * [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md)
 * [LogicalInterpretationEnum](LogicalInterpretationEnum.md)
 * [PhaseEnum](PhaseEnum.md) - phase
 * [ReactionDirectionEnum](ReactionDirectionEnum.md)
 * [ReactionSideEnum](ReactionSideEnum.md)
 * [ResourceRoleEnum](ResourceRoleEnum.md) - The role played by the information reource in serving as a source for an edge in a TRAPI message. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.  This enumeration is found in Biolink Model, but is repeated here for convenience.
 * [SequenceEnum](SequenceEnum.md) - type of sequence
 * [StrandEnum](StrandEnum.md) - strand
