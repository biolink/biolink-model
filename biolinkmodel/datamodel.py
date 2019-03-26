# Auto generated from biolink-model.yaml by pythongen.py version: 0.0.4
# Generation date: 2019-03-25 17:08
# Schema: biolink model
#
# id: https://biolink.github.io/biolink-model/ontology/biolink.ttl
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import datetime
from typing import Optional, List, Union, Dict, Any
from dataclasses import dataclass
from metamodel.utils.metamodelcore import empty_list, empty_dict
from metamodel.utils.yamlutils import YAMLRoot

metamodel_version = "None"

inherited_slots: List[str] = []


# Type names
class Phenotype(str):
    pass


class ChemicalFormulaValue(str):
    pass


class IdentifierType(str):
    pass


class IriType(str):
    pass


class LabelType(str):
    pass


class NarrativeText(str):
    pass


class SymbolType(str):
    pass


class ChemicalFormulaType(str):
    pass


class FrequencyValue(str):
    pass


class PerecentageFrequencyValue(float):
    pass


class Quotient(float):
    pass


class Unit(str):
    pass


class TimeType(datetime.time):
    pass


class BiologicalSequence(str):
    pass


# Class references
class NamedThingId(IdentifierType):
    pass


class BiologicalEntityId(IdentifierType):
    pass


class OntologyClassId(IdentifierType):
    pass


class RelationshipTypeId(IdentifierType):
    pass


class GeneOntologyClassId(IdentifierType):
    pass


class OrganismTaxonId(IdentifierType):
    pass


class OrganismalEntityId(IdentifierType):
    pass


class IndividualOrganismId(IdentifierType):
    pass


class CaseId(IdentifierType):
    pass


class PopulationOfIndividualOrganismsId(IdentifierType):
    pass


class BiosampleId(IdentifierType):
    pass


class DiseaseOrPhenotypicFeatureId(IdentifierType):
    pass


class DiseaseId(IdentifierType):
    pass


class PhenotypicFeatureId(IdentifierType):
    pass


class EnvironmentId(IdentifierType):
    pass


class InformationContentEntityId(IdentifierType):
    pass


class ConfidenceLevelId(IdentifierType):
    pass


class EvidenceTypeId(IdentifierType):
    pass


class PublicationId(IdentifierType):
    pass


class MolecularEntityId(IdentifierType):
    pass


class ChemicalSubstanceId(IdentifierType):
    pass


class CarbohydrateId(IdentifierType):
    pass


class DrugId(IdentifierType):
    pass


class MetaboliteId(IdentifierType):
    pass


class AnatomicalEntityId(IdentifierType):
    pass


class LifeStageId(IdentifierType):
    pass


class PlanetaryEntityId(IdentifierType):
    pass


class EnvironmentalProcessId(IdentifierType):
    pass


class EnvironmentalFeatureId(IdentifierType):
    pass


class ClinicalEntityId(IdentifierType):
    pass


class ClinicalTrialId(IdentifierType):
    pass


class ClinicalInterventionId(IdentifierType):
    pass


class DeviceId(IdentifierType):
    pass


class GenomicEntityId(IdentifierType):
    pass


class GenomeId(IdentifierType):
    pass


class TranscriptId(IdentifierType):
    pass


class ExonId(IdentifierType):
    pass


class CodingSequenceId(IdentifierType):
    pass


class MacromolecularMachineId(IdentifierType):
    pass


class GeneOrGeneProductId(IdentifierType):
    pass


class GeneId(IdentifierType):
    pass


class GeneProductId(IdentifierType):
    pass


class ProteinId(IdentifierType):
    pass


class GeneProductIsoformId(IdentifierType):
    pass


class ProteinIsoformId(IdentifierType):
    pass


class RNAProductId(IdentifierType):
    pass


class RNAProductIsoformId(IdentifierType):
    pass


class NoncodingRNAProductId(IdentifierType):
    pass


class MicroRNAId(IdentifierType):
    pass


class MacromolecularComplexId(IdentifierType):
    pass


class GeneFamilyId(IdentifierType):
    pass


class GenotypeId(IdentifierType):
    pass


class HaplotypeId(IdentifierType):
    pass


class DrugExposureId(IdentifierType):
    pass


class TreatmentId(IdentifierType):
    pass


class GeographicLocationId(IdentifierType):
    pass


class GeographicLocationAtTimeId(IdentifierType):
    pass


class AssociationAssociation_id(IdentifierType):
    pass


class GenotypeToGenotypePartAssociationAssociation_id(IdentifierType):
    pass


class GenotypeToGeneAssociationAssociation_id(IdentifierType):
    pass


class GenotypeToVariantAssociationAssociation_id(IdentifierType):
    pass


class GeneToGeneAssociationAssociation_id(IdentifierType):
    pass


class GeneToGeneHomologyAssociationAssociation_id(IdentifierType):
    pass


class PairwiseInteractionAssociationAssociation_id(IdentifierType):
    pass


class PairwiseGeneToGeneInteractionAssociation_id(IdentifierType):
    pass


class CellLineToThingAssociationAssociation_id(IdentifierType):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class ChemicalToThingAssociationAssociation_id(IdentifierType):
    pass


class CaseToThingAssociationAssociation_id(IdentifierType):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class ChemicalToPathwayAssociationAssociation_id(IdentifierType):
    pass


class ChemicalToGeneAssociationAssociation_id(IdentifierType):
    pass


class BiosampleToThingAssociationAssociation_id(IdentifierType):
    pass


class BiosampleToDiseaseOrPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class EntityToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationAssociation_id(IdentifierType):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationAssociation_id(IdentifierType):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class DiseaseToThingAssociationAssociation_id(IdentifierType):
    pass


class GenotypeToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class EnvironmentToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class DiseaseToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class CaseToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class GeneToThingAssociationAssociation_id(IdentifierType):
    pass


class VariantToThingAssociationAssociation_id(IdentifierType):
    pass


class GeneToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class GeneToDiseaseAssociationAssociation_id(IdentifierType):
    pass


class VariantToPopulationAssociationAssociation_id(IdentifierType):
    pass


class PopulationToPopulationAssociationAssociation_id(IdentifierType):
    pass


class VariantToPhenotypicFeatureAssociationAssociation_id(IdentifierType):
    pass


class VariantToDiseaseAssociationAssociation_id(IdentifierType):
    pass


class GeneAsAModelOfDiseaseAssociationAssociation_id(IdentifierType):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationAssociation_id(IdentifierType):
    pass


class GenotypeToThingAssociationAssociation_id(IdentifierType):
    pass


class GeneToExpressionSiteAssociationAssociation_id(IdentifierType):
    pass


class SequenceVariantModulatesTreatmentAssociationAssociation_id(IdentifierType):
    pass


class FunctionalAssociationAssociation_id(IdentifierType):
    pass


class MacromolecularMachineToMolecularActivityAssociationAssociation_id(IdentifierType):
    pass


class MacromolecularMachineToBiologicalProcessAssociationAssociation_id(IdentifierType):
    pass


class MacromolecularMachineToCellularComponentAssociationAssociation_id(IdentifierType):
    pass


class GeneToGoTermAssociationAssociation_id(IdentifierType):
    pass


class GenomicSequenceLocalizationAssociation_id(IdentifierType):
    pass


class SequenceFeatureRelationshipAssociation_id(IdentifierType):
    pass


class TranscriptToGeneRelationshipAssociation_id(IdentifierType):
    pass


class GeneToGeneProductRelationshipAssociation_id(IdentifierType):
    pass


class ExonToTranscriptRelationshipAssociation_id(IdentifierType):
    pass


class GeneRegulatoryRelationshipAssociation_id(IdentifierType):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationAssociation_id(IdentifierType):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationAssociation_id(IdentifierType):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationAssociation_id(IdentifierType):
    pass


class OccurrentId(IdentifierType):
    pass


class BiologicalProcessOrActivityId(IdentifierType):
    pass


class MolecularActivityId(IdentifierType):
    pass


class ActivityAndBehaviorId(IdentifierType):
    pass


class ProcedureId(IdentifierType):
    pass


class PhenomenonId(IdentifierType):
    pass


class BiologicalProcessId(IdentifierType):
    pass


class PathwayId(IdentifierType):
    pass


class PhysiologicalProcessId(IdentifierType):
    pass


class CellularComponentId(IdentifierType):
    pass


class CellId(IdentifierType):
    pass


class CellLineId(IdentifierType):
    pass


class GrossAnatomicalStructureId(IdentifierType):
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
    id: NamedThingId
    name: Optional[LabelType] = None
    category: List[IriType] = empty_list()
    related_to: Optional[NamedThingId] = None
    node_property: Optional[str] = None
    iri: Optional[IriType] = None
    synonym: List[LabelType] = empty_list()
    full_name: Optional[LabelType] = None
    description: Optional[NarrativeText] = None
    systematic_synonym: Optional[LabelType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]
        if self.related_to and not isinstance(self.related_to, NamedThingId):
            self.related_to = NamedThingId(self.related_to)
        if self.iri and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)
        self.synonym = [v if isinstance(v, LabelType)
                        else LabelType(v) for v in self.synonym]
        if self.full_name and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)
        if self.description and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.systematic_synonym and not isinstance(self.systematic_synonym, LabelType):
            self.systematic_synonym = LabelType(self.systematic_synonym)


@dataclass
class BiologicalEntity(NamedThing):
    id: BiologicalEntityId = None
    has_phenotype: Optional[Phenotype] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.has_phenotype and not isinstance(self.has_phenotype, Phenotype):
            self.has_phenotype = Phenotype(self.has_phenotype)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    id: OntologyClassId = None
    subclass_of: Optional[OntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        if self.subclass_of and not isinstance(self.subclass_of, OntologyClassId):
            self.subclass_of = OntologyClassId(self.subclass_of)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    id: RelationshipTypeId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    id: GeneOntologyClassId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)


@dataclass
class OrganismTaxon(OntologyClass):
    id: OrganismTaxonId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    id: OrganismalEntityId = None


@dataclass
class IndividualOrganism(OrganismalEntity):
    id: IndividualOrganismId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    id: CaseId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    id: PopulationOfIndividualOrganismsId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)


@dataclass
class Biosample(OrganismalEntity):
    id: BiosampleId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    id: DiseaseOrPhenotypicFeatureId = None
    correlated_with: Optional[MolecularEntityId] = None
    has_biomarker: Optional[MolecularEntityId] = None
    treated_by: Optional[NamedThingId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        if self.correlated_with and not isinstance(self.correlated_with, MolecularEntityId):
            self.correlated_with = MolecularEntityId(self.correlated_with)
        if self.has_biomarker and not isinstance(self.has_biomarker, MolecularEntityId):
            self.has_biomarker = MolecularEntityId(self.has_biomarker)
        if self.treated_by and not isinstance(self.treated_by, NamedThingId):
            self.treated_by = NamedThingId(self.treated_by)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    id: DiseaseId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    id: PhenotypicFeatureId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    id: EnvironmentId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    id: InformationContentEntityId = None


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    id: ConfidenceLevelId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    id: EvidenceTypeId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    id: PublicationId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)


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
    id: MolecularEntityId = None
    molecularly_interacts_with: Optional[MolecularEntityId] = None
    affects_abundance_of: Optional[MolecularEntityId] = None
    increases_abundance_of: Optional[MolecularEntityId] = None
    decreases_abundance_of: Optional[MolecularEntityId] = None
    affects_activity_of: Optional[MolecularEntityId] = None
    increases_activity_of: Optional[MolecularEntityId] = None
    decreases_activity_of: Optional[MolecularEntityId] = None
    affects_expression_of: Optional[GenomicEntityId] = None
    increases_expression_of: Optional[GenomicEntityId] = None
    decreases_expression_of: Optional[GenomicEntityId] = None
    affects_folding_of: Optional[MolecularEntityId] = None
    increases_folding_of: Optional[MolecularEntityId] = None
    decreases_folding_of: Optional[MolecularEntityId] = None
    affects_localization_of: Optional[MolecularEntityId] = None
    increases_localization_of: Optional[MolecularEntityId] = None
    decreases_localization_of: Optional[MolecularEntityId] = None
    affects_metabolic_processing_of: Optional[MolecularEntityId] = None
    increases_metabolic_processing_of: Optional[MolecularEntityId] = None
    decreases_metabolic_processing_of: Optional[MolecularEntityId] = None
    affects_molecular_modification_of: Optional[MolecularEntityId] = None
    increases_molecular_modification_of: Optional[MolecularEntityId] = None
    decreases_molecular_modification_of: Optional[MolecularEntityId] = None
    affects_synthesis_of: Optional[MolecularEntityId] = None
    increases_synthesis_of: Optional[MolecularEntityId] = None
    decreases_synthesis_of: Optional[MolecularEntityId] = None
    affects_degradation_of: Optional[MolecularEntityId] = None
    increases_degradation_of: Optional[MolecularEntityId] = None
    decreases_degradation_of: Optional[MolecularEntityId] = None
    affects_mutation_rate_of: Optional[GenomicEntityId] = None
    increases_mutation_rate_of: Optional[GenomicEntityId] = None
    decreases_mutation_rate_of: Optional[GenomicEntityId] = None
    affects_response_to: Optional[MolecularEntityId] = None
    increases_response_to: Optional[MolecularEntityId] = None
    decreases_response_to: Optional[MolecularEntityId] = None
    affects_splicing_of: Optional[TranscriptId] = None
    increases_splicing_of: Optional[TranscriptId] = None
    decreases_splicing_of: Optional[TranscriptId] = None
    affects_stability_of: Optional[MolecularEntityId] = None
    increases_stability_of: Optional[MolecularEntityId] = None
    decreases_stability_of: Optional[MolecularEntityId] = None
    affects_transport_of: Optional[MolecularEntityId] = None
    increases_transport_of: Optional[MolecularEntityId] = None
    decreases_transport_of: Optional[MolecularEntityId] = None
    affects_secretion_of: Optional[MolecularEntityId] = None
    increases_secretion_of: Optional[MolecularEntityId] = None
    decreases_secretion_of: Optional[MolecularEntityId] = None
    affects_uptake_of: Optional[MolecularEntityId] = None
    increases_uptake_of: Optional[MolecularEntityId] = None
    decreases_uptake_of: Optional[MolecularEntityId] = None
    regulates_entity_to_entity: Optional[MolecularEntityId] = None
    biomarker_for: Optional[DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        if self.molecularly_interacts_with and not isinstance(self.molecularly_interacts_with, MolecularEntityId):
            self.molecularly_interacts_with = MolecularEntityId(self.molecularly_interacts_with)
        if self.affects_abundance_of and not isinstance(self.affects_abundance_of, MolecularEntityId):
            self.affects_abundance_of = MolecularEntityId(self.affects_abundance_of)
        if self.increases_abundance_of and not isinstance(self.increases_abundance_of, MolecularEntityId):
            self.increases_abundance_of = MolecularEntityId(self.increases_abundance_of)
        if self.decreases_abundance_of and not isinstance(self.decreases_abundance_of, MolecularEntityId):
            self.decreases_abundance_of = MolecularEntityId(self.decreases_abundance_of)
        if self.affects_activity_of and not isinstance(self.affects_activity_of, MolecularEntityId):
            self.affects_activity_of = MolecularEntityId(self.affects_activity_of)
        if self.increases_activity_of and not isinstance(self.increases_activity_of, MolecularEntityId):
            self.increases_activity_of = MolecularEntityId(self.increases_activity_of)
        if self.decreases_activity_of and not isinstance(self.decreases_activity_of, MolecularEntityId):
            self.decreases_activity_of = MolecularEntityId(self.decreases_activity_of)
        if self.affects_expression_of and not isinstance(self.affects_expression_of, GenomicEntityId):
            self.affects_expression_of = GenomicEntityId(self.affects_expression_of)
        if self.increases_expression_of and not isinstance(self.increases_expression_of, GenomicEntityId):
            self.increases_expression_of = GenomicEntityId(self.increases_expression_of)
        if self.decreases_expression_of and not isinstance(self.decreases_expression_of, GenomicEntityId):
            self.decreases_expression_of = GenomicEntityId(self.decreases_expression_of)
        if self.affects_folding_of and not isinstance(self.affects_folding_of, MolecularEntityId):
            self.affects_folding_of = MolecularEntityId(self.affects_folding_of)
        if self.increases_folding_of and not isinstance(self.increases_folding_of, MolecularEntityId):
            self.increases_folding_of = MolecularEntityId(self.increases_folding_of)
        if self.decreases_folding_of and not isinstance(self.decreases_folding_of, MolecularEntityId):
            self.decreases_folding_of = MolecularEntityId(self.decreases_folding_of)
        if self.affects_localization_of and not isinstance(self.affects_localization_of, MolecularEntityId):
            self.affects_localization_of = MolecularEntityId(self.affects_localization_of)
        if self.increases_localization_of and not isinstance(self.increases_localization_of, MolecularEntityId):
            self.increases_localization_of = MolecularEntityId(self.increases_localization_of)
        if self.decreases_localization_of and not isinstance(self.decreases_localization_of, MolecularEntityId):
            self.decreases_localization_of = MolecularEntityId(self.decreases_localization_of)
        if self.affects_metabolic_processing_of and not isinstance(self.affects_metabolic_processing_of, MolecularEntityId):
            self.affects_metabolic_processing_of = MolecularEntityId(self.affects_metabolic_processing_of)
        if self.increases_metabolic_processing_of and not isinstance(self.increases_metabolic_processing_of, MolecularEntityId):
            self.increases_metabolic_processing_of = MolecularEntityId(self.increases_metabolic_processing_of)
        if self.decreases_metabolic_processing_of and not isinstance(self.decreases_metabolic_processing_of, MolecularEntityId):
            self.decreases_metabolic_processing_of = MolecularEntityId(self.decreases_metabolic_processing_of)
        if self.affects_molecular_modification_of and not isinstance(self.affects_molecular_modification_of, MolecularEntityId):
            self.affects_molecular_modification_of = MolecularEntityId(self.affects_molecular_modification_of)
        if self.increases_molecular_modification_of and not isinstance(self.increases_molecular_modification_of, MolecularEntityId):
            self.increases_molecular_modification_of = MolecularEntityId(self.increases_molecular_modification_of)
        if self.decreases_molecular_modification_of and not isinstance(self.decreases_molecular_modification_of, MolecularEntityId):
            self.decreases_molecular_modification_of = MolecularEntityId(self.decreases_molecular_modification_of)
        if self.affects_synthesis_of and not isinstance(self.affects_synthesis_of, MolecularEntityId):
            self.affects_synthesis_of = MolecularEntityId(self.affects_synthesis_of)
        if self.increases_synthesis_of and not isinstance(self.increases_synthesis_of, MolecularEntityId):
            self.increases_synthesis_of = MolecularEntityId(self.increases_synthesis_of)
        if self.decreases_synthesis_of and not isinstance(self.decreases_synthesis_of, MolecularEntityId):
            self.decreases_synthesis_of = MolecularEntityId(self.decreases_synthesis_of)
        if self.affects_degradation_of and not isinstance(self.affects_degradation_of, MolecularEntityId):
            self.affects_degradation_of = MolecularEntityId(self.affects_degradation_of)
        if self.increases_degradation_of and not isinstance(self.increases_degradation_of, MolecularEntityId):
            self.increases_degradation_of = MolecularEntityId(self.increases_degradation_of)
        if self.decreases_degradation_of and not isinstance(self.decreases_degradation_of, MolecularEntityId):
            self.decreases_degradation_of = MolecularEntityId(self.decreases_degradation_of)
        if self.affects_mutation_rate_of and not isinstance(self.affects_mutation_rate_of, GenomicEntityId):
            self.affects_mutation_rate_of = GenomicEntityId(self.affects_mutation_rate_of)
        if self.increases_mutation_rate_of and not isinstance(self.increases_mutation_rate_of, GenomicEntityId):
            self.increases_mutation_rate_of = GenomicEntityId(self.increases_mutation_rate_of)
        if self.decreases_mutation_rate_of and not isinstance(self.decreases_mutation_rate_of, GenomicEntityId):
            self.decreases_mutation_rate_of = GenomicEntityId(self.decreases_mutation_rate_of)
        if self.affects_response_to and not isinstance(self.affects_response_to, MolecularEntityId):
            self.affects_response_to = MolecularEntityId(self.affects_response_to)
        if self.increases_response_to and not isinstance(self.increases_response_to, MolecularEntityId):
            self.increases_response_to = MolecularEntityId(self.increases_response_to)
        if self.decreases_response_to and not isinstance(self.decreases_response_to, MolecularEntityId):
            self.decreases_response_to = MolecularEntityId(self.decreases_response_to)
        if self.affects_splicing_of and not isinstance(self.affects_splicing_of, TranscriptId):
            self.affects_splicing_of = TranscriptId(self.affects_splicing_of)
        if self.increases_splicing_of and not isinstance(self.increases_splicing_of, TranscriptId):
            self.increases_splicing_of = TranscriptId(self.increases_splicing_of)
        if self.decreases_splicing_of and not isinstance(self.decreases_splicing_of, TranscriptId):
            self.decreases_splicing_of = TranscriptId(self.decreases_splicing_of)
        if self.affects_stability_of and not isinstance(self.affects_stability_of, MolecularEntityId):
            self.affects_stability_of = MolecularEntityId(self.affects_stability_of)
        if self.increases_stability_of and not isinstance(self.increases_stability_of, MolecularEntityId):
            self.increases_stability_of = MolecularEntityId(self.increases_stability_of)
        if self.decreases_stability_of and not isinstance(self.decreases_stability_of, MolecularEntityId):
            self.decreases_stability_of = MolecularEntityId(self.decreases_stability_of)
        if self.affects_transport_of and not isinstance(self.affects_transport_of, MolecularEntityId):
            self.affects_transport_of = MolecularEntityId(self.affects_transport_of)
        if self.increases_transport_of and not isinstance(self.increases_transport_of, MolecularEntityId):
            self.increases_transport_of = MolecularEntityId(self.increases_transport_of)
        if self.decreases_transport_of and not isinstance(self.decreases_transport_of, MolecularEntityId):
            self.decreases_transport_of = MolecularEntityId(self.decreases_transport_of)
        if self.affects_secretion_of and not isinstance(self.affects_secretion_of, MolecularEntityId):
            self.affects_secretion_of = MolecularEntityId(self.affects_secretion_of)
        if self.increases_secretion_of and not isinstance(self.increases_secretion_of, MolecularEntityId):
            self.increases_secretion_of = MolecularEntityId(self.increases_secretion_of)
        if self.decreases_secretion_of and not isinstance(self.decreases_secretion_of, MolecularEntityId):
            self.decreases_secretion_of = MolecularEntityId(self.decreases_secretion_of)
        if self.affects_uptake_of and not isinstance(self.affects_uptake_of, MolecularEntityId):
            self.affects_uptake_of = MolecularEntityId(self.affects_uptake_of)
        if self.increases_uptake_of and not isinstance(self.increases_uptake_of, MolecularEntityId):
            self.increases_uptake_of = MolecularEntityId(self.increases_uptake_of)
        if self.decreases_uptake_of and not isinstance(self.decreases_uptake_of, MolecularEntityId):
            self.decreases_uptake_of = MolecularEntityId(self.decreases_uptake_of)
        if self.regulates_entity_to_entity and not isinstance(self.regulates_entity_to_entity, MolecularEntityId):
            self.regulates_entity_to_entity = MolecularEntityId(self.regulates_entity_to_entity)
        if self.biomarker_for and not isinstance(self.biomarker_for, DiseaseOrPhenotypicFeatureId):
            self.biomarker_for = DiseaseOrPhenotypicFeatureId(self.biomarker_for)


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    id: ChemicalSubstanceId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)


@dataclass
class Carbohydrate(ChemicalSubstance):
    id: CarbohydrateId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    id: DrugId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    id: MetaboliteId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    id: AnatomicalEntityId = None
    expresses: Optional[GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        if self.expresses and not isinstance(self.expresses, GeneOrGeneProductId):
            self.expresses = GeneOrGeneProductId(self.expresses)


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    id: LifeStageId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    id: PlanetaryEntityId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    id: EnvironmentalProcessId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    id: EnvironmentalFeatureId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    id: ClinicalEntityId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)


@dataclass
class ClinicalTrial(ClinicalEntity):
    id: ClinicalTrialId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)


@dataclass
class ClinicalIntervention(ClinicalEntity):
    id: ClinicalInterventionId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    id: DeviceId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    id: GenomicEntityId = None
    has_biological_sequence: Optional[BiologicalSequence] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    id: GenomeId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    id: TranscriptId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    id: ExonId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)


@dataclass
class CodingSequence(GenomicEntity):
    id: CodingSequenceId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    id: MacromolecularMachineId = None
    name: Optional[SymbolType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    id: GeneOrGeneProductId = None
    in_pathway_with: Optional[GeneOrGeneProductId] = None
    in_complex_with: Optional[GeneOrGeneProductId] = None
    in_cell_population_with: Optional[GeneOrGeneProductId] = None
    expressed_in: Optional[AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        if self.in_pathway_with and not isinstance(self.in_pathway_with, GeneOrGeneProductId):
            self.in_pathway_with = GeneOrGeneProductId(self.in_pathway_with)
        if self.in_complex_with and not isinstance(self.in_complex_with, GeneOrGeneProductId):
            self.in_complex_with = GeneOrGeneProductId(self.in_complex_with)
        if self.in_cell_population_with and not isinstance(self.in_cell_population_with, GeneOrGeneProductId):
            self.in_cell_population_with = GeneOrGeneProductId(self.in_cell_population_with)
        if self.expressed_in and not isinstance(self.expressed_in, AnatomicalEntityId):
            self.expressed_in = AnatomicalEntityId(self.expressed_in)


@dataclass
class Gene(GeneOrGeneProduct):
    id: GeneId = None
    genetically_interacts_with: Optional[GeneId] = None
    has_gene_product: Optional[GeneProductId] = None
    gene_associated_with_condition: Optional[DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        if self.genetically_interacts_with and not isinstance(self.genetically_interacts_with, GeneId):
            self.genetically_interacts_with = GeneId(self.genetically_interacts_with)
        if self.has_gene_product and not isinstance(self.has_gene_product, GeneProductId):
            self.has_gene_product = GeneProductId(self.has_gene_product)
        if self.gene_associated_with_condition and not isinstance(self.gene_associated_with_condition, DiseaseOrPhenotypicFeatureId):
            self.gene_associated_with_condition = DiseaseOrPhenotypicFeatureId(self.gene_associated_with_condition)


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    id: GeneProductId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    id: ProteinId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    id: GeneProductIsoformId = None


@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    id: ProteinIsoformId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)


@dataclass
class RNAProduct(GeneProduct):
    id: RNAProductId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    id: RNAProductIsoformId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)


@dataclass
class NoncodingRNAProduct(RNAProduct):
    id: NoncodingRNAProductId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)


@dataclass
class MicroRNA(NoncodingRNAProduct):
    id: MicroRNAId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    id: MacromolecularComplexId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    id: GeneFamilyId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)


@dataclass
class Zygosity(Attribute):
    pass


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    id: GenotypeId = None
    has_zygosity: Optional[Zygosity] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity and not isinstance(self.has_zygosity, Zygosity):
            self.has_zygosity = Zygosity()


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    id: HaplotypeId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    has_gene: List[GeneId] = empty_list()
    has_biological_sequence: Optional[BiologicalSequence] = None
    id: Optional[IdentifierType] = None

    def _fix_elements(self):
        super()._fix_elements()
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]
        if self.has_biological_sequence and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        if self.id and not isinstance(self.id, IdentifierType):
            self.id = IdentifierType(self.id)


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    id: DrugExposureId = None
    drug: List[ChemicalSubstanceId] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)
        if self.Drug is None:
            raise ValueError(f"Drug must be supplied")
        if not isinstance(self.Drug, ChemicalSubstanceId):
            self.Drug = ChemicalSubstanceId(self.Drug)


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    id: TreatmentId = None
    treats: DiseaseOrPhenotypicFeatureId = None
    has_exposure_parts: List[DrugExposureId] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        if self.treats is None:
            raise ValueError(f"treats must be supplied")
        if not isinstance(self.treats, DiseaseOrPhenotypicFeatureId):
            self.treats = DiseaseOrPhenotypicFeatureId(self.treats)
        if self.has_exposure_parts is None:
            raise ValueError(f"has_exposure_parts must be supplied")
        if not isinstance(self.has_exposure_parts, DrugExposureId):
            self.has_exposure_parts = DrugExposureId(self.has_exposure_parts)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    id: GeographicLocationId = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    id: GeographicLocationAtTimeId = None
    timepoint: Optional[TimeType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """
    id: AssociationAssociation_id
    subject: IriType
    relation: IriType
    object: IriType
    negated: bool = False
    association_type: Optional[OntologyClassId] = None
    qualifiers: List[OntologyClassId] = empty_list()
    publications: List[PublicationId] = empty_list()
    provided_by: Optional[Provider] = None
    association_slot: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.association_type and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by and not isinstance(self.provided_by, Provider):
            self.provided_by = Provider()


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    id: GenotypeToGenotypePartAssociationAssociation_id
    relation: IriType
    subject: GenotypeId
    object: GenotypeId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGenotypePartAssociationAssociation_id):
            self.id = GenotypeToGenotypePartAssociationAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    id: GenotypeToGeneAssociationAssociation_id
    relation: IriType
    subject: GenotypeId
    object: GeneId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGeneAssociationAssociation_id):
            self.id = GenotypeToGeneAssociationAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    id: GenotypeToVariantAssociationAssociation_id
    relation: IriType
    subject: GenotypeId
    object: SequenceVariant

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToVariantAssociationAssociation_id):
            self.id = GenotypeToVariantAssociationAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, SequenceVariant):
            self.object = SequenceVariant(self.object)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    id: GeneToGeneAssociationAssociation_id
    subject: GeneOrGeneProductId
    object: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    id: GeneToGeneHomologyAssociationAssociation_id
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneHomologyAssociationAssociation_id):
            self.id = GeneToGeneHomologyAssociationAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    id: PairwiseGeneToGeneInteractionAssociation_id
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PairwiseGeneToGeneInteractionAssociation_id):
            self.id = PairwiseGeneToGeneInteractionAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    id: CellLineToThingAssociationAssociation_id
    subject: CellLineId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    id: CellLineToDiseaseOrPhenotypicFeatureAssociationAssociation_id
    subject: DiseaseOrPhenotypicFeatureId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationAssociation_id):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    id: ChemicalToThingAssociationAssociation_id
    subject: ChemicalSubstanceId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    id: CaseToThingAssociationAssociation_id
    subject: CaseId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    id: ChemicalToDiseaseOrPhenotypicFeatureAssociationAssociation_id
    object: DiseaseOrPhenotypicFeatureId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationAssociation_id):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    id: ChemicalToPathwayAssociationAssociation_id
    object: PathwayId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToPathwayAssociationAssociation_id):
            self.id = ChemicalToPathwayAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    id: ChemicalToGeneAssociationAssociation_id
    object: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToGeneAssociationAssociation_id):
            self.id = ChemicalToGeneAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    id: BiosampleToThingAssociationAssociation_id
    subject: BiosampleId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, BiosampleId):
            self.subject = BiosampleId(self.subject)


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    definitional: true
    """
    id: BiosampleToDiseaseOrPhenotypicFeatureAssociationAssociation_id

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiosampleToDiseaseOrPhenotypicFeatureAssociationAssociation_id):
            self.id = BiosampleToDiseaseOrPhenotypicFeatureAssociationAssociation_id(self.id)


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    id: EntityToPhenotypicFeatureAssociationAssociation_id
    sex_qualifier: Optional[BiologicalSex] = None
    description: Optional[NarrativeText] = None
    object: PhenotypicFeatureId

    def _fix_elements(self):
        super()._fix_elements()
        if self.sex_qualifier and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex()
        if self.description and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    id: DiseaseOrPhenotypicFeatureAssociationToThingAssociationAssociation_id
    subject: DiseaseOrPhenotypicFeatureId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    id: DiseaseOrPhenotypicFeatureAssociationToLocationAssociationAssociation_id
    object: AnatomicalEntityId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationAssociation_id):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    id: ThingToDiseaseOrPhenotypicFeatureAssociationAssociation_id
    object: DiseaseOrPhenotypicFeatureId

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class DiseaseToThingAssociation(Association):
    id: DiseaseToThingAssociationAssociation_id
    subject: DiseaseId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    id: GenotypeToPhenotypicFeatureAssociationAssociation_id
    relation: IriType
    subject: GenotypeId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationAssociation_id):
            self.id = GenotypeToPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    id: EnvironmentToPhenotypicFeatureAssociationAssociation_id
    subject: EnvironmentId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentToPhenotypicFeatureAssociationAssociation_id):
            self.id = EnvironmentToPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, EnvironmentId):
            self.subject = EnvironmentId(self.subject)


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    id: DiseaseToPhenotypicFeatureAssociationAssociation_id

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationAssociation_id):
            self.id = DiseaseToPhenotypicFeatureAssociationAssociation_id(self.id)


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    id: CaseToPhenotypicFeatureAssociationAssociation_id

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseToPhenotypicFeatureAssociationAssociation_id):
            self.id = CaseToPhenotypicFeatureAssociationAssociation_id(self.id)


@dataclass
class GeneToThingAssociation(Association):
    id: GeneToThingAssociationAssociation_id
    subject: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    id: GeneToPhenotypicFeatureAssociationAssociation_id
    subject: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToPhenotypicFeatureAssociationAssociation_id):
            self.id = GeneToPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneToDiseaseAssociation(Association):
    id: GeneToDiseaseAssociationAssociation_id
    subject: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToDiseaseAssociationAssociation_id):
            self.id = GeneToDiseaseAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    id: VariantToPopulationAssociationAssociation_id
    subject: SequenceVariant
    object: PopulationOfIndividualOrganismsId
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPopulationAssociationAssociation_id):
            self.id = VariantToPopulationAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariant):
            self.subject = SequenceVariant(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    id: PopulationToPopulationAssociationAssociation_id
    subject: PopulationOfIndividualOrganismsId
    object: PopulationOfIndividualOrganismsId
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationAssociation_id):
            self.id = PopulationToPopulationAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    id: VariantToPhenotypicFeatureAssociationAssociation_id
    subject: SequenceVariant

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPhenotypicFeatureAssociationAssociation_id):
            self.id = VariantToPhenotypicFeatureAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariant):
            self.subject = SequenceVariant(self.subject)


@dataclass
class VariantToDiseaseAssociation(Association):
    id: VariantToDiseaseAssociationAssociation_id
    subject: IriType
    relation: IriType
    object: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToDiseaseAssociationAssociation_id):
            self.id = VariantToDiseaseAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, IriType):
            self.object = IriType(self.object)


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    id: GeneAsAModelOfDiseaseAssociationAssociation_id
    subject: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneAsAModelOfDiseaseAssociationAssociation_id):
            self.id = GeneAsAModelOfDiseaseAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    id: GeneHasVariantThatContributesToDiseaseAssociationAssociation_id
    sequence_variant_qualifier: Optional[SequenceVariant] = None
    subject: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationAssociation_id):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationAssociation_id(self.id)
        if self.sequence_variant_qualifier and not isinstance(self.sequence_variant_qualifier, SequenceVariant):
            self.sequence_variant_qualifier = SequenceVariant(self.sequence_variant_qualifier)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GenotypeToThingAssociation(Association):
    id: GenotypeToThingAssociationAssociation_id
    subject: GenotypeId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    id: GeneToExpressionSiteAssociationAssociation_id
    stage_qualifier: Optional[LifeStageId] = None
    quantifier_qualifier: Optional[OntologyClassId] = None
    subject: GeneOrGeneProductId
    object: AnatomicalEntityId
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToExpressionSiteAssociationAssociation_id):
            self.id = GeneToExpressionSiteAssociationAssociation_id(self.id)
        if self.stage_qualifier and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    id: SequenceVariantModulatesTreatmentAssociationAssociation_id
    subject: SequenceVariant
    object: TreatmentId

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariant):
            self.subject = SequenceVariant(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    id: FunctionalAssociationAssociation_id
    subject: MacromolecularMachineId
    object: GeneOntologyClassId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, FunctionalAssociationAssociation_id):
            self.id = FunctionalAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    id: MacromolecularMachineToMolecularActivityAssociationAssociation_id
    object: MolecularActivityId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationAssociation_id):
            self.id = MacromolecularMachineToMolecularActivityAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    id: MacromolecularMachineToBiologicalProcessAssociationAssociation_id
    object: BiologicalProcessId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationAssociation_id):
            self.id = MacromolecularMachineToBiologicalProcessAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    id: MacromolecularMachineToCellularComponentAssociationAssociation_id
    object: CellularComponentId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationAssociation_id):
            self.id = MacromolecularMachineToCellularComponentAssociationAssociation_id(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    id: GeneToGoTermAssociationAssociation_id
    subject: MolecularEntityId
    object: GeneOntologyClassId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGoTermAssociationAssociation_id):
            self.id = GeneToGoTermAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    id: GenomicSequenceLocalizationAssociation_id
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None
    subject: GenomicEntityId
    object: GenomicEntityId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicSequenceLocalizationAssociation_id):
            self.id = GenomicSequenceLocalizationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    id: SequenceFeatureRelationshipAssociation_id
    subject: GenomicEntityId
    object: GenomicEntityId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipAssociation_id):
            self.id = SequenceFeatureRelationshipAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    id: TranscriptToGeneRelationshipAssociation_id
    subject: TranscriptId
    object: GeneId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptToGeneRelationshipAssociation_id):
            self.id = TranscriptToGeneRelationshipAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    id: GeneToGeneProductRelationshipAssociation_id
    subject: GeneId
    object: GeneProductId
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneProductRelationshipAssociation_id):
            self.id = GeneToGeneProductRelationshipAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    id: ExonToTranscriptRelationshipAssociation_id
    subject: ExonId
    object: TranscriptId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonToTranscriptRelationshipAssociation_id):
            self.id = ExonToTranscriptRelationshipAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    id: GeneRegulatoryRelationshipAssociation_id
    relation: IriType
    subject: GeneOrGeneProductId
    object: GeneOrGeneProductId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneRegulatoryRelationshipAssociation_id):
            self.id = GeneRegulatoryRelationshipAssociation_id(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    id: AnatomicalEntityToAnatomicalEntityAssociationAssociation_id
    subject: AnatomicalEntityId
    object: AnatomicalEntityId

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationAssociation_id):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    id: AnatomicalEntityToAnatomicalEntityPartOfAssociationAssociation_id
    subject: AnatomicalEntityId
    object: AnatomicalEntityId
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationAssociation_id):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    id: AnatomicalEntityToAnatomicalEntityOntogenicAssociationAssociation_id
    subject: AnatomicalEntityId
    object: AnatomicalEntityId
    relation: IriType

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationAssociation_id):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationAssociation_id(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    id: OccurrentId = None
    regulates_process_to_process: Optional[OccurrentId] = None
    has_participant: Optional[NamedThingId] = None
    has_input: Optional[NamedThingId] = None
    precedes: Optional[OccurrentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        if self.regulates_process_to_process and not isinstance(self.regulates_process_to_process, OccurrentId):
            self.regulates_process_to_process = OccurrentId(self.regulates_process_to_process)
        if self.has_participant and not isinstance(self.has_participant, NamedThingId):
            self.has_participant = NamedThingId(self.has_participant)
        if self.has_input and not isinstance(self.has_input, NamedThingId):
            self.has_input = NamedThingId(self.has_input)
        if self.precedes and not isinstance(self.precedes, OccurrentId):
            self.precedes = OccurrentId(self.precedes)


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    id: BiologicalProcessOrActivityId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    id: MolecularActivityId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    id: ActivityAndBehaviorId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    id: ProcedureId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    id: PhenomenonId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    id: BiologicalProcessId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)


@dataclass
class Pathway(BiologicalProcess):
    id: PathwayId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    id: PhysiologicalProcessId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    id: CellularComponentId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)


@dataclass
class Cell(AnatomicalEntity):
    id: CellId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)


@dataclass
class CellLine(Biosample):
    id: CellLineId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    id: GrossAnatomicalStructureId = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)
