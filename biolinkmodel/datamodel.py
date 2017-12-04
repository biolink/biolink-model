

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


class Cohort(PopulationOfIndividualOrganisms):
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


class ConditionOrPhenotypicFeature(OntologyClass):
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


class Disease(ConditionOrPhenotypicFeature):
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


class PhenotypicFeature(ConditionOrPhenotypicFeature):
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


class ChemicalSubstance(MolecularEntity):
    """
    may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
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


class AnatomicalEntity(NamedThing):
    """
    A subcellular location, cell type or gross anatomical part
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


class DevelopmentalStage(NamedThing):
    """
    A stage of development or growth of an organism, including post-natal adult stages
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


class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
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


class GeneOrGeneProduct(GenomicEntity):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None,
                 id=None,
                 label=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym
        self.id=id
        self.label=label

    def __str__(self):
        return "full_name={} systematic_synonym={} id={} label={} ".format(self.full_name,self.systematic_synonym,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Gene(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None,
                 id=None,
                 label=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym
        self.id=id
        self.label=label

    def __str__(self):
        return "full_name={} systematic_synonym={} id={} label={} ".format(self.full_name,self.systematic_synonym,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneProduct(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None,
                 id=None,
                 label=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym
        self.id=id
        self.label=label

    def __str__(self):
        return "full_name={} systematic_synonym={} id={} label={} ".format(self.full_name,self.systematic_synonym,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Protein(GeneProduct):
    """
    None
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None,
                 id=None,
                 label=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym
        self.id=id
        self.label=label

    def __str__(self):
        return "full_name={} systematic_synonym={} id={} label={} ".format(self.full_name,self.systematic_synonym,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class RnaProduct(GeneProduct):
    """
    None
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None,
                 id=None,
                 label=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym
        self.id=id
        self.label=label

    def __str__(self):
        return "full_name={} systematic_synonym={} id={} label={} ".format(self.full_name,self.systematic_synonym,self.id,self.label)
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


class GeneFamily(MolecularEntity):
    """
    a grouping of multiple genes or gene products related by common descent
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


class Genotype(GenomicEntity):
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


class SequenceVariant(GenomicEntity):
    """
    A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
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


class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
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


class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
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


class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
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
    An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?
    """
    def __init__(self,
                 stage=None,
                 quantifier=None,
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
        self.stage=stage
        self.quantifier=quantifier
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
        return "stage={} quantifier={} id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.stage,self.quantifier,self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
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


class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
    """
    def __init__(self,
                 start_interbase_coordinate=None,
                 end_interbase_coordinate=None,
                 genome_build=None,
                 phase=None,
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
        self.start_interbase_coordinate=start_interbase_coordinate
        self.end_interbase_coordinate=end_interbase_coordinate
        self.genome_build=genome_build
        self.phase=phase
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
        return "start_interbase_coordinate={} end_interbase_coordinate={} genome_build={} phase={} id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.start_interbase_coordinate,self.end_interbase_coordinate,self.genome_build,self.phase,self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
    def __repr__(self):
        return self.__str__()


class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    def __init__(self,
                 rank=None,
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
        self.rank=rank
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
        return "rank={} id={} type={} subject={} negated={} relation={} object={} qualifiers={} subject_extension={} object_extension={} publications={} provided_by={} evidence_graph={} evidence_type={} evidence={} ".format(self.rank,self.id,self.type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extension,self.object_extension,self.publications,self.provided_by,self.evidence_graph,self.evidence_type,self.evidence)
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


class BioentityWithGoTerms(MolecularEntity):
    """
    None
    """
    def __init__(self,
                 in_family=None,
                 isa_partof_closure=None,
                 regulates_closure=None,
                 id=None,
                 label=None):
        self.in_family=in_family
        self.isa_partof_closure=isa_partof_closure
        self.regulates_closure=regulates_closure
        self.id=id
        self.label=label

    def __str__(self):
        return "in_family={} isa_partof_closure={} regulates_closure={} id={} label={} ".format(self.in_family,self.isa_partof_closure,self.regulates_closure,self.id,self.label)
    def __repr__(self):
        return self.__str__()


