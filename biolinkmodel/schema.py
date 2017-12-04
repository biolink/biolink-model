## SCHEMA

from marshmallow import Schema, fields, pprint, post_load

class NamedThingSchema(Schema):
    id = fields.Str()
    label = fields.Str()

    @post_load
    def make_object(self, data):
        NamedThing(**data)

class OntologyClassSchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        OntologyClass(**data)

class ThingWithTaxonSchema(Schema):
    in_taxon = fields.Str()

    @post_load
    def make_object(self, data):
        ThingWithTaxon(**data)

class OrganismTypeSchema(OntologyClassSchema):

    @post_load
    def make_object(self, data):
        OrganismType(**data)

class IndividualOrganismSchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        IndividualOrganism(**data)

class PopulationOfIndividualOrganismsSchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        PopulationOfIndividualOrganisms(**data)

class ConditionOrPhenotypicConditionSchema(OntologyClassSchema):

    @post_load
    def make_object(self, data):
        ConditionOrPhenotypicCondition(**data)

class DiseaseSchema(ConditionOrPhenotypicConditionSchema):

    @post_load
    def make_object(self, data):
        Disease(**data)

class PhenotypicFeatureSchema(ConditionOrPhenotypicConditionSchema):

    @post_load
    def make_object(self, data):
        PhenotypicFeature(**data)

class EnvironmentalFeatureSchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        EnvironmentalFeature(**data)

class InformationContentEntitySchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        InformationContentEntity(**data)

class EvidenceTypeSchema(InformationContentEntitySchema):

    @post_load
    def make_object(self, data):
        EvidenceType(**data)

class PublicationSchema(InformationContentEntitySchema):

    @post_load
    def make_object(self, data):
        Publication(**data)

class MolecularEntitySchema(NamedThingSchema):

    @post_load
    def make_object(self, data):
        MolecularEntity(**data)

class GeneOrGeneProductSchema(MolecularEntitySchema):

    @post_load
    def make_object(self, data):
        GeneOrGeneProduct(**data)

class GeneSchema(GeneOrGeneProductSchema):

    @post_load
    def make_object(self, data):
        Gene(**data)

class GeneProductSchema(GeneOrGeneProductSchema):

    @post_load
    def make_object(self, data):
        GeneProduct(**data)

class ProteinSchema(GeneProductSchema):

    @post_load
    def make_object(self, data):
        Protein(**data)

class RnaProductSchema(GeneProductSchema):

    @post_load
    def make_object(self, data):
        RnaProduct(**data)

class MacromolecularComplexSchema(MolecularEntitySchema):

    @post_load
    def make_object(self, data):
        MacromolecularComplex(**data)

class AssociationSchema(Schema):
    id = fields.Str()
    type = fields.Str()
    subject = fields.Str()
    negated = fields.Str()
    relation = fields.Str()
    object = fields.Str()
    qualifiers = fields.Str()
    subject_extension = fields.Str()
    object_extension = fields.Str()
    publications = fields.Str()
    provided_by = fields.Str()
    evidence_graph = fields.Str()
    evidence_type = fields.Str()
    evidence = fields.Str()

    @post_load
    def make_object(self, data):
        Association(**data)

class GeneToGeneAssociationSchema(AssociationSchema):

    @post_load
    def make_object(self, data):
        GeneToGeneAssociation(**data)

class GeneToGeneHomologyAssociationSchema(GeneToGeneAssociationSchema):

    @post_load
    def make_object(self, data):
        GeneToGeneHomologyAssociation(**data)

class GeneOrProteinInteractionSchema(GeneToGeneAssociationSchema):

    @post_load
    def make_object(self, data):
        GeneOrProteinInteraction(**data)

class EntityToPhenotypicFeatureAssociationSchema(AssociationSchema):
    frequency = fields.Str()
    severity = fields.Str()
    onset = fields.Str()

    @post_load
    def make_object(self, data):
        EntityToPhenotypicFeatureAssociation(**data)

class DiseaseToEntityAssociationSchema(AssociationSchema):

    @post_load
    def make_object(self, data):
        DiseaseToEntityAssociation(**data)

class DiseaseToPhenotypicFeatureAssociationSchema(AssociationSchema):

    @post_load
    def make_object(self, data):
        DiseaseToPhenotypicFeatureAssociation(**data)

class GeneToPhenotypicFeatureAssociationSchema(AssociationSchema):

    @post_load
    def make_object(self, data):
        GeneToPhenotypicFeatureAssociation(**data)

class GoAssociationSchema(AssociationSchema):

    @post_load
    def make_object(self, data):
        GoAssociation(**data)

class DenormalizedAssociationSchema(AssociationSchema):
    subject_taxon = fields.Str()
    subject_taxon_label = fields.Str()
    subject_taxon_closure = fields.Str()
    subject_taxon_closure_label = fields.Str()

    @post_load
    def make_object(self, data):
        DenormalizedAssociation(**data)

class DiseaseToPhenotypicFeatureDenormalizedAssociationSchema(DiseaseToPhenotypicFeatureAssociationSchema):

    @post_load
    def make_object(self, data):
        DiseaseToPhenotypicFeatureDenormalizedAssociation(**data)

class AssociationSetSchema(Schema):
    associations = fields.Str()

    @post_load
    def make_object(self, data):
        AssociationSet(**data)

class MolecularEventSchema(Schema):
    enabled_by = fields.Str()
    part_of = fields.Str()
    occurs_in = fields.Str()
    upstream_causal_relationship = fields.Str()
    downstream_causal_relationship = fields.Str()

    @post_load
    def make_object(self, data):
        MolecularEvent(**data)

