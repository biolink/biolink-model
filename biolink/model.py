# Auto generated from biolink-model.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-03-12 14:02
# Schema: Biolink_Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, ElementIdentifier, NodeIdentifier, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, Nodeidentifier, String, Time, Uriorcurie

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BIOGRID = CurieNamespace('BIOGRID', 'http://thebiogrid.org/')
BIOSAMPLE = CurieNamespace('BioSample', 'http://example.org/UNKNOWN/BioSample/')
CAID = CurieNamespace('CAID', 'http://example.org/UNKNOWN/CAID/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMBL_TARGET = CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/')
CIO = CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_')
CIVIC = CurieNamespace('CIViC', 'http://example.org/UNKNOWN/CIViC/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
CLINVAR = CurieNamespace('ClinVar', 'http://www.ncbi.nlm.nih.gov/clinvar/')
DBSNP = CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
ECTO = CurieNamespace('ECTO', 'http://example.org/UNKNOWN/ECTO/')
EFO = CurieNamespace('EFO', 'http://purl.obolibrary.org/obo/EFO_')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://ensembl.org/id/')
EXO = CurieNamespace('ExO', 'http://example.org/UNKNOWN/ExO/')
FAO = CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GTOPDB = CurieNamespace('GTOPDB', 'http://example.org/UNKNOWN/GTOPDB/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://example.org/UNKNOWN/HANCESTRO/')
HGNC = CurieNamespace('HGNC', 'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HGVS = CurieNamespace('HGVS', 'http://example.org/UNKNOWN/HGVS/')
HMDB = CurieNamespace('HMDB', 'http://www.hmdb.ca/metabolites/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
IUPHAR = CurieNamespace('IUPHAR', 'http://example.org/UNKNOWN/IUPHAR/')
INTACT = CurieNamespace('IntAct', 'http://example.org/UNKNOWN/IntAct/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
MEDDRA = CurieNamespace('MEDDRA', 'http://purl.bioontology.org/ontology/MEDDRA/')
MESH = CurieNamespace('MESH', 'http://purl.obolibrary.org/obo/MESH_')
MGI = CurieNamespace('MGI', 'http://www.informatics.jax.org/accession/MGI:')
MIR = CurieNamespace('MIR', 'http://identifiers.org/mir/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MYVARIANT_HG19 = CurieNamespace('MYVARIANT_HG19', 'http://example.org/UNKNOWN/MYVARIANT_HG19/')
MYVARIANT_HG38 = CurieNamespace('MYVARIANT_HG38', 'http://example.org/UNKNOWN/MYVARIANT_HG38/')
NCBIGENE = CurieNamespace('NCBIGene', 'http://www.ncbi.nlm.nih.gov/gene/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OGMS = CurieNamespace('OGMS', 'http://purl.obolibrary.org/obo/OGMS_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OMIM = CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_')
ORPHANET = CurieNamespace('ORPHANET', 'http://identifiers.org/orphanet/')
PANTHER = CurieNamespace('PANTHER', 'http://www.pantherdb.org/panther/family.do?clsAccession=')
PHARMGKB = CurieNamespace('PHARMGKB', 'http://example.org/UNKNOWN/PHARMGKB/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM = CurieNamespace('PUBCHEM', 'http://example.org/UNKNOWN/PUBCHEM/')
PW = CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_')
POMBASE = CurieNamespace('PomBase', 'https://www.pombase.org/spombe/result/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RNACENTRAL = CurieNamespace('RNAcentral', 'http://example.org/UNKNOWN/RNAcentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
REACTOME = CurieNamespace('Reactome', 'http://example.org/UNKNOWN/Reactome/')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'http://example.org/UNKNOWN/SEMMEDDB/')
SGD = CurieNamespace('SGD', 'https://www.yeastgenome.org/locus/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SMPDB = CurieNamespace('SMPDB', 'http://smpdb.ca/view/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UMLS = CurieNamespace('UMLS', 'http://linkedlifedata.com/resource/umls/id/')
UMLSSC = CurieNamespace('UMLSSC', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/')
UMLSSG = CurieNamespace('UMLSSG', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/')
UMLSST = CurieNamespace('UMLSST', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/')
UNII = CurieNamespace('UNII', 'http://fdasis.nlm.nih.gov/srs/unii/')
UNIPROTKB = CurieNamespace('UNIPROTKB', 'http://example.org/UNKNOWN/UNIPROTKB/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://identifiers.org/uniprot/')
VMC = CurieNamespace('VMC', 'http://example.org/UNKNOWN/VMC/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WD = CurieNamespace('WD', 'http://example.org/UNKNOWN/WD/')
WIKIPATHWAYS = CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/')
ZFIN = CurieNamespace('ZFIN', 'http://zfin.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCT = CurieNamespace('dct', 'http://example.org/UNKNOWN/dct/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DICTYBASE = CurieNamespace('dictyBase', 'http://dictybase.org/gene/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
VOID = CurieNamespace('void', 'http://rdfs.org/ns/void#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = BIOLINK.ChemicalFormulaValue


class IdentifierType(ElementIdentifier):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "identifier type"
    type_model_uri = BIOLINK.IdentifierType


class IriType(Uriorcurie):
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


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = BIOLINK.PercentageFrequencyValue


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
class AttributeId(ElementIdentifier):
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


class NamedThingId(ElementIdentifier):
    pass


class DataFileId(NamedThingId):
    pass


class SourceFileId(DataFileId):
    pass


class DataSetId(NamedThingId):
    pass


class DataSetVersionId(DataSetId):
    pass


class DistributionLevelId(DataSetVersionId):
    pass


class DataSetSummaryId(DataSetVersionId):
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


class MaterialSampleId(NamedThingId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class ExposureEventId(BiologicalEntityId):
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


class ChemicalExposureId(ExposureEventId):
    pass


class DrugExposureId(ChemicalExposureId):
    pass


class TreatmentId(ExposureEventId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(NodeIdentifier):
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


class ChemicalToChemicalAssociationId(AssociationId):
    pass


class ChemicalToChemicalDerivationAssociationId(ChemicalToChemicalAssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class MaterialSampleToThingAssociationId(AssociationId):
    pass


class MaterialSampleDerivationAssociationId(AssociationId):
    pass


class MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
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


class DiseaseToExposureAssociationId(DiseaseToThingAssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class ExposureEventToPhenotypicFeatureAssociationId(AssociationId):
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


class PhysicalEntityId(NamedThingId):
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


class CellLineId(OrganismalEntityId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


class AbstractEntity(YAMLRoot):
    """
    Any thing that is not a process or a physical mass-bearing entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AbstractEntity
    class_class_curie: ClassVar[str] = "biolink:AbstractEntity"
    class_name: ClassVar[str] = "abstract entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AbstractEntity


@dataclass
class Attribute(AbstractEntity):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Attribute
    class_class_curie: ClassVar[str] = "biolink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Attribute

    id: Union[ElementIdentifier, AttributeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_attribute_type: Optional[Union[ElementIdentifier, OntologyClassId]] = None
    has_quantitative_value: List[Union[dict, "QuantityValue"]] = empty_list()
    has_qualitative_value: Optional[Union[ElementIdentifier, NamedThingId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        if self.has_attribute_type is not None and not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)
        self.has_quantitative_value = [v if isinstance(v, QuantityValue)
                                       else QuantityValue(**v) for v in self.has_quantitative_value]
        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)
        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(AbstractEntity):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.QuantityValue
    class_class_curie: ClassVar[str] = "biolink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex
    class_class_curie: ClassVar[str] = "biolink:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex

    id: Union[ElementIdentifier, BiologicalSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, PhenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, SeverityValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, FrequencyValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, ClinicalModifierId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, OnsetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "physically_interacts_with", "affects", "regulates", "positively_regulates", "negatively_regulates", "disrupts", "homologous_to", "paralogous_to", "orthologous_to", "xenologous_to", "coexists_with", "colocalizes_with", "affects_risk_for", "predisposes", "contributes_to", "causes", "caused_by", "prevents", "occurs_in", "located_in", "location_of", "model_of", "overlaps", "has_part", "part_of", "participates_in", "actively_involved_in", "capable_of", "derives_into", "derives_from", "manifestation_of", "produces", "same_as", "has_molecular_consequence"]

    class_class_uri: ClassVar[URIRef] = WD.Q35120
    class_class_curie: ClassVar[str] = "WD:Q35120"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NamedThing

    id: Union[ElementIdentifier, NamedThingId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        if not isinstance(self.category, list) or len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]
        super().__post_init__(**kwargs)


@dataclass
class DataFile(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = EFO["0004095"]
    class_class_curie: ClassVar[str] = "EFO:0004095"
    class_name: ClassVar[str] = "data file"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataFile

    id: Union[ElementIdentifier, DataFileId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class SourceFile(DataFile):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.SourceFile
    class_class_curie: ClassVar[str] = "biolink:SourceFile"
    class_name: ClassVar[str] = "source file"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SourceFile

    id: Union[ElementIdentifier, SourceFileId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    source_version: Optional[str] = None
    retrievedOn: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SourceFileId):
            self.id = SourceFileId(self.id)
        if self.retrievedOn is not None and not isinstance(self.retrievedOn, XSDDate):
            self.retrievedOn = XSDDate(self.retrievedOn)
        super().__post_init__(**kwargs)


@dataclass
class DataSet(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = IAO["0000100"]
    class_class_curie: ClassVar[str] = "IAO:0000100"
    class_name: ClassVar[str] = "data set"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataSet

    id: Union[ElementIdentifier, DataSetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataSetId):
            self.id = DataSetId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DataSetVersion(DataSet):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.DataSetVersion
    class_class_curie: ClassVar[str] = "biolink:DataSetVersion"
    class_name: ClassVar[str] = "data set version"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataSetVersion

    id: Union[ElementIdentifier, DataSetVersionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    title: Optional[str] = None
    source_data_file: Optional[Union[ElementIdentifier, DataFileId]] = None
    versionOf: Optional[Union[ElementIdentifier, DataSetId]] = None
    distribution: Optional[Union[ElementIdentifier, DistributionLevelId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataSetVersionId):
            self.id = DataSetVersionId(self.id)
        if self.source_data_file is not None and not isinstance(self.source_data_file, DataFileId):
            self.source_data_file = DataFileId(self.source_data_file)
        if self.versionOf is not None and not isinstance(self.versionOf, DataSetId):
            self.versionOf = DataSetId(self.versionOf)
        if self.distribution is not None and not isinstance(self.distribution, DistributionLevelId):
            self.distribution = DistributionLevelId(self.distribution)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = WD.Q28845870
    class_class_curie: ClassVar[str] = "WD:Q28845870"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalEntity

    id: Union[ElementIdentifier, BiologicalEntityId] = None
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

    id: Union[ElementIdentifier, OntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, RelationshipTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeneOntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class OrganismTaxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = WD.Q16521
    class_class_curie: ClassVar[str] = "WD:Q16521"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon

    id: Union[ElementIdentifier, OrganismTaxonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, OrganismalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class IndividualOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010000"]
    class_class_curie: ClassVar[str] = "SIO:010000"
    class_name: ClassVar[str] = "individual organism"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IndividualOrganism

    id: Union[ElementIdentifier, IndividualOrganismId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, CaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSample(NamedThing):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSample
    class_class_curie: ClassVar[str] = "biolink:MaterialSample"
    class_name: ClassVar[str] = "material sample"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSample

    id: Union[ElementIdentifier, MaterialSampleId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_attribute: List[Union[ElementIdentifier, AttributeId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)
        self.has_attribute = [v if isinstance(v, AttributeId)
                              else AttributeId(v) for v in self.has_attribute]
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = MONDO["0000001"]
    class_class_curie: ClassVar[str] = "MONDO:0000001"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Disease

    id: Union[ElementIdentifier, DiseaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = UPHENO["0001001"]
    class_class_curie: ClassVar[str] = "UPHENO:0001001"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeature

    id: Union[ElementIdentifier, PhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = SIO["000955"]
    class_class_curie: ClassVar[str] = "SIO:000955"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEvent

    id: Union[ElementIdentifier, ExposureEventId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, InformationContentEntityId] = None
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

    id: Union[ElementIdentifier, ConfidenceLevelId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, EvidenceTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, PublicationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity

    id: Union[ElementIdentifier, AdministrativeEntityId] = None
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

    id: Union[ElementIdentifier, ProviderId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, MolecularEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, ChemicalSubstanceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate
    class_class_curie: ClassVar[str] = "biolink:Carbohydrate"
    class_name: ClassVar[str] = "carbohydrate"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate

    id: Union[ElementIdentifier, CarbohydrateId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, DrugId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, MetaboliteId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, AnatomicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, LifeStageId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, PlanetaryEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "has_output", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess

    id: Union[ElementIdentifier, EnvironmentalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature

    id: Union[ElementIdentifier, EnvironmentalFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, ClinicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial
    class_class_curie: ClassVar[str] = "biolink:ClinicalTrial"
    class_name: ClassVar[str] = "clinical trial"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial

    id: Union[ElementIdentifier, ClinicalTrialId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention
    class_class_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    class_name: ClassVar[str] = "clinical intervention"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention

    id: Union[ElementIdentifier, ClinicalInterventionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, DeviceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GenomicEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GenomeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, TranscriptId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, ExonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SO["0000316"]
    class_class_curie: ClassVar[str] = "SO:0000316"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CodingSequence

    id: Union[ElementIdentifier, CodingSequenceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, MacromolecularMachineId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeneOrGeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in", "genetically_interacts_with", "has_gene_product", "gene_associated_with_condition"]

    class_class_uri: ClassVar[URIRef] = SO["0000704"]
    class_class_curie: ClassVar[str] = "SO:0000704"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Gene

    id: Union[ElementIdentifier, GeneId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, ProteinId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeneProductIsoformId] = None
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

    id: Union[ElementIdentifier, ProteinIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = CHEBI["33697"]
    class_class_curie: ClassVar[str] = "CHEBI:33697"
    class_name: ClassVar[str] = "RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProduct

    id: Union[ElementIdentifier, RNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, RNAProductIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = SIO["001235"]
    class_class_curie: ClassVar[str] = "SIO:001235"
    class_name: ClassVar[str] = "noncoding RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NoncodingRNAProduct

    id: Union[ElementIdentifier, NoncodingRNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    class_class_uri: ClassVar[URIRef] = SIO["001397"]
    class_class_curie: ClassVar[str] = "SIO:001397"
    class_name: ClassVar[str] = "microRNA"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MicroRNA

    id: Union[ElementIdentifier, MicroRNAId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = SIO["010046"]
    class_class_curie: ClassVar[str] = "SIO:010046"
    class_name: ClassVar[str] = "macromolecular complex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularComplex

    id: Union[ElementIdentifier, MacromolecularComplexId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeneFamilyId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    class_class_uri: ClassVar[URIRef] = GENO["0000133"]
    class_class_curie: ClassVar[str] = "GENO:0000133"
    class_name: ClassVar[str] = "zygosity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Zygosity

    id: Union[ElementIdentifier, ZygosityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GenotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, HaplotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, SequenceVariantId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    has_gene: List[Union[ElementIdentifier, GeneId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]
        super().__post_init__(**kwargs)


@dataclass
class ChemicalExposure(ExposureEvent):
    """
    A chemical exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = ECTO["9000000"]
    class_class_curie: ClassVar[str] = "ECTO:9000000"
    class_name: ClassVar[str] = "chemical exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalExposure

    id: Union[ElementIdentifier, ChemicalExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DrugExposure(ChemicalExposure):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = ECTO["0000509"]
    class_class_curie: ClassVar[str] = "ECTO:0000509"
    class_name: ClassVar[str] = "drug exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugExposure

    id: Union[ElementIdentifier, DrugExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_drug: List[Union[ElementIdentifier, ChemicalSubstanceId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Treatment(ExposureEvent):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "treats", "has_part"]

    class_class_uri: ClassVar[URIRef] = OGMS["0000090"]
    class_class_curie: ClassVar[str] = "OGMS:0000090"
    class_name: ClassVar[str] = "treatment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Treatment

    id: Union[ElementIdentifier, TreatmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    treats: List[Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId]] = empty_list()
    has_part: List[Union[ElementIdentifier, DrugExposureId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeographicLocationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, GeographicLocationAtTimeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId]
    relation: Union[str, URIorCURIE]
    object: Union[ElementIdentifier, NamedThingId]
    edge_label: Union[str, LabelType]
    id: Union[str, AssociationId] = bnode()
    negated: Optional[Bool] = None
    association_type: Optional[Union[ElementIdentifier, OntologyClassId]] = None
    qualifiers: List[Union[ElementIdentifier, OntologyClassId]] = empty_list()
    publications: List[Union[ElementIdentifier, PublicationId]] = empty_list()
    provided_by: Optional[Union[ElementIdentifier, ProviderId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by is not None and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenotypeId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenotypeToGenotypePartAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenotypeToGeneAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, SequenceVariantId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenotypeToVariantAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToGeneAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToGeneHomologyAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, PairwiseGeneToGeneInteractionId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, CellLineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, CellLineToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, ChemicalSubstanceId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, CaseId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, CaseToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalAssociation(Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one chemical converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalAssociation"
    class_name: ClassVar[str] = "chemical to chemical association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalAssociation

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, ChemicalSubstanceId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToChemicalAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalAssociationId):
            self.id = ChemicalToChemicalAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<change is catalyzed by P>>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalDerivationAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalDerivationAssociation"
    class_name: ClassVar[str] = "chemical to chemical derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalDerivationAssociation

    subject: Union[ElementIdentifier, ChemicalSubstanceId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, ChemicalSubstanceId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToChemicalDerivationAssociationId] = bnode()
    change_is_catalyzed_by: List[Union[ElementIdentifier, MacromolecularMachineId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalDerivationAssociationId):
            self.id = ChemicalToChemicalDerivationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)
        self.change_is_catalyzed_by = [v if isinstance(v, MacromolecularMachineId)
                                       else MacromolecularMachineId(v) for v in self.change_is_catalyzed_by]
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PathwayId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToPathwayAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ChemicalToGeneAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleToThingAssociation(Association):
    """
    An association between a material sample and something
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToThingAssociation"
    class_name: ClassVar[str] = "material sample to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToThingAssociation

    subject: Union[ElementIdentifier, MaterialSampleId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MaterialSampleToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity it is derived from
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleDerivationAssociation"
    class_name: ClassVar[str] = "material sample derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleDerivationAssociation

    subject: Union[ElementIdentifier, MaterialSampleId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MaterialSampleDerivationAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleDerivationAssociationId):
            self.id = MaterialSampleDerivationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a material sample and a disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "material sample to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "entity to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, EntityToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature association to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ThingToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "thing to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ThingToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToThingAssociation"
    class_name: ClassVar[str] = "disease to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation

    subject: Union[ElementIdentifier, DiseaseId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, DiseaseToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseToExposureAssociation(DiseaseToThingAssociation):
    """
    An association between an exposure event and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToExposureAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToExposureAssociation"
    class_name: ClassVar[str] = "disease to exposure association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToExposureAssociation

    subject: Union[ElementIdentifier, DiseaseId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, ExposureEventId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, DiseaseToExposureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseToExposureAssociationId):
            self.id = DiseaseToExposureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ExposureEventId):
            self.object = ExposureEventId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ExposureEventToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, ExposureEventId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ExposureEventToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExposureEventToPhenotypicFeatureAssociationId):
            self.id = ExposureEventToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ExposureEventId):
            self.subject = ExposureEventId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, CaseToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeneToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToThingAssociation"
    class_name: ClassVar[str] = "gene to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://bio2rdf.org/wormbase_vocabulary:Gene-Phenotype-Association")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "gene to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000983"]
    class_class_curie: ClassVar[str] = "SIO:000983"
    class_name: ClassVar[str] = "gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseAssociation

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToDiseaseAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, VariantToPopulationAssociationId] = bnode()
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, PopulationToPopulationAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "variant to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, VariantToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    class_name: ClassVar[str] = "variant to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, VariantToDiseaseAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "gene as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    class_name: ClassVar[str] = "gene has variant that contributes to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToThingAssociation"
    class_name: ClassVar[str] = "genotype to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenotypeToThingAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToExpressionSiteAssociationId] = bnode()
    stage_qualifier: Optional[Union[ElementIdentifier, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[ElementIdentifier, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, TreatmentId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, FunctionalAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, MolecularActivityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, BiologicalProcessId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, CellularComponentId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "gene to go term association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGoTermAssociation

    subject: Union[ElementIdentifier, MolecularEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToGoTermAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenomicEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GenomicSequenceLocalizationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GenomicEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, SequenceFeatureRelationshipId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, TranscriptId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, TranscriptToGeneRelationshipId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneToGeneProductRelationshipId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, ExonId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, TranscriptId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, ExonToTranscriptRelationshipId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, GeneRegulatoryRelationshipId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


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

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = bnode()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "has_output", "precedes", "positively_regulates_process_to_process", "negatively_regulates_process_to_process", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BFO["0000003"]
    class_class_curie: ClassVar[str] = "BFO:0000003"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Occurrent

    id: Union[ElementIdentifier, OccurrentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhysicalEntity(NamedThing):
    """
    An entity that has physical properties such as mass, volume, or charge
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhysicalEntity
    class_class_curie: ClassVar[str] = "biolink:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysicalEntity

    id: Union[ElementIdentifier, PhysicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "has_input", "has_output", "enabled_by", "regulates_process_to_process", "has_participant", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    class_name: ClassVar[str] = "biological process or activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity

    id: Union[ElementIdentifier, BiologicalProcessOrActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "has_input", "has_output", "enabled_by", "regulates_process_to_process", "has_participant", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0003674"]
    class_class_curie: ClassVar[str] = "GO:0003674"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivity

    id: Union[ElementIdentifier, MolecularActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_input: List[Union[ElementIdentifier, ChemicalSubstanceId]] = empty_list()
    has_output: List[Union[ElementIdentifier, ChemicalSubstanceId]] = empty_list()
    enabled_by: List[Union[ElementIdentifier, MacromolecularMachineId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)
        self.has_input = [v if isinstance(v, ChemicalSubstanceId)
                          else ChemicalSubstanceId(v) for v in self.has_input]
        self.has_output = [v if isinstance(v, ChemicalSubstanceId)
                           else ChemicalSubstanceId(v) for v in self.has_output]
        self.enabled_by = [v if isinstance(v, MacromolecularMachineId)
                           else MacromolecularMachineId(v) for v in self.enabled_by]
        super().__post_init__(**kwargs)


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "has_output", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior

    id: Union[ElementIdentifier, ActivityAndBehaviorId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "has_output", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Procedure
    class_class_curie: ClassVar[str] = "biolink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Procedure

    id: Union[ElementIdentifier, ProcedureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "has_output", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Phenomenon
    class_class_curie: ClassVar[str] = "biolink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Phenomenon

    id: Union[ElementIdentifier, PhenomenonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "has_input", "has_output", "enabled_by", "regulates_process_to_process", "has_participant", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0008150"]
    class_class_curie: ClassVar[str] = "GO:0008150"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcess

    id: Union[ElementIdentifier, BiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "has_input", "has_output", "enabled_by", "regulates_process_to_process", "has_participant", "precedes"]

    class_class_uri: ClassVar[URIRef] = GO["0007165"]
    class_class_curie: ClassVar[str] = "GO:0007165"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Pathway

    id: Union[ElementIdentifier, PathwayId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "has_input", "has_output", "enabled_by", "regulates_process_to_process", "has_participant", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess
    class_class_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    class_name: ClassVar[str] = "physiological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess

    id: Union[ElementIdentifier, PhysiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[ElementIdentifier, CellularComponentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = GO["0005623"]
    class_class_curie: ClassVar[str] = "GO:0005623"
    class_name: ClassVar[str] = "cell"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Cell

    id: Union[ElementIdentifier, CellId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class CellLine(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    class_class_uri: ClassVar[URIRef] = CLO["0000031"]
    class_class_curie: ClassVar[str] = "CLO:0000031"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLine

    id: Union[ElementIdentifier, CellLineId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = UBERON["0010000"]
    class_class_curie: ClassVar[str] = "UBERON:0010000"
    class_name: ClassVar[str] = "gross anatomical structure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GrossAnatomicalStructure

    id: Union[ElementIdentifier, GrossAnatomicalStructureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.related_to = Slot(uri=OWL.ObjectProperty, name="related to", curie=OWL.curie('ObjectProperty'),
                      model_uri=BIOLINK.related_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.ASSOCIATED_WITH])

slots.interacts_with = Slot(uri=RO['0002434'], name="interacts with", curie=RO.curie('0002434'),
                      model_uri=BIOLINK.interacts_with, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.physically_interacts_with = Slot(uri=WD.P129, name="physically interacts with", curie=WD.curie('P129'),
                      model_uri=BIOLINK.physically_interacts_with, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.INTERACTS_WITH])

slots.molecularly_interacts_with = Slot(uri=RO['0002436'], name="molecularly interacts with", curie=RO.curie('0002436'),
                      model_uri=BIOLINK.molecularly_interacts_with, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.genetically_interacts_with = Slot(uri=RO['0002435'], name="genetically interacts with", curie=RO.curie('0002435'),
                      model_uri=BIOLINK.genetically_interacts_with, domain=Gene, range=List[Union[ElementIdentifier, GeneId]])

slots.affects = Slot(uri=SEMMEDDB.AFFECTS, name="affects", curie=SEMMEDDB.curie('AFFECTS'),
                      model_uri=BIOLINK.affects, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.affects_abundance_of = Slot(uri=BIOLINK.affects_abundance_of, name="affects abundance of", curie=BIOLINK.curie('affects_abundance_of'),
                      model_uri=BIOLINK.affects_abundance_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_abundance_of = Slot(uri=BIOLINK.increases_abundance_of, name="increases abundance of", curie=BIOLINK.curie('increases_abundance_of'),
                      model_uri=BIOLINK.increases_abundance_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_abundance_of = Slot(uri=BIOLINK.decreases_abundance_of, name="decreases abundance of", curie=BIOLINK.curie('decreases_abundance_of'),
                      model_uri=BIOLINK.decreases_abundance_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_activity_of = Slot(uri=BIOLINK.affects_activity_of, name="affects activity of", curie=BIOLINK.curie('affects_activity_of'),
                      model_uri=BIOLINK.affects_activity_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_activity_of = Slot(uri=BIOLINK.increases_activity_of, name="increases activity of", curie=BIOLINK.curie('increases_activity_of'),
                      model_uri=BIOLINK.increases_activity_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_activity_of = Slot(uri=BIOLINK.decreases_activity_of, name="decreases activity of", curie=BIOLINK.curie('decreases_activity_of'),
                      model_uri=BIOLINK.decreases_activity_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_expression_of = Slot(uri=BIOLINK.affects_expression_of, name="affects expression of", curie=BIOLINK.curie('affects_expression_of'),
                      model_uri=BIOLINK.affects_expression_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.increases_expression_of = Slot(uri=BIOLINK.increases_expression_of, name="increases expression of", curie=BIOLINK.curie('increases_expression_of'),
                      model_uri=BIOLINK.increases_expression_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.decreases_expression_of = Slot(uri=BIOLINK.decreases_expression_of, name="decreases expression of", curie=BIOLINK.curie('decreases_expression_of'),
                      model_uri=BIOLINK.decreases_expression_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.affects_folding_of = Slot(uri=BIOLINK.affects_folding_of, name="affects folding of", curie=BIOLINK.curie('affects_folding_of'),
                      model_uri=BIOLINK.affects_folding_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_folding_of = Slot(uri=BIOLINK.increases_folding_of, name="increases folding of", curie=BIOLINK.curie('increases_folding_of'),
                      model_uri=BIOLINK.increases_folding_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_folding_of = Slot(uri=BIOLINK.decreases_folding_of, name="decreases folding of", curie=BIOLINK.curie('decreases_folding_of'),
                      model_uri=BIOLINK.decreases_folding_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_localization_of = Slot(uri=BIOLINK.affects_localization_of, name="affects localization of", curie=BIOLINK.curie('affects_localization_of'),
                      model_uri=BIOLINK.affects_localization_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_localization_of = Slot(uri=BIOLINK.increases_localization_of, name="increases localization of", curie=BIOLINK.curie('increases_localization_of'),
                      model_uri=BIOLINK.increases_localization_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_localization_of = Slot(uri=BIOLINK.decreases_localization_of, name="decreases localization of", curie=BIOLINK.curie('decreases_localization_of'),
                      model_uri=BIOLINK.decreases_localization_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_metabolic_processing_of = Slot(uri=BIOLINK.affects_metabolic_processing_of, name="affects metabolic processing of", curie=BIOLINK.curie('affects_metabolic_processing_of'),
                      model_uri=BIOLINK.affects_metabolic_processing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_metabolic_processing_of = Slot(uri=BIOLINK.increases_metabolic_processing_of, name="increases metabolic processing of", curie=BIOLINK.curie('increases_metabolic_processing_of'),
                      model_uri=BIOLINK.increases_metabolic_processing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_metabolic_processing_of = Slot(uri=BIOLINK.decreases_metabolic_processing_of, name="decreases metabolic processing of", curie=BIOLINK.curie('decreases_metabolic_processing_of'),
                      model_uri=BIOLINK.decreases_metabolic_processing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_molecular_modification_of = Slot(uri=BIOLINK.affects_molecular_modification_of, name="affects molecular modification of", curie=BIOLINK.curie('affects_molecular_modification_of'),
                      model_uri=BIOLINK.affects_molecular_modification_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_molecular_modification_of = Slot(uri=BIOLINK.increases_molecular_modification_of, name="increases molecular modification of", curie=BIOLINK.curie('increases_molecular_modification_of'),
                      model_uri=BIOLINK.increases_molecular_modification_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_molecular_modification_of = Slot(uri=BIOLINK.decreases_molecular_modification_of, name="decreases molecular modification of", curie=BIOLINK.curie('decreases_molecular_modification_of'),
                      model_uri=BIOLINK.decreases_molecular_modification_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_synthesis_of = Slot(uri=BIOLINK.affects_synthesis_of, name="affects synthesis of", curie=BIOLINK.curie('affects_synthesis_of'),
                      model_uri=BIOLINK.affects_synthesis_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_synthesis_of = Slot(uri=BIOLINK.increases_synthesis_of, name="increases synthesis of", curie=BIOLINK.curie('increases_synthesis_of'),
                      model_uri=BIOLINK.increases_synthesis_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_synthesis_of = Slot(uri=BIOLINK.decreases_synthesis_of, name="decreases synthesis of", curie=BIOLINK.curie('decreases_synthesis_of'),
                      model_uri=BIOLINK.decreases_synthesis_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_degradation_of = Slot(uri=BIOLINK.affects_degradation_of, name="affects degradation of", curie=BIOLINK.curie('affects_degradation_of'),
                      model_uri=BIOLINK.affects_degradation_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_degradation_of = Slot(uri=BIOLINK.increases_degradation_of, name="increases degradation of", curie=BIOLINK.curie('increases_degradation_of'),
                      model_uri=BIOLINK.increases_degradation_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_degradation_of = Slot(uri=BIOLINK.decreases_degradation_of, name="decreases degradation of", curie=BIOLINK.curie('decreases_degradation_of'),
                      model_uri=BIOLINK.decreases_degradation_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_mutation_rate_of = Slot(uri=BIOLINK.affects_mutation_rate_of, name="affects mutation rate of", curie=BIOLINK.curie('affects_mutation_rate_of'),
                      model_uri=BIOLINK.affects_mutation_rate_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.increases_mutation_rate_of = Slot(uri=BIOLINK.increases_mutation_rate_of, name="increases mutation rate of", curie=BIOLINK.curie('increases_mutation_rate_of'),
                      model_uri=BIOLINK.increases_mutation_rate_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.decreases_mutation_rate_of = Slot(uri=BIOLINK.decreases_mutation_rate_of, name="decreases mutation rate of", curie=BIOLINK.curie('decreases_mutation_rate_of'),
                      model_uri=BIOLINK.decreases_mutation_rate_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, GenomicEntityId]])

slots.affects_response_to = Slot(uri=BIOLINK.affects_response_to, name="affects response to", curie=BIOLINK.curie('affects_response_to'),
                      model_uri=BIOLINK.affects_response_to, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_response_to = Slot(uri=BIOLINK.increases_response_to, name="increases response to", curie=BIOLINK.curie('increases_response_to'),
                      model_uri=BIOLINK.increases_response_to, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_response_to = Slot(uri=BIOLINK.decreases_response_to, name="decreases response to", curie=BIOLINK.curie('decreases_response_to'),
                      model_uri=BIOLINK.decreases_response_to, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_splicing_of = Slot(uri=BIOLINK.affects_splicing_of, name="affects splicing of", curie=BIOLINK.curie('affects_splicing_of'),
                      model_uri=BIOLINK.affects_splicing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, TranscriptId]])

slots.increases_splicing_of = Slot(uri=BIOLINK.increases_splicing_of, name="increases splicing of", curie=BIOLINK.curie('increases_splicing_of'),
                      model_uri=BIOLINK.increases_splicing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, TranscriptId]])

slots.decreases_splicing_of = Slot(uri=BIOLINK.decreases_splicing_of, name="decreases splicing of", curie=BIOLINK.curie('decreases_splicing_of'),
                      model_uri=BIOLINK.decreases_splicing_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, TranscriptId]])

slots.affects_stability_of = Slot(uri=BIOLINK.affects_stability_of, name="affects stability of", curie=BIOLINK.curie('affects_stability_of'),
                      model_uri=BIOLINK.affects_stability_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_stability_of = Slot(uri=BIOLINK.increases_stability_of, name="increases stability of", curie=BIOLINK.curie('increases_stability_of'),
                      model_uri=BIOLINK.increases_stability_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_stability_of = Slot(uri=BIOLINK.decreases_stability_of, name="decreases stability of", curie=BIOLINK.curie('decreases_stability_of'),
                      model_uri=BIOLINK.decreases_stability_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_transport_of = Slot(uri=BIOLINK.affects_transport_of, name="affects transport of", curie=BIOLINK.curie('affects_transport_of'),
                      model_uri=BIOLINK.affects_transport_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_transport_of = Slot(uri=BIOLINK.increases_transport_of, name="increases transport of", curie=BIOLINK.curie('increases_transport_of'),
                      model_uri=BIOLINK.increases_transport_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_transport_of = Slot(uri=BIOLINK.decreases_transport_of, name="decreases transport of", curie=BIOLINK.curie('decreases_transport_of'),
                      model_uri=BIOLINK.decreases_transport_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_secretion_of = Slot(uri=BIOLINK.affects_secretion_of, name="affects secretion of", curie=BIOLINK.curie('affects_secretion_of'),
                      model_uri=BIOLINK.affects_secretion_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_secretion_of = Slot(uri=BIOLINK.increases_secretion_of, name="increases secretion of", curie=BIOLINK.curie('increases_secretion_of'),
                      model_uri=BIOLINK.increases_secretion_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_secretion_of = Slot(uri=BIOLINK.decreases_secretion_of, name="decreases secretion of", curie=BIOLINK.curie('decreases_secretion_of'),
                      model_uri=BIOLINK.decreases_secretion_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.affects_uptake_of = Slot(uri=BIOLINK.affects_uptake_of, name="affects uptake of", curie=BIOLINK.curie('affects_uptake_of'),
                      model_uri=BIOLINK.affects_uptake_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.increases_uptake_of = Slot(uri=BIOLINK.increases_uptake_of, name="increases uptake of", curie=BIOLINK.curie('increases_uptake_of'),
                      model_uri=BIOLINK.increases_uptake_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.decreases_uptake_of = Slot(uri=BIOLINK.decreases_uptake_of, name="decreases uptake of", curie=BIOLINK.curie('decreases_uptake_of'),
                      model_uri=BIOLINK.decreases_uptake_of, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.regulates = Slot(uri=WD.P128, name="regulates", curie=WD.curie('P128'),
                      model_uri=BIOLINK.regulates, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.positively_regulates = Slot(uri=BIOLINK.positively_regulates, name="positively regulates", curie=BIOLINK.curie('positively_regulates'),
                      model_uri=BIOLINK.positively_regulates, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.negatively_regulates = Slot(uri=BIOLINK.negatively_regulates, name="negatively regulates", curie=BIOLINK.curie('negatively_regulates'),
                      model_uri=BIOLINK.negatively_regulates, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.regulates_process_to_process = Slot(uri=RO['0002211'], name="regulates, process to process", curie=RO.curie('0002211'),
                      model_uri=BIOLINK.regulates_process_to_process, domain=Occurrent, range=List[Union[ElementIdentifier, OccurrentId]])

slots.positively_regulates_process_to_process = Slot(uri=RO['0002213'], name="positively regulates, process to process", curie=RO.curie('0002213'),
                      model_uri=BIOLINK.positively_regulates_process_to_process, domain=Occurrent, range=List[Union[ElementIdentifier, OccurrentId]])

slots.negatively_regulates_process_to_process = Slot(uri=RO['0002212'], name="negatively regulates, process to process", curie=RO.curie('0002212'),
                      model_uri=BIOLINK.negatively_regulates_process_to_process, domain=Occurrent, range=List[Union[ElementIdentifier, OccurrentId]])

slots.regulates_entity_to_entity = Slot(uri=RO['0002448'], name="regulates, entity to entity", curie=RO.curie('0002448'),
                      model_uri=BIOLINK.regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.positively_regulates_entity_to_entity = Slot(uri=RO['0002450'], name="positively regulates, entity to entity", curie=RO.curie('0002450'),
                      model_uri=BIOLINK.positively_regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]], mappings = [SEMMEDDB.STIMULATES])

slots.negatively_regulates_entity_to_entity = Slot(uri=RO['0002449'], name="negatively regulates, entity to entity", curie=RO.curie('0002449'),
                      model_uri=BIOLINK.negatively_regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[ElementIdentifier, MolecularEntityId]], mappings = [SEMMEDDB.INHIBITS])

slots.disrupts = Slot(uri=SEMMEDDB.DISRUPTS, name="disrupts", curie=SEMMEDDB.curie('DISRUPTS'),
                      model_uri=BIOLINK.disrupts, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.has_gene_product = Slot(uri=RO['0002205'], name="has gene product", curie=RO.curie('0002205'),
                      model_uri=BIOLINK.has_gene_product, domain=Gene, range=List[Union[ElementIdentifier, GeneProductId]], mappings = [WD.P688])

slots.homologous_to = Slot(uri=RO.HOM0000001, name="homologous to", curie=RO.curie('HOM0000001'),
                      model_uri=BIOLINK.homologous_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SIO["010302"]])

slots.paralogous_to = Slot(uri=RO.HOM0000011, name="paralogous to", curie=RO.curie('HOM0000011'),
                      model_uri=BIOLINK.paralogous_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.orthologous_to = Slot(uri=RO.HOM0000017, name="orthologous to", curie=RO.curie('HOM0000017'),
                      model_uri=BIOLINK.orthologous_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P684])

slots.xenologous_to = Slot(uri=RO.HOM0000018, name="xenologous to", curie=RO.curie('HOM0000018'),
                      model_uri=BIOLINK.xenologous_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.coexists_with = Slot(uri=SEMMEDDB.COEXISTS_WITH, name="coexists with", curie=SEMMEDDB.curie('COEXISTS_WITH'),
                      model_uri=BIOLINK.coexists_with, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.in_pathway_with = Slot(uri=BIOLINK.in_pathway_with, name="in pathway with", curie=BIOLINK.curie('in_pathway_with'),
                      model_uri=BIOLINK.in_pathway_with, domain=GeneOrGeneProduct, range=List[Union[ElementIdentifier, GeneOrGeneProductId]])

slots.in_complex_with = Slot(uri=BIOLINK.in_complex_with, name="in complex with", curie=BIOLINK.curie('in_complex_with'),
                      model_uri=BIOLINK.in_complex_with, domain=GeneOrGeneProduct, range=List[Union[ElementIdentifier, GeneOrGeneProductId]])

slots.in_cell_population_with = Slot(uri=BIOLINK.in_cell_population_with, name="in cell population with", curie=BIOLINK.curie('in_cell_population_with'),
                      model_uri=BIOLINK.in_cell_population_with, domain=GeneOrGeneProduct, range=List[Union[ElementIdentifier, GeneOrGeneProductId]])

slots.colocalizes_with = Slot(uri=RO['00002325'], name="colocalizes with", curie=RO.curie('00002325'),
                      model_uri=BIOLINK.colocalizes_with, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.gene_associated_with_condition = Slot(uri=WD.P2293, name="gene associated with condition", curie=WD.curie('P2293'),
                      model_uri=BIOLINK.gene_associated_with_condition, domain=Gene, range=List[Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId]])

slots.affects_risk_for = Slot(uri=BIOLINK.affects_risk_for, name="affects risk for", curie=BIOLINK.curie('affects_risk_for'),
                      model_uri=BIOLINK.affects_risk_for, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.predisposes = Slot(uri=SEMMEDDB.PREDISPOSES, name="predisposes", curie=SEMMEDDB.curie('PREDISPOSES'),
                      model_uri=BIOLINK.predisposes, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.contributes_to = Slot(uri=RO['0002326'], name="contributes to", curie=RO.curie('0002326'),
                      model_uri=BIOLINK.contributes_to, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.causes = Slot(uri=RO['0002410'], name="causes", curie=RO.curie('0002410'),
                      model_uri=BIOLINK.causes, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.CAUSES, WD.P1542])

slots.caused_by = Slot(uri=BIOLINK.caused_by, name="caused by", curie=BIOLINK.curie('caused_by'),
                      model_uri=BIOLINK.caused_by, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P828])

slots.treats = Slot(uri=RO['0002606'], name="treats", curie=RO.curie('0002606'),
                      model_uri=BIOLINK.treats, domain=Treatment, range=List[Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId]], mappings = [RO["0003307"], SEMMEDDB.TREATS, WD.P2175])

slots.prevents = Slot(uri=RO['0002599'], name="prevents", curie=RO.curie('0002599'),
                      model_uri=BIOLINK.prevents, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.PREVENTS])

slots.correlated_with = Slot(uri=RO['0002610'], name="correlated with", curie=RO.curie('0002610'),
                      model_uri=BIOLINK.correlated_with, domain=DiseaseOrPhenotypicFeature, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.has_biomarker = Slot(uri=BIOLINK.has_biomarker, name="has biomarker", curie=BIOLINK.curie('has_biomarker'),
                      model_uri=BIOLINK.has_biomarker, domain=DiseaseOrPhenotypicFeature, range=List[Union[ElementIdentifier, MolecularEntityId]])

slots.biomarker_for = Slot(uri=RO['0002607'], name="biomarker for", curie=RO.curie('0002607'),
                      model_uri=BIOLINK.biomarker_for, domain=MolecularEntity, range=List[Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId]])

slots.treated_by = Slot(uri=RO['0002302'], name="treated by", curie=RO.curie('0002302'),
                      model_uri=BIOLINK.treated_by, domain=DiseaseOrPhenotypicFeature, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P2176])

slots.expressed_in = Slot(uri=RO['0002206'], name="expressed in", curie=RO.curie('0002206'),
                      model_uri=BIOLINK.expressed_in, domain=GeneOrGeneProduct, range=List[Union[ElementIdentifier, AnatomicalEntityId]])

slots.expresses = Slot(uri=RO['0002292'], name="expresses", curie=RO.curie('0002292'),
                      model_uri=BIOLINK.expresses, domain=AnatomicalEntity, range=List[Union[ElementIdentifier, GeneOrGeneProductId]])

slots.has_phenotype = Slot(uri=RO['0002200'], name="has phenotype", curie=RO.curie('0002200'),
                      model_uri=BIOLINK.has_phenotype, domain=BiologicalEntity, range=List[Union[ElementIdentifier, PhenotypicFeatureId]])

slots.occurs_in = Slot(uri=BFO['0000066'], name="occurs in", curie=BFO.curie('0000066'),
                      model_uri=BIOLINK.occurs_in, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.OCCURS_IN, SEMMEDDB.PROCESS_OF])

slots.located_in = Slot(uri=RO['0001025'], name="located in", curie=RO.curie('0001025'),
                      model_uri=BIOLINK.located_in, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.location_of = Slot(uri=RO['0001015'], name="location of", curie=RO.curie('0001015'),
                      model_uri=BIOLINK.location_of, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.LOCATION_OF, WD["276"]])

slots.model_of = Slot(uri=RO['0003301'], name="model of", curie=RO.curie('0003301'),
                      model_uri=BIOLINK.model_of, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.overlaps = Slot(uri=RO['0002131'], name="overlaps", curie=RO.curie('0002131'),
                      model_uri=BIOLINK.overlaps, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.has_part = Slot(uri=BFO['0000051'], name="has part", curie=BFO.curie('0000051'),
                      model_uri=BIOLINK.has_part, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P527])

slots.part_of = Slot(uri=BFO['0000050'], name="part of", curie=BFO.curie('0000050'),
                      model_uri=BIOLINK.part_of, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.PART_OF, WD.P361])

slots.has_participant = Slot(uri=RO['0000057'], name="has participant", curie=RO.curie('0000057'),
                      model_uri=BIOLINK.has_participant, domain=Occurrent, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P2283])

slots.has_input = Slot(uri=RO['0002233'], name="has input", curie=RO.curie('0002233'),
                      model_uri=BIOLINK.has_input, domain=Occurrent, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.USES])

slots.has_output = Slot(uri=RO['0002234'], name="has output", curie=RO.curie('0002234'),
                      model_uri=BIOLINK.has_output, domain=Occurrent, range=List[Union[ElementIdentifier, NamedThingId]])

slots.participates_in = Slot(uri=RO['0000056'], name="participates in", curie=RO.curie('0000056'),
                      model_uri=BIOLINK.participates_in, domain=NamedThing, range=List[Union[ElementIdentifier, OccurrentId]])

slots.actively_involved_in = Slot(uri=RO['0002331'], name="actively involved in", curie=RO.curie('0002331'),
                      model_uri=BIOLINK.actively_involved_in, domain=NamedThing, range=List[Union[ElementIdentifier, OccurrentId]])

slots.capable_of = Slot(uri=RO['0002215'], name="capable of", curie=RO.curie('0002215'),
                      model_uri=BIOLINK.capable_of, domain=NamedThing, range=List[Union[ElementIdentifier, OccurrentId]])

slots.enabled_by = Slot(uri=RO['0002333'], name="enabled by", curie=RO.curie('0002333'),
                      model_uri=BIOLINK.enabled_by, domain=Occurrent, range=List[Union[ElementIdentifier, BiologicalProcessOrActivityId]])

slots.derives_into = Slot(uri=RO['0001001'], name="derives into", curie=RO.curie('0001001'),
                      model_uri=BIOLINK.derives_into, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [SEMMEDDB.CONVERTS_TO])

slots.derives_from = Slot(uri=RO['0001000'], name="derives from", curie=RO.curie('0001000'),
                      model_uri=BIOLINK.derives_from, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]])

slots.manifestation_of = Slot(uri=SEMMEDDB.MANIFESTATION_OF, name="manifestation of", curie=SEMMEDDB.curie('MANIFESTATION_OF'),
                      model_uri=BIOLINK.manifestation_of, domain=NamedThing, range=List[Union[ElementIdentifier, DiseaseId]], mappings = [WD.P1557])

slots.produces = Slot(uri=RO['0003000'], name="produces", curie=RO.curie('0003000'),
                      model_uri=BIOLINK.produces, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [WD.P1056, SEMMEDDB.PRODUCES])

slots.precedes = Slot(uri=BFO['0000063'], name="precedes", curie=BFO.curie('0000063'),
                      model_uri=BIOLINK.precedes, domain=Occurrent, range=List[Union[ElementIdentifier, OccurrentId]], mappings = [SEMMEDDB.PRECEDES, WD.P156])

slots.same_as = Slot(uri=OWL.equivalentClass, name="same as", curie=OWL.curie('equivalentClass'),
                      model_uri=BIOLINK.same_as, domain=NamedThing, range=List[Union[ElementIdentifier, NamedThingId]], mappings = [OWL.sameAs, SKOS.exactMatch, WD.P2888])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass of", curie=RDFS.curie('subClassOf'),
                      model_uri=BIOLINK.subclass_of, domain=OntologyClass, range=List[Union[str, IriType]], mappings = [SEMMEDDB.IS_A, WD.P279])

slots.node_property = Slot(uri=BIOLINK.node_property, name="node property", curie=BIOLINK.curie('node_property'),
                      model_uri=BIOLINK.node_property, domain=NamedThing, range=Optional[str])

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                      model_uri=BIOLINK.title, domain=DataSetVersion, range=Optional[str])

slots.source_data_file = Slot(uri=DCTERMS.source, name="source data file", curie=DCTERMS.curie('source'),
                      model_uri=BIOLINK.source_data_file, domain=DataSetVersion, range=Optional[Union[ElementIdentifier, DataFileId]])

slots.source_web_page = Slot(uri=DCTERMS.source, name="source web page", curie=DCTERMS.curie('source'),
                      model_uri=BIOLINK.source_web_page, domain=None, range=Optional[str])

slots.retrievedOn = Slot(uri=PAV.retrievedOn, name="retrievedOn", curie=PAV.curie('retrievedOn'),
                      model_uri=BIOLINK.retrievedOn, domain=SourceFile, range=Optional[Union[str, XSDDate]])

slots.versionOf = Slot(uri=DCT.isVersionOf, name="versionOf", curie=DCT.curie('isVersionOf'),
                      model_uri=BIOLINK.versionOf, domain=DataSetVersion, range=Optional[Union[ElementIdentifier, DataSetId]])

slots.source_version = Slot(uri=PAV.version, name="source version", curie=PAV.curie('version'),
                      model_uri=BIOLINK.source_version, domain=SourceFile, range=Optional[str])

slots.downloadURL = Slot(uri=DCT.downloadURL, name="downloadURL", curie=DCT.curie('downloadURL'),
                      model_uri=BIOLINK.downloadURL, domain=None, range=Optional[str])

slots.distribution = Slot(uri=VOID.Dataset, name="distribution", curie=VOID.curie('Dataset'),
                      model_uri=BIOLINK.distribution, domain=DataSetVersion, range=Optional[Union[ElementIdentifier, DistributionLevelId]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                      model_uri=BIOLINK.type, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=BIOLINK.id, name="id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.id, domain=NamedThing, range=Union[ElementIdentifier, NamedThingId])

slots.association_id = Slot(uri=BIOLINK.id, name="association_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.association_id, domain=Association, range=Union[str, AssociationId])

slots.iri = Slot(uri=BIOLINK.iri, name="iri", curie=BIOLINK.curie('iri'),
                      model_uri=BIOLINK.iri, domain=NamedThing, range=Optional[Union[str, IriType]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                      model_uri=BIOLINK.name, domain=NamedThing, range=Union[str, LabelType])

slots.synonym = Slot(uri=BIOLINK.synonym, name="synonym", curie=BIOLINK.curie('synonym'),
                      model_uri=BIOLINK.synonym, domain=NamedThing, range=List[Union[str, LabelType]])

slots.category = Slot(uri=RDFS.subClassOf, name="category", curie=RDFS.curie('subClassOf'),
                      model_uri=BIOLINK.category, domain=NamedThing, range=List[Union[str, IriType]])

slots.full_name = Slot(uri=BIOLINK.full_name, name="full name", curie=BIOLINK.curie('full_name'),
                      model_uri=BIOLINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=BIOLINK.description, domain=NamedThing, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=BIOLINK.systematic_synonym, name="systematic synonym", curie=BIOLINK.curie('systematic_synonym'),
                      model_uri=BIOLINK.systematic_synonym, domain=NamedThing, range=List[Union[str, LabelType]])

slots.association_slot = Slot(uri=BIOLINK.association_slot, name="association slot", curie=BIOLINK.curie('association_slot'),
                      model_uri=BIOLINK.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                      model_uri=BIOLINK.subject, domain=Association, range=Union[ElementIdentifier, NamedThingId], mappings = [OWL.annotatedSource, OBAN.association_has_subject])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                      model_uri=BIOLINK.object, domain=Association, range=Union[ElementIdentifier, NamedThingId], mappings = [OWL.annotatedTarget, OBAN.association_has_object])

slots.edge_label = Slot(uri=BIOLINK.edge_label, name="edge label", curie=BIOLINK.curie('edge_label'),
                      model_uri=BIOLINK.edge_label, domain=Association, range=Union[str, LabelType])

slots.relation = Slot(uri=RDF.predicate, name="relation", curie=RDF.curie('predicate'),
                      model_uri=BIOLINK.relation, domain=Association, range=Union[str, URIorCURIE], mappings = [OWL.annotatedProperty, OBAN.association_has_predicate])

slots.negated = Slot(uri=BIOLINK.negated, name="negated", curie=BIOLINK.curie('negated'),
                      model_uri=BIOLINK.negated, domain=Association, range=Optional[Bool])

slots.has_confidence_level = Slot(uri=BIOLINK.has_confidence_level, name="has confidence level", curie=BIOLINK.curie('has_confidence_level'),
                      model_uri=BIOLINK.has_confidence_level, domain=Association, range=Optional[Union[ElementIdentifier, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=RO['0002558'], name="has evidence", curie=RO.curie('0002558'),
                      model_uri=BIOLINK.has_evidence, domain=Association, range=Optional[Union[ElementIdentifier, EvidenceTypeId]])

slots.provided_by = Slot(uri=PAV.providedBy, name="provided by", curie=PAV.curie('providedBy'),
                      model_uri=BIOLINK.provided_by, domain=Association, range=Optional[Union[ElementIdentifier, ProviderId]])

slots.association_type = Slot(uri=RDF.type, name="association type", curie=RDF.curie('type'),
                      model_uri=BIOLINK.association_type, domain=Association, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.creation_date = Slot(uri=DCTERMS.created, name="creation date", curie=DCTERMS.curie('created'),
                      model_uri=BIOLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.has_receptor = Slot(uri=EXO['0000001'], name="has receptor", curie=EXO.curie('0000001'),
                      model_uri=BIOLINK.has_receptor, domain=ExposureEvent, range=Optional[Union[ElementIdentifier, OrganismalEntityId]])

slots.has_stressor = Slot(uri=EXO['0000000'], name="has stressor", curie=EXO.curie('0000000'),
                      model_uri=BIOLINK.has_stressor, domain=ExposureEvent, range=Optional[str])

slots.has_route = Slot(uri=EXO['0000055'], name="has route", curie=EXO.curie('0000055'),
                      model_uri=BIOLINK.has_route, domain=ExposureEvent, range=Optional[str])

slots.update_date = Slot(uri=BIOLINK.update_date, name="update date", curie=BIOLINK.curie('update_date'),
                      model_uri=BIOLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.in_taxon = Slot(uri=RO['0002162'], name="in taxon", curie=RO.curie('0002162'),
                      model_uri=BIOLINK.in_taxon, domain=None, range=List[Union[ElementIdentifier, OrganismTaxonId]], mappings = [WD.P703])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                      model_uri=BIOLINK.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                      model_uri=BIOLINK.longitude, domain=NamedThing, range=Optional[float])

slots.has_chemical_formula = Slot(uri=WD.P274, name="has chemical formula", curie=WD.curie('P274'),
                      model_uri=BIOLINK.has_chemical_formula, domain=NamedThing, range=Optional[str])

slots.aggregate_statistic = Slot(uri=BIOLINK.aggregate_statistic, name="aggregate statistic", curie=BIOLINK.curie('aggregate_statistic'),
                      model_uri=BIOLINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=BIOLINK.has_count, name="has count", curie=BIOLINK.curie('has_count'),
                      model_uri=BIOLINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=BIOLINK.has_total, name="has total", curie=BIOLINK.curie('has_total'),
                      model_uri=BIOLINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=BIOLINK.has_quotient, name="has quotient", curie=BIOLINK.curie('has_quotient'),
                      model_uri=BIOLINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=BIOLINK.has_percentage, name="has percentage", curie=BIOLINK.curie('has_percentage'),
                      model_uri=BIOLINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=BIOLINK.timepoint, name="timepoint", curie=BIOLINK.curie('timepoint'),
                      model_uri=BIOLINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                      model_uri=BIOLINK.stage_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, LifeStageId]])

slots.quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                      model_uri=BIOLINK.quantifier_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.qualifiers = Slot(uri=BIOLINK.qualifiers, name="qualifiers", curie=BIOLINK.curie('qualifiers'),
                      model_uri=BIOLINK.qualifiers, domain=Association, range=List[Union[ElementIdentifier, OntologyClassId]])

slots.frequency_qualifier = Slot(uri=BIOLINK.frequency_qualifier, name="frequency qualifier", curie=BIOLINK.curie('frequency_qualifier'),
                      model_uri=BIOLINK.frequency_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, FrequencyValueId]])

slots.severity_qualifier = Slot(uri=BIOLINK.severity_qualifier, name="severity qualifier", curie=BIOLINK.curie('severity_qualifier'),
                      model_uri=BIOLINK.severity_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, SeverityValueId]])

slots.sex_qualifier = Slot(uri=BIOLINK.sex_qualifier, name="sex qualifier", curie=BIOLINK.curie('sex_qualifier'),
                      model_uri=BIOLINK.sex_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, BiologicalSexId]])

slots.onset_qualifier = Slot(uri=BIOLINK.onset_qualifier, name="onset qualifier", curie=BIOLINK.curie('onset_qualifier'),
                      model_uri=BIOLINK.onset_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, OnsetId]])

slots.clinical_modifier_qualifier = Slot(uri=BIOLINK.clinical_modifier_qualifier, name="clinical modifier qualifier", curie=BIOLINK.curie('clinical_modifier_qualifier'),
                      model_uri=BIOLINK.clinical_modifier_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, ClinicalModifierId]])

slots.sequence_variant_qualifier = Slot(uri=BIOLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=BIOLINK.curie('sequence_variant_qualifier'),
                      model_uri=BIOLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[ElementIdentifier, SequenceVariantId]])

slots.publications = Slot(uri=BIOLINK.publications, name="publications", curie=BIOLINK.curie('publications'),
                      model_uri=BIOLINK.publications, domain=Association, range=List[Union[ElementIdentifier, PublicationId]])

slots.change_is_catalyzed_by = Slot(uri=BIOLINK.change_is_catalyzed_by, name="change is catalyzed by", curie=BIOLINK.curie('change_is_catalyzed_by'),
                      model_uri=BIOLINK.change_is_catalyzed_by, domain=Association, range=List[Union[ElementIdentifier, MacromolecularMachineId]])

slots.has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                      model_uri=BIOLINK.has_biological_sequence, domain=NamedThing, range=Optional[Union[str, BiologicalSequence]])

slots.has_molecular_consequence = Slot(uri=BIOLINK.has_molecular_consequence, name="has molecular consequence", curie=BIOLINK.curie('has_molecular_consequence'),
                      model_uri=BIOLINK.has_molecular_consequence, domain=NamedThing, range=List[Union[ElementIdentifier, OntologyClassId]])

slots.has_drug = Slot(uri=BIOLINK.has_drug, name="has drug", curie=BIOLINK.curie('has_drug'),
                      model_uri=BIOLINK.has_drug, domain=NamedThing, range=Optional[Union[ElementIdentifier, DrugId]])

slots.has_gene = Slot(uri=BIOLINK.has_gene, name="has gene", curie=BIOLINK.curie('has_gene'),
                      model_uri=BIOLINK.has_gene, domain=NamedThing, range=Optional[Union[ElementIdentifier, GeneId]])

slots.has_zygosity = Slot(uri=BIOLINK.has_zygosity, name="has zygosity", curie=BIOLINK.curie('has_zygosity'),
                      model_uri=BIOLINK.has_zygosity, domain=NamedThing, range=Optional[Union[ElementIdentifier, ZygosityId]])

slots.filler = Slot(uri=BIOLINK.filler, name="filler", curie=BIOLINK.curie('filler'),
                      model_uri=BIOLINK.filler, domain=NamedThing, range=Optional[Union[ElementIdentifier, NamedThingId]])

slots.phase = Slot(uri=BIOLINK.phase, name="phase", curie=BIOLINK.curie('phase'),
                      model_uri=BIOLINK.phase, domain=NamedThing, range=Optional[str])

slots.genome_build = Slot(uri=BIOLINK.genome_build, name="genome build", curie=BIOLINK.curie('genome_build'),
                      model_uri=BIOLINK.genome_build, domain=NamedThing, range=Optional[str])

slots.interbase_coordinate = Slot(uri=BIOLINK.interbase_coordinate, name="interbase coordinate", curie=BIOLINK.curie('interbase_coordinate'),
                      model_uri=BIOLINK.interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.start_interbase_coordinate = Slot(uri=BIOLINK.start_interbase_coordinate, name="start interbase coordinate", curie=BIOLINK.curie('start_interbase_coordinate'),
                      model_uri=BIOLINK.start_interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.end_interbase_coordinate = Slot(uri=BIOLINK.end_interbase_coordinate, name="end interbase coordinate", curie=BIOLINK.curie('end_interbase_coordinate'),
                      model_uri=BIOLINK.end_interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.has_attribute = Slot(uri=BIOLINK.has_attribute, name="has attribute", curie=BIOLINK.curie('has_attribute'),
                      model_uri=BIOLINK.has_attribute, domain=None, range=List[Union[ElementIdentifier, AttributeId]], mappings = [SIO["000008"], RO["0000053"]])

slots.has_attribute_type = Slot(uri=BIOLINK.has_attribute_type, name="has attribute type", curie=BIOLINK.curie('has_attribute_type'),
                      model_uri=BIOLINK.has_attribute_type, domain=Attribute, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.has_qualitative_value = Slot(uri=BIOLINK.has_qualitative_value, name="has qualitative value", curie=BIOLINK.curie('has_qualitative_value'),
                      model_uri=BIOLINK.has_qualitative_value, domain=Attribute, range=Optional[Union[ElementIdentifier, NamedThingId]])

slots.has_quantitative_value = Slot(uri=BIOLINK.has_quantitative_value, name="has quantitative value", curie=BIOLINK.curie('has_quantitative_value'),
                      model_uri=BIOLINK.has_quantitative_value, domain=Attribute, range=List[Union[dict, "QuantityValue"]], mappings = [QUD.quantityValue])

slots.has_numeric_value = Slot(uri=BIOLINK.has_numeric_value, name="has numeric value", curie=BIOLINK.curie('has_numeric_value'),
                      model_uri=BIOLINK.has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue])

slots.has_unit = Slot(uri=BIOLINK.has_unit, name="has unit", curie=BIOLINK.curie('has_unit'),
                      model_uri=BIOLINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]], mappings = [QUD.unit])

slots.macromolecular_machine_name = Slot(uri=BIOLINK.name, name="macromolecular machine_name", curie=BIOLINK.curie('name'),
                      model_uri=BIOLINK.macromolecular_machine_name, domain=MacromolecularMachine, range=Union[str, SymbolType])

slots.sequence_variant_has_gene = Slot(uri=BIOLINK.has_gene, name="sequence variant_has gene", curie=BIOLINK.curie('has_gene'),
                      model_uri=BIOLINK.sequence_variant_has_gene, domain=SequenceVariant, range=List[Union[ElementIdentifier, GeneId]])

slots.sequence_variant_has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="sequence variant_has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                      model_uri=BIOLINK.sequence_variant_has_biological_sequence, domain=SequenceVariant, range=Optional[Union[str, BiologicalSequence]])

slots.sequence_variant_id = Slot(uri=BIOLINK.id, name="sequence variant_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.sequence_variant_id, domain=SequenceVariant, range=Union[ElementIdentifier, SequenceVariantId])

slots.drug_exposure_has_drug = Slot(uri=BIOLINK.has_drug, name="drug exposure_has drug", curie=BIOLINK.curie('has_drug'),
                      model_uri=BIOLINK.drug_exposure_has_drug, domain=DrugExposure, range=List[Union[ElementIdentifier, ChemicalSubstanceId]])

slots.treatment_has_part = Slot(uri=BIOLINK.has_part, name="treatment_has part", curie=BIOLINK.curie('has_part'),
                      model_uri=BIOLINK.treatment_has_part, domain=Treatment, range=List[Union[ElementIdentifier, DrugExposureId]])

slots.genotype_to_genotype_part_association_relation = Slot(uri=BIOLINK.relation, name="genotype to genotype part association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_relation, domain=GenotypeToGenotypePartAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_genotype_part_association_subject = Slot(uri=BIOLINK.subject, name="genotype to genotype part association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_subject, domain=GenotypeToGenotypePartAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.genotype_to_genotype_part_association_object = Slot(uri=BIOLINK.object, name="genotype to genotype part association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_object, domain=GenotypeToGenotypePartAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.genotype_to_gene_association_relation = Slot(uri=BIOLINK.relation, name="genotype to gene association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_gene_association_relation, domain=GenotypeToGeneAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_gene_association_subject = Slot(uri=BIOLINK.subject, name="genotype to gene association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_gene_association_subject, domain=GenotypeToGeneAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.genotype_to_gene_association_object = Slot(uri=BIOLINK.object, name="genotype to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_gene_association_object, domain=GenotypeToGeneAssociation, range=Union[ElementIdentifier, GeneId])

slots.genotype_to_variant_association_relation = Slot(uri=BIOLINK.relation, name="genotype to variant association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_variant_association_relation, domain=GenotypeToVariantAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_variant_association_subject = Slot(uri=BIOLINK.subject, name="genotype to variant association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_variant_association_subject, domain=GenotypeToVariantAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.genotype_to_variant_association_object = Slot(uri=BIOLINK.object, name="genotype to variant association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_variant_association_object, domain=GenotypeToVariantAssociation, range=Union[ElementIdentifier, SequenceVariantId])

slots.gene_to_gene_association_subject = Slot(uri=BIOLINK.subject, name="gene to gene association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_gene_association_subject, domain=GeneToGeneAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_to_gene_association_object = Slot(uri=BIOLINK.object, name="gene to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_gene_association_object, domain=GeneToGeneAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_to_gene_homology_association_relation = Slot(uri=BIOLINK.relation, name="gene to gene homology association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_gene_homology_association_relation, domain=GeneToGeneHomologyAssociation, range=Union[str, URIorCURIE])

slots.pairwise_interaction_association_subject = Slot(uri=BIOLINK.subject, name="pairwise interaction association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.pairwise_interaction_association_subject, domain=None, range=Union[ElementIdentifier, MolecularEntityId])

slots.pairwise_interaction_association_id = Slot(uri=BIOLINK.id, name="pairwise interaction association_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.pairwise_interaction_association_id, domain=None, range=Union[str, PairwiseInteractionAssociationId])

slots.pairwise_interaction_association_relation = Slot(uri=BIOLINK.relation, name="pairwise interaction association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.pairwise_interaction_association_relation, domain=None, range=Union[str, URIorCURIE])

slots.pairwise_interaction_association_object = Slot(uri=BIOLINK.object, name="pairwise interaction association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.pairwise_interaction_association_object, domain=None, range=Union[ElementIdentifier, MolecularEntityId])

slots.interacting_molecules_category = Slot(uri=BIOLINK.interacting_molecules_category, name="interacting molecules category", curie=BIOLINK.curie('interacting_molecules_category'),
                      model_uri=BIOLINK.interacting_molecules_category, domain=None, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.pairwise_gene_to_gene_interaction_relation = Slot(uri=BIOLINK.relation, name="pairwise gene to gene interaction_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.pairwise_gene_to_gene_interaction_relation, domain=PairwiseGeneToGeneInteraction, range=Union[str, URIorCURIE])

slots.cell_line_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="cell line to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.cell_line_to_thing_association_subject, domain=CellLineToThingAssociation, range=Union[ElementIdentifier, CellLineId])

slots.cell_line_to_disease_or_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="cell line to disease or phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.cell_line_to_disease_or_phenotypic_feature_association_subject, domain=CellLineToDiseaseOrPhenotypicFeatureAssociation, range=Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId])

slots.thing_to_disease_or_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="thing to disease or phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.thing_to_disease_or_phenotypic_feature_association_object, domain=ThingToDiseaseOrPhenotypicFeatureAssociation, range=Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId])

slots.chemical_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="chemical to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.chemical_to_thing_association_subject, domain=ChemicalToThingAssociation, range=Union[ElementIdentifier, ChemicalSubstanceId])

slots.case_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="case to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.case_to_thing_association_subject, domain=CaseToThingAssociation, range=Union[ElementIdentifier, CaseId])

slots.chemical_to_chemical_association_object = Slot(uri=BIOLINK.object, name="chemical to chemical association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_chemical_association_object, domain=ChemicalToChemicalAssociation, range=Union[ElementIdentifier, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_subject = Slot(uri=BIOLINK.subject, name="chemical to chemical derivation association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_subject, domain=ChemicalToChemicalDerivationAssociation, range=Union[ElementIdentifier, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_object = Slot(uri=BIOLINK.object, name="chemical to chemical derivation association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_object, domain=ChemicalToChemicalDerivationAssociation, range=Union[ElementIdentifier, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_relation = Slot(uri=BIOLINK.relation, name="chemical to chemical derivation association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_relation, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, URIorCURIE])

slots.chemical_to_chemical_derivation_association_change_is_catalyzed_by = Slot(uri=BIOLINK.change_is_catalyzed_by, name="chemical to chemical derivation association_change is catalyzed by", curie=BIOLINK.curie('change_is_catalyzed_by'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_change_is_catalyzed_by, domain=ChemicalToChemicalDerivationAssociation, range=List[Union[ElementIdentifier, MacromolecularMachineId]])

slots.chemical_to_disease_or_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="chemical to disease or phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_disease_or_phenotypic_feature_association_object, domain=ChemicalToDiseaseOrPhenotypicFeatureAssociation, range=Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId])

slots.chemical_to_pathway_association_object = Slot(uri=BIOLINK.object, name="chemical to pathway association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_pathway_association_object, domain=ChemicalToPathwayAssociation, range=Union[ElementIdentifier, PathwayId])

slots.chemical_to_gene_association_object = Slot(uri=BIOLINK.object, name="chemical to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_gene_association_object, domain=ChemicalToGeneAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.material_sample_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="material sample to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.material_sample_to_thing_association_subject, domain=MaterialSampleToThingAssociation, range=Union[ElementIdentifier, MaterialSampleId])

slots.material_sample_derivation_association_subject = Slot(uri=BIOLINK.subject, name="material sample derivation association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.material_sample_derivation_association_subject, domain=MaterialSampleDerivationAssociation, range=Union[ElementIdentifier, MaterialSampleId])

slots.material_sample_derivation_association_object = Slot(uri=BIOLINK.object, name="material sample derivation association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.material_sample_derivation_association_object, domain=MaterialSampleDerivationAssociation, range=Union[ElementIdentifier, NamedThingId])

slots.material_sample_derivation_association_relation = Slot(uri=BIOLINK.relation, name="material sample derivation association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.material_sample_derivation_association_relation, domain=MaterialSampleDerivationAssociation, range=Union[str, URIorCURIE])

slots.entity_to_phenotypic_feature_association_description = Slot(uri=BIOLINK.description, name="entity to phenotypic feature association_description", curie=BIOLINK.curie('description'),
                      model_uri=BIOLINK.entity_to_phenotypic_feature_association_description, domain=EntityToPhenotypicFeatureAssociation, range=Optional[Union[str, NarrativeText]])

slots.entity_to_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="entity to phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.entity_to_phenotypic_feature_association_object, domain=EntityToPhenotypicFeatureAssociation, range=Union[ElementIdentifier, PhenotypicFeatureId])

slots.entity_to_disease_association_object = Slot(uri=BIOLINK.object, name="entity to disease association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.entity_to_disease_association_object, domain=None, range=Union[ElementIdentifier, DiseaseId])

slots.disease_or_phenotypic_feature_association_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="disease or phenotypic feature association to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_or_phenotypic_feature_association_to_thing_association_subject, domain=DiseaseOrPhenotypicFeatureAssociationToThingAssociation, range=Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId])

slots.disease_or_phenotypic_feature_association_to_location_association_object = Slot(uri=BIOLINK.object, name="disease or phenotypic feature association to location association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.disease_or_phenotypic_feature_association_to_location_association_object, domain=DiseaseOrPhenotypicFeatureAssociationToLocationAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.disease_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="disease to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_to_thing_association_subject, domain=DiseaseToThingAssociation, range=Union[ElementIdentifier, DiseaseId])

slots.disease_to_exposure_association_subject = Slot(uri=BIOLINK.subject, name="disease to exposure association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_to_exposure_association_subject, domain=DiseaseToExposureAssociation, range=Union[ElementIdentifier, DiseaseId])

slots.disease_to_exposure_association_object = Slot(uri=BIOLINK.object, name="disease to exposure association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.disease_to_exposure_association_object, domain=DiseaseToExposureAssociation, range=Union[ElementIdentifier, ExposureEventId])

slots.genotype_to_phenotypic_feature_association_relation = Slot(uri=BIOLINK.relation, name="genotype to phenotypic feature association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_phenotypic_feature_association_relation, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="genotype to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_phenotypic_feature_association_subject, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.genotype_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="genotype to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_thing_association_subject, domain=GenotypeToThingAssociation, range=Union[ElementIdentifier, GenotypeId])

slots.exposure_event_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="exposure event to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.exposure_event_to_phenotypic_feature_association_subject, domain=ExposureEventToPhenotypicFeatureAssociation, range=Union[ElementIdentifier, ExposureEventId])

slots.gene_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="gene to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_thing_association_subject, domain=GeneToThingAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.variant_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="variant to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_thing_association_subject, domain=None, range=Union[ElementIdentifier, SequenceVariantId])

slots.gene_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="gene to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_phenotypic_feature_association_subject, domain=GeneToPhenotypicFeatureAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_disease_association_subject, domain=GeneToDiseaseAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.variant_to_population_association_subject = Slot(uri=BIOLINK.subject, name="variant to population association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[ElementIdentifier, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=BIOLINK.object, name="variant to population association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[ElementIdentifier, PopulationOfIndividualOrganismsId])

slots.variant_to_population_association_has_quotient = Slot(uri=BIOLINK.has_quotient, name="variant to population association_has quotient", curie=BIOLINK.curie('has_quotient'),
                      model_uri=BIOLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=BIOLINK.has_count, name="variant to population association_has count", curie=BIOLINK.curie('has_count'),
                      model_uri=BIOLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=BIOLINK.has_total, name="variant to population association_has total", curie=BIOLINK.curie('has_total'),
                      model_uri=BIOLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=BIOLINK.subject, name="population to population association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[ElementIdentifier, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_object = Slot(uri=BIOLINK.object, name="population to population association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[ElementIdentifier, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_relation = Slot(uri=BIOLINK.relation, name="population to population association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.population_to_population_association_relation, domain=PopulationToPopulationAssociation, range=Union[str, URIorCURIE])

slots.variant_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="variant to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_phenotypic_feature_association_subject, domain=VariantToPhenotypicFeatureAssociation, range=Union[ElementIdentifier, SequenceVariantId])

slots.variant_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="variant to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_disease_association_subject, domain=VariantToDiseaseAssociation, range=Union[ElementIdentifier, NamedThingId])

slots.variant_to_disease_association_relation = Slot(uri=BIOLINK.relation, name="variant to disease association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.variant_to_disease_association_relation, domain=VariantToDiseaseAssociation, range=Union[str, URIorCURIE])

slots.variant_to_disease_association_object = Slot(uri=BIOLINK.object, name="variant to disease association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.variant_to_disease_association_object, domain=VariantToDiseaseAssociation, range=Union[ElementIdentifier, NamedThingId])

slots.model_to_disease_mixin_subject = Slot(uri=BIOLINK.subject, name="model to disease mixin_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.model_to_disease_mixin_subject, domain=None, range=Union[ElementIdentifier, NamedThingId])

slots.model_to_disease_mixin_relation = Slot(uri=BIOLINK.relation, name="model to disease mixin_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.model_to_disease_mixin_relation, domain=None, range=Union[str, URIorCURIE])

slots.gene_as_a_model_of_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene as a model of disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_as_a_model_of_disease_association_subject, domain=GeneAsAModelOfDiseaseAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_has_variant_that_contributes_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene has variant that contributes to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_has_variant_that_contributes_to_disease_association_subject, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_to_expression_site_association_subject = Slot(uri=BIOLINK.subject, name="gene to expression site association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_expression_site_association_subject, domain=GeneToExpressionSiteAssociation, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_to_expression_site_association_object = Slot(uri=BIOLINK.object, name="gene to expression site association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_expression_site_association_object, domain=GeneToExpressionSiteAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.gene_to_expression_site_association_relation = Slot(uri=BIOLINK.relation, name="gene to expression site association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_expression_site_association_relation, domain=GeneToExpressionSiteAssociation, range=Union[str, URIorCURIE])

slots.gene_to_expression_site_association_stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="gene to expression site association_stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                      model_uri=BIOLINK.gene_to_expression_site_association_stage_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[ElementIdentifier, LifeStageId]])

slots.gene_to_expression_site_association_quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="gene to expression site association_quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                      model_uri=BIOLINK.gene_to_expression_site_association_quantifier_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.sequence_variant_modulates_treatment_association_subject = Slot(uri=BIOLINK.subject, name="sequence variant modulates treatment association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.sequence_variant_modulates_treatment_association_subject, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[ElementIdentifier, SequenceVariantId])

slots.sequence_variant_modulates_treatment_association_object = Slot(uri=BIOLINK.object, name="sequence variant modulates treatment association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.sequence_variant_modulates_treatment_association_object, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[ElementIdentifier, TreatmentId])

slots.functional_association_subject = Slot(uri=BIOLINK.subject, name="functional association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[ElementIdentifier, MacromolecularMachineId])

slots.functional_association_object = Slot(uri=BIOLINK.object, name="functional association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.functional_association_object, domain=FunctionalAssociation, range=Union[ElementIdentifier, GeneOntologyClassId])

slots.macromolecular_machine_to_molecular_activity_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to molecular activity association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_molecular_activity_association_object, domain=MacromolecularMachineToMolecularActivityAssociation, range=Union[ElementIdentifier, MolecularActivityId])

slots.macromolecular_machine_to_biological_process_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to biological process association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_biological_process_association_object, domain=MacromolecularMachineToBiologicalProcessAssociation, range=Union[ElementIdentifier, BiologicalProcessId])

slots.macromolecular_machine_to_cellular_component_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to cellular component association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_cellular_component_association_object, domain=MacromolecularMachineToCellularComponentAssociation, range=Union[ElementIdentifier, CellularComponentId])

slots.gene_to_go_term_association_subject = Slot(uri=BIOLINK.subject, name="gene to go term association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_go_term_association_subject, domain=GeneToGoTermAssociation, range=Union[ElementIdentifier, MolecularEntityId])

slots.gene_to_go_term_association_object = Slot(uri=BIOLINK.object, name="gene to go term association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_go_term_association_object, domain=GeneToGoTermAssociation, range=Union[ElementIdentifier, GeneOntologyClassId])

slots.genomic_sequence_localization_subject = Slot(uri=BIOLINK.subject, name="genomic sequence localization_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genomic_sequence_localization_subject, domain=GenomicSequenceLocalization, range=Union[ElementIdentifier, GenomicEntityId])

slots.genomic_sequence_localization_object = Slot(uri=BIOLINK.object, name="genomic sequence localization_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genomic_sequence_localization_object, domain=GenomicSequenceLocalization, range=Union[ElementIdentifier, GenomicEntityId])

slots.sequence_feature_relationship_subject = Slot(uri=BIOLINK.subject, name="sequence feature relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[ElementIdentifier, GenomicEntityId])

slots.sequence_feature_relationship_object = Slot(uri=BIOLINK.object, name="sequence feature relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[ElementIdentifier, GenomicEntityId])

slots.transcript_to_gene_relationship_subject = Slot(uri=BIOLINK.subject, name="transcript to gene relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.transcript_to_gene_relationship_subject, domain=TranscriptToGeneRelationship, range=Union[ElementIdentifier, TranscriptId])

slots.transcript_to_gene_relationship_object = Slot(uri=BIOLINK.object, name="transcript to gene relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.transcript_to_gene_relationship_object, domain=TranscriptToGeneRelationship, range=Union[ElementIdentifier, GeneId])

slots.gene_to_gene_product_relationship_subject = Slot(uri=BIOLINK.subject, name="gene to gene product relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_subject, domain=GeneToGeneProductRelationship, range=Union[ElementIdentifier, GeneId])

slots.gene_to_gene_product_relationship_object = Slot(uri=BIOLINK.object, name="gene to gene product relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_object, domain=GeneToGeneProductRelationship, range=Union[ElementIdentifier, GeneProductId])

slots.gene_to_gene_product_relationship_relation = Slot(uri=BIOLINK.relation, name="gene to gene product relationship_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_relation, domain=GeneToGeneProductRelationship, range=Union[str, URIorCURIE])

slots.exon_to_transcript_relationship_subject = Slot(uri=BIOLINK.subject, name="exon to transcript relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.exon_to_transcript_relationship_subject, domain=ExonToTranscriptRelationship, range=Union[ElementIdentifier, ExonId])

slots.exon_to_transcript_relationship_object = Slot(uri=BIOLINK.object, name="exon to transcript relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.exon_to_transcript_relationship_object, domain=ExonToTranscriptRelationship, range=Union[ElementIdentifier, TranscriptId])

slots.gene_regulatory_relationship_relation = Slot(uri=BIOLINK.relation, name="gene regulatory relationship_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_regulatory_relationship_relation, domain=GeneRegulatoryRelationship, range=Union[str, URIorCURIE])

slots.gene_regulatory_relationship_subject = Slot(uri=BIOLINK.subject, name="gene regulatory relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_regulatory_relationship_subject, domain=GeneRegulatoryRelationship, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.gene_regulatory_relationship_object = Slot(uri=BIOLINK.object, name="gene regulatory relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_regulatory_relationship_object, domain=GeneRegulatoryRelationship, range=Union[ElementIdentifier, GeneOrGeneProductId])

slots.anatomical_entity_to_anatomical_entity_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_subject, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_object, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity part of association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_subject, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity part of association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_object, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_relation = Slot(uri=BIOLINK.relation, name="anatomical entity to anatomical entity part of association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_relation, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, URIorCURIE])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity ontogenic association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_subject, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity ontogenic association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_object, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[ElementIdentifier, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_relation = Slot(uri=BIOLINK.relation, name="anatomical entity to anatomical entity ontogenic association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_relation, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, URIorCURIE])

slots.molecular_activity_has_input = Slot(uri=BIOLINK.has_input, name="molecular activity_has input", curie=BIOLINK.curie('has_input'),
                      model_uri=BIOLINK.molecular_activity_has_input, domain=MolecularActivity, range=List[Union[ElementIdentifier, ChemicalSubstanceId]])

slots.molecular_activity_has_output = Slot(uri=BIOLINK.has_output, name="molecular activity_has output", curie=BIOLINK.curie('has_output'),
                      model_uri=BIOLINK.molecular_activity_has_output, domain=MolecularActivity, range=List[Union[ElementIdentifier, ChemicalSubstanceId]])

slots.molecular_activity_enabled_by = Slot(uri=BIOLINK.enabled_by, name="molecular activity_enabled by", curie=BIOLINK.curie('enabled_by'),
                      model_uri=BIOLINK.molecular_activity_enabled_by, domain=MolecularActivity, range=List[Union[ElementIdentifier, MacromolecularMachineId]])
