

## CLASSES

class RelationshipType(object):
    """
    An OWL property used as an edge label
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Attribute(object):
    """
    A property or characteristic of an entity
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class BiologicalSex(Attribute):
    """
    None
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


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


class BiologicalEntity(NamedThing):
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


class OntologyClass(object):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
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


class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
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


class OrganismTaxon(OrganismalEntity):
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


class IndividualOrganism(OrganismalEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Biosample(OrganismalEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Disease(DiseaseOrPhenotypicFeature):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Environment(BiologicalEntity):
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


class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
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
    Class of evidence that supports an association
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


class AdministrativeEntity(object):
    """
    None
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
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


class EnvironmentalProcess(PlanetaryEntity):
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


class EnvironmentalFeature(PlanetaryEntity):
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


class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
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


class ClinicalTrial(ClinicalEntity):
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


class ClinicalIntervention(ClinicalEntity):
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


class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
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
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class CodingSequence(GenomicEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class GeneOrGeneProduct(GenomicEntity):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Gene(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class RnaProduct(GeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class RnaProductIsoform(RnaProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class NoncodingRnaProduct(RnaProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Microrna(NoncodingRnaProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class MacromolecularComplex(MolecularEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class GeneGrouping(object):
    """
    any grouping of multiple genes or gene products
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Zygosity(Attribute):
    """
    None
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
    """
    def __init__(self,
                 has_zygosity=None,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.has_zygosity=has_zygosity
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "has_zygosity={} id={} label={} in_taxon={} ".format(self.has_zygosity,self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Allele(Genotype):
    """
    A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus
    """
    def __init__(self,
                 has_gene=None,
                 has_zygosity=None,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.has_gene=has_gene
        self.has_zygosity=has_zygosity
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "has_gene={} has_zygosity={} id={} label={} in_taxon={} ".format(self.has_gene,self.has_zygosity,self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class SequenceVariant(GenomicEntity):
    """
    A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    def __init__(self,
                 drug=None,
                 id=None,
                 label=None):
        self.drug=drug
        self.id=id
        self.label=label

    def __str__(self):
        return "drug={} id={} label={} ".format(self.drug,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    def __init__(self,
                 treats=None,
                 has_exposure_parts=None,
                 id=None,
                 label=None):
        self.treats=treats
        self.has_exposure_parts=has_exposure_parts
        self.id=id
        self.label=label

    def __str__(self):
        return "treats={} has_exposure_parts={} id={} label={} ".format(self.treats,self.has_exposure_parts,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    def __init__(self,
                 latitude=None,
                 longitude=None,
                 id=None,
                 label=None):
        self.latitude=latitude
        self.longitude=longitude
        self.id=id
        self.label=label

    def __str__(self):
        return "latitude={} longitude={} id={} label={} ".format(self.latitude,self.longitude,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeographicLocationAtTime(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    def __init__(self,
                 latitude=None,
                 longitude=None,
                 timepoint=None,
                 id=None,
                 label=None):
        self.latitude=latitude
        self.longitude=longitude
        self.timepoint=timepoint
        self.id=id
        self.label=label

    def __str__(self):
        return "latitude={} longitude={} timepoint={} id={} label={} ".format(self.latitude,self.longitude,self.timepoint,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Association(InformationContentEntity):
    """
    A typed association between two entities, supported by evidence
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class MolecularInteraction(Association):
    """
    An interaction at the molecular level between two physical entities
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PairwiseGeneOrProteinInteractionAssociation(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
  definitional: true
  
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EntityToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EntityToDiseaseAssociation(object):
    """
    None
    """
    def __init__(self,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None):
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier

    def __str__(self):
        return "frequency_qualifier={} severity_qualifier={} onset_qualifier={} ".format(self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier)
    def __repr__(self):
        return self.__str__()


class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class DiseaseToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier)
    def __repr__(self):
        return self.__str__()


class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier)
    def __repr__(self):
        return self.__str__()


class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier)
    def __repr__(self):
        return self.__str__()


class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier)
    def __repr__(self):
        return self.__str__()


class GeneToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 sex_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.sex_qualifier=sex_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} sex_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.sex_qualifier)
    def __repr__(self):
        return self.__str__()


class GeneToDiseaseAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier)
    def __repr__(self):
        return self.__str__()


class ModelToDiseaseMixin(object):
    """
    This mixin is used for any association class for which the subject plays the role of a 'model'
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier)
    def __repr__(self):
        return self.__str__()


class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} frequency_qualifier={} severity_qualifier={} onset_qualifier={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label,self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier)
    def __repr__(self):
        return self.__str__()


class GenotypeToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    def __init__(self,
                 stage_qualifier=None,
                 quantifier_qualifier=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.stage_qualifier=stage_qualifier
        self.quantifier_qualifier=quantifier_qualifier
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "stage_qualifier={} quantifier_qualifier={} association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.stage_qualifier,self.quantifier_qualifier,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGoTermAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class AssociationResultSet(InformationContentEntity):
    """
    None
    """
    def __init__(self,
                 associations=None,
                 id=None,
                 label=None):
        self.associations=associations
        self.id=id
        self.label=label

    def __str__(self):
        return "associations={} id={} label={} ".format(self.associations,self.id,self.label)
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
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.start_interbase_coordinate=start_interbase_coordinate
        self.end_interbase_coordinate=end_interbase_coordinate
        self.genome_build=genome_build
        self.phase=phase
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "start_interbase_coordinate={} end_interbase_coordinate={} genome_build={} phase={} association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.start_interbase_coordinate,self.end_interbase_coordinate,self.genome_build,self.phase,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceFeatureToSequenceRelationship(Association):
    """
    Relates a sequence feature such as a gene to its sequence
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class AnatomicalEntityPartOfAnatomicalEntityAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 publications=None,
                 provided_by=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.publications=publications
        self.provided_by=provided_by
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} publications={} provided_by={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.publications,self.provided_by,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Occurrent(object):
    """
    A processual entity
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class MolecularActivity(BiologicalEntity):
    """
    An execution of a molecular function
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


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class BiologicalProcess(BiologicalEntity):
    """
    One or more causally connected executions of molecular functions
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


class Pathway(BiologicalProcess):
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


class Physiology(BiologicalProcess):
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


class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class Cell(AnatomicalEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


class GrossAnatomicalStructure(AnatomicalEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None,
                 in_taxon=None):
        self.id=id
        self.label=label
        self.in_taxon=in_taxon

    def __str__(self):
        return "id={} label={} in_taxon={} ".format(self.id,self.label,self.in_taxon)
    def __repr__(self):
        return self.__str__()


