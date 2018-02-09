import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * monarch biolink extensions
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "AnatomicalEntity",
    "AnatomicalEntityPartOfAnatomicalEntityAssociation",
    "AnatomicalEntityToAnatomicalEntityAssociation",
    "AssociationResultSet",
    "Attribute",
    "BiologicalEntity",
    "BiologicalProcess",
    "Biosample",
    "BiosampleToDiseaseOrPhenotypicFeatureAssociation",
    "Case",
    "CaseToPhenotypicFeatureAssociation",
    "Cell",
    "CellularComponent",
    "ChemicalSubstance",
    "ChemicalToDiseaseOrPhenotypicFeatureAssociation",
    "ChemicalToGeneAssociation",
    "ChemicalToPathwayAssociation",
    "ClinicalEntity",
    "ClinicalIntervention",
    "ClinicalTrial",
    "CodingSequence",
    "Cohort",
    "Disease",
    "DiseaseOrPhenotypicFeature",
    "DiseaseToPhenotypicFeatureAssociation",
    "DrugExposure",
    "Environment",
    "EnvironmentToPhenotypicFeatureAssociation",
    "EnvironmentalFeature",
    "EnvironmentalProcess",
    "EvidenceType",
    "Exon",
    "ExonToTranscriptRelationship",
    "FrequencyValue",
    "Gene",
    "GeneFamily",
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
    "GeographicLocation",
    "GeographicLocationAtTime",
    "GrossAnatomicalStructure",
    "IndividualOrganism",
    "LifeStage",
    "MacromolecularComplex",
    "Microrna",
    "MolecularActivity",
    "MolecularActivityToBiologicalProcessAssociation",
    "MolecularActivityToDownstreamMolecularActivityAssociation",
    "MolecularActivityToGeneProductAssociation",
    "MolecularActivityToLocationAssociation",
    "MolecularEntity",
    "MolecularEvent",
    "NamedThing",
    "NoncodingRnaProduct",
    "Occurrent",
    "OntologyClass",
    "OrganismTaxon",
    "PairwiseGeneOrProteinInteractionAssociation",
    "Pathway",
    "PhenotypicFeature",
    "PlanetaryEntity",
    "PopulationOfIndividualOrganisms",
    "PropertyValuePair",
    "Protein",
    "Provider",
    "Publication",
    "RelationshipType",
    "RnaProduct",
    "SequenceFeatureRelationship",
    "SequenceFeatureToSequenceRelationship",
    "SequenceVariant",
    "SeverityValue",
    "TaxonClosureMixin",
    "Transcript",
    "TranscriptToGeneRelationship",
    "Treatment",
    "Zygosity"
})
public class Schema {

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
     * AnatomicalEntityPartOfAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityPartOfAnatomicalEntityAssociation")
    @JsonPropertyDescription("null")
    private AnatomicalEntityPartOfAnatomicalEntityAssociation anatomicalEntityPartOfAnatomicalEntityAssociation;
    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    @JsonPropertyDescription("null")
    private AnatomicalEntityToAnatomicalEntityAssociation anatomicalEntityToAnatomicalEntityAssociation;
    /**
     * AssociationResultSet
     * <p>
     * null
     * 
     */
    @JsonProperty("AssociationResultSet")
    @JsonPropertyDescription("null")
    private AssociationResultSet associationResultSet;
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
     * BiologicalEntity
     * <p>
     * null
     * 
     */
    @JsonProperty("BiologicalEntity")
    @JsonPropertyDescription("null")
    private BiologicalEntity biologicalEntity;
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
     * Biosample
     * <p>
     * null
     * 
     */
    @JsonProperty("Biosample")
    @JsonPropertyDescription("null")
    private Biosample biosample;
    /**
     * BiosampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a biosample and a disease or phenotype
     *   definitional: true
     *   
     * 
     */
    @JsonProperty("BiosampleToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a biosample and a disease or phenotype\n  definitional: true\n  ")
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
     * null
     * 
     */
    @JsonProperty("Cell")
    @JsonPropertyDescription("null")
    private Cell cell;
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
     * may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
     * 
     */
    @JsonProperty("ChemicalSubstance")
    @JsonPropertyDescription("may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part")
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
     * null
     * 
     */
    @JsonProperty("ClinicalIntervention")
    @JsonPropertyDescription("null")
    private ClinicalIntervention clinicalIntervention;
    /**
     * ClinicalTrial
     * <p>
     * null
     * 
     */
    @JsonProperty("ClinicalTrial")
    @JsonPropertyDescription("null")
    private ClinicalTrial clinicalTrial;
    /**
     * CodingSequence
     * <p>
     * null
     * 
     */
    @JsonProperty("CodingSequence")
    @JsonPropertyDescription("null")
    private CodingSequence codingSequence;
    /**
     * Cohort
     * <p>
     * null
     * 
     */
    @JsonProperty("Cohort")
    @JsonPropertyDescription("null")
    private Cohort cohort;
    /**
     * Disease
     * <p>
     * null
     * 
     */
    @JsonProperty("Disease")
    @JsonPropertyDescription("null")
    private Disease disease;
    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    @JsonPropertyDescription("null")
    private DiseaseOrPhenotypicFeature diseaseOrPhenotypicFeature;
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
     * null
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    @JsonPropertyDescription("null")
    private EnvironmentalFeature environmentalFeature;
    /**
     * EnvironmentalProcess
     * <p>
     * null
     * 
     */
    @JsonProperty("EnvironmentalProcess")
    @JsonPropertyDescription("null")
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
     * null
     * 
     */
    @JsonProperty("Exon")
    @JsonPropertyDescription("null")
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
     * FrequencyValue
     * <p>
     * describes the frequency of occurrence of an event or condition
     * 
     */
    @JsonProperty("FrequencyValue")
    @JsonPropertyDescription("describes the frequency of occurrence of an event or condition")
    private FrequencyValue frequencyValue;
    /**
     * Gene
     * <p>
     * null
     * 
     */
    @JsonProperty("Gene")
    @JsonPropertyDescription("null")
    private Gene gene;
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
     * null
     * 
     */
    @JsonProperty("GeneProduct")
    @JsonPropertyDescription("null")
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
     * null
     * 
     */
    @JsonProperty("GeneToDiseaseAssociation")
    @JsonPropertyDescription("null")
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
     * null
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    @JsonPropertyDescription("null")
    private GeneToGoTermAssociation geneToGoTermAssociation;
    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("null")
    private GeneToPhenotypicFeatureAssociation geneToPhenotypicFeatureAssociation;
    /**
     * Genome
     * <p>
     * null
     * 
     */
    @JsonProperty("Genome")
    @JsonPropertyDescription("null")
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
     * null
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    @JsonPropertyDescription("null")
    private GrossAnatomicalStructure grossAnatomicalStructure;
    /**
     * IndividualOrganism
     * <p>
     * null
     * 
     */
    @JsonProperty("IndividualOrganism")
    @JsonPropertyDescription("null")
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
     * null
     * 
     */
    @JsonProperty("MacromolecularComplex")
    @JsonPropertyDescription("null")
    private MacromolecularComplex macromolecularComplex;
    /**
     * Microrna
     * <p>
     * null
     * 
     */
    @JsonProperty("Microrna")
    @JsonPropertyDescription("null")
    private Microrna microrna;
    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function
     * 
     */
    @JsonProperty("MolecularActivity")
    @JsonPropertyDescription("An execution of a molecular function")
    private MolecularActivity molecularActivity;
    /**
     * MolecularActivityToBiologicalProcessAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToBiologicalProcessAssociation")
    @JsonPropertyDescription("null")
    private MolecularActivityToBiologicalProcessAssociation molecularActivityToBiologicalProcessAssociation;
    /**
     * MolecularActivityToDownstreamMolecularActivityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToDownstreamMolecularActivityAssociation")
    @JsonPropertyDescription("null")
    private MolecularActivityToDownstreamMolecularActivityAssociation molecularActivityToDownstreamMolecularActivityAssociation;
    /**
     * MolecularActivityToGeneProductAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToGeneProductAssociation")
    @JsonPropertyDescription("null")
    private MolecularActivityToGeneProductAssociation molecularActivityToGeneProductAssociation;
    /**
     * MolecularActivityToLocationAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToLocationAssociation")
    @JsonPropertyDescription("null")
    private MolecularActivityToLocationAssociation molecularActivityToLocationAssociation;
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
     * MolecularEvent
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularEvent")
    @JsonPropertyDescription("null")
    private MolecularEvent molecularEvent;
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
     * NoncodingRnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("NoncodingRnaProduct")
    @JsonPropertyDescription("null")
    private NoncodingRnaProduct noncodingRnaProduct;
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
     * null
     * 
     */
    @JsonProperty("OrganismTaxon")
    @JsonPropertyDescription("null")
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
     * Pathway
     * <p>
     * null
     * 
     */
    @JsonProperty("Pathway")
    @JsonPropertyDescription("null")
    private Pathway pathway;
    /**
     * PhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("PhenotypicFeature")
    @JsonPropertyDescription("null")
    private PhenotypicFeature phenotypicFeature;
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
     * null
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    @JsonPropertyDescription("null")
    private PopulationOfIndividualOrganisms populationOfIndividualOrganisms;
    /**
     * PropertyValuePair
     * <p>
     * null
     * 
     */
    @JsonProperty("PropertyValuePair")
    @JsonPropertyDescription("null")
    private PropertyValuePair propertyValuePair;
    /**
     * Protein
     * <p>
     * null
     * 
     */
    @JsonProperty("Protein")
    @JsonPropertyDescription("null")
    private Protein protein;
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
     * RelationshipType
     * <p>
     * An OWL property used as an edge label
     * 
     */
    @JsonProperty("RelationshipType")
    @JsonPropertyDescription("An OWL property used as an edge label")
    private RelationshipType relationshipType;
    /**
     * RnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("RnaProduct")
    @JsonPropertyDescription("null")
    private RnaProduct rnaProduct;
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
     * SequenceFeatureToSequenceRelationship
     * <p>
     * Relates a sequence feature such as a gene to its sequence
     * 
     */
    @JsonProperty("SequenceFeatureToSequenceRelationship")
    @JsonPropertyDescription("Relates a sequence feature such as a gene to its sequence")
    private SequenceFeatureToSequenceRelationship sequenceFeatureToSequenceRelationship;
    /**
     * SequenceVariant
     * <p>
     * A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    @JsonPropertyDescription("A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.")
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
     * TaxonClosureMixin
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("TaxonClosureMixin")
    @JsonPropertyDescription("An association that includes flattened inlined objects, such as subject_taxon_closure")
    private TaxonClosureMixin taxonClosureMixin;
    /**
     * Transcript
     * <p>
     * null
     * 
     */
    @JsonProperty("Transcript")
    @JsonPropertyDescription("null")
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
     * Zygosity
     * <p>
     * null
     * 
     */
    @JsonProperty("Zygosity")
    @JsonPropertyDescription("null")
    private Zygosity zygosity;

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
     * AnatomicalEntityPartOfAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityPartOfAnatomicalEntityAssociation")
    public AnatomicalEntityPartOfAnatomicalEntityAssociation getAnatomicalEntityPartOfAnatomicalEntityAssociation() {
        return anatomicalEntityPartOfAnatomicalEntityAssociation;
    }

    /**
     * AnatomicalEntityPartOfAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityPartOfAnatomicalEntityAssociation")
    public void setAnatomicalEntityPartOfAnatomicalEntityAssociation(AnatomicalEntityPartOfAnatomicalEntityAssociation anatomicalEntityPartOfAnatomicalEntityAssociation) {
        this.anatomicalEntityPartOfAnatomicalEntityAssociation = anatomicalEntityPartOfAnatomicalEntityAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    public AnatomicalEntityToAnatomicalEntityAssociation getAnatomicalEntityToAnatomicalEntityAssociation() {
        return anatomicalEntityToAnatomicalEntityAssociation;
    }

    /**
     * AnatomicalEntityToAnatomicalEntityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("AnatomicalEntityToAnatomicalEntityAssociation")
    public void setAnatomicalEntityToAnatomicalEntityAssociation(AnatomicalEntityToAnatomicalEntityAssociation anatomicalEntityToAnatomicalEntityAssociation) {
        this.anatomicalEntityToAnatomicalEntityAssociation = anatomicalEntityToAnatomicalEntityAssociation;
    }

    /**
     * AssociationResultSet
     * <p>
     * null
     * 
     */
    @JsonProperty("AssociationResultSet")
    public AssociationResultSet getAssociationResultSet() {
        return associationResultSet;
    }

    /**
     * AssociationResultSet
     * <p>
     * null
     * 
     */
    @JsonProperty("AssociationResultSet")
    public void setAssociationResultSet(AssociationResultSet associationResultSet) {
        this.associationResultSet = associationResultSet;
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
     * BiologicalEntity
     * <p>
     * null
     * 
     */
    @JsonProperty("BiologicalEntity")
    public BiologicalEntity getBiologicalEntity() {
        return biologicalEntity;
    }

    /**
     * BiologicalEntity
     * <p>
     * null
     * 
     */
    @JsonProperty("BiologicalEntity")
    public void setBiologicalEntity(BiologicalEntity biologicalEntity) {
        this.biologicalEntity = biologicalEntity;
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
     * Biosample
     * <p>
     * null
     * 
     */
    @JsonProperty("Biosample")
    public Biosample getBiosample() {
        return biosample;
    }

    /**
     * Biosample
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("Cell")
    public Cell getCell() {
        return cell;
    }

    /**
     * Cell
     * <p>
     * null
     * 
     */
    @JsonProperty("Cell")
    public void setCell(Cell cell) {
        this.cell = cell;
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
     * may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
     * 
     */
    @JsonProperty("ChemicalSubstance")
    public ChemicalSubstance getChemicalSubstance() {
        return chemicalSubstance;
    }

    /**
     * ChemicalSubstance
     * <p>
     * may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
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
     * null
     * 
     */
    @JsonProperty("ClinicalIntervention")
    public ClinicalIntervention getClinicalIntervention() {
        return clinicalIntervention;
    }

    /**
     * ClinicalIntervention
     * <p>
     * null
     * 
     */
    @JsonProperty("ClinicalIntervention")
    public void setClinicalIntervention(ClinicalIntervention clinicalIntervention) {
        this.clinicalIntervention = clinicalIntervention;
    }

    /**
     * ClinicalTrial
     * <p>
     * null
     * 
     */
    @JsonProperty("ClinicalTrial")
    public ClinicalTrial getClinicalTrial() {
        return clinicalTrial;
    }

    /**
     * ClinicalTrial
     * <p>
     * null
     * 
     */
    @JsonProperty("ClinicalTrial")
    public void setClinicalTrial(ClinicalTrial clinicalTrial) {
        this.clinicalTrial = clinicalTrial;
    }

    /**
     * CodingSequence
     * <p>
     * null
     * 
     */
    @JsonProperty("CodingSequence")
    public CodingSequence getCodingSequence() {
        return codingSequence;
    }

    /**
     * CodingSequence
     * <p>
     * null
     * 
     */
    @JsonProperty("CodingSequence")
    public void setCodingSequence(CodingSequence codingSequence) {
        this.codingSequence = codingSequence;
    }

    /**
     * Cohort
     * <p>
     * null
     * 
     */
    @JsonProperty("Cohort")
    public Cohort getCohort() {
        return cohort;
    }

    /**
     * Cohort
     * <p>
     * null
     * 
     */
    @JsonProperty("Cohort")
    public void setCohort(Cohort cohort) {
        this.cohort = cohort;
    }

    /**
     * Disease
     * <p>
     * null
     * 
     */
    @JsonProperty("Disease")
    public Disease getDisease() {
        return disease;
    }

    /**
     * Disease
     * <p>
     * null
     * 
     */
    @JsonProperty("Disease")
    public void setDisease(Disease disease) {
        this.disease = disease;
    }

    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    public DiseaseOrPhenotypicFeature getDiseaseOrPhenotypicFeature() {
        return diseaseOrPhenotypicFeature;
    }

    /**
     * DiseaseOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseOrPhenotypicFeature")
    public void setDiseaseOrPhenotypicFeature(DiseaseOrPhenotypicFeature diseaseOrPhenotypicFeature) {
        this.diseaseOrPhenotypicFeature = diseaseOrPhenotypicFeature;
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
     * null
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public EnvironmentalFeature getEnvironmentalFeature() {
        return environmentalFeature;
    }

    /**
     * EnvironmentalFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public void setEnvironmentalFeature(EnvironmentalFeature environmentalFeature) {
        this.environmentalFeature = environmentalFeature;
    }

    /**
     * EnvironmentalProcess
     * <p>
     * null
     * 
     */
    @JsonProperty("EnvironmentalProcess")
    public EnvironmentalProcess getEnvironmentalProcess() {
        return environmentalProcess;
    }

    /**
     * EnvironmentalProcess
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("Exon")
    public Exon getExon() {
        return exon;
    }

    /**
     * Exon
     * <p>
     * null
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
     * Gene
     * <p>
     * null
     * 
     */
    @JsonProperty("Gene")
    public Gene getGene() {
        return gene;
    }

    /**
     * Gene
     * <p>
     * null
     * 
     */
    @JsonProperty("Gene")
    public void setGene(Gene gene) {
        this.gene = gene;
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
     * null
     * 
     */
    @JsonProperty("GeneProduct")
    public GeneProduct getGeneProduct() {
        return geneProduct;
    }

    /**
     * GeneProduct
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("GeneToDiseaseAssociation")
    public GeneToDiseaseAssociation getGeneToDiseaseAssociation() {
        return geneToDiseaseAssociation;
    }

    /**
     * GeneToDiseaseAssociation
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    public GeneToGoTermAssociation getGeneToGoTermAssociation() {
        return geneToGoTermAssociation;
    }

    /**
     * GeneToGoTermAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GeneToGoTermAssociation")
    public void setGeneToGoTermAssociation(GeneToGoTermAssociation geneToGoTermAssociation) {
        this.geneToGoTermAssociation = geneToGoTermAssociation;
    }

    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    public GeneToPhenotypicFeatureAssociation getGeneToPhenotypicFeatureAssociation() {
        return geneToPhenotypicFeatureAssociation;
    }

    /**
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    public void setGeneToPhenotypicFeatureAssociation(GeneToPhenotypicFeatureAssociation geneToPhenotypicFeatureAssociation) {
        this.geneToPhenotypicFeatureAssociation = geneToPhenotypicFeatureAssociation;
    }

    /**
     * Genome
     * <p>
     * null
     * 
     */
    @JsonProperty("Genome")
    public Genome getGenome() {
        return genome;
    }

    /**
     * Genome
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    public GrossAnatomicalStructure getGrossAnatomicalStructure() {
        return grossAnatomicalStructure;
    }

    /**
     * GrossAnatomicalStructure
     * <p>
     * null
     * 
     */
    @JsonProperty("GrossAnatomicalStructure")
    public void setGrossAnatomicalStructure(GrossAnatomicalStructure grossAnatomicalStructure) {
        this.grossAnatomicalStructure = grossAnatomicalStructure;
    }

    /**
     * IndividualOrganism
     * <p>
     * null
     * 
     */
    @JsonProperty("IndividualOrganism")
    public IndividualOrganism getIndividualOrganism() {
        return individualOrganism;
    }

    /**
     * IndividualOrganism
     * <p>
     * null
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
     * null
     * 
     */
    @JsonProperty("MacromolecularComplex")
    public MacromolecularComplex getMacromolecularComplex() {
        return macromolecularComplex;
    }

    /**
     * MacromolecularComplex
     * <p>
     * null
     * 
     */
    @JsonProperty("MacromolecularComplex")
    public void setMacromolecularComplex(MacromolecularComplex macromolecularComplex) {
        this.macromolecularComplex = macromolecularComplex;
    }

    /**
     * Microrna
     * <p>
     * null
     * 
     */
    @JsonProperty("Microrna")
    public Microrna getMicrorna() {
        return microrna;
    }

    /**
     * Microrna
     * <p>
     * null
     * 
     */
    @JsonProperty("Microrna")
    public void setMicrorna(Microrna microrna) {
        this.microrna = microrna;
    }

    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function
     * 
     */
    @JsonProperty("MolecularActivity")
    public MolecularActivity getMolecularActivity() {
        return molecularActivity;
    }

    /**
     * MolecularActivity
     * <p>
     * An execution of a molecular function
     * 
     */
    @JsonProperty("MolecularActivity")
    public void setMolecularActivity(MolecularActivity molecularActivity) {
        this.molecularActivity = molecularActivity;
    }

    /**
     * MolecularActivityToBiologicalProcessAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToBiologicalProcessAssociation")
    public MolecularActivityToBiologicalProcessAssociation getMolecularActivityToBiologicalProcessAssociation() {
        return molecularActivityToBiologicalProcessAssociation;
    }

    /**
     * MolecularActivityToBiologicalProcessAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToBiologicalProcessAssociation")
    public void setMolecularActivityToBiologicalProcessAssociation(MolecularActivityToBiologicalProcessAssociation molecularActivityToBiologicalProcessAssociation) {
        this.molecularActivityToBiologicalProcessAssociation = molecularActivityToBiologicalProcessAssociation;
    }

    /**
     * MolecularActivityToDownstreamMolecularActivityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToDownstreamMolecularActivityAssociation")
    public MolecularActivityToDownstreamMolecularActivityAssociation getMolecularActivityToDownstreamMolecularActivityAssociation() {
        return molecularActivityToDownstreamMolecularActivityAssociation;
    }

    /**
     * MolecularActivityToDownstreamMolecularActivityAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToDownstreamMolecularActivityAssociation")
    public void setMolecularActivityToDownstreamMolecularActivityAssociation(MolecularActivityToDownstreamMolecularActivityAssociation molecularActivityToDownstreamMolecularActivityAssociation) {
        this.molecularActivityToDownstreamMolecularActivityAssociation = molecularActivityToDownstreamMolecularActivityAssociation;
    }

    /**
     * MolecularActivityToGeneProductAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToGeneProductAssociation")
    public MolecularActivityToGeneProductAssociation getMolecularActivityToGeneProductAssociation() {
        return molecularActivityToGeneProductAssociation;
    }

    /**
     * MolecularActivityToGeneProductAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToGeneProductAssociation")
    public void setMolecularActivityToGeneProductAssociation(MolecularActivityToGeneProductAssociation molecularActivityToGeneProductAssociation) {
        this.molecularActivityToGeneProductAssociation = molecularActivityToGeneProductAssociation;
    }

    /**
     * MolecularActivityToLocationAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToLocationAssociation")
    public MolecularActivityToLocationAssociation getMolecularActivityToLocationAssociation() {
        return molecularActivityToLocationAssociation;
    }

    /**
     * MolecularActivityToLocationAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularActivityToLocationAssociation")
    public void setMolecularActivityToLocationAssociation(MolecularActivityToLocationAssociation molecularActivityToLocationAssociation) {
        this.molecularActivityToLocationAssociation = molecularActivityToLocationAssociation;
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
     * MolecularEvent
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularEvent")
    public MolecularEvent getMolecularEvent() {
        return molecularEvent;
    }

    /**
     * MolecularEvent
     * <p>
     * null
     * 
     */
    @JsonProperty("MolecularEvent")
    public void setMolecularEvent(MolecularEvent molecularEvent) {
        this.molecularEvent = molecularEvent;
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
     * NoncodingRnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("NoncodingRnaProduct")
    public NoncodingRnaProduct getNoncodingRnaProduct() {
        return noncodingRnaProduct;
    }

    /**
     * NoncodingRnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("NoncodingRnaProduct")
    public void setNoncodingRnaProduct(NoncodingRnaProduct noncodingRnaProduct) {
        this.noncodingRnaProduct = noncodingRnaProduct;
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
     * null
     * 
     */
    @JsonProperty("OrganismTaxon")
    public OrganismTaxon getOrganismTaxon() {
        return organismTaxon;
    }

    /**
     * OrganismTaxon
     * <p>
     * null
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
     * Pathway
     * <p>
     * null
     * 
     */
    @JsonProperty("Pathway")
    public Pathway getPathway() {
        return pathway;
    }

    /**
     * Pathway
     * <p>
     * null
     * 
     */
    @JsonProperty("Pathway")
    public void setPathway(Pathway pathway) {
        this.pathway = pathway;
    }

    /**
     * PhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("PhenotypicFeature")
    public PhenotypicFeature getPhenotypicFeature() {
        return phenotypicFeature;
    }

    /**
     * PhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("PhenotypicFeature")
    public void setPhenotypicFeature(PhenotypicFeature phenotypicFeature) {
        this.phenotypicFeature = phenotypicFeature;
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
     * null
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    public PopulationOfIndividualOrganisms getPopulationOfIndividualOrganisms() {
        return populationOfIndividualOrganisms;
    }

    /**
     * PopulationOfIndividualOrganisms
     * <p>
     * null
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    public void setPopulationOfIndividualOrganisms(PopulationOfIndividualOrganisms populationOfIndividualOrganisms) {
        this.populationOfIndividualOrganisms = populationOfIndividualOrganisms;
    }

    /**
     * PropertyValuePair
     * <p>
     * null
     * 
     */
    @JsonProperty("PropertyValuePair")
    public PropertyValuePair getPropertyValuePair() {
        return propertyValuePair;
    }

    /**
     * PropertyValuePair
     * <p>
     * null
     * 
     */
    @JsonProperty("PropertyValuePair")
    public void setPropertyValuePair(PropertyValuePair propertyValuePair) {
        this.propertyValuePair = propertyValuePair;
    }

    /**
     * Protein
     * <p>
     * null
     * 
     */
    @JsonProperty("Protein")
    public Protein getProtein() {
        return protein;
    }

    /**
     * Protein
     * <p>
     * null
     * 
     */
    @JsonProperty("Protein")
    public void setProtein(Protein protein) {
        this.protein = protein;
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
     * RnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("RnaProduct")
    public RnaProduct getRnaProduct() {
        return rnaProduct;
    }

    /**
     * RnaProduct
     * <p>
     * null
     * 
     */
    @JsonProperty("RnaProduct")
    public void setRnaProduct(RnaProduct rnaProduct) {
        this.rnaProduct = rnaProduct;
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
     * SequenceFeatureToSequenceRelationship
     * <p>
     * Relates a sequence feature such as a gene to its sequence
     * 
     */
    @JsonProperty("SequenceFeatureToSequenceRelationship")
    public SequenceFeatureToSequenceRelationship getSequenceFeatureToSequenceRelationship() {
        return sequenceFeatureToSequenceRelationship;
    }

    /**
     * SequenceFeatureToSequenceRelationship
     * <p>
     * Relates a sequence feature such as a gene to its sequence
     * 
     */
    @JsonProperty("SequenceFeatureToSequenceRelationship")
    public void setSequenceFeatureToSequenceRelationship(SequenceFeatureToSequenceRelationship sequenceFeatureToSequenceRelationship) {
        this.sequenceFeatureToSequenceRelationship = sequenceFeatureToSequenceRelationship;
    }

    /**
     * SequenceVariant
     * <p>
     * A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    public SequenceVariant getSequenceVariant() {
        return sequenceVariant;
    }

    /**
     * SequenceVariant
     * <p>
     * A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
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
     * TaxonClosureMixin
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("TaxonClosureMixin")
    public TaxonClosureMixin getTaxonClosureMixin() {
        return taxonClosureMixin;
    }

    /**
     * TaxonClosureMixin
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("TaxonClosureMixin")
    public void setTaxonClosureMixin(TaxonClosureMixin taxonClosureMixin) {
        this.taxonClosureMixin = taxonClosureMixin;
    }

    /**
     * Transcript
     * <p>
     * null
     * 
     */
    @JsonProperty("Transcript")
    public Transcript getTranscript() {
        return transcript;
    }

    /**
     * Transcript
     * <p>
     * null
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
     * Zygosity
     * <p>
     * null
     * 
     */
    @JsonProperty("Zygosity")
    public Zygosity getZygosity() {
        return zygosity;
    }

    /**
     * Zygosity
     * <p>
     * null
     * 
     */
    @JsonProperty("Zygosity")
    public void setZygosity(Zygosity zygosity) {
        this.zygosity = zygosity;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("anatomicalEntity", anatomicalEntity).append("anatomicalEntityPartOfAnatomicalEntityAssociation", anatomicalEntityPartOfAnatomicalEntityAssociation).append("anatomicalEntityToAnatomicalEntityAssociation", anatomicalEntityToAnatomicalEntityAssociation).append("associationResultSet", associationResultSet).append("attribute", attribute).append("biologicalEntity", biologicalEntity).append("biologicalProcess", biologicalProcess).append("biosample", biosample).append("biosampleToDiseaseOrPhenotypicFeatureAssociation", biosampleToDiseaseOrPhenotypicFeatureAssociation).append("_case", _case).append("caseToPhenotypicFeatureAssociation", caseToPhenotypicFeatureAssociation).append("cell", cell).append("cellularComponent", cellularComponent).append("chemicalSubstance", chemicalSubstance).append("chemicalToDiseaseOrPhenotypicFeatureAssociation", chemicalToDiseaseOrPhenotypicFeatureAssociation).append("chemicalToGeneAssociation", chemicalToGeneAssociation).append("chemicalToPathwayAssociation", chemicalToPathwayAssociation).append("clinicalEntity", clinicalEntity).append("clinicalIntervention", clinicalIntervention).append("clinicalTrial", clinicalTrial).append("codingSequence", codingSequence).append("cohort", cohort).append("disease", disease).append("diseaseOrPhenotypicFeature", diseaseOrPhenotypicFeature).append("diseaseToPhenotypicFeatureAssociation", diseaseToPhenotypicFeatureAssociation).append("drugExposure", drugExposure).append("environment", environment).append("environmentToPhenotypicFeatureAssociation", environmentToPhenotypicFeatureAssociation).append("environmentalFeature", environmentalFeature).append("environmentalProcess", environmentalProcess).append("evidenceType", evidenceType).append("exon", exon).append("exonToTranscriptRelationship", exonToTranscriptRelationship).append("frequencyValue", frequencyValue).append("gene", gene).append("geneFamily", geneFamily).append("geneOntologyClass", geneOntologyClass).append("geneOrGeneProduct", geneOrGeneProduct).append("geneProduct", geneProduct).append("geneRegulatoryRelationship", geneRegulatoryRelationship).append("geneToDiseaseAssociation", geneToDiseaseAssociation).append("geneToExpressionSiteAssociation", geneToExpressionSiteAssociation).append("geneToGeneHomologyAssociation", geneToGeneHomologyAssociation).append("geneToGeneProductRelationship", geneToGeneProductRelationship).append("geneToGoTermAssociation", geneToGoTermAssociation).append("geneToPhenotypicFeatureAssociation", geneToPhenotypicFeatureAssociation).append("genome", genome).append("genomicEntity", genomicEntity).append("genomicSequenceLocalization", genomicSequenceLocalization).append("genotype", genotype).append("genotypeToGeneAssociation", genotypeToGeneAssociation).append("genotypeToGenotypePartAssociation", genotypeToGenotypePartAssociation).append("genotypeToPhenotypicFeatureAssociation", genotypeToPhenotypicFeatureAssociation).append("genotypeToVariantAssociation", genotypeToVariantAssociation).append("geographicLocation", geographicLocation).append("geographicLocationAtTime", geographicLocationAtTime).append("grossAnatomicalStructure", grossAnatomicalStructure).append("individualOrganism", individualOrganism).append("lifeStage", lifeStage).append("macromolecularComplex", macromolecularComplex).append("microrna", microrna).append("molecularActivity", molecularActivity).append("molecularActivityToBiologicalProcessAssociation", molecularActivityToBiologicalProcessAssociation).append("molecularActivityToDownstreamMolecularActivityAssociation", molecularActivityToDownstreamMolecularActivityAssociation).append("molecularActivityToGeneProductAssociation", molecularActivityToGeneProductAssociation).append("molecularActivityToLocationAssociation", molecularActivityToLocationAssociation).append("molecularEntity", molecularEntity).append("molecularEvent", molecularEvent).append("namedThing", namedThing).append("noncodingRnaProduct", noncodingRnaProduct).append("occurrent", occurrent).append("ontologyClass", ontologyClass).append("organismTaxon", organismTaxon).append("pairwiseGeneOrProteinInteractionAssociation", pairwiseGeneOrProteinInteractionAssociation).append("pathway", pathway).append("phenotypicFeature", phenotypicFeature).append("planetaryEntity", planetaryEntity).append("populationOfIndividualOrganisms", populationOfIndividualOrganisms).append("propertyValuePair", propertyValuePair).append("protein", protein).append("provider", provider).append("publication", publication).append("relationshipType", relationshipType).append("rnaProduct", rnaProduct).append("sequenceFeatureRelationship", sequenceFeatureRelationship).append("sequenceFeatureToSequenceRelationship", sequenceFeatureToSequenceRelationship).append("sequenceVariant", sequenceVariant).append("severityValue", severityValue).append("taxonClosureMixin", taxonClosureMixin).append("transcript", transcript).append("transcriptToGeneRelationship", transcriptToGeneRelationship).append("treatment", treatment).append("zygosity", zygosity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(sequenceVariant).append(anatomicalEntityToAnatomicalEntityAssociation).append(geneOrGeneProduct).append(geneRegulatoryRelationship).append(chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature).append(frequencyValue).append(sequenceFeatureRelationship).append(transcriptToGeneRelationship).append(genotypeToPhenotypicFeatureAssociation).append(biologicalProcess).append(macromolecularComplex).append(namedThing).append(chemicalToGeneAssociation).append(molecularEvent).append(severityValue).append(caseToPhenotypicFeatureAssociation).append(molecularActivityToBiologicalProcessAssociation).append(protein).append(publication).append(geneProduct).append(biologicalEntity).append(exonToTranscriptRelationship).append(biosample).append(molecularEntity).append(geneToExpressionSiteAssociation).append(molecularActivityToLocationAssociation).append(geneToGoTermAssociation).append(noncodingRnaProduct).append(cellularComponent).append(drugExposure).append(gene).append(anatomicalEntityPartOfAnatomicalEntityAssociation).append(taxonClosureMixin).append(genotypeToGenotypePartAssociation).append(diseaseToPhenotypicFeatureAssociation).append(chemicalToPathwayAssociation).append(genotypeToVariantAssociation).append(genotype).append(geographicLocationAtTime).append(molecularActivity).append(genomicSequenceLocalization).append(molecularActivityToGeneProductAssociation).append(grossAnatomicalStructure).append(geneToGeneHomologyAssociation).append(individualOrganism).append(geneOntologyClass).append(genomicEntity).append(rnaProduct).append(clinicalTrial).append(treatment).append(geographicLocation).append(molecularActivityToDownstreamMolecularActivityAssociation).append(phenotypicFeature).append(planetaryEntity).append(cohort).append(occurrent).append(pairwiseGeneOrProteinInteractionAssociation).append(sequenceFeatureToSequenceRelationship).append(cell).append(transcript).append(provider).append(geneToDiseaseAssociation).append(organismTaxon).append(microrna).append(attribute).append(geneToGeneProductRelationship).append(codingSequence).append(disease).append(populationOfIndividualOrganisms).append(relationshipType).append(environmentToPhenotypicFeatureAssociation).append(_case).append(associationResultSet).append(environmentalProcess).append(anatomicalEntity).append(chemicalSubstance).append(clinicalEntity).append(genome).append(environment).append(genotypeToGeneAssociation).append(propertyValuePair).append(zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation).append(clinicalIntervention).append(lifeStage).append(evidenceType).append(ontologyClass).append(geneFamily).append(pathway).append(geneToPhenotypicFeatureAssociation).append(diseaseOrPhenotypicFeature).append(exon).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Schema) == false) {
            return false;
        }
        Schema rhs = ((Schema) other);
        return new EqualsBuilder().append(sequenceVariant, rhs.sequenceVariant).append(anatomicalEntityToAnatomicalEntityAssociation, rhs.anatomicalEntityToAnatomicalEntityAssociation).append(geneOrGeneProduct, rhs.geneOrGeneProduct).append(geneRegulatoryRelationship, rhs.geneRegulatoryRelationship).append(chemicalToDiseaseOrPhenotypicFeatureAssociation, rhs.chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature, rhs.environmentalFeature).append(frequencyValue, rhs.frequencyValue).append(sequenceFeatureRelationship, rhs.sequenceFeatureRelationship).append(transcriptToGeneRelationship, rhs.transcriptToGeneRelationship).append(genotypeToPhenotypicFeatureAssociation, rhs.genotypeToPhenotypicFeatureAssociation).append(biologicalProcess, rhs.biologicalProcess).append(macromolecularComplex, rhs.macromolecularComplex).append(namedThing, rhs.namedThing).append(chemicalToGeneAssociation, rhs.chemicalToGeneAssociation).append(molecularEvent, rhs.molecularEvent).append(severityValue, rhs.severityValue).append(caseToPhenotypicFeatureAssociation, rhs.caseToPhenotypicFeatureAssociation).append(molecularActivityToBiologicalProcessAssociation, rhs.molecularActivityToBiologicalProcessAssociation).append(protein, rhs.protein).append(publication, rhs.publication).append(geneProduct, rhs.geneProduct).append(biologicalEntity, rhs.biologicalEntity).append(exonToTranscriptRelationship, rhs.exonToTranscriptRelationship).append(biosample, rhs.biosample).append(molecularEntity, rhs.molecularEntity).append(geneToExpressionSiteAssociation, rhs.geneToExpressionSiteAssociation).append(molecularActivityToLocationAssociation, rhs.molecularActivityToLocationAssociation).append(geneToGoTermAssociation, rhs.geneToGoTermAssociation).append(noncodingRnaProduct, rhs.noncodingRnaProduct).append(cellularComponent, rhs.cellularComponent).append(drugExposure, rhs.drugExposure).append(gene, rhs.gene).append(anatomicalEntityPartOfAnatomicalEntityAssociation, rhs.anatomicalEntityPartOfAnatomicalEntityAssociation).append(taxonClosureMixin, rhs.taxonClosureMixin).append(genotypeToGenotypePartAssociation, rhs.genotypeToGenotypePartAssociation).append(diseaseToPhenotypicFeatureAssociation, rhs.diseaseToPhenotypicFeatureAssociation).append(chemicalToPathwayAssociation, rhs.chemicalToPathwayAssociation).append(genotypeToVariantAssociation, rhs.genotypeToVariantAssociation).append(genotype, rhs.genotype).append(geographicLocationAtTime, rhs.geographicLocationAtTime).append(molecularActivity, rhs.molecularActivity).append(genomicSequenceLocalization, rhs.genomicSequenceLocalization).append(molecularActivityToGeneProductAssociation, rhs.molecularActivityToGeneProductAssociation).append(grossAnatomicalStructure, rhs.grossAnatomicalStructure).append(geneToGeneHomologyAssociation, rhs.geneToGeneHomologyAssociation).append(individualOrganism, rhs.individualOrganism).append(geneOntologyClass, rhs.geneOntologyClass).append(genomicEntity, rhs.genomicEntity).append(rnaProduct, rhs.rnaProduct).append(clinicalTrial, rhs.clinicalTrial).append(treatment, rhs.treatment).append(geographicLocation, rhs.geographicLocation).append(molecularActivityToDownstreamMolecularActivityAssociation, rhs.molecularActivityToDownstreamMolecularActivityAssociation).append(phenotypicFeature, rhs.phenotypicFeature).append(planetaryEntity, rhs.planetaryEntity).append(cohort, rhs.cohort).append(occurrent, rhs.occurrent).append(pairwiseGeneOrProteinInteractionAssociation, rhs.pairwiseGeneOrProteinInteractionAssociation).append(sequenceFeatureToSequenceRelationship, rhs.sequenceFeatureToSequenceRelationship).append(cell, rhs.cell).append(transcript, rhs.transcript).append(provider, rhs.provider).append(geneToDiseaseAssociation, rhs.geneToDiseaseAssociation).append(organismTaxon, rhs.organismTaxon).append(microrna, rhs.microrna).append(attribute, rhs.attribute).append(geneToGeneProductRelationship, rhs.geneToGeneProductRelationship).append(codingSequence, rhs.codingSequence).append(disease, rhs.disease).append(populationOfIndividualOrganisms, rhs.populationOfIndividualOrganisms).append(relationshipType, rhs.relationshipType).append(environmentToPhenotypicFeatureAssociation, rhs.environmentToPhenotypicFeatureAssociation).append(_case, rhs._case).append(associationResultSet, rhs.associationResultSet).append(environmentalProcess, rhs.environmentalProcess).append(anatomicalEntity, rhs.anatomicalEntity).append(chemicalSubstance, rhs.chemicalSubstance).append(clinicalEntity, rhs.clinicalEntity).append(genome, rhs.genome).append(environment, rhs.environment).append(genotypeToGeneAssociation, rhs.genotypeToGeneAssociation).append(propertyValuePair, rhs.propertyValuePair).append(zygosity, rhs.zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation, rhs.biosampleToDiseaseOrPhenotypicFeatureAssociation).append(clinicalIntervention, rhs.clinicalIntervention).append(lifeStage, rhs.lifeStage).append(evidenceType, rhs.evidenceType).append(ontologyClass, rhs.ontologyClass).append(geneFamily, rhs.geneFamily).append(pathway, rhs.pathway).append(geneToPhenotypicFeatureAssociation, rhs.geneToPhenotypicFeatureAssociation).append(diseaseOrPhenotypicFeature, rhs.diseaseOrPhenotypicFeature).append(exon, rhs.exon).isEquals();
    }

}
