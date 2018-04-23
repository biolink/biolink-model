## SCHEMA

from marshmallow import Schema, fields, pprint, post_load

class RelationshipTypeSchema(Schema):
    """
    An OWL property used as an edge label
    """

    @post_load
    def make_object(self, data):
        RelationshipType(**data)

class BiologicalSexSchema(AttributeSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        BiologicalSex(**data)

class PhenotypicSexSchema(BiologicalSexSchema):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """

    @post_load
    def make_object(self, data):
        PhenotypicSex(**data)

class GenotypicSexSchema(BiologicalSexSchema):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
    """

    @post_load
    def make_object(self, data):
        GenotypicSex(**data)

class SeverityValueSchema(AttributeSchema):
    """
    describes the severity of a phenotypic feature or disease
    """

    @post_load
    def make_object(self, data):
        SeverityValue(**data)

class FrequencyValueSchema(AttributeSchema):
    """
    describes the frequency of occurrence of an event or condition
    """

    @post_load
    def make_object(self, data):
        FrequencyValue(**data)

class ClinicalModifierSchema(AttributeSchema):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    """

    @post_load
    def make_object(self, data):
        ClinicalModifier(**data)

class OnsetSchema(AttributeSchema):
    """
    The age group in which manifestations appear
    """

    @post_load
    def make_object(self, data):
        Onset(**data)

class RelationshipQuantifierSchema(Schema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        RelationshipQuantifier(**data)

class SenstivityQuantifierSchema(RelationshipQuantifierSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        SenstivityQuantifier(**data)

class SpecificityQuantifierSchema(RelationshipQuantifierSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        SpecificityQuantifier(**data)

class PathognomonicityQuantifierSchema(SpecificityQuantifierSchema):
    """
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
    """

    @post_load
    def make_object(self, data):
        PathognomonicityQuantifier(**data)

class FrequencyQuantifierSchema(RelationshipQuantifierSchema):
    """
    None
    """
    has_count = fields.Str()
    has_total = fields.Str()
    has_quotient = fields.Str()
    has_percentage = fields.Str()

    @post_load
    def make_object(self, data):
        FrequencyQuantifier(**data)

class NamedThingSchema(Schema):
    """
    a databased entity or concept/class
    """
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        NamedThing(**data)

class BiologicalEntitySchema(NamedThingSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        BiologicalEntity(**data)

class OntologyClassSchema(Schema):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """

    @post_load
    def make_object(self, data):
        OntologyClass(**data)

class GeneOntologyClassSchema(OntologyClassSchema):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """

    @post_load
    def make_object(self, data):
        GeneOntologyClass(**data)

class ThingWithTaxonSchema(Schema):
    """
    A mixin that can be used on any entity with a taxon
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        ThingWithTaxon(**data)

class OrganismTaxonSchema(OntologyClassSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        OrganismTaxon(**data)

class OrganismalEntitySchema(BiologicalEntitySchema):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
    """

    @post_load
    def make_object(self, data):
        OrganismalEntity(**data)

class IndividualOrganismSchema(OrganismalEntitySchema):
    """
    None
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        IndividualOrganism(**data)

class CaseSchema(IndividualOrganismSchema):
    """
    An individual organism that has a patient role in some clinical context.
    """

    @post_load
    def make_object(self, data):
        Case(**data)

class PopulationOfIndividualOrganismsSchema(OrganismalEntitySchema):
    """
    None
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        PopulationOfIndividualOrganisms(**data)

class BiosampleSchema(OrganismalEntitySchema):
    """
    None
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        Biosample(**data)

class DiseaseOrPhenotypicFeatureSchema(BiologicalEntitySchema):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        DiseaseOrPhenotypicFeature(**data)

class DiseaseSchema(DiseaseOrPhenotypicFeatureSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Disease(**data)

class PhenotypicFeatureSchema(DiseaseOrPhenotypicFeatureSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        PhenotypicFeature(**data)

class EnvironmentSchema(BiologicalEntitySchema):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
    """

    @post_load
    def make_object(self, data):
        Environment(**data)

class InformationContentEntitySchema(NamedThingSchema):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """

    @post_load
    def make_object(self, data):
        InformationContentEntity(**data)

class ConfidenceLevelSchema(InformationContentEntitySchema):
    """
    Level of confidence in a statement
    """

    @post_load
    def make_object(self, data):
        ConfidenceLevel(**data)

class EvidenceTypeSchema(InformationContentEntitySchema):
    """
    Class of evidence that supports an association
    """

    @post_load
    def make_object(self, data):
        EvidenceType(**data)

class PublicationSchema(InformationContentEntitySchema):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
    """

    @post_load
    def make_object(self, data):
        Publication(**data)

class AdministrativeEntitySchema(Schema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        AdministrativeEntity(**data)

class ProviderSchema(AdministrativeEntitySchema):
    """
    person, group, organization or project that provides a piece of information
    """

    @post_load
    def make_object(self, data):
        Provider(**data)

class MolecularEntitySchema(BiologicalEntitySchema):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        MolecularEntity(**data)

class ChemicalSubstanceSchema(MolecularEntitySchema):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
    """

    @post_load
    def make_object(self, data):
        ChemicalSubstance(**data)

class DrugSchema(ChemicalSubstanceSchema):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """

    @post_load
    def make_object(self, data):
        Drug(**data)

class MetaboliteSchema(ChemicalSubstanceSchema):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """

    @post_load
    def make_object(self, data):
        Metabolite(**data)

class AttributeSchema(Schema):
    """
    A property or characteristic of an entity
    """

    @post_load
    def make_object(self, data):
        Attribute(**data)

class AnatomicalEntitySchema(OrganismalEntitySchema):
    """
    A subcellular location, cell type or gross anatomical part
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        AnatomicalEntity(**data)

class LifeStageSchema(OrganismalEntitySchema):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        LifeStage(**data)

class PlanetaryEntitySchema(NamedThingSchema):
    """
    Any entity or process that exists at the level of the whole planet
    """

    @post_load
    def make_object(self, data):
        PlanetaryEntity(**data)

class EnvironmentalProcessSchema(PlanetaryEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        EnvironmentalProcess(**data)

class EnvironmentalFeatureSchema(PlanetaryEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        EnvironmentalFeature(**data)

class ClinicalEntitySchema(NamedThingSchema):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
    """

    @post_load
    def make_object(self, data):
        ClinicalEntity(**data)

class ClinicalTrialSchema(ClinicalEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        ClinicalTrial(**data)

class ClinicalInterventionSchema(ClinicalEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        ClinicalIntervention(**data)

class DeviceSchema(NamedThingSchema):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """

    @post_load
    def make_object(self, data):
        Device(**data)

class GenomicEntitySchema(MolecularEntitySchema):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
    """
    has_biological_sequence = fields.Str()

    @post_load
    def make_object(self, data):
        GenomicEntity(**data)

class GenomeSchema(GenomicEntitySchema):
    """
    A genome is the sum of genetic material within a cell or virion.
    """

    @post_load
    def make_object(self, data):
        Genome(**data)

class TranscriptSchema(GenomicEntitySchema):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """

    @post_load
    def make_object(self, data):
        Transcript(**data)

class ExonSchema(GenomicEntitySchema):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
    """

    @post_load
    def make_object(self, data):
        Exon(**data)

class CodingSequenceSchema(GenomicEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        CodingSequence(**data)

class GeneOrGeneProductSchema(GenomicEntitySchema):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """

    @post_load
    def make_object(self, data):
        GeneOrGeneProduct(**data)

class GeneSchema(GeneOrGeneProductSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Gene(**data)

class GeneProductSchema(GeneOrGeneProductSchema):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """

    @post_load
    def make_object(self, data):
        GeneProduct(**data)

class ProteinSchema(GeneProductSchema):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
    """

    @post_load
    def make_object(self, data):
        Protein(**data)

class GeneProductIsoformSchema(GeneProductSchema):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """

    @post_load
    def make_object(self, data):
        GeneProductIsoform(**data)

class ProteinIsoformSchema(ProteinSchema):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    has_biological_sequence = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        ProteinIsoform(**data)

class RnaProductSchema(GeneProductSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        RnaProduct(**data)

class RnaProductIsoformSchema(RnaProductSchema):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    has_biological_sequence = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        RnaProductIsoform(**data)

class NoncodingRnaProductSchema(RnaProductSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        NoncodingRnaProduct(**data)

class MicrornaSchema(NoncodingRnaProductSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Microrna(**data)

class MacromolecularComplexSchema(MolecularEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        MacromolecularComplex(**data)

class GeneGroupingSchema(Schema):
    """
    any grouping of multiple genes or gene products
    """

    @post_load
    def make_object(self, data):
        GeneGrouping(**data)

class GeneFamilySchema(MolecularEntitySchema):
    """
    any grouping of multiple genes or gene products related by common descent
    """

    @post_load
    def make_object(self, data):
        GeneFamily(**data)

class ZygositySchema(AttributeSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Zygosity(**data)

class GenotypeSchema(GenomicEntitySchema):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
    """
    has_zygosity = fields.Str()

    @post_load
    def make_object(self, data):
        Genotype(**data)

class HaplotypeSchema(GenomicEntitySchema):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """

    @post_load
    def make_object(self, data):
        Haplotype(**data)

class SequenceVariantSchema(GenomicEntitySchema):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    has_gene = fields.Str()

    @post_load
    def make_object(self, data):
        SequenceVariant(**data)

class DrugExposureSchema(EnvironmentSchema):
    """
    A drug exposure is an intake of a particular chemical substance
    """

    @post_load
    def make_object(self, data):
        DrugExposure(**data)

class TreatmentSchema(EnvironmentSchema):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    treats = fields.Str()
    has_exposure_parts = fields.Str()

    @post_load
    def make_object(self, data):
        Treatment(**data)

class GeographicLocationSchema(PlanetaryEntitySchema):
    """
    a location that can be described in lat/long coordinates
    """
    latitude = fields.Str()
    longitude = fields.Str()

    @post_load
    def make_object(self, data):
        GeographicLocation(**data)

class GeographicLocationAtTimeSchema(PlanetaryEntitySchema):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    latitude = fields.Str()
    longitude = fields.Str()
    timepoint = fields.Str()

    @post_load
    def make_object(self, data):
        GeographicLocationAtTime(**data)

class AssociationSchema(InformationContentEntitySchema):
    """
    A typed association between two entities, supported by evidence
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()

    @post_load
    def make_object(self, data):
        Association(**data)

class GenotypeToGenotypePartAssociationSchema(AssociationSchema):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """

    @post_load
    def make_object(self, data):
        GenotypeToGenotypePartAssociation(**data)

class GenotypeToGeneAssociationSchema(AssociationSchema):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    """

    @post_load
    def make_object(self, data):
        GenotypeToGeneAssociation(**data)

class GenotypeToVariantAssociationSchema(AssociationSchema):
    """
    Any association between a genotype and a sequence variant.
    """

    @post_load
    def make_object(self, data):
        GenotypeToVariantAssociation(**data)

class GeneToGeneAssociationSchema(AssociationSchema):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
    """

    @post_load
    def make_object(self, data):
        GeneToGeneAssociation(**data)

class GeneToGeneHomologyAssociationSchema(GeneToGeneAssociationSchema):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """

    @post_load
    def make_object(self, data):
        GeneToGeneHomologyAssociation(**data)

class MolecularInteractionSchema(AssociationSchema):
    """
    An interaction at the molecular level between two physical entities
    """

    @post_load
    def make_object(self, data):
        MolecularInteraction(**data)

class PairwiseGeneOrProteinInteractionAssociationSchema(GeneToGeneAssociationSchema):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        PairwiseGeneOrProteinInteractionAssociation(**data)

class ChemicalToThingAssociationSchema(AssociationSchema):
    """
    An interaction between a chemical entity and another entity
    """

    @post_load
    def make_object(self, data):
        ChemicalToThingAssociation(**data)

class CaseToThingAssociationSchema(AssociationSchema):
    """
    An abstract association for use where the case is the subject
    """

    @post_load
    def make_object(self, data):
        CaseToThingAssociation(**data)

class ChemicalToGeneAssociationSchema(AssociationSchema):
    """
    An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        ChemicalToGeneAssociation(**data)

class ChemicalToDiseaseOrPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        ChemicalToDiseaseOrPhenotypicFeatureAssociation(**data)

class ChemicalToPathwayAssociationSchema(AssociationSchema):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        ChemicalToPathwayAssociation(**data)

class ChemicalToGeneAssociationSchema(AssociationSchema):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        ChemicalToGeneAssociation(**data)

class BiosampleToThingAssociationSchema(AssociationSchema):
    """
    An association between a biosample and something
    """

    @post_load
    def make_object(self, data):
        BiosampleToThingAssociation(**data)

class BiosampleToDiseaseOrPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    An association between a biosample and a disease or phenotype
  definitional: true
  
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        BiosampleToDiseaseOrPhenotypicFeatureAssociation(**data)

class EntityToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    None
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        EntityToPhenotypicFeatureAssociation(**data)

class EntityToDiseaseAssociationSchema(Schema):
    """
    mixin class for any association whose object (target node) is a disease
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        EntityToDiseaseAssociation(**data)

class DiseaseOrPhenotypicFeatureAssociationToThingAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        DiseaseOrPhenotypicFeatureAssociationToThingAssociation(**data)

class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationSchema(DiseaseOrPhenotypicFeatureAssociationToThingAssociationSchema):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
    """

    @post_load
    def make_object(self, data):
        DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(**data)

class ThingToDiseaseOrPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        ThingToDiseaseOrPhenotypicFeatureAssociation(**data)

class DiseaseToThingAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        DiseaseToThingAssociation(**data)

class GenotypeToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        GenotypeToPhenotypicFeatureAssociation(**data)

class EnvironmentToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        EnvironmentToPhenotypicFeatureAssociation(**data)

class DiseaseToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        DiseaseToPhenotypicFeatureAssociation(**data)

class CaseToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        CaseToPhenotypicFeatureAssociation(**data)

class GeneToThingAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        GeneToThingAssociation(**data)

class VariantToThingAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        VariantToThingAssociation(**data)

class GeneToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    None
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        GeneToPhenotypicFeatureAssociation(**data)

class GeneToDiseaseAssociationSchema(AssociationSchema):
    """
    None
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()

    @post_load
    def make_object(self, data):
        GeneToDiseaseAssociation(**data)

class VariantToPopulationAssociationSchema(AssociationSchema):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    frequency_qualifier = fields.Str()
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()
    has_count = fields.Str()
    has_total = fields.Str()
    has_quotient = fields.Str()
    has_percentage = fields.Str()

    @post_load
    def make_object(self, data):
        VariantToPopulationAssociation(**data)

class VariantToPhenotypicFeatureAssociationSchema(AssociationSchema):
    """
    None
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()
    sex_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        VariantToPhenotypicFeatureAssociation(**data)

class VariantToDiseaseAssociationSchema(AssociationSchema):
    """
    None
    """
    association_type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    id = fields.Str()
    label = fields.Str()
    category = fields.Str()
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        VariantToDiseaseAssociation(**data)

class ModelToDiseaseMixinSchema(Schema):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
    """

    @post_load
    def make_object(self, data):
        ModelToDiseaseMixin(**data)

class GeneAsAModelOfDiseaseAssociationSchema(GeneToDiseaseAssociationSchema):
    """
    None
    """
    frequency_qualifier = fields.Str()
    severity_qualifier = fields.Str()
    onset_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        GeneAsAModelOfDiseaseAssociation(**data)

class GeneHasVariantThatContributesToDiseaseAssociationSchema(GeneToDiseaseAssociationSchema):
    """
    None
    """
    sequence_variant_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        GeneHasVariantThatContributesToDiseaseAssociation(**data)

class GenotypeToThingAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        GenotypeToThingAssociation(**data)

class GeneToExpressionSiteAssociationSchema(AssociationSchema):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    stage_qualifier = fields.Str()
    quantifier_qualifier = fields.Str()

    @post_load
    def make_object(self, data):
        GeneToExpressionSiteAssociation(**data)

class SequenceVariantModulatesTreatmentAssociationSchema(AssociationSchema):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
    """

    @post_load
    def make_object(self, data):
        SequenceVariantModulatesTreatmentAssociation(**data)

class GeneToGoTermAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        GeneToGoTermAssociation(**data)

class AssociationResultSetSchema(InformationContentEntitySchema):
    """
    None
    """
    associations = fields.Str()

    @post_load
    def make_object(self, data):
        AssociationResultSet(**data)

class GenomicSequenceLocalizationSchema(AssociationSchema):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
    """
    start_interbase_coordinate = fields.Str()
    end_interbase_coordinate = fields.Str()
    genome_build = fields.Str()
    phase = fields.Str()

    @post_load
    def make_object(self, data):
        GenomicSequenceLocalization(**data)

class SequenceFeatureRelationshipSchema(AssociationSchema):
    """
    For example, a particular exon is part of a particular transcript or gene
    """

    @post_load
    def make_object(self, data):
        SequenceFeatureRelationship(**data)

class TranscriptToGeneRelationshipSchema(SequenceFeatureRelationshipSchema):
    """
    A gene is a collection of transcripts
    """

    @post_load
    def make_object(self, data):
        TranscriptToGeneRelationship(**data)

class GeneToGeneProductRelationshipSchema(SequenceFeatureRelationshipSchema):
    """
    A gene is transcribed and potentially translated to a gene product
    """

    @post_load
    def make_object(self, data):
        GeneToGeneProductRelationship(**data)

class ExonToTranscriptRelationshipSchema(SequenceFeatureRelationshipSchema):
    """
    A transcript is formed from multiple exons
    """

    @post_load
    def make_object(self, data):
        ExonToTranscriptRelationship(**data)

class GeneRegulatoryRelationshipSchema(AssociationSchema):
    """
    A regulatory relationship between two genes
    """

    @post_load
    def make_object(self, data):
        GeneRegulatoryRelationship(**data)

class AnatomicalEntityToAnatomicalEntityAssociationSchema(AssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        AnatomicalEntityToAnatomicalEntityAssociation(**data)

class AnatomicalEntityPartOfAnatomicalEntityAssociationSchema(AnatomicalEntityToAnatomicalEntityAssociationSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        AnatomicalEntityPartOfAnatomicalEntityAssociation(**data)

class OccurrentSchema(Schema):
    """
    A processual entity
    """

    @post_load
    def make_object(self, data):
        Occurrent(**data)

class MolecularActivitySchema(BiologicalEntitySchema):
    """
    An execution of a molecular function
    """

    @post_load
    def make_object(self, data):
        MolecularActivity(**data)

class ActivityAndBehaviorSchema(OccurrentSchema):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """

    @post_load
    def make_object(self, data):
        ActivityAndBehavior(**data)

class ProcedureSchema(OccurrentSchema):
    """
    A series of actions conducted in a certain order or manner
    """

    @post_load
    def make_object(self, data):
        Procedure(**data)

class PhenomenonSchema(OccurrentSchema):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """

    @post_load
    def make_object(self, data):
        Phenomenon(**data)

class BiologicalProcessSchema(BiologicalEntitySchema):
    """
    One or more causally connected executions of molecular functions
    """

    @post_load
    def make_object(self, data):
        BiologicalProcess(**data)

class PathwaySchema(BiologicalProcessSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Pathway(**data)

class PhysiologySchema(BiologicalProcessSchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Physiology(**data)

class CellularComponentSchema(AnatomicalEntitySchema):
    """
    A location in or around a cell
    """

    @post_load
    def make_object(self, data):
        CellularComponent(**data)

class CellSchema(AnatomicalEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        Cell(**data)

class GrossAnatomicalStructureSchema(AnatomicalEntitySchema):
    """
    None
    """

    @post_load
    def make_object(self, data):
        GrossAnatomicalStructure(**data)

