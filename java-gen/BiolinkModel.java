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
    "AnatomicalEntity",
    "AssociationResultSet",
    "BioentityWithGoTerms",
    "Biosample",
    "BiosampleToDiseaseOrPhenotypicFeatureAssociation",
    "Case",
    "CaseToPhenotypicFeatureAssociation",
    "ChemicalSubstance",
    "ChemicalToDiseaseOrPhenotypicFeatureAssociation",
    "ChemicalToGeneAssociation",
    "Cohort",
    "ConditionOrPhenotypicFeature",
    "DenormalizedAssociation",
    "Disease",
    "DiseaseToPhenotypicFeatureAssociation",
    "DiseaseToPhenotypicFeatureDenormalizedAssociation",
    "EnvironmentToPhenotypicFeatureAssociation",
    "EnvironmentalFeature",
    "EvidenceType",
    "Gene",
    "GeneFamily",
    "GeneOrGeneProduct",
    "GeneProduct",
    "GeneToExpressionSiteAssociation",
    "GeneToGeneHomologyAssociation",
    "GeneToPhenotypicFeatureAssociation",
    "GenomicEntity",
    "GenomicSequenceLocalization",
    "Genotype",
    "GenotypeToGenotypePartAssociation",
    "GenotypeToPhenotypicFeatureAssociation",
    "GoAssociation",
    "IndividualOrganism",
    "LifeStage",
    "MacromolecularComplex",
    "MolecularEntity",
    "MolecularEvent",
    "NamedThing",
    "OntologyClass",
    "OrganismTaxon",
    "PairwiseGeneOrProteinInteractionAssociation",
    "PhenotypicFeature",
    "PopulationOfIndividualOrganisms",
    "PropertyValuePair",
    "Protein",
    "Provider",
    "Publication",
    "RnaProduct",
    "SequenceFeatureRelationship",
    "SequenceVariant",
    "Zygosity"
})
public class BiolinkModel {

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
     * AssociationResultSet
     * <p>
     * null
     * 
     */
    @JsonProperty("AssociationResultSet")
    @JsonPropertyDescription("null")
    private AssociationResultSet associationResultSet;
    /**
     * BioentityWithGoTerms
     * <p>
     * this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information
     * 
     */
    @JsonProperty("BioentityWithGoTerms")
    @JsonPropertyDescription("this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information")
    private BioentityWithGoTerms bioentityWithGoTerms;
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
     *   
     * 
     */
    @JsonProperty("BiosampleToDiseaseOrPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a biosample and a disease or phenotype\n  ")
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
     * An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    @JsonPropertyDescription("An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.")
    private ChemicalToGeneAssociation chemicalToGeneAssociation;
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
     * ConditionOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("ConditionOrPhenotypicFeature")
    @JsonPropertyDescription("null")
    private ConditionOrPhenotypicFeature conditionOrPhenotypicFeature;
    /**
     * DenormalizedAssociation
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("DenormalizedAssociation")
    @JsonPropertyDescription("An association that includes flattened inlined objects, such as subject_taxon_closure")
    private DenormalizedAssociation denormalizedAssociation;
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
     * DiseaseToPhenotypicFeatureAssociation
     * <p>
     * An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way")
    private DiseaseToPhenotypicFeatureAssociation diseaseToPhenotypicFeatureAssociation;
    /**
     * DiseaseToPhenotypicFeatureDenormalizedAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureDenormalizedAssociation")
    @JsonPropertyDescription("null")
    private DiseaseToPhenotypicFeatureDenormalizedAssociation diseaseToPhenotypicFeatureDenormalizedAssociation;
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
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    @JsonPropertyDescription("A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes")
    private EnvironmentalFeature environmentalFeature;
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
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?
     * 
     */
    @JsonProperty("GeneToExpressionSiteAssociation")
    @JsonPropertyDescription("An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?")
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
     * GeneToPhenotypicFeatureAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GeneToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("null")
    private GeneToPhenotypicFeatureAssociation geneToPhenotypicFeatureAssociation;
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
     * null
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    @JsonPropertyDescription("null")
    private GenotypeToPhenotypicFeatureAssociation genotypeToPhenotypicFeatureAssociation;
    /**
     * GoAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GoAssociation")
    @JsonPropertyDescription("null")
    private GoAssociation goAssociation;
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
     * PhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("PhenotypicFeature")
    @JsonPropertyDescription("null")
    private PhenotypicFeature phenotypicFeature;
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
     * SequenceVariant
     * <p>
     * A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
     * 
     */
    @JsonProperty("SequenceVariant")
    @JsonPropertyDescription("A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.")
    private SequenceVariant sequenceVariant;
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
     * BioentityWithGoTerms
     * <p>
     * this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information
     * 
     */
    @JsonProperty("BioentityWithGoTerms")
    public BioentityWithGoTerms getBioentityWithGoTerms() {
        return bioentityWithGoTerms;
    }

    /**
     * BioentityWithGoTerms
     * <p>
     * this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information
     * 
     */
    @JsonProperty("BioentityWithGoTerms")
    public void setBioentityWithGoTerms(BioentityWithGoTerms bioentityWithGoTerms) {
        this.bioentityWithGoTerms = bioentityWithGoTerms;
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
     * An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    public ChemicalToGeneAssociation getChemicalToGeneAssociation() {
        return chemicalToGeneAssociation;
    }

    /**
     * ChemicalToGeneAssociation
     * <p>
     * An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
     * 
     */
    @JsonProperty("ChemicalToGeneAssociation")
    public void setChemicalToGeneAssociation(ChemicalToGeneAssociation chemicalToGeneAssociation) {
        this.chemicalToGeneAssociation = chemicalToGeneAssociation;
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
     * ConditionOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("ConditionOrPhenotypicFeature")
    public ConditionOrPhenotypicFeature getConditionOrPhenotypicFeature() {
        return conditionOrPhenotypicFeature;
    }

    /**
     * ConditionOrPhenotypicFeature
     * <p>
     * null
     * 
     */
    @JsonProperty("ConditionOrPhenotypicFeature")
    public void setConditionOrPhenotypicFeature(ConditionOrPhenotypicFeature conditionOrPhenotypicFeature) {
        this.conditionOrPhenotypicFeature = conditionOrPhenotypicFeature;
    }

    /**
     * DenormalizedAssociation
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("DenormalizedAssociation")
    public DenormalizedAssociation getDenormalizedAssociation() {
        return denormalizedAssociation;
    }

    /**
     * DenormalizedAssociation
     * <p>
     * An association that includes flattened inlined objects, such as subject_taxon_closure
     * 
     */
    @JsonProperty("DenormalizedAssociation")
    public void setDenormalizedAssociation(DenormalizedAssociation denormalizedAssociation) {
        this.denormalizedAssociation = denormalizedAssociation;
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
     * DiseaseToPhenotypicFeatureDenormalizedAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureDenormalizedAssociation")
    public DiseaseToPhenotypicFeatureDenormalizedAssociation getDiseaseToPhenotypicFeatureDenormalizedAssociation() {
        return diseaseToPhenotypicFeatureDenormalizedAssociation;
    }

    /**
     * DiseaseToPhenotypicFeatureDenormalizedAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("DiseaseToPhenotypicFeatureDenormalizedAssociation")
    public void setDiseaseToPhenotypicFeatureDenormalizedAssociation(DiseaseToPhenotypicFeatureDenormalizedAssociation diseaseToPhenotypicFeatureDenormalizedAssociation) {
        this.diseaseToPhenotypicFeatureDenormalizedAssociation = diseaseToPhenotypicFeatureDenormalizedAssociation;
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
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public EnvironmentalFeature getEnvironmentalFeature() {
        return environmentalFeature;
    }

    /**
     * EnvironmentalFeature
     * <p>
     * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
     * 
     */
    @JsonProperty("EnvironmentalFeature")
    public void setEnvironmentalFeature(EnvironmentalFeature environmentalFeature) {
        this.environmentalFeature = environmentalFeature;
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
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?
     * 
     */
    @JsonProperty("GeneToExpressionSiteAssociation")
    public GeneToExpressionSiteAssociation getGeneToExpressionSiteAssociation() {
        return geneToExpressionSiteAssociation;
    }

    /**
     * GeneToExpressionSiteAssociation
     * <p>
     * An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?
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
     * null
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    public GenotypeToPhenotypicFeatureAssociation getGenotypeToPhenotypicFeatureAssociation() {
        return genotypeToPhenotypicFeatureAssociation;
    }

    /**
     * GenotypeToPhenotypicFeatureAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GenotypeToPhenotypicFeatureAssociation")
    public void setGenotypeToPhenotypicFeatureAssociation(GenotypeToPhenotypicFeatureAssociation genotypeToPhenotypicFeatureAssociation) {
        this.genotypeToPhenotypicFeatureAssociation = genotypeToPhenotypicFeatureAssociation;
    }

    /**
     * GoAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GoAssociation")
    public GoAssociation getGoAssociation() {
        return goAssociation;
    }

    /**
     * GoAssociation
     * <p>
     * null
     * 
     */
    @JsonProperty("GoAssociation")
    public void setGoAssociation(GoAssociation goAssociation) {
        this.goAssociation = goAssociation;
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
        return new ToStringBuilder(this).append("anatomicalEntity", anatomicalEntity).append("associationResultSet", associationResultSet).append("bioentityWithGoTerms", bioentityWithGoTerms).append("biosample", biosample).append("biosampleToDiseaseOrPhenotypicFeatureAssociation", biosampleToDiseaseOrPhenotypicFeatureAssociation).append("_case", _case).append("caseToPhenotypicFeatureAssociation", caseToPhenotypicFeatureAssociation).append("chemicalSubstance", chemicalSubstance).append("chemicalToDiseaseOrPhenotypicFeatureAssociation", chemicalToDiseaseOrPhenotypicFeatureAssociation).append("chemicalToGeneAssociation", chemicalToGeneAssociation).append("cohort", cohort).append("conditionOrPhenotypicFeature", conditionOrPhenotypicFeature).append("denormalizedAssociation", denormalizedAssociation).append("disease", disease).append("diseaseToPhenotypicFeatureAssociation", diseaseToPhenotypicFeatureAssociation).append("diseaseToPhenotypicFeatureDenormalizedAssociation", diseaseToPhenotypicFeatureDenormalizedAssociation).append("environmentToPhenotypicFeatureAssociation", environmentToPhenotypicFeatureAssociation).append("environmentalFeature", environmentalFeature).append("evidenceType", evidenceType).append("gene", gene).append("geneFamily", geneFamily).append("geneOrGeneProduct", geneOrGeneProduct).append("geneProduct", geneProduct).append("geneToExpressionSiteAssociation", geneToExpressionSiteAssociation).append("geneToGeneHomologyAssociation", geneToGeneHomologyAssociation).append("geneToPhenotypicFeatureAssociation", geneToPhenotypicFeatureAssociation).append("genomicEntity", genomicEntity).append("genomicSequenceLocalization", genomicSequenceLocalization).append("genotype", genotype).append("genotypeToGenotypePartAssociation", genotypeToGenotypePartAssociation).append("genotypeToPhenotypicFeatureAssociation", genotypeToPhenotypicFeatureAssociation).append("goAssociation", goAssociation).append("individualOrganism", individualOrganism).append("lifeStage", lifeStage).append("macromolecularComplex", macromolecularComplex).append("molecularEntity", molecularEntity).append("molecularEvent", molecularEvent).append("namedThing", namedThing).append("ontologyClass", ontologyClass).append("organismTaxon", organismTaxon).append("pairwiseGeneOrProteinInteractionAssociation", pairwiseGeneOrProteinInteractionAssociation).append("phenotypicFeature", phenotypicFeature).append("populationOfIndividualOrganisms", populationOfIndividualOrganisms).append("propertyValuePair", propertyValuePair).append("protein", protein).append("provider", provider).append("publication", publication).append("rnaProduct", rnaProduct).append("sequenceFeatureRelationship", sequenceFeatureRelationship).append("sequenceVariant", sequenceVariant).append("zygosity", zygosity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(sequenceVariant).append(geneOrGeneProduct).append(bioentityWithGoTerms).append(goAssociation).append(chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature).append(sequenceFeatureRelationship).append(genotypeToPhenotypicFeatureAssociation).append(macromolecularComplex).append(namedThing).append(chemicalToGeneAssociation).append(molecularEvent).append(caseToPhenotypicFeatureAssociation).append(protein).append(publication).append(geneProduct).append(biosample).append(molecularEntity).append(geneToExpressionSiteAssociation).append(gene).append(genotypeToGenotypePartAssociation).append(diseaseToPhenotypicFeatureAssociation).append(genotype).append(genomicSequenceLocalization).append(diseaseToPhenotypicFeatureDenormalizedAssociation).append(geneToGeneHomologyAssociation).append(individualOrganism).append(genomicEntity).append(rnaProduct).append(phenotypicFeature).append(cohort).append(pairwiseGeneOrProteinInteractionAssociation).append(denormalizedAssociation).append(provider).append(organismTaxon).append(conditionOrPhenotypicFeature).append(disease).append(populationOfIndividualOrganisms).append(environmentToPhenotypicFeatureAssociation).append(_case).append(associationResultSet).append(anatomicalEntity).append(chemicalSubstance).append(propertyValuePair).append(zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation).append(lifeStage).append(evidenceType).append(ontologyClass).append(geneFamily).append(geneToPhenotypicFeatureAssociation).toHashCode();
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
        return new EqualsBuilder().append(sequenceVariant, rhs.sequenceVariant).append(geneOrGeneProduct, rhs.geneOrGeneProduct).append(bioentityWithGoTerms, rhs.bioentityWithGoTerms).append(goAssociation, rhs.goAssociation).append(chemicalToDiseaseOrPhenotypicFeatureAssociation, rhs.chemicalToDiseaseOrPhenotypicFeatureAssociation).append(environmentalFeature, rhs.environmentalFeature).append(sequenceFeatureRelationship, rhs.sequenceFeatureRelationship).append(genotypeToPhenotypicFeatureAssociation, rhs.genotypeToPhenotypicFeatureAssociation).append(macromolecularComplex, rhs.macromolecularComplex).append(namedThing, rhs.namedThing).append(chemicalToGeneAssociation, rhs.chemicalToGeneAssociation).append(molecularEvent, rhs.molecularEvent).append(caseToPhenotypicFeatureAssociation, rhs.caseToPhenotypicFeatureAssociation).append(protein, rhs.protein).append(publication, rhs.publication).append(geneProduct, rhs.geneProduct).append(biosample, rhs.biosample).append(molecularEntity, rhs.molecularEntity).append(geneToExpressionSiteAssociation, rhs.geneToExpressionSiteAssociation).append(gene, rhs.gene).append(genotypeToGenotypePartAssociation, rhs.genotypeToGenotypePartAssociation).append(diseaseToPhenotypicFeatureAssociation, rhs.diseaseToPhenotypicFeatureAssociation).append(genotype, rhs.genotype).append(genomicSequenceLocalization, rhs.genomicSequenceLocalization).append(diseaseToPhenotypicFeatureDenormalizedAssociation, rhs.diseaseToPhenotypicFeatureDenormalizedAssociation).append(geneToGeneHomologyAssociation, rhs.geneToGeneHomologyAssociation).append(individualOrganism, rhs.individualOrganism).append(genomicEntity, rhs.genomicEntity).append(rnaProduct, rhs.rnaProduct).append(phenotypicFeature, rhs.phenotypicFeature).append(cohort, rhs.cohort).append(pairwiseGeneOrProteinInteractionAssociation, rhs.pairwiseGeneOrProteinInteractionAssociation).append(denormalizedAssociation, rhs.denormalizedAssociation).append(provider, rhs.provider).append(organismTaxon, rhs.organismTaxon).append(conditionOrPhenotypicFeature, rhs.conditionOrPhenotypicFeature).append(disease, rhs.disease).append(populationOfIndividualOrganisms, rhs.populationOfIndividualOrganisms).append(environmentToPhenotypicFeatureAssociation, rhs.environmentToPhenotypicFeatureAssociation).append(_case, rhs._case).append(associationResultSet, rhs.associationResultSet).append(anatomicalEntity, rhs.anatomicalEntity).append(chemicalSubstance, rhs.chemicalSubstance).append(propertyValuePair, rhs.propertyValuePair).append(zygosity, rhs.zygosity).append(biosampleToDiseaseOrPhenotypicFeatureAssociation, rhs.biosampleToDiseaseOrPhenotypicFeatureAssociation).append(lifeStage, rhs.lifeStage).append(evidenceType, rhs.evidenceType).append(ontologyClass, rhs.ontologyClass).append(geneFamily, rhs.geneFamily).append(geneToPhenotypicFeatureAssociation, rhs.geneToPhenotypicFeatureAssociation).isEquals();
    }

}
