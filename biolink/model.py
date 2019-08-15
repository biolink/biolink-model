# Auto generated from biolink-model.yaml by pythongen.py version: 0.2.1
# Generation date: 2019-07-19 16:59
# Schema: biolink_model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.metamodelcore import Bool, URI, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uri

metamodel_version = "1.4.0"


# Namespaces
BFO = Namespace('http://purl.obolibrary.org/obo/BFO_')
BIOGRID = Namespace('http://thebiogrid.org/')
CHEBI = Namespace('http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = Namespace('http://identifiers.org/chembl.compound/')
CHEMBL_TARGET = Namespace('http://identifiers.org/chembl.target/')
CIO = Namespace('http://purl.obolibrary.org/obo/CIO_')
CIVIC = Namespace('http://example.org/UNKNOWN/CIViC/')
CL = Namespace('http://purl.obolibrary.org/obo/CL_')
CLO = Namespace('http://purl.obolibrary.org/obo/CLO_')
CLINVAR = Namespace('http://www.ncbi.nlm.nih.gov/clinvar/')
ECO = Namespace('http://purl.obolibrary.org/obo/ECO_')
ECTO = Namespace('http://example.org/UNKNOWN/ECTO/')
ENSEMBL = Namespace('http://ensembl.org/id/')
FAO = Namespace('http://purl.obolibrary.org/obo/FAO_')
GENO = Namespace('http://purl.obolibrary.org/obo/GENO_')
GO = Namespace('http://purl.obolibrary.org/obo/GO_')
HANCESTRO = Namespace('http://example.org/UNKNOWN/HANCESTRO/')
HGNC = Namespace('http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HP = Namespace('http://purl.obolibrary.org/obo/HP_')
IAO = Namespace('http://purl.obolibrary.org/obo/IAO_')
INTACT = Namespace('http://example.org/UNKNOWN/IntAct/')
MGI = Namespace('http://www.informatics.jax.org/accession/MGI:')
MIR = Namespace('http://identifiers.org/mir/')
MONDO = Namespace('http://purl.obolibrary.org/obo/MONDO_')
NCBIGENE = Namespace('http://www.ncbi.nlm.nih.gov/gene/')
NCIT = Namespace('http://purl.obolibrary.org/obo/NCIT_')
OBAN = Namespace('http://purl.org/oban/')
OGMS = Namespace('http://purl.obolibrary.org/obo/OGMS_')
OIO = Namespace('http://www.geneontology.org/formats/oboInOwl#')
PANTHER = Namespace('http://www.pantherdb.org/panther/family.do?clsAccession=')
PMID = Namespace('http://www.ncbi.nlm.nih.gov/pubmed/')
PO = Namespace('http://purl.obolibrary.org/obo/PO_')
PR = Namespace('http://purl.obolibrary.org/obo/PR_')
PW = Namespace('http://purl.obolibrary.org/obo/PW_')
POMBASE = Namespace('https://www.pombase.org/spombe/result/')
RNACENTRAL = Namespace('http://example.org/UNKNOWN/RNAcentral/')
RO = Namespace('http://purl.obolibrary.org/obo/RO_')
REACTOME = Namespace('http://example.org/UNKNOWN/Reactome/')
SEMMEDDB = Namespace('http://example.org/UNKNOWN/SEMMEDDB/')
SGD = Namespace('https://www.yeastgenome.org/locus/')
SIO = Namespace('http://semanticscience.org/resource/SIO_')
SO = Namespace('http://purl.obolibrary.org/obo/SO_')
UBERON = Namespace('http://purl.obolibrary.org/obo/UBERON_')
UMLSSC = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/')
UMLSSG = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/')
UMLSST = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/')
UO = Namespace('http://purl.obolibrary.org/obo/UO_')
UPHENO = Namespace('http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = Namespace('http://identifiers.org/uniprot/')
VMC = Namespace('http://example.org/UNKNOWN/VMC/')
WB = Namespace('http://identifiers.org/wb/')
WD = Namespace('http://example.org/UNKNOWN/WD/')
ZFIN = Namespace('http://zfin.org/')
BIOLINK = Namespace('https://w3id.org/biolink/vocab/')
DCTERMS = Namespace('http://purl.org/dc/terms/')
DICTYBASE = Namespace('http://dictybase.org/gene/')
FALDO = Namespace('http://biohackathon.org/resource/faldo#')
OBAN = Namespace('http://example.org/UNKNOWN/oban/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
PAV = Namespace('http://purl.org/pav/')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
SHEX = Namespace('http://www.w3.org/ns/shex#')
SKOS = Namespace('https://www.w3.org/TR/skos-reference/#')
WGS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = BIOLINK.ChemicalFormulaValue


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier type"
    type_model_uri = BIOLINK.IdentifierType


class IriType(Uri):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = BIOLINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = BIOLINK.LabelType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = BIOLINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = BIOLINK.SymbolType


class Frequency(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency"
    type_model_uri = BIOLINK.Frequency


class PerecentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "perecentage frequency value"
    type_model_uri = BIOLINK.PerecentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = BIOLINK.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = BIOLINK.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = BIOLINK.TimeType


class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = BIOLINK.BiologicalSequence


# Class references
class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class PhenotypicSexId(BiologicalSexId):
    pass


class GenotypicSexId(BiologicalSexId):
    pass


class SeverityValueId(AttributeId):
    pass


class FrequencyValueId(AttributeId):
    pass


class ClinicalModifierId(AttributeId):
    pass


class OnsetId(AttributeId):
    pass


class NamedThingId(IdentifierType):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class GeneOntologyClassId(OntologyClassId):
    pass


class OrganismTaxonId(OntologyClassId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class CaseId(IndividualOrganismId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class BiosampleId(OrganismalEntityId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class EnvironmentId(BiologicalEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


class MolecularEntityId(BiologicalEntityId):
    pass


class ChemicalSubstanceId(MolecularEntityId):
    pass


class CarbohydrateId(ChemicalSubstanceId):
    pass


class DrugId(ChemicalSubstanceId):
    pass


class MetaboliteId(ChemicalSubstanceId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(ClinicalEntityId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class DeviceId(NamedThingId):
    pass


class GenomicEntityId(MolecularEntityId):
    pass


class GenomeId(GenomicEntityId):
    pass


class TranscriptId(GenomicEntityId):
    pass


class ExonId(GenomicEntityId):
    pass


class CodingSequenceId(GenomicEntityId):
    pass


class MacromolecularMachineId(GenomicEntityId):
    pass


class GeneOrGeneProductId(MacromolecularMachineId):
    pass


class GeneId(GeneOrGeneProductId):
    pass


class GeneProductId(GeneOrGeneProductId):
    pass


class ProteinId(GeneProductId):
    pass


class GeneProductIsoformId(GeneProductId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class RNAProductId(GeneProductId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class MacromolecularComplexId(MacromolecularMachineId):
    pass


class GeneFamilyId(MolecularEntityId):
    pass


class ZygosityId(AttributeId):
    pass


class GenotypeId(GenomicEntityId):
    pass


class HaplotypeId(GenomicEntityId):
    pass


class SequenceVariantId(GenomicEntityId):
    pass


class DrugExposureId(EnvironmentId):
    pass


class TreatmentId(EnvironmentId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(IdentifierType):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseInteractionAssociationId(AssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class CellLineToThingAssociationId(AssociationId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToThingAssociationId(AssociationId):
    pass


class CaseToThingAssociationId(AssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class BiosampleToThingAssociationId(AssociationId):
    pass


class BiosampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(DiseaseOrPhenotypicFeatureAssociationToThingAssociationId):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToThingAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class EnvironmentToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToThingAssociationId(AssociationId):
    pass


class VariantToThingAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GenotypeToThingAssociationId(AssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class GenomicSequenceLocalizationId(AssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneRegulatoryRelationshipId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class OccurrentId(NamedThingId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class ActivityAndBehaviorId(OccurrentId):
    pass


class ProcedureId(OccurrentId):
    pass


class PhenomenonId(OccurrentId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(BiosampleId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Attribute
    class_class_curie: ClassVar[str] = "biolink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Attribute

    id: Union[str, AttributeId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        super().__post_init__()


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex
    class_class_curie: ClassVar[str] = "biolink:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex

    id: Union[str, BiologicalSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__()


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhenotypicSex
    class_class_curie: ClassVar[str] = "biolink:PhenotypicSex"
    class_name: ClassVar[str] = "phenotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicSex

    id: Union[str, PhenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)
        super().__post_init__()


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypicSex
    class_class_curie: ClassVar[str] = "biolink:GenotypicSex"
    class_name: ClassVar[str] = "genotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypicSex

    id: Union[str, GenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)
        super().__post_init__()


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.SeverityValue
    class_class_curie: ClassVar[str] = "biolink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SeverityValue

    id: Union[str, SeverityValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)
        super().__post_init__()


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.FrequencyValue
    class_class_curie: ClassVar[str] = "biolink:FrequencyValue"
    class_name: ClassVar[str] = "frequency value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FrequencyValue

    id: Union[str, FrequencyValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)
        super().__post_init__()


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalModifier
    class_class_curie: ClassVar[str] = "biolink:ClinicalModifier"
    class_name: ClassVar[str] = "clinical modifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalModifier

    id: Union[str, ClinicalModifierId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)
        super().__post_init__()


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = HP["0003674"]
    class_class_curie: ClassVar[str] = "HP:0003674"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Onset

    id: Union[str, OnsetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)
        super().__post_init__()


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "physically_interacts_with", "affects", "regulates", "positively_regulates", "negatively_regulates", "disrupts", "homologous_to", "paralogous_to", "orthologous_to", "xenologous_to", "coexists_with", "colocalizes_with", "affects_risk_for", "predisposes", "contributes_to", "causes", "prevents", "occurs_in", "located_in", "location_of", "model_of", "overlaps", "has_part", "part_of", "participates_in", "actively_involved_in", "capable_of", "derives_into", "derives_from", "manifestation_of", "produces", "same_as", "has_molecular_consequence"]

    class_class_uri: ClassVar[URIRef] = WD.Q35120
    class_class_curie: ClassVar[str] = "WD:Q35120"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NamedThing

    id: Union[str, NamedThingId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        if not isinstance(self.category, IriType):
            self.category = IriType(self.category)
        super().__post_init__()


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = WD.Q28845870
    class_class_curie: ClassVar[str] = "WD:Q28845870"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.OntologyClass
    class_class_curie: ClassVar[str] = "biolink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OntologyClass

    id: Union[str, OntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__()


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.RelationshipType
    class_class_curie: ClassVar[str] = "biolink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)
        super().__post_init__()


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneOntologyClass
    class_class_curie: ClassVar[str] = "biolink:GeneOntologyClass"
    class_name: ClassVar[str] = "gene ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneOntologyClass

    id: Union[str, GeneOntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)
        super().__post_init__()


@dataclass
class OrganismTaxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = WD.Q16521
    class_class_curie: ClassVar[str] = "WD:Q16521"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)
        super().__post_init__()


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = WD.Q7239
    class_class_curie: ClassVar[str] = "WD:Q7239"
    class_name: ClassVar[str] = "organismal entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismalEntity

    id: Union[str, OrganismalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class IndividualOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010000"]
    class_class_curie: ClassVar[str] = "SIO:010000"
    class_name: ClassVar[str] = "individual organism"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IndividualOrganism

    id: Union[str, IndividualOrganismId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)
        super().__post_init__()


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Case
    class_class_curie: ClassVar[str] = "biolink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Case

    id: Union[str, CaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)
        super().__post_init__()


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["001061"]
    class_class_curie: ClassVar[str] = "SIO:001061"
    class_name: ClassVar[str] = "population of individual organisms"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationOfIndividualOrganisms

    id: Union[str, PopulationOfIndividualOrganismsId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)
        super().__post_init__()


@dataclass
class Biosample(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["001050"]
    class_class_curie: ClassVar[str] = "SIO:001050"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Biosample

    id: Union[str, BiosampleId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        super().__post_init__()


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = MONDO["0000001"]
    class_class_curie: ClassVar[str] = "MONDO:0000001"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Disease

    id: Union[str, DiseaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)
        super().__post_init__()


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = UPHENO["0001001"]
    class_class_curie: ClassVar[str] = "UPHENO:0001001"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeature

    id: Union[str, PhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)
        super().__post_init__()


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = SIO["000955"]
    class_class_curie: ClassVar[str] = "SIO:000955"
    class_name: ClassVar[str] = "environment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Environment

    id: Union[str, EnvironmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)
        super().__post_init__()


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = IAO["0000030"]
    class_class_curie: ClassVar[str] = "IAO:0000030"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = CIO["0000028"]
    class_class_curie: ClassVar[str] = "CIO:0000028"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)
        super().__post_init__()


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = ECO["0000000"]
    class_class_curie: ClassVar[str] = "ECO:0000000"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)
        super().__post_init__()


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = IAO["0000311"]
    class_class_curie: ClassVar[str] = "IAO:0000311"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Publication

    id: Union[str, PublicationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)
        super().__post_init__()


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Provider
    class_class_curie: ClassVar[str] = "biolink:Provider"
    class_name: ClassVar[str] = "provider"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Provider

    id: Union[str, ProviderId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)
        super().__post_init__()


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "positively_regulates_entity_to_entity", "negatively_regulates_entity_to_entity"]

    class_class_uri: ClassVar[URIRef] = SIO["010341"]
    class_class_curie: ClassVar[str] = "SIO:010341"
    class_name: ClassVar[str] = "molecular entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularEntity

    id: Union[str, MolecularEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        super().__post_init__()


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010004"]
    class_class_curie: ClassVar[str] = "SIO:010004"
    class_name: ClassVar[str] = "chemical substance"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)
        super().__post_init__()


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate
    class_class_curie: ClassVar[str] = "biolink:Carbohydrate"
    class_name: ClassVar[str] = "carbohydrate"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate

    id: Union[str, CarbohydrateId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)
        super().__post_init__()


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = WD.Q12140
    class_class_curie: ClassVar[str] = "WD:Q12140"
    class_name: ClassVar[str] = "drug"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Drug

    id: Union[str, DrugId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)
        super().__post_init__()


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = CHEBI["25212"]
    class_class_curie: ClassVar[str] = "CHEBI:25212"
    class_name: ClassVar[str] = "metabolite"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Metabolite

    id: Union[str, MetaboliteId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)
        super().__post_init__()


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010046"]
    class_class_curie: ClassVar[str] = "SIO:010046"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        super().__post_init__()


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.LifeStage
    class_class_curie: ClassVar[str] = "biolink:LifeStage"
    class_name: ClassVar[str] = "life stage"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LifeStage

    id: Union[str, LifeStageId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)
        super().__post_init__()


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PlanetaryEntity
    class_class_curie: ClassVar[str] = "biolink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)
        super().__post_init__()


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)
        super().__post_init__()


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)
        super().__post_init__()


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalEntity
    class_class_curie: ClassVar[str] = "biolink:ClinicalEntity"
    class_name: ClassVar[str] = "clinical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalEntity

    id: Union[str, ClinicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)
        super().__post_init__()


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial
    class_class_curie: ClassVar[str] = "biolink:ClinicalTrial"
    class_name: ClassVar[str] = "clinical trial"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial

    id: Union[str, ClinicalTrialId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)
        super().__post_init__()


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention
    class_class_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    class_name: ClassVar[str] = "clinical intervention"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention

    id: Union[str, ClinicalInterventionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)
        super().__post_init__()


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Device
    class_class_curie: ClassVar[str] = "biolink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Device

    id: Union[str, DeviceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)
        super().__post_init__()


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0000110"]
    class_class_curie: ClassVar[str] = "SO:0000110"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicEntity

    id: Union[str, GenomicEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        super().__post_init__()


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0001026"]
    class_class_curie: ClassVar[str] = "SO:0001026"
    class_name: ClassVar[str] = "genome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genome

    id: Union[str, GenomeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)
        super().__post_init__()


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0000673"]
    class_class_curie: ClassVar[str] = "SO:0000673"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Transcript

    id: Union[str, TranscriptId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)
        super().__post_init__()


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0000147"]
    class_class_curie: ClassVar[str] = "SO:0000147"
    class_name: ClassVar[str] = "exon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Exon

    id: Union[str, ExonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)
        super().__post_init__()


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0000316"]
    class_class_curie: ClassVar[str] = "SO:0000316"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)
        super().__post_init__()


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachine
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachine"
    class_name: ClassVar[str] = "macromolecular machine"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachine

    id: Union[str, MacromolecularMachineId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)
        super().__post_init__()


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneOrGeneProduct
    class_class_curie: ClassVar[str] = "biolink:GeneOrGeneProduct"
    class_name: ClassVar[str] = "gene or gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneOrGeneProduct

    id: Union[str, GeneOrGeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        super().__post_init__()


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in", "genetically_interacts_with", "has_gene_product", "gene_associated_with_condition"]

    class_class_uri: ClassVar[URIRef] = SO["0000704"]
    class_class_curie: ClassVar[str] = "SO:0000704"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Gene

    id: Union[str, GeneId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        super().__post_init__()


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = WD.Q424689
    class_class_curie: ClassVar[str] = "WD:Q424689"
    class_name: ClassVar[str] = "gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProduct

    id: Union[str, GeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)
        super().__post_init__()


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = PR["000000001"]
    class_class_curie: ClassVar[str] = "PR:000000001"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Protein

    id: Union[str, ProteinId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)
        super().__post_init__()


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneProductIsoform
    class_class_curie: ClassVar[str] = "biolink:GeneProductIsoform"
    class_name: ClassVar[str] = "gene product isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProductIsoform

    id: Union[str, GeneProductIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ProteinIsoform
    class_class_curie: ClassVar[str] = "biolink:ProteinIsoform"
    class_name: ClassVar[str] = "protein isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProteinIsoform

    id: Union[str, ProteinIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)
        super().__post_init__()


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = CHEBI["33697"]
    class_class_curie: ClassVar[str] = "CHEBI:33697"
    class_name: ClassVar[str] = "RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProduct

    id: Union[str, RNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)
        super().__post_init__()


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.RNAProductIsoform
    class_class_curie: ClassVar[str] = "biolink:RNAProductIsoform"
    class_name: ClassVar[str] = "RNA product isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProductIsoform

    id: Union[str, RNAProductIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)
        super().__post_init__()


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = SIO["001235"]
    class_class_curie: ClassVar[str] = "SIO:001235"
    class_name: ClassVar[str] = "noncoding RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NoncodingRNAProduct

    id: Union[str, NoncodingRNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)
        super().__post_init__()


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = SIO["001397"]
    class_class_curie: ClassVar[str] = "SIO:001397"
    class_name: ClassVar[str] = "microRNA"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MicroRNA

    id: Union[str, MicroRNAId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)
        super().__post_init__()


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010046"]
    class_class_curie: ClassVar[str] = "SIO:010046"
    class_name: ClassVar[str] = "macromolecular complex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularComplex

    id: Union[str, MacromolecularComplexId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)
        super().__post_init__()


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["001380"]
    class_class_curie: ClassVar[str] = "SIO:001380"
    class_name: ClassVar[str] = "gene family"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneFamily

    id: Union[str, GeneFamilyId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)
        super().__post_init__()


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = GENO["0000133"]
    class_class_curie: ClassVar[str] = "GENO:0000133"
    class_name: ClassVar[str] = "zygosity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Zygosity

    id: Union[str, ZygosityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)
        super().__post_init__()


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENO["0000536"]
    class_class_curie: ClassVar[str] = "GENO:0000536"
    class_name: ClassVar[str] = "genotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genotype

    id: Union[str, GenotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_zygosity: Optional[Union[str, ZygosityId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)
        super().__post_init__()


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENO["0000871"]
    class_class_curie: ClassVar[str] = "GENO:0000871"
    class_name: ClassVar[str] = "haplotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Haplotype

    id: Union[str, HaplotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)
        super().__post_init__()


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENO["0000002"]
    class_class_curie: ClassVar[str] = "GENO:0000002"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    has_gene: List[Union[str, GeneId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]
        super().__post_init__()


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = ECTO["0000509"]
    class_class_curie: ClassVar[str] = "ECTO:0000509"
    class_name: ClassVar[str] = "drug exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugExposure

    id: Union[str, DrugExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    drug: List[Union[str, ChemicalSubstanceId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)
        super().__post_init__()


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "treats"]

    class_class_uri: ClassVar[URIRef] = OGMS["0000090"]
    class_class_curie: ClassVar[str] = "OGMS:0000090"
    class_name: ClassVar[str] = "treatment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Treatment

    id: Union[str, TreatmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    treats: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    has_exposure_parts: List[Union[str, DrugExposureId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        super().__post_init__()


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeographicLocation
    class_class_curie: ClassVar[str] = "biolink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)
        super().__post_init__()


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "biolink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
        super().__post_init__()


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBAN.association
    class_class_curie: ClassVar[str] = "OBAN:association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Association

    id: Union[str, AssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    edge_label: Union[str, LabelType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None

    def __post_init__(self):
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if not isinstance(self.object, IriType):
            self.object = IriType(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by is not None and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)
        super().__post_init__()


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGenotypePartAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGenotypePartAssociation"
    class_name: ClassVar[str] = "genotype to genotype part association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGenotypePartAssociation

    id: Union[str, GenotypeToGenotypePartAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenotypeId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)
        super().__post_init__()


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGeneAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGeneAssociation"
    class_name: ClassVar[str] = "genotype to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGeneAssociation

    id: Union[str, GenotypeToGeneAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__()


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToVariantAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToVariantAssociation"
    class_name: ClassVar[str] = "genotype to variant association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToVariantAssociation

    id: Union[str, GenotypeToVariantAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, SequenceVariantId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneAssociation"
    class_name: ClassVar[str] = "gene to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneAssociation

    id: Union[str, GeneToGeneAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneHomologyAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneHomologyAssociation"
    class_name: ClassVar[str] = "gene to gene homology association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneHomologyAssociation

    id: Union[str, GeneToGeneHomologyAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        super().__post_init__()


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PairwiseGeneToGeneInteraction
    class_class_curie: ClassVar[str] = "biolink:PairwiseGeneToGeneInteraction"
    class_name: ClassVar[str] = "pairwise gene to gene interaction"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PairwiseGeneToGeneInteraction

    id: Union[str, PairwiseGeneToGeneInteractionId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        super().__post_init__()


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellLineToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:CellLineToThingAssociation"
    class_name: ClassVar[str] = "cell line to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToThingAssociation

    id: Union[str, CellLineToThingAssociationId] = None
    subject: Union[str, CellLineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)
        super().__post_init__()


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "cell line to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__()


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToThingAssociation"
    class_name: ClassVar[str] = "chemical to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToThingAssociation

    id: Union[str, ChemicalToThingAssociationId] = None
    subject: Union[str, ChemicalSubstanceId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        super().__post_init__()


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CaseToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:CaseToThingAssociation"
    class_name: ClassVar[str] = "case to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToThingAssociation

    id: Union[str, CaseToThingAssociationId] = None
    subject: Union[str, CaseId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)
        super().__post_init__()


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000993"]
    class_class_curie: ClassVar[str] = "SIO:000993"
    class_name: ClassVar[str] = "chemical to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__()


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001250"]
    class_class_curie: ClassVar[str] = "SIO:001250"
    class_name: ClassVar[str] = "chemical to pathway association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToPathwayAssociation

    id: Union[str, ChemicalToPathwayAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, PathwayId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)
        super().__post_init__()


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001257"]
    class_class_curie: ClassVar[str] = "SIO:001257"
    class_name: ClassVar[str] = "chemical to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToGeneAssociation

    id: Union[str, ChemicalToGeneAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiosampleToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:BiosampleToThingAssociation"
    class_name: ClassVar[str] = "biosample to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiosampleToThingAssociation

    id: Union[str, BiosampleToThingAssociationId] = None
    subject: Union[str, BiosampleId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, BiosampleId):
            self.subject = BiosampleId(self.subject)
        super().__post_init__()


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiosampleToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:BiosampleToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "biosample to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiosampleToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, BiosampleToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiosampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = BiosampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "entity to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation

    id: Union[str, EntityToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, PhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def __post_init__(self):
        if self.object is not None and not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature association to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT.R100
    class_class_curie: ClassVar[str] = "NCIT:R100"
    class_name: ClassVar[str] = "disease or phenotypic feature association to location association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToLocationAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ThingToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "thing to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ThingToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__()


@dataclass
class DiseaseToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToThingAssociation"
    class_name: ClassVar[str] = "disease to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation

    id: Union[str, DiseaseToThingAssociationId] = None
    subject: Union[str, DiseaseId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        super().__post_init__()


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "genotype to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToPhenotypicFeatureAssociation

    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        super().__post_init__()


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:EnvironmentToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "environment to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentToPhenotypicFeatureAssociation

    id: Union[str, EnvironmentToPhenotypicFeatureAssociationId] = None
    subject: Union[str, EnvironmentId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentToPhenotypicFeatureAssociationId):
            self.id = EnvironmentToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, EnvironmentId):
            self.subject = EnvironmentId(self.subject)
        super().__post_init__()


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "disease to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToPhenotypicFeatureAssociation

    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:CaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "case to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToPhenotypicFeatureAssociation

    id: Union[str, CaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class GeneToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToThingAssociation"
    class_name: ClassVar[str] = "gene to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation

    id: Union[str, GeneToThingAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://bio2rdf.org/wormbase_vocabulary:Gene-Phenotype-Association")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "gene to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToPhenotypicFeatureAssociation

    id: Union[str, GeneToPhenotypicFeatureAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000983"]
    class_class_curie: ClassVar[str] = "SIO:000983"
    class_name: ClassVar[str] = "gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToPopulationAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__()


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "biolink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, IriType] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__()


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "variant to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation

    id: Union[str, VariantToPhenotypicFeatureAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        super().__post_init__()


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    class_name: ClassVar[str] = "variant to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation

    id: Union[str, VariantToDiseaseAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, IriType):
            self.object = IriType(self.object)
        super().__post_init__()


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "gene as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation

    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    class_name: ClassVar[str] = "gene has variant that contributes to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation

    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)
        super().__post_init__()


@dataclass
class GenotypeToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToThingAssociation"
    class_name: ClassVar[str] = "genotype to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation

    id: Union[str, GenotypeToThingAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        super().__post_init__()


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToExpressionSiteAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToExpressionSiteAssociation"
    class_name: ClassVar[str] = "gene to expression site association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToExpressionSiteAssociation

    id: Union[str, GeneToExpressionSiteAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)
        super().__post_init__()


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SequenceVariantModulatesTreatmentAssociation
    class_class_curie: ClassVar[str] = "biolink:SequenceVariantModulatesTreatmentAssociation"
    class_name: ClassVar[str] = "sequence variant modulates treatment association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariantModulatesTreatmentAssociation

    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, TreatmentId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)
        super().__post_init__()


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.FunctionalAssociation
    class_class_curie: ClassVar[str] = "biolink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToMolecularActivityAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToMolecularActivityAssociation"
    class_name: ClassVar[str] = "macromolecular machine to molecular activity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToMolecularActivityAssociation

    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, MolecularActivityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToBiologicalProcessAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToBiologicalProcessAssociation"
    class_name: ClassVar[str] = "macromolecular machine to biological process association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToBiologicalProcessAssociation

    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, BiologicalProcessId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToCellularComponentAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToCellularComponentAssociation"
    class_name: ClassVar[str] = "macromolecular machine to cellular component association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToCellularComponentAssociation

    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, CellularComponentId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)
        super().__post_init__()


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "gene to go term association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGoTermAssociation

    id: Union[str, GeneToGoTermAssociationId] = None
    subject: Union[str, MolecularEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__()


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FALDO.location
    class_class_curie: ClassVar[str] = "faldo:location"
    class_name: ClassVar[str] = "genomic sequence localization"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicSequenceLocalization

    id: Union[str, GenomicSequenceLocalizationId] = None
    subject: Union[str, GenomicEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__()


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SequenceFeatureRelationship
    class_class_curie: ClassVar[str] = "biolink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    subject: Union[str, GenomicEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__()


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.TranscriptToGeneRelationship
    class_class_curie: ClassVar[str] = "biolink:TranscriptToGeneRelationship"
    class_name: ClassVar[str] = "transcript to gene relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TranscriptToGeneRelationship

    id: Union[str, TranscriptToGeneRelationshipId] = None
    subject: Union[str, TranscriptId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneProductRelationship
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneProductRelationship"
    class_name: ClassVar[str] = "gene to gene product relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneProductRelationship

    id: Union[str, GeneToGeneProductRelationshipId] = None
    subject: Union[str, GeneId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)
        super().__post_init__()


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExonToTranscriptRelationship
    class_class_curie: ClassVar[str] = "biolink:ExonToTranscriptRelationship"
    class_name: ClassVar[str] = "exon to transcript relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExonToTranscriptRelationship

    id: Union[str, ExonToTranscriptRelationshipId] = None
    subject: Union[str, ExonId] = None
    relation: Union[str, IriType] = None
    object: Union[str, TranscriptId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is not None and not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)
        super().__post_init__()


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneRegulatoryRelationship
    class_class_curie: ClassVar[str] = "biolink:GeneRegulatoryRelationship"
    class_name: ClassVar[str] = "gene regulatory relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneRegulatoryRelationship

    id: Union[str, GeneRegulatoryRelationshipId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes", "positively_regulates_process_to_process", "negatively_regulates_process_to_process"]

    class_class_uri: ClassVar[URIRef] = BFO["0000003"]
    class_class_curie: ClassVar[str] = "BFO:0000003"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Occurrent

    id: Union[str, OccurrentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        super().__post_init__()


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    class_name: ClassVar[str] = "biological process or activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity

    id: Union[str, BiologicalProcessOrActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)
        super().__post_init__()


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0003674"]
    class_class_curie: ClassVar[str] = "GO:0003674"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)
        super().__post_init__()


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior

    id: Union[str, ActivityAndBehaviorId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)
        super().__post_init__()


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Procedure
    class_class_curie: ClassVar[str] = "biolink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Procedure

    id: Union[str, ProcedureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)
        super().__post_init__()


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Phenomenon
    class_class_curie: ClassVar[str] = "biolink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)
        super().__post_init__()


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0008150"]
    class_class_curie: ClassVar[str] = "GO:0008150"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)
        super().__post_init__()


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0007165"]
    class_class_curie: ClassVar[str] = "GO:0007165"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Pathway

    id: Union[str, PathwayId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)
        super().__post_init__()


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess
    class_class_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    class_name: ClassVar[str] = "physiological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess

    id: Union[str, PhysiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)
        super().__post_init__()


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GO["0005575"]
    class_class_curie: ClassVar[str] = "GO:0005575"
    class_name: ClassVar[str] = "cellular component"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellularComponent

    id: Union[str, CellularComponentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)
        super().__post_init__()


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GO["0005623"]
    class_class_curie: ClassVar[str] = "GO:0005623"
    class_name: ClassVar[str] = "cell"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Cell

    id: Union[str, CellId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellId):
            self.id = CellId(self.id)
        super().__post_init__()


@dataclass
class CellLine(Biosample):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = CLO["0000031"]
    class_class_curie: ClassVar[str] = "CLO:0000031"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLine

    id: Union[str, CellLineId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)
        super().__post_init__()


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = UBERON["0010000"]
    class_class_curie: ClassVar[str] = "UBERON:0010000"
    class_name: ClassVar[str] = "gross anatomical structure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GrossAnatomicalStructure

    id: Union[str, GrossAnatomicalStructureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)
        super().__post_init__()

