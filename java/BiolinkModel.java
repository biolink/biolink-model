import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * biolink model
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "ActivityAndBehavior",
    "AnatomicalEntity",
    "AnatomicalEntityToAnatomicalEntityAssociation",
    "AnatomicalEntityToAnatomicalEntityOntogenicAssociation",
    "AnatomicalEntityToAnatomicalEntityPartOfAssociation",
    "Association",
    "Attribute",
    "BiologicalProcess",
    "BiologicalProcessOrActivity",
    "BiologicalSex",
    "Biosample",
    "BiosampleToDiseaseOrPhenotypicFeatureAssociation",
    "Case",
    "CaseToPhenotypicFeatureAssociation",
    "Cell",
    "CellLine",
    "CellLineToDiseaseOrPhenotypicFeatureAssociation",
    "CellularComponent",
    "ChemicalSubstance",
    "ChemicalToDiseaseOrPhenotypicFeatureAssociation",
    "ChemicalToGeneAssociation",
    "ChemicalToPathwayAssociation",
    "ClinicalEntity",
    "ClinicalIntervention",
    "ClinicalModifier",
    "ClinicalTrial",
    "CodingSequence",
    "ConfidenceLevel",
    "Device",
    "Disease",
    "DiseaseOrPhenotypicFeature",
    "DiseaseOrPhenotypicFeatureAssociationToLocationAssociation",
    "DiseaseToPhenotypicFeatureAssociation",
    "Drug",
    "DrugExposure",
    "Environment",
    "EnvironmentToPhenotypicFeatureAssociation",
    "EnvironmentalFeature",
    "EnvironmentalProcess",
    "EvidenceType",
    "Exon",
    "ExonToTranscriptRelationship",
    "FrequencyQualifier",
    "FrequencyQuantifier",
    "FrequencyValue",
    "FunctionalAssociation",
    "Gene",
    "GeneAsAModelOfDiseaseAssociation",
    "GeneFamily",
    "GeneHasVariantThatContributesToDiseaseAssociation",
    "GeneOntologyClass",
    "GeneOrGeneProduct",
    "GeneProduct",
    "GeneRegulatoryRelationship",
    "GeneToDiseaseAssociation",
    "GeneToExpressionSiteAssociation",
    "GeneToGeneHomologyAssociation",
    "GeneToGeneProductRelationship",
    "GeneToGoTermAssociation",
    "GeneToPhenotypicFeatureAssociation",
    "Genome",
    "GenomicEntity",
    "GenomicSequenceLocalization",
    "Genotype",
    "GenotypeToGeneAssociation",
    "GenotypeToGenotypePartAssociation",
    "GenotypeToPhenotypicFeatureAssociation",
    "GenotypeToVariantAssociation",
    "GenotypicSex",
    "GeographicLocation",
    "GeographicLocationAtTime",
    "GrossAnatomicalStructure",
    "Haplotype",
    "IndividualOrganism",
    "LifeStage",
    "MacromolecularComplex",
    "MacromolecularMachine",
    "MacromolecularMachineToBiologicalProcessAssociation",
    "MacromolecularMachineToCellularComponentAssociation",
    "MacromolecularMachineToMolecularActivityAssociation",
    "Metabolite",
    "MicroRNA",
    "MolecularActivity",
    "MolecularEntity",
    "NamedThing",
    "NoncodingRNAProduct",
    "Occurrent",
    "Onset",
    "OntologyClass",
    "OrganismTaxon",
    "PairwiseGeneOrProteinInteractionAssociation",
    "PathognomonicityQuantifier",
    "Pathway",
    "Phenomenon",
    "PhenotypicFeature",
    "PhenotypicSex",
    "PhysiologicalProcess",
    "PlanetaryEntity",
    "PopulationOfIndividualOrganisms",
    "PopulationToPopulationAssociation",
    "Procedure",
    "Protein",
    "ProteinIsoform",
    "Provider",
    "Publication",
    "RNAProduct",
    "RNAProductIsoform",
    "RelationshipType",
    "SenstivityQuantifier",
    "SequenceFeatureRelationship",
    "SequenceVariant",
    "SeverityValue",
    "SpecificityQuantifier",
    "Transcript",
    "TranscriptToGeneRelationship",
    "Treatment",
    "VariantToDiseaseAssociation",
    "VariantToPhenotypicFeatureAssociation",
    "VariantToPopulationAssociation",
    "Zygosity"
})
public class BiolinkModel {

    /**
     * ActivityAndBehavior
     * <p>
     * Activity or behavior of any independent integral living, organization or mechanical actor in the world
     * 
     */
    @JsonProperty("ActivityAndBehavior")
    @JsonPropertyDescription("Activity or behavior of any independent integral living, organization or mechanical actor in the world")
    private ActivityAndBehavior activityAndBehavior;
    /**
     * AnatomicalEntity
     * <p>
     * A subcellular location, cell type or gross anatomical part
     * 
     */
    @JsonProperty("AnatomicalEntity")
    @JsonPropertyDescription("A subcellular location, cell type or gross anatomical part")
    private AnatomicalEntity anatomicalEntity;
    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    @JsonPropertyDescription("")
    private AnatomicalEntityToAnatomicalEntityAssociation anatomicalEntityToAnatomicalEntityAssociation;
    /**
     * AnatomicalEntityToAnatomicalEntityOntogenicAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityOntogenicAssociation")
    @JsonPropertyDescription("A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship")
    private AnatomicalEntityToAnatomicalEntityOntogenicAssociation anatomicalEntityToAnatomicalEntityOntogenicAssociation;
    /**
     * AnatomicalEntityToAnatomicalEntityPartOfAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityPartOfAssociation")
    @JsonPropertyDescription("A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms")
    private AnatomicalEntityToAnatomicalEntityPartOfAssociation anatomicalEntityToAnatomicalEntityPartOfAssociation;
    /**
     * Association
     * <p>
     * A typed association between two entities, supported by evidence
     * 
     */
    @JsonProperty("Association")
    @JsonPropertyDescription("A typed association between two entities, supported by evidence")
    private Association association;
    /**
     * Attribute
     * <p>
     * A property or characteristic of an entity
     * 
     */
    @JsonProperty("Attribute")
    @JsonPropertyDescription("A property or characteristic of an entity")
    private Attribute attribute;
    /**
     * BiologicalProcess
     * <p>
     * One or more causally connected executions of molecular functions
     * 
     */
    @JsonProperty("BiologicalProcess")
    @JsonPropertyDescription("One or more causally connected executions of molecular functions")
    private BiologicalProcess biologicalProcess;
    /**
     * BiologicalProcessOrActivity
     * <p>
     * Either an individual molecular activity, or a collection of causally connected molecular activities
     * 
     */
    @JsonProperty("BiologicalProcessOrActivity")
    @JsonPropertyDescription("Either an individual molecular activity, or a collection of causally connected molecular activities")
    private BiologicalProcessOrActivity biologicalProcessOrActivity;
    /**
     * BiologicalSex
     * <p>
     * 
     * 
     */
    @JsonProperty("BiologicalSex")
    @JsonPropertyDescription("")
    private BiologicalSex biologicalSex;
    /**
     * Biosample
     * <p>
     * 
     * 
     */
    @JsonProperty("Biosample")
    @JsonPropertyDescription("")
    private Biosample biosample;
    /**
     * BiosampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a biosample and a disease or phenotype
     *   definitional: true
     * 
     */
    @JsonProperty("BiosampleToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a biosample and a disease or phenotype\n  definitional: true")
    private BiosampleToDiseaseOrPhenotypicFeatureAssociation biosampleToDiseaseOrPhenotypicFeatureAssociation;
    /**
     * Case
     * <p>
     * An individual organism that has a patient role in some clinical context.
     * 
     */
    @JsonProperty("Case")
    @JsonPropertyDescription("An individual organism that has a patient role in some clinical context.")
    private Case _case;
    /**
     * CaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
     * 
     */
    @JsonProperty("CaseToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype")
    private CaseToPhenotypicFeatureAssociation caseToPhenotypicFeatureAssociation;
    /**
     * Cell
     * <p>
     * 
     * 
     */
    @JsonProperty("Cell")
    @JsonPropertyDescription("")
    private Cell cell;
    /**
     * CellLine
     * <p>
     * 
     * 
     */
    @JsonProperty("CellLine")
    @JsonPropertyDescription("")
    private CellLine cellLine;
    /**
     * CellLineToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
     * 
     */
    @JsonProperty("CellLineToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype")
    private CellLineToDiseaseOrPhenotypicFeatureAssociation cellLineToDiseaseOrPhenotypicFeatureAssociation;
    /**
     * CellularComponent
     * <p>
     * A location in or around a cell
     * 
     */
    @JsonProperty("CellularComponent")
    @JsonPropertyDescription("A location in or around a cell")
    private CellularComponent cellularComponent;
    /**
     * ChemicalSubstance
     * <p>
     * May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
     * 
     */
    @JsonProperty("ChemicalSubstance")
    @JsonPropertyDescription("May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part")
    private ChemicalSubstance chemicalSubstance;
    /**
     * ChemicalToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
     * 
     */
    @JsonProperty("ChemicalToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype")
    private ChemicalToDiseaseOrPhenotypicFeatureAssociation chemicalToDiseaseOrPhenotypicFeatureAssociation;
    /**
     * ChemicalToGeneAssociation
     * <p>
     * An interaction between a chemical entity and a gene or gene product
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    @JsonPropertyDescription("An interaction between a chemical entity and a gene or gene product")
    private ChemicalToGeneAssociation chemicalToGeneAssociation;
    /**
     * ChemicalToPathwayAssociation
     * <p>
     * An interaction between a chemical entity and a biological process or pathway
     * 
     */
    @JsonProperty("ChemicalToPathwayAssociation")
    @JsonPropertyDescription("An interaction between a chemical entity and a biological process or pathway")
    private ChemicalToPathwayAssociation chemicalToPathwayAssociation;
    /**
     * ClinicalEntity
     * <p>
     * Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
     * 
     */
    @JsonProperty("ClinicalEntity")
    @JsonPropertyDescription("Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities")
    private ClinicalEntity clinicalEntity;
    /**
     * ClinicalIntervention
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalIntervention")
    @JsonPropertyDescription("")
    private ClinicalIntervention clinicalIntervention;
    /**
     * ClinicalModifier
     * <p>
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("ClinicalModifier")
    @JsonPropertyDescription("Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects")
    private ClinicalModifier clinicalModifier;
    /**
     * ClinicalTrial
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalTrial")
    @JsonPropertyDescription("")
    private ClinicalTrial clinicalTrial;
    /**
     * CodingSequence
     * <p>
     * 
     * 
     */
    @JsonProperty("CodingSequence")
    @JsonPropertyDescription("")
    private CodingSequence codingSequence;
    /**
     * ConfidenceLevel
     * <p>
     * Level of confidence in a statement
     * 
     */
    @JsonProperty("ConfidenceLevel")
    @JsonPropertyDescription("Level of confidence in a statement")
    private ConfidenceLevel confidenceLevel;
    /**
     * Device
     * <p>
     * A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
     * 
     */
    @JsonProperty("Device")
    @JsonPropertyDescription("A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment")
    private Device device;
    /**
     * Disease
     * <p>
     * 
     * 
     */
    @JsonProperty("Disease")
    @JsonPropertyDescription("")
    private Disease disease;
    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    @JsonPropertyDescription("Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.")
    private DiseaseOrPhenotypicFeature diseaseOrPhenotypicFeature;
    /**
     * DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
     * <p>
     * An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeatureAssociationToLocationAssociation")
    @JsonPropertyDescription("An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.")
    private DiseaseOrPhenotypicFeatureAssociationToLocationAssociation diseaseOrPhenotypicFeatureAssociationToLocationAssociation;
    /**
     * DiseaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way")
    private DiseaseToPhenotypicFeatureAssociation diseaseToPhenotypicFeatureAssociation;
    /**
     * Drug
     * <p>
     * A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
     * 
     */
    @JsonProperty("Drug")
    @JsonPropertyDescription("A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease")
    private Drug drug;
    /**
     * DrugExposure
     * <p>
     * A drug exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("DrugExposure")
    @JsonPropertyDescription("A drug exposure is an intake of a particular chemical substance")
    private DrugExposure drugExposure;
    /**
     * Environment
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("Environment")
    @JsonPropertyDescription("A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes")
    private Environment environment;
    /**
     * EnvironmentToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("EnvironmentToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype")
    private EnvironmentToPhenotypicFeatureAssociation environmentToPhenotypicFeatureAssociation;
    /**
     * EnvironmentalFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    @JsonPropertyDescription("")
    private EnvironmentalFeature environmentalFeature;
    /**
     * EnvironmentalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalProcess")
    @JsonPropertyDescription("")
    private EnvironmentalProcess environmentalProcess;
    /**
     * EvidenceType
     * <p>
     * Class of evidence that supports an association
     * 
     */
    @JsonProperty("EvidenceType")
    @JsonPropertyDescription("Class of evidence that supports an association")
    private EvidenceType evidenceType;
    /**
     * Exon
     * <p>
     * A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
     * 
     */
    @JsonProperty("Exon")
    @JsonPropertyDescription("A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing")
    private Exon exon;
    /**
     * ExonToTranscriptRelationship
     * <p>
     * A transcript is formed from multiple exons
     * 
     */
    @JsonProperty("ExonToTranscriptRelationship")
    @JsonPropertyDescription("A transcript is formed from multiple exons")
    private ExonToTranscriptRelationship exonToTranscriptRelationship;
    /**
     * FrequencyQualifier
     * <p>
     * Qualifier for freqency type associations
     * 
     */
    @JsonProperty("FrequencyQualifier")
    @JsonPropertyDescription("Qualifier for freqency type associations")
    private FrequencyQualifier frequencyQualifier;
    /**
     * FrequencyQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("FrequencyQuantifier")
    @JsonPropertyDescription("")
    private FrequencyQuantifier frequencyQuantifier;
    /**
     * FrequencyValue
     * <p>
     * describes the frequency of occurrence of an event or condition
     * 
     */
    @JsonProperty("FrequencyValue")
    @JsonPropertyDescription("describes the frequency of occurrence of an event or condition")
    private FrequencyValue frequencyValue;
    /**
     * FunctionalAssociation
     * <p>
     * An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
     * 
     */
    @JsonProperty("FunctionalAssociation")
    @JsonPropertyDescription("An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed")
    private FunctionalAssociation functionalAssociation;
    /**
     * Gene
     * <p>
     * 
     * 
     */
    @JsonProperty("Gene")
    @JsonPropertyDescription("")
    private Gene gene;
    /**
     * GeneAsAModelOfDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneAsAModelOfDiseaseAssociation")
    @JsonPropertyDescription("")
    private GeneAsAModelOfDiseaseAssociation geneAsAModelOfDiseaseAssociation;
    /**
     * GeneFamily
     * <p>
     * any grouping of multiple genes or gene products related by common descent
     * 
     */
    @JsonProperty("GeneFamily")
    @JsonPropertyDescription("any grouping of multiple genes or gene products related by common descent")
    private GeneFamily geneFamily;
    /**
     * GeneHasVariantThatContributesToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneHasVariantThatContributesToDiseaseAssociation")
    @JsonPropertyDescription("")
    private GeneHasVariantThatContributesToDiseaseAssociation geneHasVariantThatContributesToDiseaseAssociation;
    /**
     * GeneOntologyClass
     * <p>
     * an ontology class that describes a functional aspect of a gene, gene prodoct or complex
     * 
     */
    @JsonProperty("GeneOntologyClass")
    @JsonPropertyDescription("an ontology class that describes a functional aspect of a gene, gene prodoct or complex")
    private GeneOntologyClass geneOntologyClass;
    /**
     * GeneOrGeneProduct
     * <p>
     * a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
     * 
     */
    @JsonProperty("GeneOrGeneProduct")
    @JsonPropertyDescription("a union of genes or gene products. Frequently an identifier for one will be used as proxy for another")
    private GeneOrGeneProduct geneOrGeneProduct;
    /**
     * GeneProduct
     * <p>
     * The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
     * 
     */
    @JsonProperty("GeneProduct")
    @JsonPropertyDescription("The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules")
    private GeneProduct geneProduct;
    /**
     * GeneRegulatoryRelationship
     * <p>
     * A regulatory relationship between two genes
     * 
     */
    @JsonProperty("GeneRegulatoryRelationship")
    @JsonPropertyDescription("A regulatory relationship between two genes")
    private GeneRegulatoryRelationship geneRegulatoryRelationship;
    /**
     * GeneToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToDiseaseAssociation")
    @JsonPropertyDescription("")
    private GeneToDiseaseAssociation geneToDiseaseAssociation;
    /**
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info.
     * 
     */
    @JsonProperty("GeneToExpressionSiteAssociation")
    @JsonPropertyDescription("An association between a gene and an expression site, possibly qualified by stage/timing info.")
    private GeneToExpressionSiteAssociation geneToExpressionSiteAssociation;
    /**
     * GeneToGeneHomologyAssociation
     * <p>
     * A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
     * 
     */
    @JsonProperty("GeneToGeneHomologyAssociation")
    @JsonPropertyDescription("A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)")
    private GeneToGeneHomologyAssociation geneToGeneHomologyAssociation;
    /**
     * GeneToGeneProductRelationship
     * <p>
     * A gene is transcribed and potentially translated to a gene product
     * 
     */
    @JsonProperty("GeneToGeneProductRelationship")
    @JsonPropertyDescription("A gene is transcribed and potentially translated to a gene product")
    private GeneToGeneProductRelationship geneToGeneProductRelationship;
    /**
     * GeneToGoTermAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    @JsonPropertyDescription("")
    private GeneToGoTermAssociation geneToGoTermAssociation;
    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("")
    private GeneToPhenotypicFeatureAssociation geneToPhenotypicFeatureAssociation;
    /**
     * Genome
     * <p>
     * A genome is the sum of genetic material within a cell or virion.
     * 
     */
    @JsonProperty("Genome")
    @JsonPropertyDescription("A genome is the sum of genetic material within a cell or virion.")
    private Genome genome;
    /**
     * GenomicEntity
     * <p>
     * an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
     * 
     */
    @JsonProperty("GenomicEntity")
    @JsonPropertyDescription("an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)")
    private GenomicEntity genomicEntity;
    /**
     * GenomicSequenceLocalization
     * <p>
     * A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
     * 
     */
    @JsonProperty("GenomicSequenceLocalization")
    @JsonPropertyDescription("A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig")
    private GenomicSequenceLocalization genomicSequenceLocalization;
    /**
     * Genotype
     * <p>
     * An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
     * 
     */
    @JsonProperty("Genotype")
    @JsonPropertyDescription("An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background")
    private Genotype genotype;
    /**
     * GenotypeToGeneAssociation
     * <p>
     * Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
     * 
     */
    @JsonProperty("GenotypeToGeneAssociation")
    @JsonPropertyDescription("Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality")
    private GenotypeToGeneAssociation genotypeToGeneAssociation;
    /**
     * GenotypeToGenotypePartAssociation
     * <p>
     * Any association between one genotype and a genotypic entity that is a sub-component of it
     * 
     */
    @JsonProperty("GenotypeToGenotypePartAssociation")
    @JsonPropertyDescription("Any association between one genotype and a genotypic entity that is a sub-component of it")
    private GenotypeToGenotypePartAssociation genotypeToGenotypePartAssociation;
    /**
     * GenotypeToPhenotypicFeatureAssociation
     * <p>
     * Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment")
    private GenotypeToPhenotypicFeatureAssociation genotypeToPhenotypicFeatureAssociation;
    /**
     * GenotypeToVariantAssociation
     * <p>
     * Any association between a genotype and a sequence variant.
     * 
     */
    @JsonProperty("GenotypeToVariantAssociation")
    @JsonPropertyDescription("Any association between a genotype and a sequence variant.")
    private GenotypeToVariantAssociation genotypeToVariantAssociation;
    /**
     * GenotypicSex
     * <p>
     * An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
     * 
     */
    @JsonProperty("GenotypicSex")
    @JsonPropertyDescription("An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.")
    private GenotypicSex genotypicSex;
    /**
     * GeographicLocation
     * <p>
     * a location that can be described in lat/long coordinates
     * 
     */
    @JsonProperty("GeographicLocation")
    @JsonPropertyDescription("a location that can be described in lat/long coordinates")
    private GeographicLocation geographicLocation;
    /**
     * GeographicLocationAtTime
     * <p>
     * a location that can be described in lat/long coordinates, for a particular time
     * 
     */
    @JsonProperty("GeographicLocationAtTime")
    @JsonPropertyDescription("a location that can be described in lat/long coordinates, for a particular time")
    private GeographicLocationAtTime geographicLocationAtTime;
    /**
     * GrossAnatomicalStructure
     * <p>
     * 
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    @JsonPropertyDescription("")
    private GrossAnatomicalStructure grossAnatomicalStructure;
    /**
     * Haplotype
     * <p>
     * A set of zero or more Alleles on a single instance of a Sequence[VMC]
     * 
     */
    @JsonProperty("Haplotype")
    @JsonPropertyDescription("A set of zero or more Alleles on a single instance of a Sequence[VMC]")
    private Haplotype haplotype;
    /**
     * IndividualOrganism
     * <p>
     * 
     * 
     */
    @JsonProperty("IndividualOrganism")
    @JsonPropertyDescription("")
    private IndividualOrganism individualOrganism;
    /**
     * LifeStage
     * <p>
     * A stage of development or growth of an organism, including post-natal adult stages
     * 
     */
    @JsonProperty("LifeStage")
    @JsonPropertyDescription("A stage of development or growth of an organism, including post-natal adult stages")
    private LifeStage lifeStage;
    /**
     * MacromolecularComplex
     * <p>
     * 
     * 
     */
    @JsonProperty("MacromolecularComplex")
    @JsonPropertyDescription("")
    private MacromolecularComplex macromolecularComplex;
    /**
     * MacromolecularMachine
     * <p>
     * A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
     * 
     */
    @JsonProperty("MacromolecularMachine")
    @JsonPropertyDescription("A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.")
    private MacromolecularMachine macromolecularMachine;
    /**
     * MacromolecularMachineToBiologicalProcessAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
     * 
     */
    @JsonProperty("MacromolecularMachineToBiologicalProcessAssociation")
    @JsonPropertyDescription("A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it")
    private MacromolecularMachineToBiologicalProcessAssociation macromolecularMachineToBiologicalProcessAssociation;
    /**
     * MacromolecularMachineToCellularComponentAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
     * 
     */
    @JsonProperty("MacromolecularMachineToCellularComponentAssociation")
    @JsonPropertyDescription("A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component")
    private MacromolecularMachineToCellularComponentAssociation macromolecularMachineToCellularComponentAssociation;
    /**
     * MacromolecularMachineToMolecularActivityAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
     * 
     */
    @JsonProperty("MacromolecularMachineToMolecularActivityAssociation")
    @JsonPropertyDescription("A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution")
    private MacromolecularMachineToMolecularActivityAssociation macromolecularMachineToMolecularActivityAssociation;
    /**
     * Metabolite
     * <p>
     * Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
     * 
     */
    @JsonProperty("Metabolite")
    @JsonPropertyDescription("Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.")
    private Metabolite metabolite;
    /**
     * MicroRNA
     * <p>
     * 
     * 
     */
    @JsonProperty("MicroRNA")
    @JsonPropertyDescription("")
    private MicroRNA microRNA;
    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function carried out by a gene product or macromolecular complex.
     * 
     */
    @JsonProperty("MolecularActivity")
    @JsonPropertyDescription("An execution of a molecular function carried out by a gene product or macromolecular complex.")
    private MolecularActivity molecularActivity;
    /**
     * MolecularEntity
     * <p>
     * A gene, gene product, small molecule or macromolecule (including protein complex)
     * 
     */
    @JsonProperty("MolecularEntity")
    @JsonPropertyDescription("A gene, gene product, small molecule or macromolecule (including protein complex)")
    private MolecularEntity molecularEntity;
    /**
     * NamedThing
     * <p>
     * a databased entity or concept/class
     * 
     */
    @JsonProperty("NamedThing")
    @JsonPropertyDescription("a databased entity or concept/class")
    private NamedThing namedThing;
    /**
     * NoncodingRNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("NoncodingRNAProduct")
    @JsonPropertyDescription("")
    private NoncodingRNAProduct noncodingRNAProduct;
    /**
     * Occurrent
     * <p>
     * A processual entity
     * 
     */
    @JsonProperty("Occurrent")
    @JsonPropertyDescription("A processual entity")
    private Occurrent occurrent;
    /**
     * Onset
     * <p>
     * The age group in which manifestations appear
     * 
     */
    @JsonProperty("Onset")
    @JsonPropertyDescription("The age group in which manifestations appear")
    private Onset onset;
    /**
     * OntologyClass
     * <p>
     * a concept or class in an ontology, vocabulary or thesaurus
     * 
     */
    @JsonProperty("OntologyClass")
    @JsonPropertyDescription("a concept or class in an ontology, vocabulary or thesaurus")
    private OntologyClass ontologyClass;
    /**
     * OrganismTaxon
     * <p>
     * 
     * 
     */
    @JsonProperty("OrganismTaxon")
    @JsonPropertyDescription("")
    private OrganismTaxon organismTaxon;
    /**
     * PairwiseGeneOrProteinInteractionAssociation
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneOrProteinInteractionAssociation")
    @JsonPropertyDescription("An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)")
    private PairwiseGeneOrProteinInteractionAssociation pairwiseGeneOrProteinInteractionAssociation;
    /**
     * PathognomonicityQuantifier
     * <p>
     * A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
     * 
     */
    @JsonProperty("PathognomonicityQuantifier")
    @JsonPropertyDescription("A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease")
    private PathognomonicityQuantifier pathognomonicityQuantifier;
    /**
     * Pathway
     * <p>
     * 
     * 
     */
    @JsonProperty("Pathway")
    @JsonPropertyDescription("")
    private Pathway pathway;
    /**
     * Phenomenon
     * <p>
     * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
     * 
     */
    @JsonProperty("Phenomenon")
    @JsonPropertyDescription("a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question")
    private Phenomenon phenomenon;
    /**
     * PhenotypicFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("PhenotypicFeature")
    @JsonPropertyDescription("")
    private PhenotypicFeature phenotypicFeature;
    /**
     * PhenotypicSex
     * <p>
     * An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
     * 
     */
    @JsonProperty("PhenotypicSex")
    @JsonPropertyDescription("An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.")
    private PhenotypicSex phenotypicSex;
    /**
     * PhysiologicalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("PhysiologicalProcess")
    @JsonPropertyDescription("")
    private PhysiologicalProcess physiologicalProcess;
    /**
     * PlanetaryEntity
     * <p>
     * Any entity or process that exists at the level of the whole planet
     * 
     */
    @JsonProperty("PlanetaryEntity")
    @JsonPropertyDescription("Any entity or process that exists at the level of the whole planet")
    private PlanetaryEntity planetaryEntity;
    /**
     * PopulationOfIndividualOrganisms
     * <p>
     * 
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    @JsonPropertyDescription("")
    private PopulationOfIndividualOrganisms populationOfIndividualOrganisms;
    /**
     * PopulationToPopulationAssociation
     * <p>
     * An association between a two populations
     * 
     */
    @JsonProperty("PopulationToPopulationAssociation")
    @JsonPropertyDescription("An association between a two populations")
    private PopulationToPopulationAssociation populationToPopulationAssociation;
    /**
     * Procedure
     * <p>
     * A series of actions conducted in a certain order or manner
     * 
     */
    @JsonProperty("Procedure")
    @JsonPropertyDescription("A series of actions conducted in a certain order or manner")
    private Procedure procedure;
    /**
     * Protein
     * <p>
     * A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
     * 
     */
    @JsonProperty("Protein")
    @JsonPropertyDescription("A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA")
    private Protein protein;
    /**
     * ProteinIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
     * 
     */
    @JsonProperty("ProteinIsoform")
    @JsonPropertyDescription("Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/")
    private ProteinIsoform proteinIsoform;
    /**
     * Provider
     * <p>
     * person, group, organization or project that provides a piece of information
     * 
     */
    @JsonProperty("Provider")
    @JsonPropertyDescription("person, group, organization or project that provides a piece of information")
    private Provider provider;
    /**
     * Publication
     * <p>
     * Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
     * 
     */
    @JsonProperty("Publication")
    @JsonPropertyDescription("Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.")
    private Publication publication;
    /**
     * RNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("RNAProduct")
    @JsonPropertyDescription("")
    private RNAProduct rNAProduct;
    /**
     * RNAProductIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference RNA
     * 
     */
    @JsonProperty("RNAProductIsoform")
    @JsonPropertyDescription("Represents a protein that is a specific isoform of the canonical or reference RNA")
    private RNAProductIsoform rNAProductIsoform;
    /**
     * RelationshipType
     * <p>
     * An OWL property used as an edge label
     * 
     */
    @JsonProperty("RelationshipType")
    @JsonPropertyDescription("An OWL property used as an edge label")
    private RelationshipType relationshipType;
    /**
     * SenstivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SenstivityQuantifier")
    @JsonPropertyDescription("")
    private SenstivityQuantifier senstivityQuantifier;
    /**
     * SequenceFeatureRelationship
     * <p>
     * For example, a particular exon is part of a particular transcript or gene
     * 
     */
    @JsonProperty("SequenceFeatureRelationship")
    @JsonPropertyDescription("For example, a particular exon is part of a particular transcript or gene")
    private SequenceFeatureRelationship sequenceFeatureRelationship;
    /**
     * SequenceVariant
     * <p>
     * An allele that varies in its sequence from what is considered the reference allele at that locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    @JsonPropertyDescription("An allele that varies in its sequence from what is considered the reference allele at that locus.")
    private SequenceVariant sequenceVariant;
    /**
     * SeverityValue
     * <p>
     * describes the severity of a phenotypic feature or disease
     * 
     */
    @JsonProperty("SeverityValue")
    @JsonPropertyDescription("describes the severity of a phenotypic feature or disease")
    private SeverityValue severityValue;
    /**
     * SpecificityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SpecificityQuantifier")
    @JsonPropertyDescription("")
    private SpecificityQuantifier specificityQuantifier;
    /**
     * Transcript
     * <p>
     * An RNA synthesized on a DNA or RNA template by an RNA polymerase
     * 
     */
    @JsonProperty("Transcript")
    @JsonPropertyDescription("An RNA synthesized on a DNA or RNA template by an RNA polymerase")
    private Transcript transcript;
    /**
     * TranscriptToGeneRelationship
     * <p>
     * A gene is a collection of transcripts
     * 
     */
    @JsonProperty("TranscriptToGeneRelationship")
    @JsonPropertyDescription("A gene is a collection of transcripts")
    private TranscriptToGeneRelationship transcriptToGeneRelationship;
    /**
     * Treatment
     * <p>
     * A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
     * 
     */
    @JsonProperty("Treatment")
    @JsonPropertyDescription("A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'")
    private Treatment treatment;
    /**
     * VariantToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToDiseaseAssociation")
    @JsonPropertyDescription("")
    private VariantToDiseaseAssociation variantToDiseaseAssociation;
    /**
     * VariantToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("")
    private VariantToPhenotypicFeatureAssociation variantToPhenotypicFeatureAssociation;
    /**
     * VariantToPopulationAssociation
     * <p>
     * An association between a variant and a population, where the variant has particular frequency in the population
     * 
     */
    @JsonProperty("VariantToPopulationAssociation")
    @JsonPropertyDescription("An association between a variant and a population, where the variant has particular frequency in the population")
    private VariantToPopulationAssociation variantToPopulationAssociation;
    /**
     * Zygosity
     * <p>
     * 
     * 
     */
    @JsonProperty("Zygosity")
    @JsonPropertyDescription("")
    private Zygosity zygosity;

    /**
     * ActivityAndBehavior
     * <p>
     * Activity or behavior of any independent integral living, organization or mechanical actor in the world
     * 
     */
    @JsonProperty("ActivityAndBehavior")
    public ActivityAndBehavior getActivityAndBehavior() {
        return activityAndBehavior;
    }

    /**
     * ActivityAndBehavior
     * <p>
     * Activity or behavior of any independent integral living, organization or mechanical actor in the world
     * 
     */
    @JsonProperty("ActivityAndBehavior")
    public void setActivityAndBehavior(ActivityAndBehavior activityAndBehavior) {
        this.activityAndBehavior = activityAndBehavior;
    }

    /**
     * AnatomicalEntity
     * <p>
     * A subcellular location, cell type or gross anatomical part
     * 
     */
    @JsonProperty("AnatomicalEntity")
    public AnatomicalEntity getAnatomicalEntity() {
        return anatomicalEntity;
    }

    /**
     * AnatomicalEntity
     * <p>
     * A subcellular location, cell type or gross anatomical part
     * 
     */
    @JsonProperty("AnatomicalEntity")
    public void setAnatomicalEntity(AnatomicalEntity anatomicalEntity) {
        this.anatomicalEntity = anatomicalEntity;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    public AnatomicalEntityToAnatomicalEntityAssociation getAnatomicalEntityToAnatomicalEntityAssociation() {
        return anatomicalEntityToAnatomicalEntityAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    public void setAnatomicalEntityToAnatomicalEntityAssociation(AnatomicalEntityToAnatomicalEntityAssociation anatomicalEntityToAnatomicalEntityAssociation) {
        this.anatomicalEntityToAnatomicalEntityAssociation = anatomicalEntityToAnatomicalEntityAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityOntogenicAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityOntogenicAssociation")
    public AnatomicalEntityToAnatomicalEntityOntogenicAssociation getAnatomicalEntityToAnatomicalEntityOntogenicAssociation() {
        return anatomicalEntityToAnatomicalEntityOntogenicAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityOntogenicAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityOntogenicAssociation")
    public void setAnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityOntogenicAssociation anatomicalEntityToAnatomicalEntityOntogenicAssociation) {
        this.anatomicalEntityToAnatomicalEntityOntogenicAssociation = anatomicalEntityToAnatomicalEntityOntogenicAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityPartOfAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityPartOfAssociation")
    public AnatomicalEntityToAnatomicalEntityPartOfAssociation getAnatomicalEntityToAnatomicalEntityPartOfAssociation() {
        return anatomicalEntityToAnatomicalEntityPartOfAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityPartOfAssociation
     * <p>
     * A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityPartOfAssociation")
    public void setAnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityPartOfAssociation anatomicalEntityToAnatomicalEntityPartOfAssociation) {
        this.anatomicalEntityToAnatomicalEntityPartOfAssociation = anatomicalEntityToAnatomicalEntityPartOfAssociation;
    }

    /**
     * Association
     * <p>
     * A typed association between two entities, supported by evidence
     * 
     */
    @JsonProperty("Association")
    public Association getAssociation() {
        return association;
    }

    /**
     * Association
     * <p>
     * A typed association between two entities, supported by evidence
     * 
     */
    @JsonProperty("Association")
    public void setAssociation(Association association) {
        this.association = association;
    }

    /**
     * Attribute
     * <p>
     * A property or characteristic of an entity
     * 
     */
    @JsonProperty("Attribute")
    public Attribute getAttribute() {
        return attribute;
    }

    /**
     * Attribute
     * <p>
     * A property or characteristic of an entity
     * 
     */
    @JsonProperty("Attribute")
    public void setAttribute(Attribute attribute) {
        this.attribute = attribute;
    }

    /**
     * BiologicalProcess
     * <p>
     * One or more causally connected executions of molecular functions
     * 
     */
    @JsonProperty("BiologicalProcess")
    public BiologicalProcess getBiologicalProcess() {
        return biologicalProcess;
    }

    /**
     * BiologicalProcess
     * <p>
     * One or more causally connected executions of molecular functions
     * 
     */
    @JsonProperty("BiologicalProcess")
    public void setBiologicalProcess(BiologicalProcess biologicalProcess) {
        this.biologicalProcess = biologicalProcess;
    }

    /**
     * BiologicalProcessOrActivity
     * <p>
     * Either an individual molecular activity, or a collection of causally connected molecular activities
     * 
     */
    @JsonProperty("BiologicalProcessOrActivity")
    public BiologicalProcessOrActivity getBiologicalProcessOrActivity() {
        return biologicalProcessOrActivity;
    }

    /**
     * BiologicalProcessOrActivity
     * <p>
     * Either an individual molecular activity, or a collection of causally connected molecular activities
     * 
     */
    @JsonProperty("BiologicalProcessOrActivity")
    public void setBiologicalProcessOrActivity(BiologicalProcessOrActivity biologicalProcessOrActivity) {
        this.biologicalProcessOrActivity = biologicalProcessOrActivity;
    }

    /**
     * BiologicalSex
     * <p>
     * 
     * 
     */
    @JsonProperty("BiologicalSex")
    public BiologicalSex getBiologicalSex() {
        return biologicalSex;
    }

    /**
     * BiologicalSex
     * <p>
     * 
     * 
     */
    @JsonProperty("BiologicalSex")
    public void setBiologicalSex(BiologicalSex biologicalSex) {
        this.biologicalSex = biologicalSex;
    }

    /**
     * Biosample
     * <p>
     * 
     * 
     */
    @JsonProperty("Biosample")
    public Biosample getBiosample() {
        return biosample;
    }

    /**
     * Biosample
     * <p>
     * 
     * 
     */
    @JsonProperty("Biosample")
    public void setBiosample(Biosample biosample) {
        this.biosample = biosample;
    }

    /**
     * BiosampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a biosample and a disease or phenotype
     *   definitional: true
     * 
     */
    @JsonProperty("BiosampleToDiseaseOrPhenotypicFeatureAssociation")
    public BiosampleToDiseaseOrPhenotypicFeatureAssociation getBiosampleToDiseaseOrPhenotypicFeatureAssociation() {
        return biosampleToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * BiosampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a biosample and a disease or phenotype
     *   definitional: true
     * 
     */
    @JsonProperty("BiosampleToDiseaseOrPhenotypicFeatureAssociation")
    public void setBiosampleToDiseaseOrPhenotypicFeatureAssociation(BiosampleToDiseaseOrPhenotypicFeatureAssociation biosampleToDiseaseOrPhenotypicFeatureAssociation) {
        this.biosampleToDiseaseOrPhenotypicFeatureAssociation = biosampleToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * Case
     * <p>
     * An individual organism that has a patient role in some clinical context.
     * 
     */
    @JsonProperty("Case")
    public Case getCase() {
        return _case;
    }

    /**
     * Case
     * <p>
     * An individual organism that has a patient role in some clinical context.
     * 
     */
    @JsonProperty("Case")
    public void setCase(Case _case) {
        this._case = _case;
    }

    /**
     * CaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
     * 
     */
    @JsonProperty("CaseToPhenotypicFeatureAssociation")
    public CaseToPhenotypicFeatureAssociation getCaseToPhenotypicFeatureAssociation() {
        return caseToPhenotypicFeatureAssociation;
    }

    /**
     * CaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
     * 
     */
    @JsonProperty("CaseToPhenotypicFeatureAssociation")
    public void setCaseToPhenotypicFeatureAssociation(CaseToPhenotypicFeatureAssociation caseToPhenotypicFeatureAssociation) {
        this.caseToPhenotypicFeatureAssociation = caseToPhenotypicFeatureAssociation;
    }

    /**
     * Cell
     * <p>
     * 
     * 
     */
    @JsonProperty("Cell")
    public Cell getCell() {
        return cell;
    }

    /**
     * Cell
     * <p>
     * 
     * 
     */
    @JsonProperty("Cell")
    public void setCell(Cell cell) {
        this.cell = cell;
    }

    /**
     * CellLine
     * <p>
     * 
     * 
     */
    @JsonProperty("CellLine")
    public CellLine getCellLine() {
        return cellLine;
    }

    /**
     * CellLine
     * <p>
     * 
     * 
     */
    @JsonProperty("CellLine")
    public void setCellLine(CellLine cellLine) {
        this.cellLine = cellLine;
    }

    /**
     * CellLineToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
     * 
     */
    @JsonProperty("CellLineToDiseaseOrPhenotypicFeatureAssociation")
    public CellLineToDiseaseOrPhenotypicFeatureAssociation getCellLineToDiseaseOrPhenotypicFeatureAssociation() {
        return cellLineToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * CellLineToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
     * 
     */
    @JsonProperty("CellLineToDiseaseOrPhenotypicFeatureAssociation")
    public void setCellLineToDiseaseOrPhenotypicFeatureAssociation(CellLineToDiseaseOrPhenotypicFeatureAssociation cellLineToDiseaseOrPhenotypicFeatureAssociation) {
        this.cellLineToDiseaseOrPhenotypicFeatureAssociation = cellLineToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * CellularComponent
     * <p>
     * A location in or around a cell
     * 
     */
    @JsonProperty("CellularComponent")
    public CellularComponent getCellularComponent() {
        return cellularComponent;
    }

    /**
     * CellularComponent
     * <p>
     * A location in or around a cell
     * 
     */
    @JsonProperty("CellularComponent")
    public void setCellularComponent(CellularComponent cellularComponent) {
        this.cellularComponent = cellularComponent;
    }

    /**
     * ChemicalSubstance
     * <p>
     * May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
     * 
     */
    @JsonProperty("ChemicalSubstance")
    public ChemicalSubstance getChemicalSubstance() {
        return chemicalSubstance;
    }

    /**
     * ChemicalSubstance
     * <p>
     * May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
     * 
     */
    @JsonProperty("ChemicalSubstance")
    public void setChemicalSubstance(ChemicalSubstance chemicalSubstance) {
        this.chemicalSubstance = chemicalSubstance;
    }

    /**
     * ChemicalToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
     * 
     */
    @JsonProperty("ChemicalToDiseaseOrPhenotypicFeatureAssociation")
    public ChemicalToDiseaseOrPhenotypicFeatureAssociation getChemicalToDiseaseOrPhenotypicFeatureAssociation() {
        return chemicalToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * ChemicalToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
     * 
     */
    @JsonProperty("ChemicalToDiseaseOrPhenotypicFeatureAssociation")
    public void setChemicalToDiseaseOrPhenotypicFeatureAssociation(ChemicalToDiseaseOrPhenotypicFeatureAssociation chemicalToDiseaseOrPhenotypicFeatureAssociation) {
        this.chemicalToDiseaseOrPhenotypicFeatureAssociation = chemicalToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * ChemicalToGeneAssociation
     * <p>
     * An interaction between a chemical entity and a gene or gene product
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    public ChemicalToGeneAssociation getChemicalToGeneAssociation() {
        return chemicalToGeneAssociation;
    }

    /**
     * ChemicalToGeneAssociation
     * <p>
     * An interaction between a chemical entity and a gene or gene product
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    public void setChemicalToGeneAssociation(ChemicalToGeneAssociation chemicalToGeneAssociation) {
        this.chemicalToGeneAssociation = chemicalToGeneAssociation;
    }

    /**
     * ChemicalToPathwayAssociation
     * <p>
     * An interaction between a chemical entity and a biological process or pathway
     * 
     */
    @JsonProperty("ChemicalToPathwayAssociation")
    public ChemicalToPathwayAssociation getChemicalToPathwayAssociation() {
        return chemicalToPathwayAssociation;
    }

    /**
     * ChemicalToPathwayAssociation
     * <p>
     * An interaction between a chemical entity and a biological process or pathway
     * 
     */
    @JsonProperty("ChemicalToPathwayAssociation")
    public void setChemicalToPathwayAssociation(ChemicalToPathwayAssociation chemicalToPathwayAssociation) {
        this.chemicalToPathwayAssociation = chemicalToPathwayAssociation;
    }

    /**
     * ClinicalEntity
     * <p>
     * Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
     * 
     */
    @JsonProperty("ClinicalEntity")
    public ClinicalEntity getClinicalEntity() {
        return clinicalEntity;
    }

    /**
     * ClinicalEntity
     * <p>
     * Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
     * 
     */
    @JsonProperty("ClinicalEntity")
    public void setClinicalEntity(ClinicalEntity clinicalEntity) {
        this.clinicalEntity = clinicalEntity;
    }

    /**
     * ClinicalIntervention
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalIntervention")
    public ClinicalIntervention getClinicalIntervention() {
        return clinicalIntervention;
    }

    /**
     * ClinicalIntervention
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalIntervention")
    public void setClinicalIntervention(ClinicalIntervention clinicalIntervention) {
        this.clinicalIntervention = clinicalIntervention;
    }

    /**
     * ClinicalModifier
     * <p>
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("ClinicalModifier")
    public ClinicalModifier getClinicalModifier() {
        return clinicalModifier;
    }

    /**
     * ClinicalModifier
     * <p>
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("ClinicalModifier")
    public void setClinicalModifier(ClinicalModifier clinicalModifier) {
        this.clinicalModifier = clinicalModifier;
    }

    /**
     * ClinicalTrial
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalTrial")
    public ClinicalTrial getClinicalTrial() {
        return clinicalTrial;
    }

    /**
     * ClinicalTrial
     * <p>
     * 
     * 
     */
    @JsonProperty("ClinicalTrial")
    public void setClinicalTrial(ClinicalTrial clinicalTrial) {
        this.clinicalTrial = clinicalTrial;
    }

    /**
     * CodingSequence
     * <p>
     * 
     * 
     */
    @JsonProperty("CodingSequence")
    public CodingSequence getCodingSequence() {
        return codingSequence;
    }

    /**
     * CodingSequence
     * <p>
     * 
     * 
     */
    @JsonProperty("CodingSequence")
    public void setCodingSequence(CodingSequence codingSequence) {
        this.codingSequence = codingSequence;
    }

    /**
     * ConfidenceLevel
     * <p>
     * Level of confidence in a statement
     * 
     */
    @JsonProperty("ConfidenceLevel")
    public ConfidenceLevel getConfidenceLevel() {
        return confidenceLevel;
    }

    /**
     * ConfidenceLevel
     * <p>
     * Level of confidence in a statement
     * 
     */
    @JsonProperty("ConfidenceLevel")
    public void setConfidenceLevel(ConfidenceLevel confidenceLevel) {
        this.confidenceLevel = confidenceLevel;
    }

    /**
     * Device
     * <p>
     * A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
     * 
     */
    @JsonProperty("Device")
    public Device getDevice() {
        return device;
    }

    /**
     * Device
     * <p>
     * A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
     * 
     */
    @JsonProperty("Device")
    public void setDevice(Device device) {
        this.device = device;
    }

    /**
     * Disease
     * <p>
     * 
     * 
     */
    @JsonProperty("Disease")
    public Disease getDisease() {
        return disease;
    }

    /**
     * Disease
     * <p>
     * 
     * 
     */
    @JsonProperty("Disease")
    public void setDisease(Disease disease) {
        this.disease = disease;
    }

    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    public DiseaseOrPhenotypicFeature getDiseaseOrPhenotypicFeature() {
        return diseaseOrPhenotypicFeature;
    }

    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    public void setDiseaseOrPhenotypicFeature(DiseaseOrPhenotypicFeature diseaseOrPhenotypicFeature) {
        this.diseaseOrPhenotypicFeature = diseaseOrPhenotypicFeature;
    }

    /**
     * DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
     * <p>
     * An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeatureAssociationToLocationAssociation")
    public DiseaseOrPhenotypicFeatureAssociationToLocationAssociation getDiseaseOrPhenotypicFeatureAssociationToLocationAssociation() {
        return diseaseOrPhenotypicFeatureAssociationToLocationAssociation;
    }

    /**
     * DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
     * <p>
     * An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeatureAssociationToLocationAssociation")
    public void setDiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToLocationAssociation diseaseOrPhenotypicFeatureAssociationToLocationAssociation) {
        this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation = diseaseOrPhenotypicFeatureAssociationToLocationAssociation;
    }

    /**
     * DiseaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureAssociation")
    public DiseaseToPhenotypicFeatureAssociation getDiseaseToPhenotypicFeatureAssociation() {
        return diseaseToPhenotypicFeatureAssociation;
    }

    /**
     * DiseaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureAssociation")
    public void setDiseaseToPhenotypicFeatureAssociation(DiseaseToPhenotypicFeatureAssociation diseaseToPhenotypicFeatureAssociation) {
        this.diseaseToPhenotypicFeatureAssociation = diseaseToPhenotypicFeatureAssociation;
    }

    /**
     * Drug
     * <p>
     * A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
     * 
     */
    @JsonProperty("Drug")
    public Drug getDrug() {
        return drug;
    }

    /**
     * Drug
     * <p>
     * A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
     * 
     */
    @JsonProperty("Drug")
    public void setDrug(Drug drug) {
        this.drug = drug;
    }

    /**
     * DrugExposure
     * <p>
     * A drug exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("DrugExposure")
    public DrugExposure getDrugExposure() {
        return drugExposure;
    }

    /**
     * DrugExposure
     * <p>
     * A drug exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("DrugExposure")
    public void setDrugExposure(DrugExposure drugExposure) {
        this.drugExposure = drugExposure;
    }

    /**
     * Environment
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("Environment")
    public Environment getEnvironment() {
        return environment;
    }

    /**
     * Environment
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("Environment")
    public void setEnvironment(Environment environment) {
        this.environment = environment;
    }

    /**
     * EnvironmentToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("EnvironmentToPhenotypicFeatureAssociation")
    public EnvironmentToPhenotypicFeatureAssociation getEnvironmentToPhenotypicFeatureAssociation() {
        return environmentToPhenotypicFeatureAssociation;
    }

    /**
     * EnvironmentToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("EnvironmentToPhenotypicFeatureAssociation")
    public void setEnvironmentToPhenotypicFeatureAssociation(EnvironmentToPhenotypicFeatureAssociation environmentToPhenotypicFeatureAssociation) {
        this.environmentToPhenotypicFeatureAssociation = environmentToPhenotypicFeatureAssociation;
    }

    /**
     * EnvironmentalFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public EnvironmentalFeature getEnvironmentalFeature() {
        return environmentalFeature;
    }

    /**
     * EnvironmentalFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public void setEnvironmentalFeature(EnvironmentalFeature environmentalFeature) {
        this.environmentalFeature = environmentalFeature;
    }

    /**
     * EnvironmentalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalProcess")
    public EnvironmentalProcess getEnvironmentalProcess() {
        return environmentalProcess;
    }

    /**
     * EnvironmentalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("EnvironmentalProcess")
    public void setEnvironmentalProcess(EnvironmentalProcess environmentalProcess) {
        this.environmentalProcess = environmentalProcess;
    }

    /**
     * EvidenceType
     * <p>
     * Class of evidence that supports an association
     * 
     */
    @JsonProperty("EvidenceType")
    public EvidenceType getEvidenceType() {
        return evidenceType;
    }

    /**
     * EvidenceType
     * <p>
     * Class of evidence that supports an association
     * 
     */
    @JsonProperty("EvidenceType")
    public void setEvidenceType(EvidenceType evidenceType) {
        this.evidenceType = evidenceType;
    }

    /**
     * Exon
     * <p>
     * A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
     * 
     */
    @JsonProperty("Exon")
    public Exon getExon() {
        return exon;
    }

    /**
     * Exon
     * <p>
     * A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
     * 
     */
    @JsonProperty("Exon")
    public void setExon(Exon exon) {
        this.exon = exon;
    }

    /**
     * ExonToTranscriptRelationship
     * <p>
     * A transcript is formed from multiple exons
     * 
     */
    @JsonProperty("ExonToTranscriptRelationship")
    public ExonToTranscriptRelationship getExonToTranscriptRelationship() {
        return exonToTranscriptRelationship;
    }

    /**
     * ExonToTranscriptRelationship
     * <p>
     * A transcript is formed from multiple exons
     * 
     */
    @JsonProperty("ExonToTranscriptRelationship")
    public void setExonToTranscriptRelationship(ExonToTranscriptRelationship exonToTranscriptRelationship) {
        this.exonToTranscriptRelationship = exonToTranscriptRelationship;
    }

    /**
     * FrequencyQualifier
     * <p>
     * Qualifier for freqency type associations
     * 
     */
    @JsonProperty("FrequencyQualifier")
    public FrequencyQualifier getFrequencyQualifier() {
        return frequencyQualifier;
    }

    /**
     * FrequencyQualifier
     * <p>
     * Qualifier for freqency type associations
     * 
     */
    @JsonProperty("FrequencyQualifier")
    public void setFrequencyQualifier(FrequencyQualifier frequencyQualifier) {
        this.frequencyQualifier = frequencyQualifier;
    }

    /**
     * FrequencyQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("FrequencyQuantifier")
    public FrequencyQuantifier getFrequencyQuantifier() {
        return frequencyQuantifier;
    }

    /**
     * FrequencyQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("FrequencyQuantifier")
    public void setFrequencyQuantifier(FrequencyQuantifier frequencyQuantifier) {
        this.frequencyQuantifier = frequencyQuantifier;
    }

    /**
     * FrequencyValue
     * <p>
     * describes the frequency of occurrence of an event or condition
     * 
     */
    @JsonProperty("FrequencyValue")
    public FrequencyValue getFrequencyValue() {
        return frequencyValue;
    }

    /**
     * FrequencyValue
     * <p>
     * describes the frequency of occurrence of an event or condition
     * 
     */
    @JsonProperty("FrequencyValue")
    public void setFrequencyValue(FrequencyValue frequencyValue) {
        this.frequencyValue = frequencyValue;
    }

    /**
     * FunctionalAssociation
     * <p>
     * An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
     * 
     */
    @JsonProperty("FunctionalAssociation")
    public FunctionalAssociation getFunctionalAssociation() {
        return functionalAssociation;
    }

    /**
     * FunctionalAssociation
     * <p>
     * An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
     * 
     */
    @JsonProperty("FunctionalAssociation")
    public void setFunctionalAssociation(FunctionalAssociation functionalAssociation) {
        this.functionalAssociation = functionalAssociation;
    }

    /**
     * Gene
     * <p>
     * 
     * 
     */
    @JsonProperty("Gene")
    public Gene getGene() {
        return gene;
    }

    /**
     * Gene
     * <p>
     * 
     * 
     */
    @JsonProperty("Gene")
    public void setGene(Gene gene) {
        this.gene = gene;
    }

    /**
     * GeneAsAModelOfDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneAsAModelOfDiseaseAssociation")
    public GeneAsAModelOfDiseaseAssociation getGeneAsAModelOfDiseaseAssociation() {
        return geneAsAModelOfDiseaseAssociation;
    }

    /**
     * GeneAsAModelOfDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneAsAModelOfDiseaseAssociation")
    public void setGeneAsAModelOfDiseaseAssociation(GeneAsAModelOfDiseaseAssociation geneAsAModelOfDiseaseAssociation) {
        this.geneAsAModelOfDiseaseAssociation = geneAsAModelOfDiseaseAssociation;
    }

    /**
     * GeneFamily
     * <p>
     * any grouping of multiple genes or gene products related by common descent
     * 
     */
    @JsonProperty("GeneFamily")
    public GeneFamily getGeneFamily() {
        return geneFamily;
    }

    /**
     * GeneFamily
     * <p>
     * any grouping of multiple genes or gene products related by common descent
     * 
     */
    @JsonProperty("GeneFamily")
    public void setGeneFamily(GeneFamily geneFamily) {
        this.geneFamily = geneFamily;
    }

    /**
     * GeneHasVariantThatContributesToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneHasVariantThatContributesToDiseaseAssociation")
    public GeneHasVariantThatContributesToDiseaseAssociation getGeneHasVariantThatContributesToDiseaseAssociation() {
        return geneHasVariantThatContributesToDiseaseAssociation;
    }

    /**
     * GeneHasVariantThatContributesToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneHasVariantThatContributesToDiseaseAssociation")
    public void setGeneHasVariantThatContributesToDiseaseAssociation(GeneHasVariantThatContributesToDiseaseAssociation geneHasVariantThatContributesToDiseaseAssociation) {
        this.geneHasVariantThatContributesToDiseaseAssociation = geneHasVariantThatContributesToDiseaseAssociation;
    }

    /**
     * GeneOntologyClass
     * <p>
     * an ontology class that describes a functional aspect of a gene, gene prodoct or complex
     * 
     */
    @JsonProperty("GeneOntologyClass")
    public GeneOntologyClass getGeneOntologyClass() {
        return geneOntologyClass;
    }

    /**
     * GeneOntologyClass
     * <p>
     * an ontology class that describes a functional aspect of a gene, gene prodoct or complex
     * 
     */
    @JsonProperty("GeneOntologyClass")
    public void setGeneOntologyClass(GeneOntologyClass geneOntologyClass) {
        this.geneOntologyClass = geneOntologyClass;
    }

    /**
     * GeneOrGeneProduct
     * <p>
     * a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
     * 
     */
    @JsonProperty("GeneOrGeneProduct")
    public GeneOrGeneProduct getGeneOrGeneProduct() {
        return geneOrGeneProduct;
    }

    /**
     * GeneOrGeneProduct
     * <p>
     * a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
     * 
     */
    @JsonProperty("GeneOrGeneProduct")
    public void setGeneOrGeneProduct(GeneOrGeneProduct geneOrGeneProduct) {
        this.geneOrGeneProduct = geneOrGeneProduct;
    }

    /**
     * GeneProduct
     * <p>
     * The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
     * 
     */
    @JsonProperty("GeneProduct")
    public GeneProduct getGeneProduct() {
        return geneProduct;
    }

    /**
     * GeneProduct
     * <p>
     * The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
     * 
     */
    @JsonProperty("GeneProduct")
    public void setGeneProduct(GeneProduct geneProduct) {
        this.geneProduct = geneProduct;
    }

    /**
     * GeneRegulatoryRelationship
     * <p>
     * A regulatory relationship between two genes
     * 
     */
    @JsonProperty("GeneRegulatoryRelationship")
    public GeneRegulatoryRelationship getGeneRegulatoryRelationship() {
        return geneRegulatoryRelationship;
    }

    /**
     * GeneRegulatoryRelationship
     * <p>
     * A regulatory relationship between two genes
     * 
     */
    @JsonProperty("GeneRegulatoryRelationship")
    public void setGeneRegulatoryRelationship(GeneRegulatoryRelationship geneRegulatoryRelationship) {
        this.geneRegulatoryRelationship = geneRegulatoryRelationship;
    }

    /**
     * GeneToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToDiseaseAssociation")
    public GeneToDiseaseAssociation getGeneToDiseaseAssociation() {
        return geneToDiseaseAssociation;
    }

    /**
     * GeneToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToDiseaseAssociation")
    public void setGeneToDiseaseAssociation(GeneToDiseaseAssociation geneToDiseaseAssociation) {
        this.geneToDiseaseAssociation = geneToDiseaseAssociation;
    }

    /**
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info.
     * 
     */
    @JsonProperty("GeneToExpressionSiteAssociation")
    public GeneToExpressionSiteAssociation getGeneToExpressionSiteAssociation() {
        return geneToExpressionSiteAssociation;
    }

    /**
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info.
     * 
     */
    @JsonProperty("GeneToExpressionSiteAssociation")
    public void setGeneToExpressionSiteAssociation(GeneToExpressionSiteAssociation geneToExpressionSiteAssociation) {
        this.geneToExpressionSiteAssociation = geneToExpressionSiteAssociation;
    }

    /**
     * GeneToGeneHomologyAssociation
     * <p>
     * A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
     * 
     */
    @JsonProperty("GeneToGeneHomologyAssociation")
    public GeneToGeneHomologyAssociation getGeneToGeneHomologyAssociation() {
        return geneToGeneHomologyAssociation;
    }

    /**
     * GeneToGeneHomologyAssociation
     * <p>
     * A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
     * 
     */
    @JsonProperty("GeneToGeneHomologyAssociation")
    public void setGeneToGeneHomologyAssociation(GeneToGeneHomologyAssociation geneToGeneHomologyAssociation) {
        this.geneToGeneHomologyAssociation = geneToGeneHomologyAssociation;
    }

    /**
     * GeneToGeneProductRelationship
     * <p>
     * A gene is transcribed and potentially translated to a gene product
     * 
     */
    @JsonProperty("GeneToGeneProductRelationship")
    public GeneToGeneProductRelationship getGeneToGeneProductRelationship() {
        return geneToGeneProductRelationship;
    }

    /**
     * GeneToGeneProductRelationship
     * <p>
     * A gene is transcribed and potentially translated to a gene product
     * 
     */
    @JsonProperty("GeneToGeneProductRelationship")
    public void setGeneToGeneProductRelationship(GeneToGeneProductRelationship geneToGeneProductRelationship) {
        this.geneToGeneProductRelationship = geneToGeneProductRelationship;
    }

    /**
     * GeneToGoTermAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    public GeneToGoTermAssociation getGeneToGoTermAssociation() {
        return geneToGoTermAssociation;
    }

    /**
     * GeneToGoTermAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    public void setGeneToGoTermAssociation(GeneToGoTermAssociation geneToGoTermAssociation) {
        this.geneToGoTermAssociation = geneToGoTermAssociation;
    }

    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    public GeneToPhenotypicFeatureAssociation getGeneToPhenotypicFeatureAssociation() {
        return geneToPhenotypicFeatureAssociation;
    }

    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    public void setGeneToPhenotypicFeatureAssociation(GeneToPhenotypicFeatureAssociation geneToPhenotypicFeatureAssociation) {
        this.geneToPhenotypicFeatureAssociation = geneToPhenotypicFeatureAssociation;
    }

    /**
     * Genome
     * <p>
     * A genome is the sum of genetic material within a cell or virion.
     * 
     */
    @JsonProperty("Genome")
    public Genome getGenome() {
        return genome;
    }

    /**
     * Genome
     * <p>
     * A genome is the sum of genetic material within a cell or virion.
     * 
     */
    @JsonProperty("Genome")
    public void setGenome(Genome genome) {
        this.genome = genome;
    }

    /**
     * GenomicEntity
     * <p>
     * an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
     * 
     */
    @JsonProperty("GenomicEntity")
    public GenomicEntity getGenomicEntity() {
        return genomicEntity;
    }

    /**
     * GenomicEntity
     * <p>
     * an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
     * 
     */
    @JsonProperty("GenomicEntity")
    public void setGenomicEntity(GenomicEntity genomicEntity) {
        this.genomicEntity = genomicEntity;
    }

    /**
     * GenomicSequenceLocalization
     * <p>
     * A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
     * 
     */
    @JsonProperty("GenomicSequenceLocalization")
    public GenomicSequenceLocalization getGenomicSequenceLocalization() {
        return genomicSequenceLocalization;
    }

    /**
     * GenomicSequenceLocalization
     * <p>
     * A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
     * 
     */
    @JsonProperty("GenomicSequenceLocalization")
    public void setGenomicSequenceLocalization(GenomicSequenceLocalization genomicSequenceLocalization) {
        this.genomicSequenceLocalization = genomicSequenceLocalization;
    }

    /**
     * Genotype
     * <p>
     * An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
     * 
     */
    @JsonProperty("Genotype")
    public Genotype getGenotype() {
        return genotype;
    }

    /**
     * Genotype
     * <p>
     * An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
     * 
     */
    @JsonProperty("Genotype")
    public void setGenotype(Genotype genotype) {
        this.genotype = genotype;
    }

    /**
     * GenotypeToGeneAssociation
     * <p>
     * Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
     * 
     */
    @JsonProperty("GenotypeToGeneAssociation")
    public GenotypeToGeneAssociation getGenotypeToGeneAssociation() {
        return genotypeToGeneAssociation;
    }

    /**
     * GenotypeToGeneAssociation
     * <p>
     * Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
     * 
     */
    @JsonProperty("GenotypeToGeneAssociation")
    public void setGenotypeToGeneAssociation(GenotypeToGeneAssociation genotypeToGeneAssociation) {
        this.genotypeToGeneAssociation = genotypeToGeneAssociation;
    }

    /**
     * GenotypeToGenotypePartAssociation
     * <p>
     * Any association between one genotype and a genotypic entity that is a sub-component of it
     * 
     */
    @JsonProperty("GenotypeToGenotypePartAssociation")
    public GenotypeToGenotypePartAssociation getGenotypeToGenotypePartAssociation() {
        return genotypeToGenotypePartAssociation;
    }

    /**
     * GenotypeToGenotypePartAssociation
     * <p>
     * Any association between one genotype and a genotypic entity that is a sub-component of it
     * 
     */
    @JsonProperty("GenotypeToGenotypePartAssociation")
    public void setGenotypeToGenotypePartAssociation(GenotypeToGenotypePartAssociation genotypeToGenotypePartAssociation) {
        this.genotypeToGenotypePartAssociation = genotypeToGenotypePartAssociation;
    }

    /**
     * GenotypeToPhenotypicFeatureAssociation
     * <p>
     * Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    public GenotypeToPhenotypicFeatureAssociation getGenotypeToPhenotypicFeatureAssociation() {
        return genotypeToPhenotypicFeatureAssociation;
    }

    /**
     * GenotypeToPhenotypicFeatureAssociation
     * <p>
     * Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    public void setGenotypeToPhenotypicFeatureAssociation(GenotypeToPhenotypicFeatureAssociation genotypeToPhenotypicFeatureAssociation) {
        this.genotypeToPhenotypicFeatureAssociation = genotypeToPhenotypicFeatureAssociation;
    }

    /**
     * GenotypeToVariantAssociation
     * <p>
     * Any association between a genotype and a sequence variant.
     * 
     */
    @JsonProperty("GenotypeToVariantAssociation")
    public GenotypeToVariantAssociation getGenotypeToVariantAssociation() {
        return genotypeToVariantAssociation;
    }

    /**
     * GenotypeToVariantAssociation
     * <p>
     * Any association between a genotype and a sequence variant.
     * 
     */
    @JsonProperty("GenotypeToVariantAssociation")
    public void setGenotypeToVariantAssociation(GenotypeToVariantAssociation genotypeToVariantAssociation) {
        this.genotypeToVariantAssociation = genotypeToVariantAssociation;
    }

    /**
     * GenotypicSex
     * <p>
     * An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
     * 
     */
    @JsonProperty("GenotypicSex")
    public GenotypicSex getGenotypicSex() {
        return genotypicSex;
    }

    /**
     * GenotypicSex
     * <p>
     * An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
     * 
     */
    @JsonProperty("GenotypicSex")
    public void setGenotypicSex(GenotypicSex genotypicSex) {
        this.genotypicSex = genotypicSex;
    }

    /**
     * GeographicLocation
     * <p>
     * a location that can be described in lat/long coordinates
     * 
     */
    @JsonProperty("GeographicLocation")
    public GeographicLocation getGeographicLocation() {
        return geographicLocation;
    }

    /**
     * GeographicLocation
     * <p>
     * a location that can be described in lat/long coordinates
     * 
     */
    @JsonProperty("GeographicLocation")
    public void setGeographicLocation(GeographicLocation geographicLocation) {
        this.geographicLocation = geographicLocation;
    }

    /**
     * GeographicLocationAtTime
     * <p>
     * a location that can be described in lat/long coordinates, for a particular time
     * 
     */
    @JsonProperty("GeographicLocationAtTime")
    public GeographicLocationAtTime getGeographicLocationAtTime() {
        return geographicLocationAtTime;
    }

    /**
     * GeographicLocationAtTime
     * <p>
     * a location that can be described in lat/long coordinates, for a particular time
     * 
     */
    @JsonProperty("GeographicLocationAtTime")
    public void setGeographicLocationAtTime(GeographicLocationAtTime geographicLocationAtTime) {
        this.geographicLocationAtTime = geographicLocationAtTime;
    }

    /**
     * GrossAnatomicalStructure
     * <p>
     * 
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    public GrossAnatomicalStructure getGrossAnatomicalStructure() {
        return grossAnatomicalStructure;
    }

    /**
     * GrossAnatomicalStructure
     * <p>
     * 
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    public void setGrossAnatomicalStructure(GrossAnatomicalStructure grossAnatomicalStructure) {
        this.grossAnatomicalStructure = grossAnatomicalStructure;
    }

    /**
     * Haplotype
     * <p>
     * A set of zero or more Alleles on a single instance of a Sequence[VMC]
     * 
     */
    @JsonProperty("Haplotype")
    public Haplotype getHaplotype() {
        return haplotype;
    }

    /**
     * Haplotype
     * <p>
     * A set of zero or more Alleles on a single instance of a Sequence[VMC]
     * 
     */
    @JsonProperty("Haplotype")
    public void setHaplotype(Haplotype haplotype) {
        this.haplotype = haplotype;
    }

    /**
     * IndividualOrganism
     * <p>
     * 
     * 
     */
    @JsonProperty("IndividualOrganism")
    public IndividualOrganism getIndividualOrganism() {
        return individualOrganism;
    }

    /**
     * IndividualOrganism
     * <p>
     * 
     * 
     */
    @JsonProperty("IndividualOrganism")
    public void setIndividualOrganism(IndividualOrganism individualOrganism) {
        this.individualOrganism = individualOrganism;
    }

    /**
     * LifeStage
     * <p>
     * A stage of development or growth of an organism, including post-natal adult stages
     * 
     */
    @JsonProperty("LifeStage")
    public LifeStage getLifeStage() {
        return lifeStage;
    }

    /**
     * LifeStage
     * <p>
     * A stage of development or growth of an organism, including post-natal adult stages
     * 
     */
    @JsonProperty("LifeStage")
    public void setLifeStage(LifeStage lifeStage) {
        this.lifeStage = lifeStage;
    }

    /**
     * MacromolecularComplex
     * <p>
     * 
     * 
     */
    @JsonProperty("MacromolecularComplex")
    public MacromolecularComplex getMacromolecularComplex() {
        return macromolecularComplex;
    }

    /**
     * MacromolecularComplex
     * <p>
     * 
     * 
     */
    @JsonProperty("MacromolecularComplex")
    public void setMacromolecularComplex(MacromolecularComplex macromolecularComplex) {
        this.macromolecularComplex = macromolecularComplex;
    }

    /**
     * MacromolecularMachine
     * <p>
     * A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
     * 
     */
    @JsonProperty("MacromolecularMachine")
    public MacromolecularMachine getMacromolecularMachine() {
        return macromolecularMachine;
    }

    /**
     * MacromolecularMachine
     * <p>
     * A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
     * 
     */
    @JsonProperty("MacromolecularMachine")
    public void setMacromolecularMachine(MacromolecularMachine macromolecularMachine) {
        this.macromolecularMachine = macromolecularMachine;
    }

    /**
     * MacromolecularMachineToBiologicalProcessAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
     * 
     */
    @JsonProperty("MacromolecularMachineToBiologicalProcessAssociation")
    public MacromolecularMachineToBiologicalProcessAssociation getMacromolecularMachineToBiologicalProcessAssociation() {
        return macromolecularMachineToBiologicalProcessAssociation;
    }

    /**
     * MacromolecularMachineToBiologicalProcessAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
     * 
     */
    @JsonProperty("MacromolecularMachineToBiologicalProcessAssociation")
    public void setMacromolecularMachineToBiologicalProcessAssociation(MacromolecularMachineToBiologicalProcessAssociation macromolecularMachineToBiologicalProcessAssociation) {
        this.macromolecularMachineToBiologicalProcessAssociation = macromolecularMachineToBiologicalProcessAssociation;
    }

    /**
     * MacromolecularMachineToCellularComponentAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
     * 
     */
    @JsonProperty("MacromolecularMachineToCellularComponentAssociation")
    public MacromolecularMachineToCellularComponentAssociation getMacromolecularMachineToCellularComponentAssociation() {
        return macromolecularMachineToCellularComponentAssociation;
    }

    /**
     * MacromolecularMachineToCellularComponentAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
     * 
     */
    @JsonProperty("MacromolecularMachineToCellularComponentAssociation")
    public void setMacromolecularMachineToCellularComponentAssociation(MacromolecularMachineToCellularComponentAssociation macromolecularMachineToCellularComponentAssociation) {
        this.macromolecularMachineToCellularComponentAssociation = macromolecularMachineToCellularComponentAssociation;
    }

    /**
     * MacromolecularMachineToMolecularActivityAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
     * 
     */
    @JsonProperty("MacromolecularMachineToMolecularActivityAssociation")
    public MacromolecularMachineToMolecularActivityAssociation getMacromolecularMachineToMolecularActivityAssociation() {
        return macromolecularMachineToMolecularActivityAssociation;
    }

    /**
     * MacromolecularMachineToMolecularActivityAssociation
     * <p>
     * A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
     * 
     */
    @JsonProperty("MacromolecularMachineToMolecularActivityAssociation")
    public void setMacromolecularMachineToMolecularActivityAssociation(MacromolecularMachineToMolecularActivityAssociation macromolecularMachineToMolecularActivityAssociation) {
        this.macromolecularMachineToMolecularActivityAssociation = macromolecularMachineToMolecularActivityAssociation;
    }

    /**
     * Metabolite
     * <p>
     * Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
     * 
     */
    @JsonProperty("Metabolite")
    public Metabolite getMetabolite() {
        return metabolite;
    }

    /**
     * Metabolite
     * <p>
     * Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
     * 
     */
    @JsonProperty("Metabolite")
    public void setMetabolite(Metabolite metabolite) {
        this.metabolite = metabolite;
    }

    /**
     * MicroRNA
     * <p>
     * 
     * 
     */
    @JsonProperty("MicroRNA")
    public MicroRNA getMicroRNA() {
        return microRNA;
    }

    /**
     * MicroRNA
     * <p>
     * 
     * 
     */
    @JsonProperty("MicroRNA")
    public void setMicroRNA(MicroRNA microRNA) {
        this.microRNA = microRNA;
    }

    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function carried out by a gene product or macromolecular complex.
     * 
     */
    @JsonProperty("MolecularActivity")
    public MolecularActivity getMolecularActivity() {
        return molecularActivity;
    }

    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function carried out by a gene product or macromolecular complex.
     * 
     */
    @JsonProperty("MolecularActivity")
    public void setMolecularActivity(MolecularActivity molecularActivity) {
        this.molecularActivity = molecularActivity;
    }

    /**
     * MolecularEntity
     * <p>
     * A gene, gene product, small molecule or macromolecule (including protein complex)
     * 
     */
    @JsonProperty("MolecularEntity")
    public MolecularEntity getMolecularEntity() {
        return molecularEntity;
    }

    /**
     * MolecularEntity
     * <p>
     * A gene, gene product, small molecule or macromolecule (including protein complex)
     * 
     */
    @JsonProperty("MolecularEntity")
    public void setMolecularEntity(MolecularEntity molecularEntity) {
        this.molecularEntity = molecularEntity;
    }

    /**
     * NamedThing
     * <p>
     * a databased entity or concept/class
     * 
     */
    @JsonProperty("NamedThing")
    public NamedThing getNamedThing() {
        return namedThing;
    }

    /**
     * NamedThing
     * <p>
     * a databased entity or concept/class
     * 
     */
    @JsonProperty("NamedThing")
    public void setNamedThing(NamedThing namedThing) {
        this.namedThing = namedThing;
    }

    /**
     * NoncodingRNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("NoncodingRNAProduct")
    public NoncodingRNAProduct getNoncodingRNAProduct() {
        return noncodingRNAProduct;
    }

    /**
     * NoncodingRNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("NoncodingRNAProduct")
    public void setNoncodingRNAProduct(NoncodingRNAProduct noncodingRNAProduct) {
        this.noncodingRNAProduct = noncodingRNAProduct;
    }

    /**
     * Occurrent
     * <p>
     * A processual entity
     * 
     */
    @JsonProperty("Occurrent")
    public Occurrent getOccurrent() {
        return occurrent;
    }

    /**
     * Occurrent
     * <p>
     * A processual entity
     * 
     */
    @JsonProperty("Occurrent")
    public void setOccurrent(Occurrent occurrent) {
        this.occurrent = occurrent;
    }

    /**
     * Onset
     * <p>
     * The age group in which manifestations appear
     * 
     */
    @JsonProperty("Onset")
    public Onset getOnset() {
        return onset;
    }

    /**
     * Onset
     * <p>
     * The age group in which manifestations appear
     * 
     */
    @JsonProperty("Onset")
    public void setOnset(Onset onset) {
        this.onset = onset;
    }

    /**
     * OntologyClass
     * <p>
     * a concept or class in an ontology, vocabulary or thesaurus
     * 
     */
    @JsonProperty("OntologyClass")
    public OntologyClass getOntologyClass() {
        return ontologyClass;
    }

    /**
     * OntologyClass
     * <p>
     * a concept or class in an ontology, vocabulary or thesaurus
     * 
     */
    @JsonProperty("OntologyClass")
    public void setOntologyClass(OntologyClass ontologyClass) {
        this.ontologyClass = ontologyClass;
    }

    /**
     * OrganismTaxon
     * <p>
     * 
     * 
     */
    @JsonProperty("OrganismTaxon")
    public OrganismTaxon getOrganismTaxon() {
        return organismTaxon;
    }

    /**
     * OrganismTaxon
     * <p>
     * 
     * 
     */
    @JsonProperty("OrganismTaxon")
    public void setOrganismTaxon(OrganismTaxon organismTaxon) {
        this.organismTaxon = organismTaxon;
    }

    /**
     * PairwiseGeneOrProteinInteractionAssociation
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneOrProteinInteractionAssociation")
    public PairwiseGeneOrProteinInteractionAssociation getPairwiseGeneOrProteinInteractionAssociation() {
        return pairwiseGeneOrProteinInteractionAssociation;
    }

    /**
     * PairwiseGeneOrProteinInteractionAssociation
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneOrProteinInteractionAssociation")
    public void setPairwiseGeneOrProteinInteractionAssociation(PairwiseGeneOrProteinInteractionAssociation pairwiseGeneOrProteinInteractionAssociation) {
        this.pairwiseGeneOrProteinInteractionAssociation = pairwiseGeneOrProteinInteractionAssociation;
    }

    /**
     * PathognomonicityQuantifier
     * <p>
     * A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
     * 
     */
    @JsonProperty("PathognomonicityQuantifier")
    public PathognomonicityQuantifier getPathognomonicityQuantifier() {
        return pathognomonicityQuantifier;
    }

    /**
     * PathognomonicityQuantifier
     * <p>
     * A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
     * 
     */
    @JsonProperty("PathognomonicityQuantifier")
    public void setPathognomonicityQuantifier(PathognomonicityQuantifier pathognomonicityQuantifier) {
        this.pathognomonicityQuantifier = pathognomonicityQuantifier;
    }

    /**
     * Pathway
     * <p>
     * 
     * 
     */
    @JsonProperty("Pathway")
    public Pathway getPathway() {
        return pathway;
    }

    /**
     * Pathway
     * <p>
     * 
     * 
     */
    @JsonProperty("Pathway")
    public void setPathway(Pathway pathway) {
        this.pathway = pathway;
    }

    /**
     * Phenomenon
     * <p>
     * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
     * 
     */
    @JsonProperty("Phenomenon")
    public Phenomenon getPhenomenon() {
        return phenomenon;
    }

    /**
     * Phenomenon
     * <p>
     * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
     * 
     */
    @JsonProperty("Phenomenon")
    public void setPhenomenon(Phenomenon phenomenon) {
        this.phenomenon = phenomenon;
    }

    /**
     * PhenotypicFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("PhenotypicFeature")
    public PhenotypicFeature getPhenotypicFeature() {
        return phenotypicFeature;
    }

    /**
     * PhenotypicFeature
     * <p>
     * 
     * 
     */
    @JsonProperty("PhenotypicFeature")
    public void setPhenotypicFeature(PhenotypicFeature phenotypicFeature) {
        this.phenotypicFeature = phenotypicFeature;
    }

    /**
     * PhenotypicSex
     * <p>
     * An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
     * 
     */
    @JsonProperty("PhenotypicSex")
    public PhenotypicSex getPhenotypicSex() {
        return phenotypicSex;
    }

    /**
     * PhenotypicSex
     * <p>
     * An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
     * 
     */
    @JsonProperty("PhenotypicSex")
    public void setPhenotypicSex(PhenotypicSex phenotypicSex) {
        this.phenotypicSex = phenotypicSex;
    }

    /**
     * PhysiologicalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("PhysiologicalProcess")
    public PhysiologicalProcess getPhysiologicalProcess() {
        return physiologicalProcess;
    }

    /**
     * PhysiologicalProcess
     * <p>
     * 
     * 
     */
    @JsonProperty("PhysiologicalProcess")
    public void setPhysiologicalProcess(PhysiologicalProcess physiologicalProcess) {
        this.physiologicalProcess = physiologicalProcess;
    }

    /**
     * PlanetaryEntity
     * <p>
     * Any entity or process that exists at the level of the whole planet
     * 
     */
    @JsonProperty("PlanetaryEntity")
    public PlanetaryEntity getPlanetaryEntity() {
        return planetaryEntity;
    }

    /**
     * PlanetaryEntity
     * <p>
     * Any entity or process that exists at the level of the whole planet
     * 
     */
    @JsonProperty("PlanetaryEntity")
    public void setPlanetaryEntity(PlanetaryEntity planetaryEntity) {
        this.planetaryEntity = planetaryEntity;
    }

    /**
     * PopulationOfIndividualOrganisms
     * <p>
     * 
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    public PopulationOfIndividualOrganisms getPopulationOfIndividualOrganisms() {
        return populationOfIndividualOrganisms;
    }

    /**
     * PopulationOfIndividualOrganisms
     * <p>
     * 
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    public void setPopulationOfIndividualOrganisms(PopulationOfIndividualOrganisms populationOfIndividualOrganisms) {
        this.populationOfIndividualOrganisms = populationOfIndividualOrganisms;
    }

    /**
     * PopulationToPopulationAssociation
     * <p>
     * An association between a two populations
     * 
     */
    @JsonProperty("PopulationToPopulationAssociation")
    public PopulationToPopulationAssociation getPopulationToPopulationAssociation() {
        return populationToPopulationAssociation;
    }

    /**
     * PopulationToPopulationAssociation
     * <p>
     * An association between a two populations
     * 
     */
    @JsonProperty("PopulationToPopulationAssociation")
    public void setPopulationToPopulationAssociation(PopulationToPopulationAssociation populationToPopulationAssociation) {
        this.populationToPopulationAssociation = populationToPopulationAssociation;
    }

    /**
     * Procedure
     * <p>
     * A series of actions conducted in a certain order or manner
     * 
     */
    @JsonProperty("Procedure")
    public Procedure getProcedure() {
        return procedure;
    }

    /**
     * Procedure
     * <p>
     * A series of actions conducted in a certain order or manner
     * 
     */
    @JsonProperty("Procedure")
    public void setProcedure(Procedure procedure) {
        this.procedure = procedure;
    }

    /**
     * Protein
     * <p>
     * A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
     * 
     */
    @JsonProperty("Protein")
    public Protein getProtein() {
        return protein;
    }

    /**
     * Protein
     * <p>
     * A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
     * 
     */
    @JsonProperty("Protein")
    public void setProtein(Protein protein) {
        this.protein = protein;
    }

    /**
     * ProteinIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
     * 
     */
    @JsonProperty("ProteinIsoform")
    public ProteinIsoform getProteinIsoform() {
        return proteinIsoform;
    }

    /**
     * ProteinIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
     * 
     */
    @JsonProperty("ProteinIsoform")
    public void setProteinIsoform(ProteinIsoform proteinIsoform) {
        this.proteinIsoform = proteinIsoform;
    }

    /**
     * Provider
     * <p>
     * person, group, organization or project that provides a piece of information
     * 
     */
    @JsonProperty("Provider")
    public Provider getProvider() {
        return provider;
    }

    /**
     * Provider
     * <p>
     * person, group, organization or project that provides a piece of information
     * 
     */
    @JsonProperty("Provider")
    public void setProvider(Provider provider) {
        this.provider = provider;
    }

    /**
     * Publication
     * <p>
     * Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
     * 
     */
    @JsonProperty("Publication")
    public Publication getPublication() {
        return publication;
    }

    /**
     * Publication
     * <p>
     * Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
     * 
     */
    @JsonProperty("Publication")
    public void setPublication(Publication publication) {
        this.publication = publication;
    }

    /**
     * RNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("RNAProduct")
    public RNAProduct getRNAProduct() {
        return rNAProduct;
    }

    /**
     * RNAProduct
     * <p>
     * 
     * 
     */
    @JsonProperty("RNAProduct")
    public void setRNAProduct(RNAProduct rNAProduct) {
        this.rNAProduct = rNAProduct;
    }

    /**
     * RNAProductIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference RNA
     * 
     */
    @JsonProperty("RNAProductIsoform")
    public RNAProductIsoform getRNAProductIsoform() {
        return rNAProductIsoform;
    }

    /**
     * RNAProductIsoform
     * <p>
     * Represents a protein that is a specific isoform of the canonical or reference RNA
     * 
     */
    @JsonProperty("RNAProductIsoform")
    public void setRNAProductIsoform(RNAProductIsoform rNAProductIsoform) {
        this.rNAProductIsoform = rNAProductIsoform;
    }

    /**
     * RelationshipType
     * <p>
     * An OWL property used as an edge label
     * 
     */
    @JsonProperty("RelationshipType")
    public RelationshipType getRelationshipType() {
        return relationshipType;
    }

    /**
     * RelationshipType
     * <p>
     * An OWL property used as an edge label
     * 
     */
    @JsonProperty("RelationshipType")
    public void setRelationshipType(RelationshipType relationshipType) {
        this.relationshipType = relationshipType;
    }

    /**
     * SenstivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SenstivityQuantifier")
    public SenstivityQuantifier getSenstivityQuantifier() {
        return senstivityQuantifier;
    }

    /**
     * SenstivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SenstivityQuantifier")
    public void setSenstivityQuantifier(SenstivityQuantifier senstivityQuantifier) {
        this.senstivityQuantifier = senstivityQuantifier;
    }

    /**
     * SequenceFeatureRelationship
     * <p>
     * For example, a particular exon is part of a particular transcript or gene
     * 
     */
    @JsonProperty("SequenceFeatureRelationship")
    public SequenceFeatureRelationship getSequenceFeatureRelationship() {
        return sequenceFeatureRelationship;
    }

    /**
     * SequenceFeatureRelationship
     * <p>
     * For example, a particular exon is part of a particular transcript or gene
     * 
     */
    @JsonProperty("SequenceFeatureRelationship")
    public void setSequenceFeatureRelationship(SequenceFeatureRelationship sequenceFeatureRelationship) {
        this.sequenceFeatureRelationship = sequenceFeatureRelationship;
    }

    /**
     * SequenceVariant
     * <p>
     * An allele that varies in its sequence from what is considered the reference allele at that locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    public SequenceVariant getSequenceVariant() {
        return sequenceVariant;
    }

    /**
     * SequenceVariant
     * <p>
     * An allele that varies in its sequence from what is considered the reference allele at that locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    public void setSequenceVariant(SequenceVariant sequenceVariant) {
        this.sequenceVariant = sequenceVariant;
    }

    /**
     * SeverityValue
     * <p>
     * describes the severity of a phenotypic feature or disease
     * 
     */
    @JsonProperty("SeverityValue")
    public SeverityValue getSeverityValue() {
        return severityValue;
    }

    /**
     * SeverityValue
     * <p>
     * describes the severity of a phenotypic feature or disease
     * 
     */
    @JsonProperty("SeverityValue")
    public void setSeverityValue(SeverityValue severityValue) {
        this.severityValue = severityValue;
    }

    /**
     * SpecificityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SpecificityQuantifier")
    public SpecificityQuantifier getSpecificityQuantifier() {
        return specificityQuantifier;
    }

    /**
     * SpecificityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SpecificityQuantifier")
    public void setSpecificityQuantifier(SpecificityQuantifier specificityQuantifier) {
        this.specificityQuantifier = specificityQuantifier;
    }

    /**
     * Transcript
     * <p>
     * An RNA synthesized on a DNA or RNA template by an RNA polymerase
     * 
     */
    @JsonProperty("Transcript")
    public Transcript getTranscript() {
        return transcript;
    }

    /**
     * Transcript
     * <p>
     * An RNA synthesized on a DNA or RNA template by an RNA polymerase
     * 
     */
    @JsonProperty("Transcript")
    public void setTranscript(Transcript transcript) {
        this.transcript = transcript;
    }

    /**
     * TranscriptToGeneRelationship
     * <p>
     * A gene is a collection of transcripts
     * 
     */
    @JsonProperty("TranscriptToGeneRelationship")
    public TranscriptToGeneRelationship getTranscriptToGeneRelationship() {
        return transcriptToGeneRelationship;
    }

    /**
     * TranscriptToGeneRelationship
     * <p>
     * A gene is a collection of transcripts
     * 
     */
    @JsonProperty("TranscriptToGeneRelationship")
    public void setTranscriptToGeneRelationship(TranscriptToGeneRelationship transcriptToGeneRelationship) {
        this.transcriptToGeneRelationship = transcriptToGeneRelationship;
    }

    /**
     * Treatment
     * <p>
     * A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
     * 
     */
    @JsonProperty("Treatment")
    public Treatment getTreatment() {
        return treatment;
    }

    /**
     * Treatment
     * <p>
     * A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
     * 
     */
    @JsonProperty("Treatment")
    public void setTreatment(Treatment treatment) {
        this.treatment = treatment;
    }

    /**
     * VariantToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToDiseaseAssociation")
    public VariantToDiseaseAssociation getVariantToDiseaseAssociation() {
        return variantToDiseaseAssociation;
    }

    /**
     * VariantToDiseaseAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToDiseaseAssociation")
    public void setVariantToDiseaseAssociation(VariantToDiseaseAssociation variantToDiseaseAssociation) {
        this.variantToDiseaseAssociation = variantToDiseaseAssociation;
    }

    /**
     * VariantToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToPhenotypicFeatureAssociation")
    public VariantToPhenotypicFeatureAssociation getVariantToPhenotypicFeatureAssociation() {
        return variantToPhenotypicFeatureAssociation;
    }

    /**
     * VariantToPhenotypicFeatureAssociation
     * <p>
     * 
     * 
     */
    @JsonProperty("VariantToPhenotypicFeatureAssociation")
    public void setVariantToPhenotypicFeatureAssociation(VariantToPhenotypicFeatureAssociation variantToPhenotypicFeatureAssociation) {
        this.variantToPhenotypicFeatureAssociation = variantToPhenotypicFeatureAssociation;
    }

    /**
     * VariantToPopulationAssociation
     * <p>
     * An association between a variant and a population, where the variant has particular frequency in the population
     * 
     */
    @JsonProperty("VariantToPopulationAssociation")
    public VariantToPopulationAssociation getVariantToPopulationAssociation() {
        return variantToPopulationAssociation;
    }

    /**
     * VariantToPopulationAssociation
     * <p>
     * An association between a variant and a population, where the variant has particular frequency in the population
     * 
     */
    @JsonProperty("VariantToPopulationAssociation")
    public void setVariantToPopulationAssociation(VariantToPopulationAssociation variantToPopulationAssociation) {
        this.variantToPopulationAssociation = variantToPopulationAssociation;
    }

    /**
     * Zygosity
     * <p>
     * 
     * 
     */
    @JsonProperty("Zygosity")
    public Zygosity getZygosity() {
        return zygosity;
    }

    /**
     * Zygosity
     * <p>
     * 
     * 
     */
    @JsonProperty("Zygosity")
    public void setZygosity(Zygosity zygosity) {
        this.zygosity = zygosity;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("activityAndBehavior", activityAndBehavior).append("anatomicalEntity", anatomicalEntity).append("anatomicalEntityToAnatomicalEntityAssociation", anatomicalEntityToAnatomicalEntityAssociation).append("anatomicalEntityToAnatomicalEntityOntogenicAssociation", anatomicalEntityToAnatomicalEntityOntogenicAssociation).append("anatomicalEntityToAnatomicalEntityPartOfAssociation", anatomicalEntityToAnatomicalEntityPartOfAssociation).append("association", association).append("attribute", attribute).append("biologicalProcess", biologicalProcess).append("biologicalProcessOrActivity", biologicalProcessOrActivity).append("biologicalSex", biologicalSex).append("biosample", biosample).append("biosampleToDiseaseOrPhenotypicFeatureAssociation", biosampleToDiseaseOrPhenotypicFeatureAssociation).append("_case", _case).append("caseToPhenotypicFeatureAssociation", caseToPhenotypicFeatureAssociation).append("cell", cell).append("cellLine", cellLine).append("cellLineToDiseaseOrPhenotypicFeatureAssociation", cellLineToDiseaseOrPhenotypicFeatureAssociation).append("cellularComponent", cellularComponent).append("chemicalSubstance", chemicalSubstance).append("chemicalToDiseaseOrPhenotypicFeatureAssociation", chemicalToDiseaseOrPhenotypicFeatureAssociation).append("chemicalToGeneAssociation", chemicalToGeneAssociation).append("chemicalToPathwayAssociation", chemicalToPathwayAssociation).append("clinicalEntity", clinicalEntity).append("clinicalIntervention", clinicalIntervention).append("clinicalModifier", clinicalModifier).append("clinicalTrial", clinicalTrial).append("codingSequence", codingSequence).append("confidenceLevel", confidenceLevel).append("device", device).append("disease", disease).append("diseaseOrPhenotypicFeature", diseaseOrPhenotypicFeature).append("diseaseOrPhenotypicFeatureAssociationToLocationAssociation", diseaseOrPhenotypicFeatureAssociationToLocationAssociation).append("diseaseToPhenotypicFeatureAssociation", diseaseToPhenotypicFeatureAssociation).append("drug", drug).append("drugExposure", drugExposure).append("environment", environment).append("environmentToPhenotypicFeatureAssociation", environmentToPhenotypicFeatureAssociation).append("environmentalFeature", environmentalFeature).append("environmentalProcess", environmentalProcess).append("evidenceType", evidenceType).append("exon", exon).append("exonToTranscriptRelationship", exonToTranscriptRelationship).append("frequencyQualifier", frequencyQualifier).append("frequencyQuantifier", frequencyQuantifier).append("frequencyValue", frequencyValue).append("functionalAssociation", functionalAssociation).append("gene", gene).append("geneAsAModelOfDiseaseAssociation", geneAsAModelOfDiseaseAssociation).append("geneFamily", geneFamily).append("geneHasVariantThatContributesToDiseaseAssociation", geneHasVariantThatContributesToDiseaseAssociation).append("geneOntologyClass", geneOntologyClass).append("geneOrGeneProduct", geneOrGeneProduct).append("geneProduct", geneProduct).append("geneRegulatoryRelationship", geneRegulatoryRelationship).append("geneToDiseaseAssociation", geneToDiseaseAssociation).append("geneToExpressionSiteAssociation", geneToExpressionSiteAssociation).append("geneToGeneHomologyAssociation", geneToGeneHomologyAssociation).append("geneToGeneProductRelationship", geneToGeneProductRelationship).append("geneToGoTermAssociation", geneToGoTermAssociation).append("geneToPhenotypicFeatureAssociation", geneToPhenotypicFeatureAssociation).append("genome", genome).append("genomicEntity", genomicEntity).append("genomicSequenceLocalization", genomicSequenceLocalization).append("genotype", genotype).append("genotypeToGeneAssociation", genotypeToGeneAssociation).append("genotypeToGenotypePartAssociation", genotypeToGenotypePartAssociation).append("genotypeToPhenotypicFeatureAssociation", genotypeToPhenotypicFeatureAssociation).append("genotypeToVariantAssociation", genotypeToVariantAssociation).append("genotypicSex", genotypicSex).append("geographicLocation", geographicLocation).append("geographicLocationAtTime", geographicLocationAtTime).append("grossAnatomicalStructure", grossAnatomicalStructure).append("haplotype", haplotype).append("individualOrganism", individualOrganism).append("lifeStage", lifeStage).append("macromolecularComplex", macromolecularComplex).append("macromolecularMachine", macromolecularMachine).append("macromolecularMachineToBiologicalProcessAssociation", macromolecularMachineToBiologicalProcessAssociation).append("macromolecularMachineToCellularComponentAssociation", macromolecularMachineToCellularComponentAssociation).append("macromolecularMachineToMolecularActivityAssociation", macromolecularMachineToMolecularActivityAssociation).append("metabolite", metabolite).append("microRNA", microRNA).append("molecularActivity", molecularActivity).append("molecularEntity", molecularEntity).append("namedThing", namedThing).append("noncodingRNAProduct", noncodingRNAProduct).append("occurrent", occurrent).append("onset", onset).append("ontologyClass", ontologyClass).append("organismTaxon", organismTaxon).append("pairwiseGeneOrProteinInteractionAssociation", pairwiseGeneOrProteinInteractionAssociation).append("pathognomonicityQuantifier", pathognomonicityQuantifier).append("pathway", pathway).append("phenomenon", phenomenon).append("phenotypicFeature", phenotypicFeature).append("phenotypicSex", phenotypicSex).append("physiologicalProcess", physiologicalProcess).append("planetaryEntity", planetaryEntity).append("populationOfIndividualOrganisms", populationOfIndividualOrganisms).append("populationToPopulationAssociation", populationToPopulationAssociation).append("procedure", procedure).append("protein", protein).append("proteinIsoform", proteinIsoform).append("provider", provider).append("publication", publication).append("rNAProduct", rNAProduct).append("rNAProductIsoform", rNAProductIsoform).append("relationshipType", relationshipType).append("senstivityQuantifier", senstivityQuantifier).append("sequenceFeatureRelationship", sequenceFeatureRelationship).append("sequenceVariant", sequenceVariant).append("severityValue", severityValue).append("specificityQuantifier", specificityQuantifier).append("transcript", transcript).append("transcriptToGeneRelationship", transcriptToGeneRelationship).append("treatment", treatment).append("variantToDiseaseAssociation", variantToDiseaseAssociation).append("variantToPhenotypicFeatureAssociation", variantToPhenotypicFeatureAssociation).append("variantToPopulationAssociation", variantToPopulationAssociation).append("zygosity", zygosity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(sequenceVariant).append(anatomicalEntityToAnatomicalEntityAssociation).append(confidenceLevel).append(chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature).append(frequencyValue).append(rNAProduct).append(sequenceFeatureRelationship).append(transcriptToGeneRelationship).append(genotypeToPhenotypicFeatureAssociation).append(chemicalToGeneAssociation).append(protein).append(biologicalProcessOrActivity).append(geneProduct).append(macromolecularMachineToCellularComponentAssociation).append(anatomicalEntityToAnatomicalEntityOntogenicAssociation).append(cellularComponent).append(specificityQuantifier).append(gene).append(senstivityQuantifier).append(genotypeToGenotypePartAssociation).append(geographicLocationAtTime).append(macromolecularMachineToMolecularActivityAssociation).append(molecularActivity).append(grossAnatomicalStructure).append(individualOrganism).append(cellLine).append(device).append(geneOntologyClass).append(treatment).append(geographicLocation).append(association).append(pairwiseGeneOrProteinInteractionAssociation).append(phenomenon).append(cell).append(transcript).append(geneToDiseaseAssociation).append(attribute).append(clinicalModifier).append(codingSequence).append(environmentToPhenotypicFeatureAssociation).append(_case).append(frequencyQualifier).append(procedure).append(environmentalProcess).append(onset).append(noncodingRNAProduct).append(chemicalSubstance).append(genome).append(genotypeToGeneAssociation).append(zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation).append(lifeStage).append(ontologyClass).append(pathway).append(frequencyQuantifier).append(variantToDiseaseAssociation).append(geneOrGeneProduct).append(anatomicalEntityToAnatomicalEntityPartOfAssociation).append(macromolecularMachine).append(geneRegulatoryRelationship).append(geneAsAModelOfDiseaseAssociation).append(drug).append(biologicalProcess).append(macromolecularComplex).append(namedThing).append(severityValue).append(caseToPhenotypicFeatureAssociation).append(publication).append(geneHasVariantThatContributesToDiseaseAssociation).append(exonToTranscriptRelationship).append(biosample).append(diseaseOrPhenotypicFeatureAssociationToLocationAssociation).append(molecularEntity).append(geneToExpressionSiteAssociation).append(geneToGoTermAssociation).append(populationToPopulationAssociation).append(drugExposure).append(diseaseToPhenotypicFeatureAssociation).append(chemicalToPathwayAssociation).append(genotypeToVariantAssociation).append(genotype).append(genomicSequenceLocalization).append(geneToGeneHomologyAssociation).append(pathognomonicityQuantifier).append(genotypicSex).append(genomicEntity).append(clinicalTrial).append(activityAndBehavior).append(proteinIsoform).append(variantToPhenotypicFeatureAssociation).append(phenotypicFeature).append(cellLineToDiseaseOrPhenotypicFeatureAssociation).append(planetaryEntity).append(occurrent).append(phenotypicSex).append(macromolecularMachineToBiologicalProcessAssociation).append(rNAProductIsoform).append(metabolite).append(provider).append(organismTaxon).append(geneToGeneProductRelationship).append(physiologicalProcess).append(disease).append(haplotype).append(populationOfIndividualOrganisms).append(relationshipType).append(variantToPopulationAssociation).append(anatomicalEntity).append(clinicalEntity).append(functionalAssociation).append(biologicalSex).append(environment).append(clinicalIntervention).append(evidenceType).append(geneFamily).append(microRNA).append(geneToPhenotypicFeatureAssociation).append(diseaseOrPhenotypicFeature).append(exon).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof BiolinkModel) == false) {
            return false;
        }
        BiolinkModel rhs = ((BiolinkModel) other);
        return new EqualsBuilder().append(sequenceVariant, rhs.sequenceVariant).append(anatomicalEntityToAnatomicalEntityAssociation, rhs.anatomicalEntityToAnatomicalEntityAssociation).append(confidenceLevel, rhs.confidenceLevel).append(chemicalToDiseaseOrPhenotypicFeatureAssociation, rhs.chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature, rhs.environmentalFeature).append(frequencyValue, rhs.frequencyValue).append(rNAProduct, rhs.rNAProduct).append(sequenceFeatureRelationship, rhs.sequenceFeatureRelationship).append(transcriptToGeneRelationship, rhs.transcriptToGeneRelationship).append(genotypeToPhenotypicFeatureAssociation, rhs.genotypeToPhenotypicFeatureAssociation).append(chemicalToGeneAssociation, rhs.chemicalToGeneAssociation).append(protein, rhs.protein).append(biologicalProcessOrActivity, rhs.biologicalProcessOrActivity).append(geneProduct, rhs.geneProduct).append(macromolecularMachineToCellularComponentAssociation, rhs.macromolecularMachineToCellularComponentAssociation).append(anatomicalEntityToAnatomicalEntityOntogenicAssociation, rhs.anatomicalEntityToAnatomicalEntityOntogenicAssociation).append(cellularComponent, rhs.cellularComponent).append(specificityQuantifier, rhs.specificityQuantifier).append(gene, rhs.gene).append(senstivityQuantifier, rhs.senstivityQuantifier).append(genotypeToGenotypePartAssociation, rhs.genotypeToGenotypePartAssociation).append(geographicLocationAtTime, rhs.geographicLocationAtTime).append(macromolecularMachineToMolecularActivityAssociation, rhs.macromolecularMachineToMolecularActivityAssociation).append(molecularActivity, rhs.molecularActivity).append(grossAnatomicalStructure, rhs.grossAnatomicalStructure).append(individualOrganism, rhs.individualOrganism).append(cellLine, rhs.cellLine).append(device, rhs.device).append(geneOntologyClass, rhs.geneOntologyClass).append(treatment, rhs.treatment).append(geographicLocation, rhs.geographicLocation).append(association, rhs.association).append(pairwiseGeneOrProteinInteractionAssociation, rhs.pairwiseGeneOrProteinInteractionAssociation).append(phenomenon, rhs.phenomenon).append(cell, rhs.cell).append(transcript, rhs.transcript).append(geneToDiseaseAssociation, rhs.geneToDiseaseAssociation).append(attribute, rhs.attribute).append(clinicalModifier, rhs.clinicalModifier).append(codingSequence, rhs.codingSequence).append(environmentToPhenotypicFeatureAssociation, rhs.environmentToPhenotypicFeatureAssociation).append(_case, rhs._case).append(frequencyQualifier, rhs.frequencyQualifier).append(procedure, rhs.procedure).append(environmentalProcess, rhs.environmentalProcess).append(onset, rhs.onset).append(noncodingRNAProduct, rhs.noncodingRNAProduct).append(chemicalSubstance, rhs.chemicalSubstance).append(genome, rhs.genome).append(genotypeToGeneAssociation, rhs.genotypeToGeneAssociation).append(zygosity, rhs.zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation, rhs.biosampleToDiseaseOrPhenotypicFeatureAssociation).append(lifeStage, rhs.lifeStage).append(ontologyClass, rhs.ontologyClass).append(pathway, rhs.pathway).append(frequencyQuantifier, rhs.frequencyQuantifier).append(variantToDiseaseAssociation, rhs.variantToDiseaseAssociation).append(geneOrGeneProduct, rhs.geneOrGeneProduct).append(anatomicalEntityToAnatomicalEntityPartOfAssociation, rhs.anatomicalEntityToAnatomicalEntityPartOfAssociation).append(macromolecularMachine, rhs.macromolecularMachine).append(geneRegulatoryRelationship, rhs.geneRegulatoryRelationship).append(geneAsAModelOfDiseaseAssociation, rhs.geneAsAModelOfDiseaseAssociation).append(drug, rhs.drug).append(biologicalProcess, rhs.biologicalProcess).append(macromolecularComplex, rhs.macromolecularComplex).append(namedThing, rhs.namedThing).append(severityValue, rhs.severityValue).append(caseToPhenotypicFeatureAssociation, rhs.caseToPhenotypicFeatureAssociation).append(publication, rhs.publication).append(geneHasVariantThatContributesToDiseaseAssociation, rhs.geneHasVariantThatContributesToDiseaseAssociation).append(exonToTranscriptRelationship, rhs.exonToTranscriptRelationship).append(biosample, rhs.biosample).append(diseaseOrPhenotypicFeatureAssociationToLocationAssociation, rhs.diseaseOrPhenotypicFeatureAssociationToLocationAssociation).append(molecularEntity, rhs.molecularEntity).append(geneToExpressionSiteAssociation, rhs.geneToExpressionSiteAssociation).append(geneToGoTermAssociation, rhs.geneToGoTermAssociation).append(populationToPopulationAssociation, rhs.populationToPopulationAssociation).append(drugExposure, rhs.drugExposure).append(diseaseToPhenotypicFeatureAssociation, rhs.diseaseToPhenotypicFeatureAssociation).append(chemicalToPathwayAssociation, rhs.chemicalToPathwayAssociation).append(genotypeToVariantAssociation, rhs.genotypeToVariantAssociation).append(genotype, rhs.genotype).append(genomicSequenceLocalization, rhs.genomicSequenceLocalization).append(geneToGeneHomologyAssociation, rhs.geneToGeneHomologyAssociation).append(pathognomonicityQuantifier, rhs.pathognomonicityQuantifier).append(genotypicSex, rhs.genotypicSex).append(genomicEntity, rhs.genomicEntity).append(clinicalTrial, rhs.clinicalTrial).append(activityAndBehavior, rhs.activityAndBehavior).append(proteinIsoform, rhs.proteinIsoform).append(variantToPhenotypicFeatureAssociation, rhs.variantToPhenotypicFeatureAssociation).append(phenotypicFeature, rhs.phenotypicFeature).append(cellLineToDiseaseOrPhenotypicFeatureAssociation, rhs.cellLineToDiseaseOrPhenotypicFeatureAssociation).append(planetaryEntity, rhs.planetaryEntity).append(occurrent, rhs.occurrent).append(phenotypicSex, rhs.phenotypicSex).append(macromolecularMachineToBiologicalProcessAssociation, rhs.macromolecularMachineToBiologicalProcessAssociation).append(rNAProductIsoform, rhs.rNAProductIsoform).append(metabolite, rhs.metabolite).append(provider, rhs.provider).append(organismTaxon, rhs.organismTaxon).append(geneToGeneProductRelationship, rhs.geneToGeneProductRelationship).append(physiologicalProcess, rhs.physiologicalProcess).append(disease, rhs.disease).append(haplotype, rhs.haplotype).append(populationOfIndividualOrganisms, rhs.populationOfIndividualOrganisms).append(relationshipType, rhs.relationshipType).append(variantToPopulationAssociation, rhs.variantToPopulationAssociation).append(anatomicalEntity, rhs.anatomicalEntity).append(clinicalEntity, rhs.clinicalEntity).append(functionalAssociation, rhs.functionalAssociation).append(biologicalSex, rhs.biologicalSex).append(environment, rhs.environment).append(clinicalIntervention, rhs.clinicalIntervention).append(evidenceType, rhs.evidenceType).append(geneFamily, rhs.geneFamily).append(microRNA, rhs.microRNA).append(geneToPhenotypicFeatureAssociation, rhs.geneToPhenotypicFeatureAssociation).append(diseaseOrPhenotypicFeature, rhs.diseaseOrPhenotypicFeature).append(exon, rhs.exon).isEquals();
    }

}
