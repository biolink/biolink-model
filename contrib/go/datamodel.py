# Auto generated from contrib/go.yaml by pythongen.py version: 0.0.2
# Generation date: 2018-06-13 14:25
# Schema: go biolink extensions
#
# id: http://bioentity.io/json-schema/biolink/contrib/go.json
# description: GO specific extensions
# license: https://creativecommons.org/publicdomain/zero/1.0/

import datetime
from typing import Optional, List, Union, Dict, NewType
from dataclasses import dataclass
from metamodel.utils.metamodelcore import empty_list, empty_dict
from metamodel.utils.yamlutils import YAMLRoot

metamodel_version = "0.2.0"

not_inherited_slots: List[str] = []

# Class references
HasGenomicNameName = NewType("HasGenomicNameName", str)
ExtensionsAndEvidenceAssociationMixinName = NewType("ExtensionsAndEvidenceAssociationMixinName", str)
TaxonClosureMixinName = NewType("TaxonClosureMixinName", str)
GoTermBioentityMixinName = NewType("GoTermBioentityMixinName", str)
CausalActivityModelName = NewType("CausalActivityModelName", str)
MolecularEventName = NewType("MolecularEventName", str)
MolecularActivityToGeneProductAssociationName = NewType("MolecularActivityToGeneProductAssociationName", str)
MolecularActivityToLocationAssociationName = NewType("MolecularActivityToLocationAssociationName", str)
MolecularActivityToBiologicalProcessAssociationName = NewType("MolecularActivityToBiologicalProcessAssociationName", str)
MolecularActivityToDownstreamMolecularActivityAssociationName = NewType("MolecularActivityToDownstreamMolecularActivityAssociationName", str)
RelationshipTypeName = NewType("RelationshipTypeName", str)
AttributeName = NewType("AttributeName", str)
BiologicalSexName = NewType("BiologicalSexName", str)
PhenotypicSexName = NewType("PhenotypicSexName", str)
GenotypicSexName = NewType("GenotypicSexName", str)
SeverityValueName = NewType("SeverityValueName", str)
FrequencyValueName = NewType("FrequencyValueName", str)
ClinicalModifierName = NewType("ClinicalModifierName", str)
OnsetName = NewType("OnsetName", str)
RelationshipQuantifierName = NewType("RelationshipQuantifierName", str)
SenstivityQuantifierName = NewType("SenstivityQuantifierName", str)
SpecificityQuantifierName = NewType("SpecificityQuantifierName", str)
PathognomonicityQuantifierName = NewType("PathognomonicityQuantifierName", str)
FrequencyQuantifierName = NewType("FrequencyQuantifierName", str)
NamedThingName = NewType("NamedThingName", str)
BiologicalEntityName = NewType("BiologicalEntityName", str)
OntologyClassName = NewType("OntologyClassName", str)
GeneOntologyClassName = NewType("GeneOntologyClassName", str)
ThingWithTaxonName = NewType("ThingWithTaxonName", str)
OrganismTaxonName = NewType("OrganismTaxonName", str)
OrganismalEntityName = NewType("OrganismalEntityName", str)
IndividualOrganismName = NewType("IndividualOrganismName", str)
CaseName = NewType("CaseName", str)
PopulationOfIndividualOrganismsName = NewType("PopulationOfIndividualOrganismsName", str)
BiosampleName = NewType("BiosampleName", str)
DiseaseOrPhenotypicFeatureName = NewType("DiseaseOrPhenotypicFeatureName", str)
DiseaseName = NewType("DiseaseName", str)
PhenotypicFeatureName = NewType("PhenotypicFeatureName", str)
EnvironmentName = NewType("EnvironmentName", str)
InformationContentEntityName = NewType("InformationContentEntityName", str)
ConfidenceLevelName = NewType("ConfidenceLevelName", str)
EvidenceTypeName = NewType("EvidenceTypeName", str)
PublicationName = NewType("PublicationName", str)
AdministrativeEntityName = NewType("AdministrativeEntityName", str)
ProviderName = NewType("ProviderName", str)
MolecularEntityName = NewType("MolecularEntityName", str)
ChemicalSubstanceName = NewType("ChemicalSubstanceName", str)
DrugName = NewType("DrugName", str)
MetaboliteName = NewType("MetaboliteName", str)
AnatomicalEntityName = NewType("AnatomicalEntityName", str)
LifeStageName = NewType("LifeStageName", str)
PlanetaryEntityName = NewType("PlanetaryEntityName", str)
EnvironmentalProcessName = NewType("EnvironmentalProcessName", str)
EnvironmentalFeatureName = NewType("EnvironmentalFeatureName", str)
ClinicalEntityName = NewType("ClinicalEntityName", str)
ClinicalTrialName = NewType("ClinicalTrialName", str)
ClinicalInterventionName = NewType("ClinicalInterventionName", str)
DeviceName = NewType("DeviceName", str)
GenomicEntityName = NewType("GenomicEntityName", str)
GenomeName = NewType("GenomeName", str)
TranscriptName = NewType("TranscriptName", str)
ExonName = NewType("ExonName", str)
CodingSequenceName = NewType("CodingSequenceName", str)
MacromolecularMachineName = NewType("MacromolecularMachineName", str)
GeneOrGeneProductName = NewType("GeneOrGeneProductName", str)
GeneName = NewType("GeneName", str)
GeneProductName = NewType("GeneProductName", str)
ProteinName = NewType("ProteinName", str)
GeneProductIsoformName = NewType("GeneProductIsoformName", str)
ProteinIsoformName = NewType("ProteinIsoformName", str)
RNAProductName = NewType("RNAProductName", str)
RNAProductIsoformName = NewType("RNAProductIsoformName", str)
NoncodingRNAProductName = NewType("NoncodingRNAProductName", str)
MicroRNAName = NewType("MicroRNAName", str)
MacromolecularComplexName = NewType("MacromolecularComplexName", str)
GeneGroupingName = NewType("GeneGroupingName", str)
GeneFamilyName = NewType("GeneFamilyName", str)
ZygosityName = NewType("ZygosityName", str)
GenotypeName = NewType("GenotypeName", str)
HaplotypeName = NewType("HaplotypeName", str)
SequenceVariantName = NewType("SequenceVariantName", str)
DrugExposureName = NewType("DrugExposureName", str)
TreatmentName = NewType("TreatmentName", str)
GeographicLocationName = NewType("GeographicLocationName", str)
GeographicLocationAtTimeName = NewType("GeographicLocationAtTimeName", str)
AssociationName = NewType("AssociationName", str)
GenotypeToGenotypePartAssociationName = NewType("GenotypeToGenotypePartAssociationName", str)
GenotypeToGeneAssociationName = NewType("GenotypeToGeneAssociationName", str)
GenotypeToVariantAssociationName = NewType("GenotypeToVariantAssociationName", str)
GeneToGeneAssociationName = NewType("GeneToGeneAssociationName", str)
GeneToGeneHomologyAssociationName = NewType("GeneToGeneHomologyAssociationName", str)
MolecularInteractionName = NewType("MolecularInteractionName", str)
PairwiseGeneOrProteinInteractionAssociationName = NewType("PairwiseGeneOrProteinInteractionAssociationName", str)
CellLineToThingAssociationName = NewType("CellLineToThingAssociationName", str)
CellLineToDiseaseOrPhenotypicFeatureAssociationName = NewType("CellLineToDiseaseOrPhenotypicFeatureAssociationName", str)
ChemicalToThingAssociationName = NewType("ChemicalToThingAssociationName", str)
CaseToThingAssociationName = NewType("CaseToThingAssociationName", str)
ChemicalToDiseaseOrPhenotypicFeatureAssociationName = NewType("ChemicalToDiseaseOrPhenotypicFeatureAssociationName", str)
ChemicalToPathwayAssociationName = NewType("ChemicalToPathwayAssociationName", str)
ChemicalToGeneAssociationName = NewType("ChemicalToGeneAssociationName", str)
BiosampleToThingAssociationName = NewType("BiosampleToThingAssociationName", str)
BiosampleToDiseaseOrPhenotypicFeatureAssociationName = NewType("BiosampleToDiseaseOrPhenotypicFeatureAssociationName", str)
FrequencyQualifierName = NewType("FrequencyQualifierName", str)
EntityToFeatureOrDiseaseQualifiersName = NewType("EntityToFeatureOrDiseaseQualifiersName", str)
EntityToPhenotypicFeatureAssociationName = NewType("EntityToPhenotypicFeatureAssociationName", str)
EntityToDiseaseAssociationName = NewType("EntityToDiseaseAssociationName", str)
DiseaseOrPhenotypicFeatureAssociationToThingAssociationName = NewType("DiseaseOrPhenotypicFeatureAssociationToThingAssociationName", str)
DiseaseOrPhenotypicFeatureAssociationToLocationAssociationName = NewType("DiseaseOrPhenotypicFeatureAssociationToLocationAssociationName", str)
ThingToDiseaseOrPhenotypicFeatureAssociationName = NewType("ThingToDiseaseOrPhenotypicFeatureAssociationName", str)
DiseaseToThingAssociationName = NewType("DiseaseToThingAssociationName", str)
GenotypeToPhenotypicFeatureAssociationName = NewType("GenotypeToPhenotypicFeatureAssociationName", str)
EnvironmentToPhenotypicFeatureAssociationName = NewType("EnvironmentToPhenotypicFeatureAssociationName", str)
DiseaseToPhenotypicFeatureAssociationName = NewType("DiseaseToPhenotypicFeatureAssociationName", str)
CaseToPhenotypicFeatureAssociationName = NewType("CaseToPhenotypicFeatureAssociationName", str)
GeneToThingAssociationName = NewType("GeneToThingAssociationName", str)
VariantToThingAssociationName = NewType("VariantToThingAssociationName", str)
GeneToPhenotypicFeatureAssociationName = NewType("GeneToPhenotypicFeatureAssociationName", str)
GeneToDiseaseAssociationName = NewType("GeneToDiseaseAssociationName", str)
VariantToPopulationAssociationName = NewType("VariantToPopulationAssociationName", str)
PopulationToPopulationAssociationName = NewType("PopulationToPopulationAssociationName", str)
VariantToPhenotypicFeatureAssociationName = NewType("VariantToPhenotypicFeatureAssociationName", str)
VariantToDiseaseAssociationName = NewType("VariantToDiseaseAssociationName", str)
ModelToDiseaseMixinName = NewType("ModelToDiseaseMixinName", str)
GeneAsAModelOfDiseaseAssociationName = NewType("GeneAsAModelOfDiseaseAssociationName", str)
GeneHasVariantThatContributesToDiseaseAssociationName = NewType("GeneHasVariantThatContributesToDiseaseAssociationName", str)
GenotypeToThingAssociationName = NewType("GenotypeToThingAssociationName", str)
GeneToExpressionSiteAssociationName = NewType("GeneToExpressionSiteAssociationName", str)
SequenceVariantModulatesTreatmentAssociationName = NewType("SequenceVariantModulatesTreatmentAssociationName", str)
FunctionalAssociationName = NewType("FunctionalAssociationName", str)
MacromolecularMachineToMolecularActivityAssociationName = NewType("MacromolecularMachineToMolecularActivityAssociationName", str)
MacromolecularMachineToBiologicalProcessAssociationName = NewType("MacromolecularMachineToBiologicalProcessAssociationName", str)
MacromolecularMachineToCellularComponentAssociationName = NewType("MacromolecularMachineToCellularComponentAssociationName", str)
GeneToGoTermAssociationName = NewType("GeneToGoTermAssociationName", str)
GenomicSequenceLocalizationName = NewType("GenomicSequenceLocalizationName", str)
SequenceFeatureRelationshipName = NewType("SequenceFeatureRelationshipName", str)
TranscriptToGeneRelationshipName = NewType("TranscriptToGeneRelationshipName", str)
GeneToGeneProductRelationshipName = NewType("GeneToGeneProductRelationshipName", str)
ExonToTranscriptRelationshipName = NewType("ExonToTranscriptRelationshipName", str)
GeneRegulatoryRelationshipName = NewType("GeneRegulatoryRelationshipName", str)
AnatomicalEntityToAnatomicalEntityAssociationName = NewType("AnatomicalEntityToAnatomicalEntityAssociationName", str)
AnatomicalEntityToAnatomicalEntityPartOfAssociationName = NewType("AnatomicalEntityToAnatomicalEntityPartOfAssociationName", str)
AnatomicalEntityToAnatomicalEntityOntogenicAssociationName = NewType("AnatomicalEntityToAnatomicalEntityOntogenicAssociationName", str)
OccurrentName = NewType("OccurrentName", str)
BiologicalProcessOrActivityName = NewType("BiologicalProcessOrActivityName", str)
MolecularActivityName = NewType("MolecularActivityName", str)
ActivityAndBehaviorName = NewType("ActivityAndBehaviorName", str)
ProcedureName = NewType("ProcedureName", str)
PhenomenonName = NewType("PhenomenonName", str)
BiologicalProcessName = NewType("BiologicalProcessName", str)
PathwayName = NewType("PathwayName", str)
PhysiologicalProcessName = NewType("PhysiologicalProcessName", str)
CellularComponentName = NewType("CellularComponentName", str)
CellName = NewType("CellName", str)
CellLineName = NewType("CellLineName", str)
GrossAnatomicalStructureName = NewType("GrossAnatomicalStructureName", str)
NamedGraphName = NewType("NamedGraphName", str)
PropertyValuePairName = NewType("PropertyValuePairName", str)

# Type references
Phenotype = NewType("Phenotype", str)
EvidenceInstance = NewType("EvidenceInstance", str)
ChemicalFormulaValue = NewType("ChemicalFormulaValue", str)
IdentifierType = NewType("IdentifierType", str)
IriType = NewType("IriType", str)
LabelType = NewType("LabelType", str)
NarrativeText = NewType("NarrativeText", str)
SymbolType = NewType("SymbolType", str)
ChemicalFormulaType = NewType("ChemicalFormulaType", str)
FrequencyValue = NewType("FrequencyValue", str)
PerecentageFrequencyValue = NewType("PerecentageFrequencyValue", float)
Quotient = NewType("Quotient", float)
Unit = NewType("Unit", str)
TimeType = NewType("TimeType", datetime.time)
BiologicalSequence = NewType("BiologicalSequence", str)


@dataclass
class GoTermBioentityMixin(YAMLRoot):
    """
    mixes in GO properties to bio-entities
    """
    isa_partof_closure: List[OntologyClassName] = empty_list()
    isa_partof_closure_label: List[str] = empty_list()
    regulates_closure: List[RelationshipTypeName] = empty_list()
    regulates_closure_label: List[str] = empty_list()


@dataclass
class CausalActivityModel(NamedGraph):
    """
    A graph-based representation of how a collection of gene products operate together to achieve a biological
    objective. A GO-CAM model is a specialization of a named graph containing instances of GO molecular functions,
    entities, processes, cellular components etc, connected via causal relationships.
    """
    title: Optional[LabelType] = None


@dataclass
class MolecularEvent(YAMLRoot):
    enabled_by: Optional[GeneOrGeneProductName] = None
    part_of: Optional[str] = None
    occurs_in: Optional[str] = None
    upstream_causal_relationship: Optional[str] = None
    downstream_causal_relationship: Optional[str] = None


@dataclass
class MolecularActivityToGeneProductAssociation(Association):
    subject: MolecularActivityName = None
    object: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MolecularActivityToLocationAssociation(Association):
    subject: MolecularActivityName = None
    object: CellularComponentName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MolecularActivityToBiologicalProcessAssociation(Association):
    subject: MolecularActivityName = None
    object: BiologicalProcessName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MolecularActivityToDownstreamMolecularActivityAssociation(Association):
    subject: MolecularActivityName = None
    object: MolecularActivityName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class RelationshipType(YAMLRoot):
    """
    An OWL property used as an edge label
    """
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    pass


@dataclass
class BiologicalSex(Attribute):
    pass


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    pass


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    pass


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    pass


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    pass


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """
    pass


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    id: Optional[IdentifierType] = None
    name: Optional[LabelType] = None
    category: Optional[LabelType] = None
    related_to: Optional[NamedThingName] = None
    node_property: Optional[str] = None
    iri: Optional[IriType] = None
    full_name: Optional[LabelType] = None
    description: Optional[NarrativeText] = None
    systematic_synonym: Optional[LabelType] = None


@dataclass
class BiologicalEntity(NamedThing):
    has_phenotype: Optional[Phenotype] = None


@dataclass
class OntologyClass(YAMLRoot):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    subclass_of: Optional[OntologyClassName] = None


@dataclass
class OrganismTaxon(OntologyClass):
    pass


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    pass


@dataclass
class IndividualOrganism(OrganismalEntity):
    pass


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    pass


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    pass


@dataclass
class Biosample(OrganismalEntity):
    pass


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    correlated_with: Optional[MolecularEntityName] = None
    has_biomarker: Optional[MolecularEntityName] = None
    treated_by: Optional[str] = None


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    pass


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    pass


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    pass


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    title: Optional[LabelType] = None


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    pass


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    pass


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    pass


@dataclass
class AdministrativeEntity(YAMLRoot):
    pass


@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    pass


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    molecularly_interacts_with: Optional[MolecularEntityName] = None
    regulates_entity_to_entity: Optional[MolecularEntityName] = None
    biomarker_for: Optional[DiseaseOrPhenotypicFeatureName] = None


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    pass


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    pass


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    pass


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    expresses: Optional[GeneOrGeneProductName] = None


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    pass


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    pass


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    pass


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    pass


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    pass


@dataclass
class ClinicalTrial(ClinicalEntity):
    pass


@dataclass
class ClinicalIntervention(ClinicalEntity):
    pass


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    pass


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    has_biological_sequence: Optional[BiologicalSequence] = None


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    pass


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    pass


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    pass


@dataclass
class CodingSequence(GenomicEntity):
    pass


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    name: Optional[LabelType] = None


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    in_pathway_with: Optional[GeneOrGeneProductName] = None
    in_complex_with: Optional[GeneOrGeneProductName] = None
    in_cell_population_with: Optional[GeneOrGeneProductName] = None
    expressed_in: Optional[AnatomicalEntityName] = None


@dataclass
class Gene(GeneOrGeneProduct):
    genetically_interacts_with: Optional[GeneName] = None
    has_gene_product: Optional[GeneProductName] = None
    gene_associated_with_condition: Optional[DiseaseOrPhenotypicFeatureName] = None


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    pass


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    pass


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    pass


@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    pass


@dataclass
class RNAProduct(GeneProduct):
    pass


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    pass


@dataclass
class NoncodingRNAProduct(RNAProduct):
    pass


@dataclass
class MicroRNA(NoncodingRNAProduct):
    pass


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    pass


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    pass


@dataclass
class Zygosity(Attribute):
    pass


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    has_zygosity: Optional[ZygosityName] = None


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    pass


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    has_gene: List[str] = empty_list()
    has_biological_sequence: Optional[BiologicalSequence] = None
    id: Optional[IdentifierType] = None


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    drug: List[ChemicalSubstanceName] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.drug is None:
            raise ValueError(f"drug must be supplied")


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    treats: DiseaseOrPhenotypicFeatureName = None
    has_exposure_parts: List[DrugExposureName] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.treats is None:
            raise ValueError(f"treats must be supplied")
        if self.has_exposure_parts is None:
            raise ValueError(f"has_exposure_parts must be supplied")


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    timepoint: Optional[TimeType] = None


@dataclass
class Association(InformationContentEntity):
    """
    A typed association between two entities, supported by evidence
    """
    association_type: Optional[OntologyClassName] = None
    subject: str = None
    negated: bool = False
    relation: RelationshipTypeName = None
    object: str = None
    qualifiers: List[OntologyClassName] = empty_list()
    publications: List[PublicationName] = empty_list()
    provided_by: Optional[ProviderName] = None
    association_slot: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    relation: RelationshipTypeName = None
    subject: GenotypeName = None
    object: GenotypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    relation: RelationshipTypeName = None
    subject: GenotypeName = None
    object: GeneName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    relation: RelationshipTypeName = None
    subject: GenotypeName = None
    object: SequenceVariantName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    subject: GeneOrGeneProductName = None
    object: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class PairwiseGeneOrProteinInteractionAssociation(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    subject: CellLineName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    subject: DiseaseOrPhenotypicFeatureName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    subject: ChemicalSubstanceName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    subject: CaseName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    object: DiseaseOrPhenotypicFeatureName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    object: PathwayName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    object: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    subject: BiosampleName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    definitional: true
    """
    pass


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    sex_qualifier: Optional[BiologicalSexName] = None
    description: Optional[NarrativeText] = None
    object: PhenotypicFeatureName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    subject: DiseaseOrPhenotypicFeatureName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    object: AnatomicalEntityName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    object: DiseaseOrPhenotypicFeatureName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class DiseaseToThingAssociation(Association):
    subject: DiseaseName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    relation: RelationshipTypeName = None
    subject: GenotypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    subject: EnvironmentName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    pass


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    pass


@dataclass
class GeneToThingAssociation(Association):
    subject: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    subject: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GeneToDiseaseAssociation(Association):
    subject: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    subject: SequenceVariantName = None
    object: PopulationOfIndividualOrganismsName = None
    has_quotient: Optional[str] = None
    has_count: Optional[str] = None
    has_total: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    subject: PopulationOfIndividualOrganismsName = None
    object: PopulationOfIndividualOrganismsName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    subject: SequenceVariantName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class VariantToDiseaseAssociation(Association):
    subject: str = None
    relation: RelationshipTypeName = None
    object: str = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    subject: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    sequence_variant_qualifier: Optional[SequenceVariantName] = None
    subject: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GenotypeToThingAssociation(Association):
    subject: GenotypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    stage_qualifier: Optional[LifeStageName] = None
    quantifier_qualifier: Optional[str] = None
    subject: GeneOrGeneProductName = None
    object: AnatomicalEntityName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    subject: SequenceVariantName = None
    object: TreatmentName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    subject: MacromolecularMachineName = None
    object: GeneOntologyClassName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    object: MolecularActivityName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    object: BiologicalProcessName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    object: CellularComponentName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    subject: MolecularEntityName = None
    object: GeneOntologyClassName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None
    subject: GenomicEntityName = None
    object: GenomicEntityName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    subject: GenomicEntityName = None
    object: GenomicEntityName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    subject: TranscriptName = None
    object: GeneName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    subject: GeneName = None
    object: GeneProductName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    subject: ExonName = None
    object: TranscriptName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    relation: RelationshipTypeName = None
    subject: GeneOrGeneProductName = None
    object: GeneOrGeneProductName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    subject: AnatomicalEntityName = None
    object: AnatomicalEntityName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    subject: AnatomicalEntityName = None
    object: AnatomicalEntityName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    subject: AnatomicalEntityName = None
    object: AnatomicalEntityName = None
    relation: RelationshipTypeName = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if self.relation is None:
            raise ValueError(f"relation must be supplied")


@dataclass
class Occurrent(YAMLRoot):
    """
    A processual entity
    """
    regulates_process_to_process: Optional[OccurrentName] = None
    has_participant: Optional[str] = None
    has_input: Optional[str] = None
    precedes: Optional[OccurrentName] = None


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    pass


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    enabled_by: Optional[GeneOrGeneProductName] = None


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    pass


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    pass


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    pass


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    pass


@dataclass
class Pathway(BiologicalProcess):
    pass


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    pass


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    pass


@dataclass
class Cell(AnatomicalEntity):
    pass


@dataclass
class CellLine(Biosample):
    pass


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    pass


@dataclass
class NamedGraph(InformationContentEntity):
    title: Optional[LabelType] = None


@dataclass
class PropertyValuePair(YAMLRoot):
    relation: RelationshipTypeName
    filler: Optional[NamedThingName] = None

