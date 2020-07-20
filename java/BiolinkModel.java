import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Biolink-Model
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "AbstractEntity",
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
    "Carbohydrate",
    "Case",
    "CaseToPhenotypicFeatureAssociation",
    "Cell",
    "CellLine",
    "CellLineToDiseaseOrPhenotypicFeatureAssociation",
    "CellularComponent",
    "ChemicalExposure",
    "ChemicalSubstance",
    "ChemicalToChemicalAssociation",
    "ChemicalToChemicalDerivationAssociation",
    "ChemicalToDiseaseOrPhenotypicFeatureAssociation",
    "ChemicalToGeneAssociation",
    "ChemicalToPathwayAssociation",
    "ClinicalEntity",
    "ClinicalIntervention",
    "ClinicalModifier",
    "ClinicalTrial",
    "CodingSequence",
    "ConfidenceLevel",
    "DataFile",
    "DataSet",
    "DataSetSummary",
    "DataSetVersion",
    "Device",
    "Disease",
    "DiseaseOrPhenotypicFeature",
    "DiseaseOrPhenotypicFeatureAssociationToLocationAssociation",
    "DiseaseToExposureAssociation",
    "DiseaseToPhenotypicFeatureAssociation",
    "DistributionLevel",
    "Drug",
    "DrugExposure",
    "EnvironmentalFeature",
    "EnvironmentalProcess",
    "EvidenceType",
    "Exon",
    "ExonToTranscriptRelationship",
    "ExposureEvent",
    "ExposureEventToPhenotypicFeatureAssociation",
    "FrequencyQualifierMixin",
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
    "MaterialSample",
    "MaterialSampleDerivationAssociation",
    "MaterialSampleToDiseaseOrPhenotypicFeatureAssociation",
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
    "PairwiseGeneToGeneInteraction",
    "PathognomonicityQuantifier",
    "Pathway",
    "Phenomenon",
    "PhenotypicFeature",
    "PhenotypicSex",
    "PhysicalEntity",
    "PhysiologicalProcess",
    "PlanetaryEntity",
    "PopulationOfIndividualOrganisms",
    "PopulationToPopulationAssociation",
    "Procedure",
    "Protein",
    "ProteinIsoform",
    "Provider",
    "Publication",
    "QuantityValue",
    "RNAProduct",
    "RNAProductIsoform",
    "RelationshipType",
    "SensitivityQuantifier",
    "SequenceFeatureRelationship",
    "SequenceVariant",
    "SeverityValue",
    "SourceFile",
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
     * AbstractEntity
     * <p>
     * Any thing that is not a process or a physical mass-bearing entity
     * 
     */
    @JsonProperty("AbstractEntity")
    @JsonPropertyDescription("Any thing that is not a process or a physical mass-bearing entity")
    private AbstractEntity abstractEntity;
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
     * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
     * 
     */
    @JsonProperty("Attribute")
    @JsonPropertyDescription("A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.")
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
     * Carbohydrate
     * <p>
     * 
     * 
     */
    @JsonProperty("Carbohydrate")
    @JsonPropertyDescription("")
    private Carbohydrate carbohydrate;
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
     * ChemicalExposure
     * <p>
     * A chemical exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("ChemicalExposure")
    @JsonPropertyDescription("A chemical exposure is an intake of a particular chemical substance")
    private ChemicalExposure chemicalExposure;
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
     * ChemicalToChemicalAssociation
     * <p>
     * A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
     * 
     */
    @JsonProperty("ChemicalToChemicalAssociation")
    @JsonPropertyDescription("A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.")
    private ChemicalToChemicalAssociation chemicalToChemicalAssociation;
    /**
     * ChemicalToChemicalDerivationAssociation
     * <p>
     * A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
     *   IF
     *   R has-input C1 AND
     *   R has-output C2 AND
     *   R enabled-by P AND
     *   R type Reaction
     *   THEN
     *   C1 derives-into C2 <<change is catalyzed by P>>
     * 
     */
    @JsonProperty("ChemicalToChemicalDerivationAssociation")
    @JsonPropertyDescription("A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:\n  IF\n  R has-input C1 AND\n  R has-output C2 AND\n  R enabled-by P AND\n  R type Reaction\n  THEN\n  C1 derives-into C2 <<change is catalyzed by P>>")
    private ChemicalToChemicalDerivationAssociation chemicalToChemicalDerivationAssociation;
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
     * DataFile
     * <p>
     * 
     * 
     */
    @JsonProperty("DataFile")
    @JsonPropertyDescription("")
    private DataFile dataFile;
    /**
     * DataSet
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSet")
    @JsonPropertyDescription("")
    private DataSet dataSet;
    /**
     * DataSetSummary
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetSummary")
    @JsonPropertyDescription("")
    private DataSetSummary dataSetSummary;
    /**
     * DataSetVersion
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetVersion")
    @JsonPropertyDescription("")
    private DataSetVersion dataSetVersion;
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
     * DiseaseToExposureAssociation
     * <p>
     * An association between an exposure event and a disease
     * 
     */
    @JsonProperty("DiseaseToExposureAssociation")
    @JsonPropertyDescription("An association between an exposure event and a disease")
    private DiseaseToExposureAssociation diseaseToExposureAssociation;
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
     * DistributionLevel
     * <p>
     * 
     * 
     */
    @JsonProperty("DistributionLevel")
    @JsonPropertyDescription("")
    private DistributionLevel distributionLevel;
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
     * ExposureEvent
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("ExposureEvent")
    @JsonPropertyDescription("A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes")
    private ExposureEvent exposureEvent;
    /**
     * ExposureEventToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("ExposureEventToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype")
    private ExposureEventToPhenotypicFeatureAssociation exposureEventToPhenotypicFeatureAssociation;
    /**
     * FrequencyQualifierMixin
     * <p>
     * Qualifier for frequency type associations
     * 
     */
    @JsonProperty("FrequencyQualifierMixin")
    @JsonPropertyDescription("Qualifier for frequency type associations")
    private FrequencyQualifierMixin frequencyQualifierMixin;
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
     * MaterialSample
     * <p>
     * A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
     * 
     */
    @JsonProperty("MaterialSample")
    @JsonPropertyDescription("A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]")
    private MaterialSample materialSample;
    /**
     * MaterialSampleDerivationAssociation
     * <p>
     * An association between a material sample and the material entity it is derived from
     * 
     */
    @JsonProperty("MaterialSampleDerivationAssociation")
    @JsonPropertyDescription("An association between a material sample and the material entity it is derived from")
    private MaterialSampleDerivationAssociation materialSampleDerivationAssociation;
    /**
     * MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a material sample and a disease or phenotype
     * 
     */
    @JsonProperty("MaterialSampleToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a material sample and a disease or phenotype")
    private MaterialSampleToDiseaseOrPhenotypicFeatureAssociation materialSampleToDiseaseOrPhenotypicFeatureAssociation;
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
     * PairwiseGeneToGeneInteraction
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneToGeneInteraction")
    @JsonPropertyDescription("An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)")
    private PairwiseGeneToGeneInteraction pairwiseGeneToGeneInteraction;
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
     * PhysicalEntity
     * <p>
     * An entity that has physical properties such as mass, volume, or charge
     * 
     */
    @JsonProperty("PhysicalEntity")
    @JsonPropertyDescription("An entity that has physical properties such as mass, volume, or charge")
    private PhysicalEntity physicalEntity;
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
     * A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    @JsonPropertyDescription("A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]")
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
     * QuantityValue
     * <p>
     * A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
     * 
     */
    @JsonProperty("QuantityValue")
    @JsonPropertyDescription("A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value")
    private QuantityValue quantityValue;
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
     * SensitivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SensitivityQuantifier")
    @JsonPropertyDescription("")
    private SensitivityQuantifier sensitivityQuantifier;
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
     * SourceFile
     * <p>
     * 
     * 
     */
    @JsonProperty("SourceFile")
    @JsonPropertyDescription("")
    private SourceFile sourceFile;
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
     * AbstractEntity
     * <p>
     * Any thing that is not a process or a physical mass-bearing entity
     * 
     */
    @JsonProperty("AbstractEntity")
    public AbstractEntity getAbstractEntity() {
        return abstractEntity;
    }

    /**
     * AbstractEntity
     * <p>
     * Any thing that is not a process or a physical mass-bearing entity
     * 
     */
    @JsonProperty("AbstractEntity")
    public void setAbstractEntity(AbstractEntity abstractEntity) {
        this.abstractEntity = abstractEntity;
    }

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
     * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
     * 
     */
    @JsonProperty("Attribute")
    public Attribute getAttribute() {
        return attribute;
    }

    /**
     * Attribute
     * <p>
     * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
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
     * Carbohydrate
     * <p>
     * 
     * 
     */
    @JsonProperty("Carbohydrate")
    public Carbohydrate getCarbohydrate() {
        return carbohydrate;
    }

    /**
     * Carbohydrate
     * <p>
     * 
     * 
     */
    @JsonProperty("Carbohydrate")
    public void setCarbohydrate(Carbohydrate carbohydrate) {
        this.carbohydrate = carbohydrate;
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
     * ChemicalExposure
     * <p>
     * A chemical exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("ChemicalExposure")
    public ChemicalExposure getChemicalExposure() {
        return chemicalExposure;
    }

    /**
     * ChemicalExposure
     * <p>
     * A chemical exposure is an intake of a particular chemical substance
     * 
     */
    @JsonProperty("ChemicalExposure")
    public void setChemicalExposure(ChemicalExposure chemicalExposure) {
        this.chemicalExposure = chemicalExposure;
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
     * ChemicalToChemicalAssociation
     * <p>
     * A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
     * 
     */
    @JsonProperty("ChemicalToChemicalAssociation")
    public ChemicalToChemicalAssociation getChemicalToChemicalAssociation() {
        return chemicalToChemicalAssociation;
    }

    /**
     * ChemicalToChemicalAssociation
     * <p>
     * A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
     * 
     */
    @JsonProperty("ChemicalToChemicalAssociation")
    public void setChemicalToChemicalAssociation(ChemicalToChemicalAssociation chemicalToChemicalAssociation) {
        this.chemicalToChemicalAssociation = chemicalToChemicalAssociation;
    }

    /**
     * ChemicalToChemicalDerivationAssociation
     * <p>
     * A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
     *   IF
     *   R has-input C1 AND
     *   R has-output C2 AND
     *   R enabled-by P AND
     *   R type Reaction
     *   THEN
     *   C1 derives-into C2 <<change is catalyzed by P>>
     * 
     */
    @JsonProperty("ChemicalToChemicalDerivationAssociation")
    public ChemicalToChemicalDerivationAssociation getChemicalToChemicalDerivationAssociation() {
        return chemicalToChemicalDerivationAssociation;
    }

    /**
     * ChemicalToChemicalDerivationAssociation
     * <p>
     * A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
     *   IF
     *   R has-input C1 AND
     *   R has-output C2 AND
     *   R enabled-by P AND
     *   R type Reaction
     *   THEN
     *   C1 derives-into C2 <<change is catalyzed by P>>
     * 
     */
    @JsonProperty("ChemicalToChemicalDerivationAssociation")
    public void setChemicalToChemicalDerivationAssociation(ChemicalToChemicalDerivationAssociation chemicalToChemicalDerivationAssociation) {
        this.chemicalToChemicalDerivationAssociation = chemicalToChemicalDerivationAssociation;
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
     * DataFile
     * <p>
     * 
     * 
     */
    @JsonProperty("DataFile")
    public DataFile getDataFile() {
        return dataFile;
    }

    /**
     * DataFile
     * <p>
     * 
     * 
     */
    @JsonProperty("DataFile")
    public void setDataFile(DataFile dataFile) {
        this.dataFile = dataFile;
    }

    /**
     * DataSet
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSet")
    public DataSet getDataSet() {
        return dataSet;
    }

    /**
     * DataSet
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSet")
    public void setDataSet(DataSet dataSet) {
        this.dataSet = dataSet;
    }

    /**
     * DataSetSummary
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetSummary")
    public DataSetSummary getDataSetSummary() {
        return dataSetSummary;
    }

    /**
     * DataSetSummary
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetSummary")
    public void setDataSetSummary(DataSetSummary dataSetSummary) {
        this.dataSetSummary = dataSetSummary;
    }

    /**
     * DataSetVersion
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetVersion")
    public DataSetVersion getDataSetVersion() {
        return dataSetVersion;
    }

    /**
     * DataSetVersion
     * <p>
     * 
     * 
     */
    @JsonProperty("DataSetVersion")
    public void setDataSetVersion(DataSetVersion dataSetVersion) {
        this.dataSetVersion = dataSetVersion;
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
     * DiseaseToExposureAssociation
     * <p>
     * An association between an exposure event and a disease
     * 
     */
    @JsonProperty("DiseaseToExposureAssociation")
    public DiseaseToExposureAssociation getDiseaseToExposureAssociation() {
        return diseaseToExposureAssociation;
    }

    /**
     * DiseaseToExposureAssociation
     * <p>
     * An association between an exposure event and a disease
     * 
     */
    @JsonProperty("DiseaseToExposureAssociation")
    public void setDiseaseToExposureAssociation(DiseaseToExposureAssociation diseaseToExposureAssociation) {
        this.diseaseToExposureAssociation = diseaseToExposureAssociation;
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
     * DistributionLevel
     * <p>
     * 
     * 
     */
    @JsonProperty("DistributionLevel")
    public DistributionLevel getDistributionLevel() {
        return distributionLevel;
    }

    /**
     * DistributionLevel
     * <p>
     * 
     * 
     */
    @JsonProperty("DistributionLevel")
    public void setDistributionLevel(DistributionLevel distributionLevel) {
        this.distributionLevel = distributionLevel;
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
     * ExposureEvent
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("ExposureEvent")
    public ExposureEvent getExposureEvent() {
        return exposureEvent;
    }

    /**
     * ExposureEvent
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("ExposureEvent")
    public void setExposureEvent(ExposureEvent exposureEvent) {
        this.exposureEvent = exposureEvent;
    }

    /**
     * ExposureEventToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("ExposureEventToPhenotypicFeatureAssociation")
    public ExposureEventToPhenotypicFeatureAssociation getExposureEventToPhenotypicFeatureAssociation() {
        return exposureEventToPhenotypicFeatureAssociation;
    }

    /**
     * ExposureEventToPhenotypicFeatureAssociation
     * <p>
     * Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
     * 
     */
    @JsonProperty("ExposureEventToPhenotypicFeatureAssociation")
    public void setExposureEventToPhenotypicFeatureAssociation(ExposureEventToPhenotypicFeatureAssociation exposureEventToPhenotypicFeatureAssociation) {
        this.exposureEventToPhenotypicFeatureAssociation = exposureEventToPhenotypicFeatureAssociation;
    }

    /**
     * FrequencyQualifierMixin
     * <p>
     * Qualifier for frequency type associations
     * 
     */
    @JsonProperty("FrequencyQualifierMixin")
    public FrequencyQualifierMixin getFrequencyQualifierMixin() {
        return frequencyQualifierMixin;
    }

    /**
     * FrequencyQualifierMixin
     * <p>
     * Qualifier for frequency type associations
     * 
     */
    @JsonProperty("FrequencyQualifierMixin")
    public void setFrequencyQualifierMixin(FrequencyQualifierMixin frequencyQualifierMixin) {
        this.frequencyQualifierMixin = frequencyQualifierMixin;
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
     * MaterialSample
     * <p>
     * A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
     * 
     */
    @JsonProperty("MaterialSample")
    public MaterialSample getMaterialSample() {
        return materialSample;
    }

    /**
     * MaterialSample
     * <p>
     * A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
     * 
     */
    @JsonProperty("MaterialSample")
    public void setMaterialSample(MaterialSample materialSample) {
        this.materialSample = materialSample;
    }

    /**
     * MaterialSampleDerivationAssociation
     * <p>
     * An association between a material sample and the material entity it is derived from
     * 
     */
    @JsonProperty("MaterialSampleDerivationAssociation")
    public MaterialSampleDerivationAssociation getMaterialSampleDerivationAssociation() {
        return materialSampleDerivationAssociation;
    }

    /**
     * MaterialSampleDerivationAssociation
     * <p>
     * An association between a material sample and the material entity it is derived from
     * 
     */
    @JsonProperty("MaterialSampleDerivationAssociation")
    public void setMaterialSampleDerivationAssociation(MaterialSampleDerivationAssociation materialSampleDerivationAssociation) {
        this.materialSampleDerivationAssociation = materialSampleDerivationAssociation;
    }

    /**
     * MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a material sample and a disease or phenotype
     * 
     */
    @JsonProperty("MaterialSampleToDiseaseOrPhenotypicFeatureAssociation")
    public MaterialSampleToDiseaseOrPhenotypicFeatureAssociation getMaterialSampleToDiseaseOrPhenotypicFeatureAssociation() {
        return materialSampleToDiseaseOrPhenotypicFeatureAssociation;
    }

    /**
     * MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
     * <p>
     * An association between a material sample and a disease or phenotype
     * 
     */
    @JsonProperty("MaterialSampleToDiseaseOrPhenotypicFeatureAssociation")
    public void setMaterialSampleToDiseaseOrPhenotypicFeatureAssociation(MaterialSampleToDiseaseOrPhenotypicFeatureAssociation materialSampleToDiseaseOrPhenotypicFeatureAssociation) {
        this.materialSampleToDiseaseOrPhenotypicFeatureAssociation = materialSampleToDiseaseOrPhenotypicFeatureAssociation;
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
     * PairwiseGeneToGeneInteraction
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneToGeneInteraction")
    public PairwiseGeneToGeneInteraction getPairwiseGeneToGeneInteraction() {
        return pairwiseGeneToGeneInteraction;
    }

    /**
     * PairwiseGeneToGeneInteraction
     * <p>
     * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
     * 
     */
    @JsonProperty("PairwiseGeneToGeneInteraction")
    public void setPairwiseGeneToGeneInteraction(PairwiseGeneToGeneInteraction pairwiseGeneToGeneInteraction) {
        this.pairwiseGeneToGeneInteraction = pairwiseGeneToGeneInteraction;
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
     * PhysicalEntity
     * <p>
     * An entity that has physical properties such as mass, volume, or charge
     * 
     */
    @JsonProperty("PhysicalEntity")
    public PhysicalEntity getPhysicalEntity() {
        return physicalEntity;
    }

    /**
     * PhysicalEntity
     * <p>
     * An entity that has physical properties such as mass, volume, or charge
     * 
     */
    @JsonProperty("PhysicalEntity")
    public void setPhysicalEntity(PhysicalEntity physicalEntity) {
        this.physicalEntity = physicalEntity;
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
     * A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
     * 
     */
    @JsonProperty("PopulationOfIndividualOrganisms")
    public PopulationOfIndividualOrganisms getPopulationOfIndividualOrganisms() {
        return populationOfIndividualOrganisms;
    }

    /**
     * PopulationOfIndividualOrganisms
     * <p>
     * A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
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
     * QuantityValue
     * <p>
     * A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
     * 
     */
    @JsonProperty("QuantityValue")
    public QuantityValue getQuantityValue() {
        return quantityValue;
    }

    /**
     * QuantityValue
     * <p>
     * A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
     * 
     */
    @JsonProperty("QuantityValue")
    public void setQuantityValue(QuantityValue quantityValue) {
        this.quantityValue = quantityValue;
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
     * SensitivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SensitivityQuantifier")
    public SensitivityQuantifier getSensitivityQuantifier() {
        return sensitivityQuantifier;
    }

    /**
     * SensitivityQuantifier
     * <p>
     * 
     * 
     */
    @JsonProperty("SensitivityQuantifier")
    public void setSensitivityQuantifier(SensitivityQuantifier sensitivityQuantifier) {
        this.sensitivityQuantifier = sensitivityQuantifier;
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
     * SourceFile
     * <p>
     * 
     * 
     */
    @JsonProperty("SourceFile")
    public SourceFile getSourceFile() {
        return sourceFile;
    }

    /**
     * SourceFile
     * <p>
     * 
     * 
     */
    @JsonProperty("SourceFile")
    public void setSourceFile(SourceFile sourceFile) {
        this.sourceFile = sourceFile;
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
        StringBuilder sb = new StringBuilder();
        sb.append(BiolinkModel.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("abstractEntity");
        sb.append('=');
        sb.append(((this.abstractEntity == null)?"<null>":this.abstractEntity));
        sb.append(',');
        sb.append("activityAndBehavior");
        sb.append('=');
        sb.append(((this.activityAndBehavior == null)?"<null>":this.activityAndBehavior));
        sb.append(',');
        sb.append("anatomicalEntity");
        sb.append('=');
        sb.append(((this.anatomicalEntity == null)?"<null>":this.anatomicalEntity));
        sb.append(',');
        sb.append("anatomicalEntityToAnatomicalEntityAssociation");
        sb.append('=');
        sb.append(((this.anatomicalEntityToAnatomicalEntityAssociation == null)?"<null>":this.anatomicalEntityToAnatomicalEntityAssociation));
        sb.append(',');
        sb.append("anatomicalEntityToAnatomicalEntityOntogenicAssociation");
        sb.append('=');
        sb.append(((this.anatomicalEntityToAnatomicalEntityOntogenicAssociation == null)?"<null>":this.anatomicalEntityToAnatomicalEntityOntogenicAssociation));
        sb.append(',');
        sb.append("anatomicalEntityToAnatomicalEntityPartOfAssociation");
        sb.append('=');
        sb.append(((this.anatomicalEntityToAnatomicalEntityPartOfAssociation == null)?"<null>":this.anatomicalEntityToAnatomicalEntityPartOfAssociation));
        sb.append(',');
        sb.append("association");
        sb.append('=');
        sb.append(((this.association == null)?"<null>":this.association));
        sb.append(',');
        sb.append("attribute");
        sb.append('=');
        sb.append(((this.attribute == null)?"<null>":this.attribute));
        sb.append(',');
        sb.append("biologicalProcess");
        sb.append('=');
        sb.append(((this.biologicalProcess == null)?"<null>":this.biologicalProcess));
        sb.append(',');
        sb.append("biologicalProcessOrActivity");
        sb.append('=');
        sb.append(((this.biologicalProcessOrActivity == null)?"<null>":this.biologicalProcessOrActivity));
        sb.append(',');
        sb.append("biologicalSex");
        sb.append('=');
        sb.append(((this.biologicalSex == null)?"<null>":this.biologicalSex));
        sb.append(',');
        sb.append("carbohydrate");
        sb.append('=');
        sb.append(((this.carbohydrate == null)?"<null>":this.carbohydrate));
        sb.append(',');
        sb.append("_case");
        sb.append('=');
        sb.append(((this._case == null)?"<null>":this._case));
        sb.append(',');
        sb.append("caseToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.caseToPhenotypicFeatureAssociation == null)?"<null>":this.caseToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("cell");
        sb.append('=');
        sb.append(((this.cell == null)?"<null>":this.cell));
        sb.append(',');
        sb.append("cellLine");
        sb.append('=');
        sb.append(((this.cellLine == null)?"<null>":this.cellLine));
        sb.append(',');
        sb.append("cellLineToDiseaseOrPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.cellLineToDiseaseOrPhenotypicFeatureAssociation == null)?"<null>":this.cellLineToDiseaseOrPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("cellularComponent");
        sb.append('=');
        sb.append(((this.cellularComponent == null)?"<null>":this.cellularComponent));
        sb.append(',');
        sb.append("chemicalExposure");
        sb.append('=');
        sb.append(((this.chemicalExposure == null)?"<null>":this.chemicalExposure));
        sb.append(',');
        sb.append("chemicalSubstance");
        sb.append('=');
        sb.append(((this.chemicalSubstance == null)?"<null>":this.chemicalSubstance));
        sb.append(',');
        sb.append("chemicalToChemicalAssociation");
        sb.append('=');
        sb.append(((this.chemicalToChemicalAssociation == null)?"<null>":this.chemicalToChemicalAssociation));
        sb.append(',');
        sb.append("chemicalToChemicalDerivationAssociation");
        sb.append('=');
        sb.append(((this.chemicalToChemicalDerivationAssociation == null)?"<null>":this.chemicalToChemicalDerivationAssociation));
        sb.append(',');
        sb.append("chemicalToDiseaseOrPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.chemicalToDiseaseOrPhenotypicFeatureAssociation == null)?"<null>":this.chemicalToDiseaseOrPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("chemicalToGeneAssociation");
        sb.append('=');
        sb.append(((this.chemicalToGeneAssociation == null)?"<null>":this.chemicalToGeneAssociation));
        sb.append(',');
        sb.append("chemicalToPathwayAssociation");
        sb.append('=');
        sb.append(((this.chemicalToPathwayAssociation == null)?"<null>":this.chemicalToPathwayAssociation));
        sb.append(',');
        sb.append("clinicalEntity");
        sb.append('=');
        sb.append(((this.clinicalEntity == null)?"<null>":this.clinicalEntity));
        sb.append(',');
        sb.append("clinicalIntervention");
        sb.append('=');
        sb.append(((this.clinicalIntervention == null)?"<null>":this.clinicalIntervention));
        sb.append(',');
        sb.append("clinicalModifier");
        sb.append('=');
        sb.append(((this.clinicalModifier == null)?"<null>":this.clinicalModifier));
        sb.append(',');
        sb.append("clinicalTrial");
        sb.append('=');
        sb.append(((this.clinicalTrial == null)?"<null>":this.clinicalTrial));
        sb.append(',');
        sb.append("codingSequence");
        sb.append('=');
        sb.append(((this.codingSequence == null)?"<null>":this.codingSequence));
        sb.append(',');
        sb.append("confidenceLevel");
        sb.append('=');
        sb.append(((this.confidenceLevel == null)?"<null>":this.confidenceLevel));
        sb.append(',');
        sb.append("dataFile");
        sb.append('=');
        sb.append(((this.dataFile == null)?"<null>":this.dataFile));
        sb.append(',');
        sb.append("dataSet");
        sb.append('=');
        sb.append(((this.dataSet == null)?"<null>":this.dataSet));
        sb.append(',');
        sb.append("dataSetSummary");
        sb.append('=');
        sb.append(((this.dataSetSummary == null)?"<null>":this.dataSetSummary));
        sb.append(',');
        sb.append("dataSetVersion");
        sb.append('=');
        sb.append(((this.dataSetVersion == null)?"<null>":this.dataSetVersion));
        sb.append(',');
        sb.append("device");
        sb.append('=');
        sb.append(((this.device == null)?"<null>":this.device));
        sb.append(',');
        sb.append("disease");
        sb.append('=');
        sb.append(((this.disease == null)?"<null>":this.disease));
        sb.append(',');
        sb.append("diseaseOrPhenotypicFeature");
        sb.append('=');
        sb.append(((this.diseaseOrPhenotypicFeature == null)?"<null>":this.diseaseOrPhenotypicFeature));
        sb.append(',');
        sb.append("diseaseOrPhenotypicFeatureAssociationToLocationAssociation");
        sb.append('=');
        sb.append(((this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation == null)?"<null>":this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation));
        sb.append(',');
        sb.append("diseaseToExposureAssociation");
        sb.append('=');
        sb.append(((this.diseaseToExposureAssociation == null)?"<null>":this.diseaseToExposureAssociation));
        sb.append(',');
        sb.append("diseaseToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.diseaseToPhenotypicFeatureAssociation == null)?"<null>":this.diseaseToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("distributionLevel");
        sb.append('=');
        sb.append(((this.distributionLevel == null)?"<null>":this.distributionLevel));
        sb.append(',');
        sb.append("drug");
        sb.append('=');
        sb.append(((this.drug == null)?"<null>":this.drug));
        sb.append(',');
        sb.append("drugExposure");
        sb.append('=');
        sb.append(((this.drugExposure == null)?"<null>":this.drugExposure));
        sb.append(',');
        sb.append("environmentalFeature");
        sb.append('=');
        sb.append(((this.environmentalFeature == null)?"<null>":this.environmentalFeature));
        sb.append(',');
        sb.append("environmentalProcess");
        sb.append('=');
        sb.append(((this.environmentalProcess == null)?"<null>":this.environmentalProcess));
        sb.append(',');
        sb.append("evidenceType");
        sb.append('=');
        sb.append(((this.evidenceType == null)?"<null>":this.evidenceType));
        sb.append(',');
        sb.append("exon");
        sb.append('=');
        sb.append(((this.exon == null)?"<null>":this.exon));
        sb.append(',');
        sb.append("exonToTranscriptRelationship");
        sb.append('=');
        sb.append(((this.exonToTranscriptRelationship == null)?"<null>":this.exonToTranscriptRelationship));
        sb.append(',');
        sb.append("exposureEvent");
        sb.append('=');
        sb.append(((this.exposureEvent == null)?"<null>":this.exposureEvent));
        sb.append(',');
        sb.append("exposureEventToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.exposureEventToPhenotypicFeatureAssociation == null)?"<null>":this.exposureEventToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("frequencyQualifierMixin");
        sb.append('=');
        sb.append(((this.frequencyQualifierMixin == null)?"<null>":this.frequencyQualifierMixin));
        sb.append(',');
        sb.append("frequencyQuantifier");
        sb.append('=');
        sb.append(((this.frequencyQuantifier == null)?"<null>":this.frequencyQuantifier));
        sb.append(',');
        sb.append("frequencyValue");
        sb.append('=');
        sb.append(((this.frequencyValue == null)?"<null>":this.frequencyValue));
        sb.append(',');
        sb.append("functionalAssociation");
        sb.append('=');
        sb.append(((this.functionalAssociation == null)?"<null>":this.functionalAssociation));
        sb.append(',');
        sb.append("gene");
        sb.append('=');
        sb.append(((this.gene == null)?"<null>":this.gene));
        sb.append(',');
        sb.append("geneAsAModelOfDiseaseAssociation");
        sb.append('=');
        sb.append(((this.geneAsAModelOfDiseaseAssociation == null)?"<null>":this.geneAsAModelOfDiseaseAssociation));
        sb.append(',');
        sb.append("geneFamily");
        sb.append('=');
        sb.append(((this.geneFamily == null)?"<null>":this.geneFamily));
        sb.append(',');
        sb.append("geneHasVariantThatContributesToDiseaseAssociation");
        sb.append('=');
        sb.append(((this.geneHasVariantThatContributesToDiseaseAssociation == null)?"<null>":this.geneHasVariantThatContributesToDiseaseAssociation));
        sb.append(',');
        sb.append("geneOntologyClass");
        sb.append('=');
        sb.append(((this.geneOntologyClass == null)?"<null>":this.geneOntologyClass));
        sb.append(',');
        sb.append("geneOrGeneProduct");
        sb.append('=');
        sb.append(((this.geneOrGeneProduct == null)?"<null>":this.geneOrGeneProduct));
        sb.append(',');
        sb.append("geneProduct");
        sb.append('=');
        sb.append(((this.geneProduct == null)?"<null>":this.geneProduct));
        sb.append(',');
        sb.append("geneRegulatoryRelationship");
        sb.append('=');
        sb.append(((this.geneRegulatoryRelationship == null)?"<null>":this.geneRegulatoryRelationship));
        sb.append(',');
        sb.append("geneToDiseaseAssociation");
        sb.append('=');
        sb.append(((this.geneToDiseaseAssociation == null)?"<null>":this.geneToDiseaseAssociation));
        sb.append(',');
        sb.append("geneToExpressionSiteAssociation");
        sb.append('=');
        sb.append(((this.geneToExpressionSiteAssociation == null)?"<null>":this.geneToExpressionSiteAssociation));
        sb.append(',');
        sb.append("geneToGeneHomologyAssociation");
        sb.append('=');
        sb.append(((this.geneToGeneHomologyAssociation == null)?"<null>":this.geneToGeneHomologyAssociation));
        sb.append(',');
        sb.append("geneToGeneProductRelationship");
        sb.append('=');
        sb.append(((this.geneToGeneProductRelationship == null)?"<null>":this.geneToGeneProductRelationship));
        sb.append(',');
        sb.append("geneToGoTermAssociation");
        sb.append('=');
        sb.append(((this.geneToGoTermAssociation == null)?"<null>":this.geneToGoTermAssociation));
        sb.append(',');
        sb.append("geneToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.geneToPhenotypicFeatureAssociation == null)?"<null>":this.geneToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("genome");
        sb.append('=');
        sb.append(((this.genome == null)?"<null>":this.genome));
        sb.append(',');
        sb.append("genomicEntity");
        sb.append('=');
        sb.append(((this.genomicEntity == null)?"<null>":this.genomicEntity));
        sb.append(',');
        sb.append("genomicSequenceLocalization");
        sb.append('=');
        sb.append(((this.genomicSequenceLocalization == null)?"<null>":this.genomicSequenceLocalization));
        sb.append(',');
        sb.append("genotype");
        sb.append('=');
        sb.append(((this.genotype == null)?"<null>":this.genotype));
        sb.append(',');
        sb.append("genotypeToGeneAssociation");
        sb.append('=');
        sb.append(((this.genotypeToGeneAssociation == null)?"<null>":this.genotypeToGeneAssociation));
        sb.append(',');
        sb.append("genotypeToGenotypePartAssociation");
        sb.append('=');
        sb.append(((this.genotypeToGenotypePartAssociation == null)?"<null>":this.genotypeToGenotypePartAssociation));
        sb.append(',');
        sb.append("genotypeToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.genotypeToPhenotypicFeatureAssociation == null)?"<null>":this.genotypeToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("genotypeToVariantAssociation");
        sb.append('=');
        sb.append(((this.genotypeToVariantAssociation == null)?"<null>":this.genotypeToVariantAssociation));
        sb.append(',');
        sb.append("genotypicSex");
        sb.append('=');
        sb.append(((this.genotypicSex == null)?"<null>":this.genotypicSex));
        sb.append(',');
        sb.append("geographicLocation");
        sb.append('=');
        sb.append(((this.geographicLocation == null)?"<null>":this.geographicLocation));
        sb.append(',');
        sb.append("geographicLocationAtTime");
        sb.append('=');
        sb.append(((this.geographicLocationAtTime == null)?"<null>":this.geographicLocationAtTime));
        sb.append(',');
        sb.append("grossAnatomicalStructure");
        sb.append('=');
        sb.append(((this.grossAnatomicalStructure == null)?"<null>":this.grossAnatomicalStructure));
        sb.append(',');
        sb.append("haplotype");
        sb.append('=');
        sb.append(((this.haplotype == null)?"<null>":this.haplotype));
        sb.append(',');
        sb.append("individualOrganism");
        sb.append('=');
        sb.append(((this.individualOrganism == null)?"<null>":this.individualOrganism));
        sb.append(',');
        sb.append("lifeStage");
        sb.append('=');
        sb.append(((this.lifeStage == null)?"<null>":this.lifeStage));
        sb.append(',');
        sb.append("macromolecularComplex");
        sb.append('=');
        sb.append(((this.macromolecularComplex == null)?"<null>":this.macromolecularComplex));
        sb.append(',');
        sb.append("macromolecularMachine");
        sb.append('=');
        sb.append(((this.macromolecularMachine == null)?"<null>":this.macromolecularMachine));
        sb.append(',');
        sb.append("macromolecularMachineToBiologicalProcessAssociation");
        sb.append('=');
        sb.append(((this.macromolecularMachineToBiologicalProcessAssociation == null)?"<null>":this.macromolecularMachineToBiologicalProcessAssociation));
        sb.append(',');
        sb.append("macromolecularMachineToCellularComponentAssociation");
        sb.append('=');
        sb.append(((this.macromolecularMachineToCellularComponentAssociation == null)?"<null>":this.macromolecularMachineToCellularComponentAssociation));
        sb.append(',');
        sb.append("macromolecularMachineToMolecularActivityAssociation");
        sb.append('=');
        sb.append(((this.macromolecularMachineToMolecularActivityAssociation == null)?"<null>":this.macromolecularMachineToMolecularActivityAssociation));
        sb.append(',');
        sb.append("materialSample");
        sb.append('=');
        sb.append(((this.materialSample == null)?"<null>":this.materialSample));
        sb.append(',');
        sb.append("materialSampleDerivationAssociation");
        sb.append('=');
        sb.append(((this.materialSampleDerivationAssociation == null)?"<null>":this.materialSampleDerivationAssociation));
        sb.append(',');
        sb.append("materialSampleToDiseaseOrPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.materialSampleToDiseaseOrPhenotypicFeatureAssociation == null)?"<null>":this.materialSampleToDiseaseOrPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("metabolite");
        sb.append('=');
        sb.append(((this.metabolite == null)?"<null>":this.metabolite));
        sb.append(',');
        sb.append("microRNA");
        sb.append('=');
        sb.append(((this.microRNA == null)?"<null>":this.microRNA));
        sb.append(',');
        sb.append("molecularActivity");
        sb.append('=');
        sb.append(((this.molecularActivity == null)?"<null>":this.molecularActivity));
        sb.append(',');
        sb.append("molecularEntity");
        sb.append('=');
        sb.append(((this.molecularEntity == null)?"<null>":this.molecularEntity));
        sb.append(',');
        sb.append("namedThing");
        sb.append('=');
        sb.append(((this.namedThing == null)?"<null>":this.namedThing));
        sb.append(',');
        sb.append("noncodingRNAProduct");
        sb.append('=');
        sb.append(((this.noncodingRNAProduct == null)?"<null>":this.noncodingRNAProduct));
        sb.append(',');
        sb.append("occurrent");
        sb.append('=');
        sb.append(((this.occurrent == null)?"<null>":this.occurrent));
        sb.append(',');
        sb.append("onset");
        sb.append('=');
        sb.append(((this.onset == null)?"<null>":this.onset));
        sb.append(',');
        sb.append("ontologyClass");
        sb.append('=');
        sb.append(((this.ontologyClass == null)?"<null>":this.ontologyClass));
        sb.append(',');
        sb.append("organismTaxon");
        sb.append('=');
        sb.append(((this.organismTaxon == null)?"<null>":this.organismTaxon));
        sb.append(',');
        sb.append("pairwiseGeneToGeneInteraction");
        sb.append('=');
        sb.append(((this.pairwiseGeneToGeneInteraction == null)?"<null>":this.pairwiseGeneToGeneInteraction));
        sb.append(',');
        sb.append("pathognomonicityQuantifier");
        sb.append('=');
        sb.append(((this.pathognomonicityQuantifier == null)?"<null>":this.pathognomonicityQuantifier));
        sb.append(',');
        sb.append("pathway");
        sb.append('=');
        sb.append(((this.pathway == null)?"<null>":this.pathway));
        sb.append(',');
        sb.append("phenomenon");
        sb.append('=');
        sb.append(((this.phenomenon == null)?"<null>":this.phenomenon));
        sb.append(',');
        sb.append("phenotypicFeature");
        sb.append('=');
        sb.append(((this.phenotypicFeature == null)?"<null>":this.phenotypicFeature));
        sb.append(',');
        sb.append("phenotypicSex");
        sb.append('=');
        sb.append(((this.phenotypicSex == null)?"<null>":this.phenotypicSex));
        sb.append(',');
        sb.append("physicalEntity");
        sb.append('=');
        sb.append(((this.physicalEntity == null)?"<null>":this.physicalEntity));
        sb.append(',');
        sb.append("physiologicalProcess");
        sb.append('=');
        sb.append(((this.physiologicalProcess == null)?"<null>":this.physiologicalProcess));
        sb.append(',');
        sb.append("planetaryEntity");
        sb.append('=');
        sb.append(((this.planetaryEntity == null)?"<null>":this.planetaryEntity));
        sb.append(',');
        sb.append("populationOfIndividualOrganisms");
        sb.append('=');
        sb.append(((this.populationOfIndividualOrganisms == null)?"<null>":this.populationOfIndividualOrganisms));
        sb.append(',');
        sb.append("populationToPopulationAssociation");
        sb.append('=');
        sb.append(((this.populationToPopulationAssociation == null)?"<null>":this.populationToPopulationAssociation));
        sb.append(',');
        sb.append("procedure");
        sb.append('=');
        sb.append(((this.procedure == null)?"<null>":this.procedure));
        sb.append(',');
        sb.append("protein");
        sb.append('=');
        sb.append(((this.protein == null)?"<null>":this.protein));
        sb.append(',');
        sb.append("proteinIsoform");
        sb.append('=');
        sb.append(((this.proteinIsoform == null)?"<null>":this.proteinIsoform));
        sb.append(',');
        sb.append("provider");
        sb.append('=');
        sb.append(((this.provider == null)?"<null>":this.provider));
        sb.append(',');
        sb.append("publication");
        sb.append('=');
        sb.append(((this.publication == null)?"<null>":this.publication));
        sb.append(',');
        sb.append("quantityValue");
        sb.append('=');
        sb.append(((this.quantityValue == null)?"<null>":this.quantityValue));
        sb.append(',');
        sb.append("rNAProduct");
        sb.append('=');
        sb.append(((this.rNAProduct == null)?"<null>":this.rNAProduct));
        sb.append(',');
        sb.append("rNAProductIsoform");
        sb.append('=');
        sb.append(((this.rNAProductIsoform == null)?"<null>":this.rNAProductIsoform));
        sb.append(',');
        sb.append("relationshipType");
        sb.append('=');
        sb.append(((this.relationshipType == null)?"<null>":this.relationshipType));
        sb.append(',');
        sb.append("sensitivityQuantifier");
        sb.append('=');
        sb.append(((this.sensitivityQuantifier == null)?"<null>":this.sensitivityQuantifier));
        sb.append(',');
        sb.append("sequenceFeatureRelationship");
        sb.append('=');
        sb.append(((this.sequenceFeatureRelationship == null)?"<null>":this.sequenceFeatureRelationship));
        sb.append(',');
        sb.append("sequenceVariant");
        sb.append('=');
        sb.append(((this.sequenceVariant == null)?"<null>":this.sequenceVariant));
        sb.append(',');
        sb.append("severityValue");
        sb.append('=');
        sb.append(((this.severityValue == null)?"<null>":this.severityValue));
        sb.append(',');
        sb.append("sourceFile");
        sb.append('=');
        sb.append(((this.sourceFile == null)?"<null>":this.sourceFile));
        sb.append(',');
        sb.append("specificityQuantifier");
        sb.append('=');
        sb.append(((this.specificityQuantifier == null)?"<null>":this.specificityQuantifier));
        sb.append(',');
        sb.append("transcript");
        sb.append('=');
        sb.append(((this.transcript == null)?"<null>":this.transcript));
        sb.append(',');
        sb.append("transcriptToGeneRelationship");
        sb.append('=');
        sb.append(((this.transcriptToGeneRelationship == null)?"<null>":this.transcriptToGeneRelationship));
        sb.append(',');
        sb.append("treatment");
        sb.append('=');
        sb.append(((this.treatment == null)?"<null>":this.treatment));
        sb.append(',');
        sb.append("variantToDiseaseAssociation");
        sb.append('=');
        sb.append(((this.variantToDiseaseAssociation == null)?"<null>":this.variantToDiseaseAssociation));
        sb.append(',');
        sb.append("variantToPhenotypicFeatureAssociation");
        sb.append('=');
        sb.append(((this.variantToPhenotypicFeatureAssociation == null)?"<null>":this.variantToPhenotypicFeatureAssociation));
        sb.append(',');
        sb.append("variantToPopulationAssociation");
        sb.append('=');
        sb.append(((this.variantToPopulationAssociation == null)?"<null>":this.variantToPopulationAssociation));
        sb.append(',');
        sb.append("zygosity");
        sb.append('=');
        sb.append(((this.zygosity == null)?"<null>":this.zygosity));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.materialSampleDerivationAssociation == null)? 0 :this.materialSampleDerivationAssociation.hashCode()));
        result = ((result* 31)+((this.sequenceVariant == null)? 0 :this.sequenceVariant.hashCode()));
        result = ((result* 31)+((this.anatomicalEntityToAnatomicalEntityAssociation == null)? 0 :this.anatomicalEntityToAnatomicalEntityAssociation.hashCode()));
        result = ((result* 31)+((this.confidenceLevel == null)? 0 :this.confidenceLevel.hashCode()));
        result = ((result* 31)+((this.abstractEntity == null)? 0 :this.abstractEntity.hashCode()));
        result = ((result* 31)+((this.chemicalToDiseaseOrPhenotypicFeatureAssociation == null)? 0 :this.chemicalToDiseaseOrPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.environmentalFeature == null)? 0 :this.environmentalFeature.hashCode()));
        result = ((result* 31)+((this.frequencyValue == null)? 0 :this.frequencyValue.hashCode()));
        result = ((result* 31)+((this.rNAProduct == null)? 0 :this.rNAProduct.hashCode()));
        result = ((result* 31)+((this.sequenceFeatureRelationship == null)? 0 :this.sequenceFeatureRelationship.hashCode()));
        result = ((result* 31)+((this.carbohydrate == null)? 0 :this.carbohydrate.hashCode()));
        result = ((result* 31)+((this.transcriptToGeneRelationship == null)? 0 :this.transcriptToGeneRelationship.hashCode()));
        result = ((result* 31)+((this.genotypeToPhenotypicFeatureAssociation == null)? 0 :this.genotypeToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.chemicalToGeneAssociation == null)? 0 :this.chemicalToGeneAssociation.hashCode()));
        result = ((result* 31)+((this.dataSetVersion == null)? 0 :this.dataSetVersion.hashCode()));
        result = ((result* 31)+((this.protein == null)? 0 :this.protein.hashCode()));
        result = ((result* 31)+((this.biologicalProcessOrActivity == null)? 0 :this.biologicalProcessOrActivity.hashCode()));
        result = ((result* 31)+((this.geneProduct == null)? 0 :this.geneProduct.hashCode()));
        result = ((result* 31)+((this.macromolecularMachineToCellularComponentAssociation == null)? 0 :this.macromolecularMachineToCellularComponentAssociation.hashCode()));
        result = ((result* 31)+((this.anatomicalEntityToAnatomicalEntityOntogenicAssociation == null)? 0 :this.anatomicalEntityToAnatomicalEntityOntogenicAssociation.hashCode()));
        result = ((result* 31)+((this.cellularComponent == null)? 0 :this.cellularComponent.hashCode()));
        result = ((result* 31)+((this.specificityQuantifier == null)? 0 :this.specificityQuantifier.hashCode()));
        result = ((result* 31)+((this.gene == null)? 0 :this.gene.hashCode()));
        result = ((result* 31)+((this.chemicalToChemicalDerivationAssociation == null)? 0 :this.chemicalToChemicalDerivationAssociation.hashCode()));
        result = ((result* 31)+((this.pairwiseGeneToGeneInteraction == null)? 0 :this.pairwiseGeneToGeneInteraction.hashCode()));
        result = ((result* 31)+((this.genotypeToGenotypePartAssociation == null)? 0 :this.genotypeToGenotypePartAssociation.hashCode()));
        result = ((result* 31)+((this.geographicLocationAtTime == null)? 0 :this.geographicLocationAtTime.hashCode()));
        result = ((result* 31)+((this.macromolecularMachineToMolecularActivityAssociation == null)? 0 :this.macromolecularMachineToMolecularActivityAssociation.hashCode()));
        result = ((result* 31)+((this.molecularActivity == null)? 0 :this.molecularActivity.hashCode()));
        result = ((result* 31)+((this.grossAnatomicalStructure == null)? 0 :this.grossAnatomicalStructure.hashCode()));
        result = ((result* 31)+((this.individualOrganism == null)? 0 :this.individualOrganism.hashCode()));
        result = ((result* 31)+((this.cellLine == null)? 0 :this.cellLine.hashCode()));
        result = ((result* 31)+((this.device == null)? 0 :this.device.hashCode()));
        result = ((result* 31)+((this.geneOntologyClass == null)? 0 :this.geneOntologyClass.hashCode()));
        result = ((result* 31)+((this.treatment == null)? 0 :this.treatment.hashCode()));
        result = ((result* 31)+((this.geographicLocation == null)? 0 :this.geographicLocation.hashCode()));
        result = ((result* 31)+((this.association == null)? 0 :this.association.hashCode()));
        result = ((result* 31)+((this.phenomenon == null)? 0 :this.phenomenon.hashCode()));
        result = ((result* 31)+((this.cell == null)? 0 :this.cell.hashCode()));
        result = ((result* 31)+((this.exposureEventToPhenotypicFeatureAssociation == null)? 0 :this.exposureEventToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.transcript == null)? 0 :this.transcript.hashCode()));
        result = ((result* 31)+((this.geneToDiseaseAssociation == null)? 0 :this.geneToDiseaseAssociation.hashCode()));
        result = ((result* 31)+((this.attribute == null)? 0 :this.attribute.hashCode()));
        result = ((result* 31)+((this.dataSet == null)? 0 :this.dataSet.hashCode()));
        result = ((result* 31)+((this.diseaseToExposureAssociation == null)? 0 :this.diseaseToExposureAssociation.hashCode()));
        result = ((result* 31)+((this.clinicalModifier == null)? 0 :this.clinicalModifier.hashCode()));
        result = ((result* 31)+((this.codingSequence == null)? 0 :this.codingSequence.hashCode()));
        result = ((result* 31)+((this._case == null)? 0 :this._case.hashCode()));
        result = ((result* 31)+((this.procedure == null)? 0 :this.procedure.hashCode()));
        result = ((result* 31)+((this.environmentalProcess == null)? 0 :this.environmentalProcess.hashCode()));
        result = ((result* 31)+((this.onset == null)? 0 :this.onset.hashCode()));
        result = ((result* 31)+((this.noncodingRNAProduct == null)? 0 :this.noncodingRNAProduct.hashCode()));
        result = ((result* 31)+((this.chemicalSubstance == null)? 0 :this.chemicalSubstance.hashCode()));
        result = ((result* 31)+((this.genome == null)? 0 :this.genome.hashCode()));
        result = ((result* 31)+((this.genotypeToGeneAssociation == null)? 0 :this.genotypeToGeneAssociation.hashCode()));
        result = ((result* 31)+((this.zygosity == null)? 0 :this.zygosity.hashCode()));
        result = ((result* 31)+((this.frequencyQualifierMixin == null)? 0 :this.frequencyQualifierMixin.hashCode()));
        result = ((result* 31)+((this.lifeStage == null)? 0 :this.lifeStage.hashCode()));
        result = ((result* 31)+((this.ontologyClass == null)? 0 :this.ontologyClass.hashCode()));
        result = ((result* 31)+((this.pathway == null)? 0 :this.pathway.hashCode()));
        result = ((result* 31)+((this.chemicalToChemicalAssociation == null)? 0 :this.chemicalToChemicalAssociation.hashCode()));
        result = ((result* 31)+((this.sensitivityQuantifier == null)? 0 :this.sensitivityQuantifier.hashCode()));
        result = ((result* 31)+((this.frequencyQuantifier == null)? 0 :this.frequencyQuantifier.hashCode()));
        result = ((result* 31)+((this.variantToDiseaseAssociation == null)? 0 :this.variantToDiseaseAssociation.hashCode()));
        result = ((result* 31)+((this.geneOrGeneProduct == null)? 0 :this.geneOrGeneProduct.hashCode()));
        result = ((result* 31)+((this.materialSample == null)? 0 :this.materialSample.hashCode()));
        result = ((result* 31)+((this.anatomicalEntityToAnatomicalEntityPartOfAssociation == null)? 0 :this.anatomicalEntityToAnatomicalEntityPartOfAssociation.hashCode()));
        result = ((result* 31)+((this.macromolecularMachine == null)? 0 :this.macromolecularMachine.hashCode()));
        result = ((result* 31)+((this.geneRegulatoryRelationship == null)? 0 :this.geneRegulatoryRelationship.hashCode()));
        result = ((result* 31)+((this.geneAsAModelOfDiseaseAssociation == null)? 0 :this.geneAsAModelOfDiseaseAssociation.hashCode()));
        result = ((result* 31)+((this.sourceFile == null)? 0 :this.sourceFile.hashCode()));
        result = ((result* 31)+((this.drug == null)? 0 :this.drug.hashCode()));
        result = ((result* 31)+((this.biologicalProcess == null)? 0 :this.biologicalProcess.hashCode()));
        result = ((result* 31)+((this.macromolecularComplex == null)? 0 :this.macromolecularComplex.hashCode()));
        result = ((result* 31)+((this.namedThing == null)? 0 :this.namedThing.hashCode()));
        result = ((result* 31)+((this.severityValue == null)? 0 :this.severityValue.hashCode()));
        result = ((result* 31)+((this.caseToPhenotypicFeatureAssociation == null)? 0 :this.caseToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.publication == null)? 0 :this.publication.hashCode()));
        result = ((result* 31)+((this.geneHasVariantThatContributesToDiseaseAssociation == null)? 0 :this.geneHasVariantThatContributesToDiseaseAssociation.hashCode()));
        result = ((result* 31)+((this.physicalEntity == null)? 0 :this.physicalEntity.hashCode()));
        result = ((result* 31)+((this.exonToTranscriptRelationship == null)? 0 :this.exonToTranscriptRelationship.hashCode()));
        result = ((result* 31)+((this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation == null)? 0 :this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation.hashCode()));
        result = ((result* 31)+((this.molecularEntity == null)? 0 :this.molecularEntity.hashCode()));
        result = ((result* 31)+((this.geneToExpressionSiteAssociation == null)? 0 :this.geneToExpressionSiteAssociation.hashCode()));
        result = ((result* 31)+((this.geneToGoTermAssociation == null)? 0 :this.geneToGoTermAssociation.hashCode()));
        result = ((result* 31)+((this.populationToPopulationAssociation == null)? 0 :this.populationToPopulationAssociation.hashCode()));
        result = ((result* 31)+((this.drugExposure == null)? 0 :this.drugExposure.hashCode()));
        result = ((result* 31)+((this.diseaseToPhenotypicFeatureAssociation == null)? 0 :this.diseaseToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.chemicalToPathwayAssociation == null)? 0 :this.chemicalToPathwayAssociation.hashCode()));
        result = ((result* 31)+((this.genotypeToVariantAssociation == null)? 0 :this.genotypeToVariantAssociation.hashCode()));
        result = ((result* 31)+((this.genotype == null)? 0 :this.genotype.hashCode()));
        result = ((result* 31)+((this.genomicSequenceLocalization == null)? 0 :this.genomicSequenceLocalization.hashCode()));
        result = ((result* 31)+((this.distributionLevel == null)? 0 :this.distributionLevel.hashCode()));
        result = ((result* 31)+((this.geneToGeneHomologyAssociation == null)? 0 :this.geneToGeneHomologyAssociation.hashCode()));
        result = ((result* 31)+((this.pathognomonicityQuantifier == null)? 0 :this.pathognomonicityQuantifier.hashCode()));
        result = ((result* 31)+((this.exposureEvent == null)? 0 :this.exposureEvent.hashCode()));
        result = ((result* 31)+((this.genotypicSex == null)? 0 :this.genotypicSex.hashCode()));
        result = ((result* 31)+((this.genomicEntity == null)? 0 :this.genomicEntity.hashCode()));
        result = ((result* 31)+((this.clinicalTrial == null)? 0 :this.clinicalTrial.hashCode()));
        result = ((result* 31)+((this.activityAndBehavior == null)? 0 :this.activityAndBehavior.hashCode()));
        result = ((result* 31)+((this.proteinIsoform == null)? 0 :this.proteinIsoform.hashCode()));
        result = ((result* 31)+((this.variantToPhenotypicFeatureAssociation == null)? 0 :this.variantToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.phenotypicFeature == null)? 0 :this.phenotypicFeature.hashCode()));
        result = ((result* 31)+((this.cellLineToDiseaseOrPhenotypicFeatureAssociation == null)? 0 :this.cellLineToDiseaseOrPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.planetaryEntity == null)? 0 :this.planetaryEntity.hashCode()));
        result = ((result* 31)+((this.occurrent == null)? 0 :this.occurrent.hashCode()));
        result = ((result* 31)+((this.phenotypicSex == null)? 0 :this.phenotypicSex.hashCode()));
        result = ((result* 31)+((this.macromolecularMachineToBiologicalProcessAssociation == null)? 0 :this.macromolecularMachineToBiologicalProcessAssociation.hashCode()));
        result = ((result* 31)+((this.rNAProductIsoform == null)? 0 :this.rNAProductIsoform.hashCode()));
        result = ((result* 31)+((this.metabolite == null)? 0 :this.metabolite.hashCode()));
        result = ((result* 31)+((this.provider == null)? 0 :this.provider.hashCode()));
        result = ((result* 31)+((this.organismTaxon == null)? 0 :this.organismTaxon.hashCode()));
        result = ((result* 31)+((this.dataFile == null)? 0 :this.dataFile.hashCode()));
        result = ((result* 31)+((this.chemicalExposure == null)? 0 :this.chemicalExposure.hashCode()));
        result = ((result* 31)+((this.geneToGeneProductRelationship == null)? 0 :this.geneToGeneProductRelationship.hashCode()));
        result = ((result* 31)+((this.physiologicalProcess == null)? 0 :this.physiologicalProcess.hashCode()));
        result = ((result* 31)+((this.materialSampleToDiseaseOrPhenotypicFeatureAssociation == null)? 0 :this.materialSampleToDiseaseOrPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.disease == null)? 0 :this.disease.hashCode()));
        result = ((result* 31)+((this.haplotype == null)? 0 :this.haplotype.hashCode()));
        result = ((result* 31)+((this.populationOfIndividualOrganisms == null)? 0 :this.populationOfIndividualOrganisms.hashCode()));
        result = ((result* 31)+((this.relationshipType == null)? 0 :this.relationshipType.hashCode()));
        result = ((result* 31)+((this.variantToPopulationAssociation == null)? 0 :this.variantToPopulationAssociation.hashCode()));
        result = ((result* 31)+((this.dataSetSummary == null)? 0 :this.dataSetSummary.hashCode()));
        result = ((result* 31)+((this.anatomicalEntity == null)? 0 :this.anatomicalEntity.hashCode()));
        result = ((result* 31)+((this.clinicalEntity == null)? 0 :this.clinicalEntity.hashCode()));
        result = ((result* 31)+((this.functionalAssociation == null)? 0 :this.functionalAssociation.hashCode()));
        result = ((result* 31)+((this.biologicalSex == null)? 0 :this.biologicalSex.hashCode()));
        result = ((result* 31)+((this.clinicalIntervention == null)? 0 :this.clinicalIntervention.hashCode()));
        result = ((result* 31)+((this.evidenceType == null)? 0 :this.evidenceType.hashCode()));
        result = ((result* 31)+((this.quantityValue == null)? 0 :this.quantityValue.hashCode()));
        result = ((result* 31)+((this.geneFamily == null)? 0 :this.geneFamily.hashCode()));
        result = ((result* 31)+((this.microRNA == null)? 0 :this.microRNA.hashCode()));
        result = ((result* 31)+((this.geneToPhenotypicFeatureAssociation == null)? 0 :this.geneToPhenotypicFeatureAssociation.hashCode()));
        result = ((result* 31)+((this.diseaseOrPhenotypicFeature == null)? 0 :this.diseaseOrPhenotypicFeature.hashCode()));
        result = ((result* 31)+((this.exon == null)? 0 :this.exon.hashCode()));
        return result;
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
        return ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((this.materialSampleDerivationAssociation == rhs.materialSampleDerivationAssociation)||((this.materialSampleDerivationAssociation!= null)&&this.materialSampleDerivationAssociation.equals(rhs.materialSampleDerivationAssociation)))&&((this.sequenceVariant == rhs.sequenceVariant)||((this.sequenceVariant!= null)&&this.sequenceVariant.equals(rhs.sequenceVariant))))&&((this.anatomicalEntityToAnatomicalEntityAssociation == rhs.anatomicalEntityToAnatomicalEntityAssociation)||((this.anatomicalEntityToAnatomicalEntityAssociation!= null)&&this.anatomicalEntityToAnatomicalEntityAssociation.equals(rhs.anatomicalEntityToAnatomicalEntityAssociation))))&&((this.confidenceLevel == rhs.confidenceLevel)||((this.confidenceLevel!= null)&&this.confidenceLevel.equals(rhs.confidenceLevel))))&&((this.abstractEntity == rhs.abstractEntity)||((this.abstractEntity!= null)&&this.abstractEntity.equals(rhs.abstractEntity))))&&((this.chemicalToDiseaseOrPhenotypicFeatureAssociation == rhs.chemicalToDiseaseOrPhenotypicFeatureAssociation)||((this.chemicalToDiseaseOrPhenotypicFeatureAssociation!= null)&&this.chemicalToDiseaseOrPhenotypicFeatureAssociation.equals(rhs.chemicalToDiseaseOrPhenotypicFeatureAssociation))))&&((this.environmentalFeature == rhs.environmentalFeature)||((this.environmentalFeature!= null)&&this.environmentalFeature.equals(rhs.environmentalFeature))))&&((this.frequencyValue == rhs.frequencyValue)||((this.frequencyValue!= null)&&this.frequencyValue.equals(rhs.frequencyValue))))&&((this.rNAProduct == rhs.rNAProduct)||((this.rNAProduct!= null)&&this.rNAProduct.equals(rhs.rNAProduct))))&&((this.sequenceFeatureRelationship == rhs.sequenceFeatureRelationship)||((this.sequenceFeatureRelationship!= null)&&this.sequenceFeatureRelationship.equals(rhs.sequenceFeatureRelationship))))&&((this.carbohydrate == rhs.carbohydrate)||((this.carbohydrate!= null)&&this.carbohydrate.equals(rhs.carbohydrate))))&&((this.transcriptToGeneRelationship == rhs.transcriptToGeneRelationship)||((this.transcriptToGeneRelationship!= null)&&this.transcriptToGeneRelationship.equals(rhs.transcriptToGeneRelationship))))&&((this.genotypeToPhenotypicFeatureAssociation == rhs.genotypeToPhenotypicFeatureAssociation)||((this.genotypeToPhenotypicFeatureAssociation!= null)&&this.genotypeToPhenotypicFeatureAssociation.equals(rhs.genotypeToPhenotypicFeatureAssociation))))&&((this.chemicalToGeneAssociation == rhs.chemicalToGeneAssociation)||((this.chemicalToGeneAssociation!= null)&&this.chemicalToGeneAssociation.equals(rhs.chemicalToGeneAssociation))))&&((this.dataSetVersion == rhs.dataSetVersion)||((this.dataSetVersion!= null)&&this.dataSetVersion.equals(rhs.dataSetVersion))))&&((this.protein == rhs.protein)||((this.protein!= null)&&this.protein.equals(rhs.protein))))&&((this.biologicalProcessOrActivity == rhs.biologicalProcessOrActivity)||((this.biologicalProcessOrActivity!= null)&&this.biologicalProcessOrActivity.equals(rhs.biologicalProcessOrActivity))))&&((this.geneProduct == rhs.geneProduct)||((this.geneProduct!= null)&&this.geneProduct.equals(rhs.geneProduct))))&&((this.macromolecularMachineToCellularComponentAssociation == rhs.macromolecularMachineToCellularComponentAssociation)||((this.macromolecularMachineToCellularComponentAssociation!= null)&&this.macromolecularMachineToCellularComponentAssociation.equals(rhs.macromolecularMachineToCellularComponentAssociation))))&&((this.anatomicalEntityToAnatomicalEntityOntogenicAssociation == rhs.anatomicalEntityToAnatomicalEntityOntogenicAssociation)||((this.anatomicalEntityToAnatomicalEntityOntogenicAssociation!= null)&&this.anatomicalEntityToAnatomicalEntityOntogenicAssociation.equals(rhs.anatomicalEntityToAnatomicalEntityOntogenicAssociation))))&&((this.cellularComponent == rhs.cellularComponent)||((this.cellularComponent!= null)&&this.cellularComponent.equals(rhs.cellularComponent))))&&((this.specificityQuantifier == rhs.specificityQuantifier)||((this.specificityQuantifier!= null)&&this.specificityQuantifier.equals(rhs.specificityQuantifier))))&&((this.gene == rhs.gene)||((this.gene!= null)&&this.gene.equals(rhs.gene))))&&((this.chemicalToChemicalDerivationAssociation == rhs.chemicalToChemicalDerivationAssociation)||((this.chemicalToChemicalDerivationAssociation!= null)&&this.chemicalToChemicalDerivationAssociation.equals(rhs.chemicalToChemicalDerivationAssociation))))&&((this.pairwiseGeneToGeneInteraction == rhs.pairwiseGeneToGeneInteraction)||((this.pairwiseGeneToGeneInteraction!= null)&&this.pairwiseGeneToGeneInteraction.equals(rhs.pairwiseGeneToGeneInteraction))))&&((this.genotypeToGenotypePartAssociation == rhs.genotypeToGenotypePartAssociation)||((this.genotypeToGenotypePartAssociation!= null)&&this.genotypeToGenotypePartAssociation.equals(rhs.genotypeToGenotypePartAssociation))))&&((this.geographicLocationAtTime == rhs.geographicLocationAtTime)||((this.geographicLocationAtTime!= null)&&this.geographicLocationAtTime.equals(rhs.geographicLocationAtTime))))&&((this.macromolecularMachineToMolecularActivityAssociation == rhs.macromolecularMachineToMolecularActivityAssociation)||((this.macromolecularMachineToMolecularActivityAssociation!= null)&&this.macromolecularMachineToMolecularActivityAssociation.equals(rhs.macromolecularMachineToMolecularActivityAssociation))))&&((this.molecularActivity == rhs.molecularActivity)||((this.molecularActivity!= null)&&this.molecularActivity.equals(rhs.molecularActivity))))&&((this.grossAnatomicalStructure == rhs.grossAnatomicalStructure)||((this.grossAnatomicalStructure!= null)&&this.grossAnatomicalStructure.equals(rhs.grossAnatomicalStructure))))&&((this.individualOrganism == rhs.individualOrganism)||((this.individualOrganism!= null)&&this.individualOrganism.equals(rhs.individualOrganism))))&&((this.cellLine == rhs.cellLine)||((this.cellLine!= null)&&this.cellLine.equals(rhs.cellLine))))&&((this.device == rhs.device)||((this.device!= null)&&this.device.equals(rhs.device))))&&((this.geneOntologyClass == rhs.geneOntologyClass)||((this.geneOntologyClass!= null)&&this.geneOntologyClass.equals(rhs.geneOntologyClass))))&&((this.treatment == rhs.treatment)||((this.treatment!= null)&&this.treatment.equals(rhs.treatment))))&&((this.geographicLocation == rhs.geographicLocation)||((this.geographicLocation!= null)&&this.geographicLocation.equals(rhs.geographicLocation))))&&((this.association == rhs.association)||((this.association!= null)&&this.association.equals(rhs.association))))&&((this.phenomenon == rhs.phenomenon)||((this.phenomenon!= null)&&this.phenomenon.equals(rhs.phenomenon))))&&((this.cell == rhs.cell)||((this.cell!= null)&&this.cell.equals(rhs.cell))))&&((this.exposureEventToPhenotypicFeatureAssociation == rhs.exposureEventToPhenotypicFeatureAssociation)||((this.exposureEventToPhenotypicFeatureAssociation!= null)&&this.exposureEventToPhenotypicFeatureAssociation.equals(rhs.exposureEventToPhenotypicFeatureAssociation))))&&((this.transcript == rhs.transcript)||((this.transcript!= null)&&this.transcript.equals(rhs.transcript))))&&((this.geneToDiseaseAssociation == rhs.geneToDiseaseAssociation)||((this.geneToDiseaseAssociation!= null)&&this.geneToDiseaseAssociation.equals(rhs.geneToDiseaseAssociation))))&&((this.attribute == rhs.attribute)||((this.attribute!= null)&&this.attribute.equals(rhs.attribute))))&&((this.dataSet == rhs.dataSet)||((this.dataSet!= null)&&this.dataSet.equals(rhs.dataSet))))&&((this.diseaseToExposureAssociation == rhs.diseaseToExposureAssociation)||((this.diseaseToExposureAssociation!= null)&&this.diseaseToExposureAssociation.equals(rhs.diseaseToExposureAssociation))))&&((this.clinicalModifier == rhs.clinicalModifier)||((this.clinicalModifier!= null)&&this.clinicalModifier.equals(rhs.clinicalModifier))))&&((this.codingSequence == rhs.codingSequence)||((this.codingSequence!= null)&&this.codingSequence.equals(rhs.codingSequence))))&&((this._case == rhs._case)||((this._case!= null)&&this._case.equals(rhs._case))))&&((this.procedure == rhs.procedure)||((this.procedure!= null)&&this.procedure.equals(rhs.procedure))))&&((this.environmentalProcess == rhs.environmentalProcess)||((this.environmentalProcess!= null)&&this.environmentalProcess.equals(rhs.environmentalProcess))))&&((this.onset == rhs.onset)||((this.onset!= null)&&this.onset.equals(rhs.onset))))&&((this.noncodingRNAProduct == rhs.noncodingRNAProduct)||((this.noncodingRNAProduct!= null)&&this.noncodingRNAProduct.equals(rhs.noncodingRNAProduct))))&&((this.chemicalSubstance == rhs.chemicalSubstance)||((this.chemicalSubstance!= null)&&this.chemicalSubstance.equals(rhs.chemicalSubstance))))&&((this.genome == rhs.genome)||((this.genome!= null)&&this.genome.equals(rhs.genome))))&&((this.genotypeToGeneAssociation == rhs.genotypeToGeneAssociation)||((this.genotypeToGeneAssociation!= null)&&this.genotypeToGeneAssociation.equals(rhs.genotypeToGeneAssociation))))&&((this.zygosity == rhs.zygosity)||((this.zygosity!= null)&&this.zygosity.equals(rhs.zygosity))))&&((this.frequencyQualifierMixin == rhs.frequencyQualifierMixin)||((this.frequencyQualifierMixin!= null)&&this.frequencyQualifierMixin.equals(rhs.frequencyQualifierMixin))))&&((this.lifeStage == rhs.lifeStage)||((this.lifeStage!= null)&&this.lifeStage.equals(rhs.lifeStage))))&&((this.ontologyClass == rhs.ontologyClass)||((this.ontologyClass!= null)&&this.ontologyClass.equals(rhs.ontologyClass))))&&((this.pathway == rhs.pathway)||((this.pathway!= null)&&this.pathway.equals(rhs.pathway))))&&((this.chemicalToChemicalAssociation == rhs.chemicalToChemicalAssociation)||((this.chemicalToChemicalAssociation!= null)&&this.chemicalToChemicalAssociation.equals(rhs.chemicalToChemicalAssociation))))&&((this.sensitivityQuantifier == rhs.sensitivityQuantifier)||((this.sensitivityQuantifier!= null)&&this.sensitivityQuantifier.equals(rhs.sensitivityQuantifier))))&&((this.frequencyQuantifier == rhs.frequencyQuantifier)||((this.frequencyQuantifier!= null)&&this.frequencyQuantifier.equals(rhs.frequencyQuantifier))))&&((this.variantToDiseaseAssociation == rhs.variantToDiseaseAssociation)||((this.variantToDiseaseAssociation!= null)&&this.variantToDiseaseAssociation.equals(rhs.variantToDiseaseAssociation))))&&((this.geneOrGeneProduct == rhs.geneOrGeneProduct)||((this.geneOrGeneProduct!= null)&&this.geneOrGeneProduct.equals(rhs.geneOrGeneProduct))))&&((this.materialSample == rhs.materialSample)||((this.materialSample!= null)&&this.materialSample.equals(rhs.materialSample))))&&((this.anatomicalEntityToAnatomicalEntityPartOfAssociation == rhs.anatomicalEntityToAnatomicalEntityPartOfAssociation)||((this.anatomicalEntityToAnatomicalEntityPartOfAssociation!= null)&&this.anatomicalEntityToAnatomicalEntityPartOfAssociation.equals(rhs.anatomicalEntityToAnatomicalEntityPartOfAssociation))))&&((this.macromolecularMachine == rhs.macromolecularMachine)||((this.macromolecularMachine!= null)&&this.macromolecularMachine.equals(rhs.macromolecularMachine))))&&((this.geneRegulatoryRelationship == rhs.geneRegulatoryRelationship)||((this.geneRegulatoryRelationship!= null)&&this.geneRegulatoryRelationship.equals(rhs.geneRegulatoryRelationship))))&&((this.geneAsAModelOfDiseaseAssociation == rhs.geneAsAModelOfDiseaseAssociation)||((this.geneAsAModelOfDiseaseAssociation!= null)&&this.geneAsAModelOfDiseaseAssociation.equals(rhs.geneAsAModelOfDiseaseAssociation))))&&((this.sourceFile == rhs.sourceFile)||((this.sourceFile!= null)&&this.sourceFile.equals(rhs.sourceFile))))&&((this.drug == rhs.drug)||((this.drug!= null)&&this.drug.equals(rhs.drug))))&&((this.biologicalProcess == rhs.biologicalProcess)||((this.biologicalProcess!= null)&&this.biologicalProcess.equals(rhs.biologicalProcess))))&&((this.macromolecularComplex == rhs.macromolecularComplex)||((this.macromolecularComplex!= null)&&this.macromolecularComplex.equals(rhs.macromolecularComplex))))&&((this.namedThing == rhs.namedThing)||((this.namedThing!= null)&&this.namedThing.equals(rhs.namedThing))))&&((this.severityValue == rhs.severityValue)||((this.severityValue!= null)&&this.severityValue.equals(rhs.severityValue))))&&((this.caseToPhenotypicFeatureAssociation == rhs.caseToPhenotypicFeatureAssociation)||((this.caseToPhenotypicFeatureAssociation!= null)&&this.caseToPhenotypicFeatureAssociation.equals(rhs.caseToPhenotypicFeatureAssociation))))&&((this.publication == rhs.publication)||((this.publication!= null)&&this.publication.equals(rhs.publication))))&&((this.geneHasVariantThatContributesToDiseaseAssociation == rhs.geneHasVariantThatContributesToDiseaseAssociation)||((this.geneHasVariantThatContributesToDiseaseAssociation!= null)&&this.geneHasVariantThatContributesToDiseaseAssociation.equals(rhs.geneHasVariantThatContributesToDiseaseAssociation))))&&((this.physicalEntity == rhs.physicalEntity)||((this.physicalEntity!= null)&&this.physicalEntity.equals(rhs.physicalEntity))))&&((this.exonToTranscriptRelationship == rhs.exonToTranscriptRelationship)||((this.exonToTranscriptRelationship!= null)&&this.exonToTranscriptRelationship.equals(rhs.exonToTranscriptRelationship))))&&((this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation == rhs.diseaseOrPhenotypicFeatureAssociationToLocationAssociation)||((this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation!= null)&&this.diseaseOrPhenotypicFeatureAssociationToLocationAssociation.equals(rhs.diseaseOrPhenotypicFeatureAssociationToLocationAssociation))))&&((this.molecularEntity == rhs.molecularEntity)||((this.molecularEntity!= null)&&this.molecularEntity.equals(rhs.molecularEntity))))&&((this.geneToExpressionSiteAssociation == rhs.geneToExpressionSiteAssociation)||((this.geneToExpressionSiteAssociation!= null)&&this.geneToExpressionSiteAssociation.equals(rhs.geneToExpressionSiteAssociation))))&&((this.geneToGoTermAssociation == rhs.geneToGoTermAssociation)||((this.geneToGoTermAssociation!= null)&&this.geneToGoTermAssociation.equals(rhs.geneToGoTermAssociation))))&&((this.populationToPopulationAssociation == rhs.populationToPopulationAssociation)||((this.populationToPopulationAssociation!= null)&&this.populationToPopulationAssociation.equals(rhs.populationToPopulationAssociation))))&&((this.drugExposure == rhs.drugExposure)||((this.drugExposure!= null)&&this.drugExposure.equals(rhs.drugExposure))))&&((this.diseaseToPhenotypicFeatureAssociation == rhs.diseaseToPhenotypicFeatureAssociation)||((this.diseaseToPhenotypicFeatureAssociation!= null)&&this.diseaseToPhenotypicFeatureAssociation.equals(rhs.diseaseToPhenotypicFeatureAssociation))))&&((this.chemicalToPathwayAssociation == rhs.chemicalToPathwayAssociation)||((this.chemicalToPathwayAssociation!= null)&&this.chemicalToPathwayAssociation.equals(rhs.chemicalToPathwayAssociation))))&&((this.genotypeToVariantAssociation == rhs.genotypeToVariantAssociation)||((this.genotypeToVariantAssociation!= null)&&this.genotypeToVariantAssociation.equals(rhs.genotypeToVariantAssociation))))&&((this.genotype == rhs.genotype)||((this.genotype!= null)&&this.genotype.equals(rhs.genotype))))&&((this.genomicSequenceLocalization == rhs.genomicSequenceLocalization)||((this.genomicSequenceLocalization!= null)&&this.genomicSequenceLocalization.equals(rhs.genomicSequenceLocalization))))&&((this.distributionLevel == rhs.distributionLevel)||((this.distributionLevel!= null)&&this.distributionLevel.equals(rhs.distributionLevel))))&&((this.geneToGeneHomologyAssociation == rhs.geneToGeneHomologyAssociation)||((this.geneToGeneHomologyAssociation!= null)&&this.geneToGeneHomologyAssociation.equals(rhs.geneToGeneHomologyAssociation))))&&((this.pathognomonicityQuantifier == rhs.pathognomonicityQuantifier)||((this.pathognomonicityQuantifier!= null)&&this.pathognomonicityQuantifier.equals(rhs.pathognomonicityQuantifier))))&&((this.exposureEvent == rhs.exposureEvent)||((this.exposureEvent!= null)&&this.exposureEvent.equals(rhs.exposureEvent))))&&((this.genotypicSex == rhs.genotypicSex)||((this.genotypicSex!= null)&&this.genotypicSex.equals(rhs.genotypicSex))))&&((this.genomicEntity == rhs.genomicEntity)||((this.genomicEntity!= null)&&this.genomicEntity.equals(rhs.genomicEntity))))&&((this.clinicalTrial == rhs.clinicalTrial)||((this.clinicalTrial!= null)&&this.clinicalTrial.equals(rhs.clinicalTrial))))&&((this.activityAndBehavior == rhs.activityAndBehavior)||((this.activityAndBehavior!= null)&&this.activityAndBehavior.equals(rhs.activityAndBehavior))))&&((this.proteinIsoform == rhs.proteinIsoform)||((this.proteinIsoform!= null)&&this.proteinIsoform.equals(rhs.proteinIsoform))))&&((this.variantToPhenotypicFeatureAssociation == rhs.variantToPhenotypicFeatureAssociation)||((this.variantToPhenotypicFeatureAssociation!= null)&&this.variantToPhenotypicFeatureAssociation.equals(rhs.variantToPhenotypicFeatureAssociation))))&&((this.phenotypicFeature == rhs.phenotypicFeature)||((this.phenotypicFeature!= null)&&this.phenotypicFeature.equals(rhs.phenotypicFeature))))&&((this.cellLineToDiseaseOrPhenotypicFeatureAssociation == rhs.cellLineToDiseaseOrPhenotypicFeatureAssociation)||((this.cellLineToDiseaseOrPhenotypicFeatureAssociation!= null)&&this.cellLineToDiseaseOrPhenotypicFeatureAssociation.equals(rhs.cellLineToDiseaseOrPhenotypicFeatureAssociation))))&&((this.planetaryEntity == rhs.planetaryEntity)||((this.planetaryEntity!= null)&&this.planetaryEntity.equals(rhs.planetaryEntity))))&&((this.occurrent == rhs.occurrent)||((this.occurrent!= null)&&this.occurrent.equals(rhs.occurrent))))&&((this.phenotypicSex == rhs.phenotypicSex)||((this.phenotypicSex!= null)&&this.phenotypicSex.equals(rhs.phenotypicSex))))&&((this.macromolecularMachineToBiologicalProcessAssociation == rhs.macromolecularMachineToBiologicalProcessAssociation)||((this.macromolecularMachineToBiologicalProcessAssociation!= null)&&this.macromolecularMachineToBiologicalProcessAssociation.equals(rhs.macromolecularMachineToBiologicalProcessAssociation))))&&((this.rNAProductIsoform == rhs.rNAProductIsoform)||((this.rNAProductIsoform!= null)&&this.rNAProductIsoform.equals(rhs.rNAProductIsoform))))&&((this.metabolite == rhs.metabolite)||((this.metabolite!= null)&&this.metabolite.equals(rhs.metabolite))))&&((this.provider == rhs.provider)||((this.provider!= null)&&this.provider.equals(rhs.provider))))&&((this.organismTaxon == rhs.organismTaxon)||((this.organismTaxon!= null)&&this.organismTaxon.equals(rhs.organismTaxon))))&&((this.dataFile == rhs.dataFile)||((this.dataFile!= null)&&this.dataFile.equals(rhs.dataFile))))&&((this.chemicalExposure == rhs.chemicalExposure)||((this.chemicalExposure!= null)&&this.chemicalExposure.equals(rhs.chemicalExposure))))&&((this.geneToGeneProductRelationship == rhs.geneToGeneProductRelationship)||((this.geneToGeneProductRelationship!= null)&&this.geneToGeneProductRelationship.equals(rhs.geneToGeneProductRelationship))))&&((this.physiologicalProcess == rhs.physiologicalProcess)||((this.physiologicalProcess!= null)&&this.physiologicalProcess.equals(rhs.physiologicalProcess))))&&((this.materialSampleToDiseaseOrPhenotypicFeatureAssociation == rhs.materialSampleToDiseaseOrPhenotypicFeatureAssociation)||((this.materialSampleToDiseaseOrPhenotypicFeatureAssociation!= null)&&this.materialSampleToDiseaseOrPhenotypicFeatureAssociation.equals(rhs.materialSampleToDiseaseOrPhenotypicFeatureAssociation))))&&((this.disease == rhs.disease)||((this.disease!= null)&&this.disease.equals(rhs.disease))))&&((this.haplotype == rhs.haplotype)||((this.haplotype!= null)&&this.haplotype.equals(rhs.haplotype))))&&((this.populationOfIndividualOrganisms == rhs.populationOfIndividualOrganisms)||((this.populationOfIndividualOrganisms!= null)&&this.populationOfIndividualOrganisms.equals(rhs.populationOfIndividualOrganisms))))&&((this.relationshipType == rhs.relationshipType)||((this.relationshipType!= null)&&this.relationshipType.equals(rhs.relationshipType))))&&((this.variantToPopulationAssociation == rhs.variantToPopulationAssociation)||((this.variantToPopulationAssociation!= null)&&this.variantToPopulationAssociation.equals(rhs.variantToPopulationAssociation))))&&((this.dataSetSummary == rhs.dataSetSummary)||((this.dataSetSummary!= null)&&this.dataSetSummary.equals(rhs.dataSetSummary))))&&((this.anatomicalEntity == rhs.anatomicalEntity)||((this.anatomicalEntity!= null)&&this.anatomicalEntity.equals(rhs.anatomicalEntity))))&&((this.clinicalEntity == rhs.clinicalEntity)||((this.clinicalEntity!= null)&&this.clinicalEntity.equals(rhs.clinicalEntity))))&&((this.functionalAssociation == rhs.functionalAssociation)||((this.functionalAssociation!= null)&&this.functionalAssociation.equals(rhs.functionalAssociation))))&&((this.biologicalSex == rhs.biologicalSex)||((this.biologicalSex!= null)&&this.biologicalSex.equals(rhs.biologicalSex))))&&((this.clinicalIntervention == rhs.clinicalIntervention)||((this.clinicalIntervention!= null)&&this.clinicalIntervention.equals(rhs.clinicalIntervention))))&&((this.evidenceType == rhs.evidenceType)||((this.evidenceType!= null)&&this.evidenceType.equals(rhs.evidenceType))))&&((this.quantityValue == rhs.quantityValue)||((this.quantityValue!= null)&&this.quantityValue.equals(rhs.quantityValue))))&&((this.geneFamily == rhs.geneFamily)||((this.geneFamily!= null)&&this.geneFamily.equals(rhs.geneFamily))))&&((this.microRNA == rhs.microRNA)||((this.microRNA!= null)&&this.microRNA.equals(rhs.microRNA))))&&((this.geneToPhenotypicFeatureAssociation == rhs.geneToPhenotypicFeatureAssociation)||((this.geneToPhenotypicFeatureAssociation!= null)&&this.geneToPhenotypicFeatureAssociation.equals(rhs.geneToPhenotypicFeatureAssociation))))&&((this.diseaseOrPhenotypicFeature == rhs.diseaseOrPhenotypicFeature)||((this.diseaseOrPhenotypicFeature!= null)&&this.diseaseOrPhenotypicFeature.equals(rhs.diseaseOrPhenotypicFeature))))&&((this.exon == rhs.exon)||((this.exon!= null)&&this.exon.equals(rhs.exon))));
    }

}
