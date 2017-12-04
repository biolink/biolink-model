

## CLASSES

class NamedThing(object):
    """
    a databased entity or concept/class
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ThingWithTaxon(object):
    """
    A mixin that can be used on any entity with a taxon
    """
    def __init__(self,
                 in_taxon=None):
        self.in_taxon=in_taxon

    def __str__(self):
        return "in_taxon={} ".format(self.in_taxon)
    def __repr__(self):
        return self.__str__()


class OrganismType(OntologyClass):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class IndividualOrganism(NamedThing):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PopulationOfIndividualOrganisms(NamedThing):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ConditionOrPhenotypicCondition(OntologyClass):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Disease(ConditionOrPhenotypicCondition):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PhenotypicFeature(ConditionOrPhenotypicCondition):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EnvironmentalFeature(NamedThing):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EvidenceType(InformationContentEntity):
    """
    Evidence that supports an association
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class MolecularEntity(NamedThing):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneOrGeneProduct(MolecularEntity):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Gene(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneProduct(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Protein(GeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class RnaProduct(GeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class MacromolecularComplex(MolecularEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Association(object):
    """
    Any kind of association between two entities
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GeneOrProteinInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class EntityToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 frequency=None,
                 severity=None,
                 onset=None,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.frequency=frequency
        self.severity=severity
        self.onset=onset
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "frequency={} severity={} onset={} id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.frequency,self.severity,self.onset,self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class DiseaseToEntityAssociation(Association):
    """
    None
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GeneToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class GoAssociation(Association):
    """
    None
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class DenormalizedAssociation(Association):
    """
    An association that includes flattened inlined objects, such as subject_taxon_closure
    """
    def __init__(self,
                 subject_taxon=None,
                 subject_taxon_label=None,
                 subject_taxon_closure=None,
                 subject_taxon_closure_label=None,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.subject_taxon=subject_taxon
        self.subject_taxon_label=subject_taxon_label
        self.subject_taxon_closure=subject_taxon_closure
        self.subject_taxon_closure_label=subject_taxon_closure_label
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "subject_taxon={} subject_taxon_label={} subject_taxon_closure={} subject_taxon_closure_label={} id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.subject_taxon,self.subject_taxon_label,self.subject_taxon_closure,self.subject_taxon_closure_label,self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class DiseaseToPhenotypicFeatureDenormalizedAssociation(DiseaseToPhenotypicFeatureAssociation):
    """
    None
    """
    def __init__(self,
                 id=None,
                 type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extension=None,
                 object_extension=None,
                 publications=None,
                 provided_by=None,
                 evidence_graph=None,
                 evidence_type=None,
                 evidence=None):
        self.id=id
        self.type=type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extension=subject_extension
        self.object_extension=object_extension
        self.publications=publications
        self.provided_by=provided_by
        self.evidence_graph=evidence_graph
        self.evidence_type=evidence_type
        self.evidence=evidence

    def __str__(self):
        return "id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class AssociationSet(object):
    """
    None
    """
    def __init__(self,
                 associations=None):
        self.associations=associations

    def __str__(self):
        return "associations={} ".format(self.associations)
    def __repr__(self):
        return self.__str__()


class MolecularEvent(object):
    """
    None
    """
    def __init__(self,
                 enabled_by=None,
                 part_of=None,
                 occurs_in=None,
                 upstream_causal_relationship=None,
                 downstream_causal_relationship=None):
        self.enabled_by=enabled_by
        self.part_of=part_of
        self.occurs_in=occurs_in
        self.upstream_causal_relationship=upstream_causal_relationship
        self.downstream_causal_relationship=downstream_causal_relationship

    def __str__(self):
        return "enabled_by={} part_of={} occurs_in={} upstream_causal_relationship={} downstream_causal_relationship={} ".format(self.enabled_by,self.part_of,self.occurs_in,self.upstream_causal_relationship,self.downstream_causal_relationship)
    def __repr__(self):
        return self.__str__()


