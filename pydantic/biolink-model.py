from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

metamodel_version = "None"
version = "2.3.1"

# Pydantic config and validators
class PydanticConfig:
    """ Pydantic config https://pydantic-docs.helpmanual.io/usage/model_config/ """

    validate_assignment = True
    validate_all = True
    underscore_attrs_are_private = True
    extra = 'forbid'
    arbitrary_types_allowed = True  # TODO re-evaluate this


class LogicalInterpretationEnum(str, Enum):
    
    SomeSome = "SomeSome"
    AllSome = "AllSome"
    InverseAllSome = "InverseAllSome"
    
    

class ReactionDirectionEnum(str, Enum):
    
    left_to_right = "left_to_right"
    right_to_left = "right_to_left"
    bidirectional = "bidirectional"
    neutral = "neutral"
    
    

class ReactionSideEnum(str, Enum):
    
    left = "left"
    right = "right"
    
    

class PhaseEnum(str, Enum):
    
    number_0 = "0"
    number_1 = "1"
    number_2 = "2"
    
    

class StrandEnum(str, Enum):
    
    PLUS_SIGN = "+"
    _ = "-"
    FULL_STOP = "."
    QUESTION_MARK = "?"
    
    

class SequenceEnum(str, Enum):
    
    NA = "NA"
    AA = "AA"
    
    

class PredicateQualifierEnum(str, Enum):
    
    predicted = "predicted"
    possibly = "possibly"
    hypothesized = "hypothesized"
    validated = "validated"
    supported_by_real_world_evidence = "supported by real-world evidence"
    supported_by_clinical_evidence = "supported by clinical evidence"
    
    

class DruggableGeneCategoryEnum(str, Enum):
    
    Tclin = "Tclin"
    Tbio = "Tbio"
    Tchem = "Tchem"
    Tdark = "Tdark"
    
    

class DrugAvailabilityEnum(str, Enum):
    
    over_the_counter = "over the counter"
    prescription = "prescription"
    
    

class DrugDeliveryEnum(str, Enum):
    
    inhalation = "inhalation"
    oral = "oral"
    absorbtion_through_the_skin = "absorbtion through the skin"
    intravenous_injection = "intravenous injection"
    
    

class FDAApprovalStatusEnum(str, Enum):
    
    Discovery_AMPERSAND_Development_Phase = "Discovery & Development Phase"
    Preclinical_Research_Phase = "Preclinical Research Phase"
    FDA_Clinical_Research_Phase = "FDA Clinical Research Phase"
    FDA_Review_Phase_4 = "FDA Review Phase 4"
    FDA_Post_Market_Safety_Monitoring = "FDA Post-Market Safety Monitoring"
    FDA_Clinical_Research_Phase_1 = "FDA Clinical Research Phase 1"
    FDA_Clinical_Research_Phase_2 = "FDA Clinical Research Phase 2"
    FDA_Clinical_Research_Phase_3 = "FDA Clinical Research Phase 3"
    FDA_Clinical_Research_Phase_4 = "FDA Clinical Research Phase 4"
    FDA_Fast_Track = "FDA Fast Track"
    FDA_Breakthrough_Therapy = "FDA Breakthrough Therapy"
    FDA_Accelerated_Approval = "FDA Accelerated Approval"
    FDA_Priority_Review = "FDA Priority Review"
    Regular_FDA_Approval = "Regular FDA Approval"
    Post_Approval_Withdrawal = "Post-Approval Withdrawal"
    
    

@dataclass(config=PydanticConfig)
class OntologyClass:
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    None
    


@dataclass(config=PydanticConfig)
class Annotation:
    """
    Biolink Model root class for entity annotations.
    """
    None
    


@dataclass(config=PydanticConfig)
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    has_unit: Optional[str] = Field(None, description="""connects a quantity value to a unit""")
    has_numeric_value: Optional[float] = Field(None, description="""connects a quantity value to a number""")
    


@dataclass(config=PydanticConfig)
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class ChemicalRole(Attribute):
    
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class BiologicalSex(Attribute):
    
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class RelationshipQuantifier:
    
    None
    


@dataclass(config=PydanticConfig)
class SensitivityQuantifier(RelationshipQuantifier):
    
    None
    


@dataclass(config=PydanticConfig)
class SpecificityQuantifier(RelationshipQuantifier):
    
    None
    


@dataclass(config=PydanticConfig)
class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
    """
    None
    


@dataclass(config=PydanticConfig)
class FrequencyQuantifier(RelationshipQuantifier):
    
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    


@dataclass(config=PydanticConfig)
class ChemicalOrDrugOrTreatment:
    
    None
    


@dataclass(config=PydanticConfig)
class Entity:
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    None
    


@dataclass(config=PydanticConfig)
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    None
    


@dataclass(config=PydanticConfig)
class UnclassifiedOntologyClass(OntologyClass):
    """
    this is used for nodes that are taken from an ontology but are not typed using an existing biolink class
    """
    None
    


@dataclass(config=PydanticConfig)
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    None
    


@dataclass(config=PydanticConfig)
class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Event(NamedThing):
    """
    Something that happens at a given place and time.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class AdministrativeEntity(NamedThing):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    affiliation: Optional[List[str]] = Field(None, description="""a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.""")
    address: Optional[str] = Field(None, description="""the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text \"blob\" containing all relevant details of the given location for fitness of purpose. For the moment, this \"address\" can include other contact details such as email and phone number(?).""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""it is recommended that an author's 'name' property be formatted as \"surname, firstname initial.\"""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """
    distribution_download_url: Optional[str] = Field(None)
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DatasetVersion(InformationContentEntity):
    """
    an item that holds version level information about a dataset.
    """
    has_dataset: Optional[str] = Field(None)
    ingest_date: Optional[str] = Field(None)
    has_distribution: Optional[str] = Field(None)
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DatasetSummary(InformationContentEntity):
    """
    an item that holds summary level information about a dataset.
    """
    source_web_page: Optional[str] = Field(None)
    source_logo: Optional[str] = Field(None)
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.
    """
    authors: Optional[List[str]] = Field(None, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(None, description="""When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(None, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: str = Field(None, description="""Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.""")
    name: Optional[str] = Field(None, description="""the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    authors: Optional[List[str]] = Field(None, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(None, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(None, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Books should have industry-standard identifier such as from ISBN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: str = Field(None, description="""Should generally be set to an ontology class defined term for 'book'.""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class BookChapter(Publication):
    
    published_in: str = Field(None, description="""The enclosing parent book containing the chapter should have industry-standard identifier from ISBN.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    chapter: Optional[str] = Field(None, description="""chapter of a book""")
    authors: Optional[List[str]] = Field(None, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(None, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(None, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: str = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    iso_abbreviation: Optional[str] = Field(None, description="""Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    issue: Optional[str] = Field(None, description="""issue of a newspaper, a scientific journal or magazine for reference purpose""")
    authors: Optional[List[str]] = Field(None, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(None, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(None, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Serials (journals) should have industry-standard identifier such as from ISSN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: str = Field(None, description="""Should generally be set to an ontology class defined term for 'serial' or 'journal'.""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Article(Publication):
    
    published_in: str = Field(None, description="""The enclosing parent serial containing the article should have industry-standard identifier from ISSN.""")
    iso_abbreviation: Optional[str] = Field(None, description="""Optional value, if used locally as a convenience, is set to the iso abbreviation of the 'published in' parent.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    issue: Optional[str] = Field(None, description="""issue of a newspaper, a scientific journal or magazine for reference purpose""")
    authors: Optional[List[str]] = Field(None, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(None, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(None, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: str = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PhysicalEssenceOrOccurrent:
    """
    Either a physical or processual entity.
    """
    None
    


@dataclass(config=PydanticConfig)
class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    None
    


@dataclass(config=PydanticConfig)
class PhysicalEntity(NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    None
    


@dataclass(config=PydanticConfig)
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    None
    


@dataclass(config=PydanticConfig)
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SubjectOfInvestigation:
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    None
    


@dataclass(config=PydanticConfig)
class MaterialSample(PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EnvironmentalProcess(PlanetaryEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EnvironmentalFeature(PlanetaryEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    latitude: Optional[float] = Field(None, description="""latitude""")
    longitude: Optional[float] = Field(None, description="""longitude""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    latitude: Optional[float] = Field(None, description="""latitude""")
    longitude: Optional[float] = Field(None, description="""longitude""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class BiologicalEntity(NamedThing):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ThingWithTaxon:
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class GenomicEntity(ThingWithTaxon):
    
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class ChemicalSubstance:
    
    None
    


@dataclass(config=PydanticConfig)
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
    """
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    has_input: Optional[List[str]] = Field(None, description="""A chemical entity that is the input for the reaction""")
    has_output: Optional[List[str]] = Field(None, description="""A chemical entity that is the output for the reaction""")
    enabled_by: Optional[List[MacromolecularMachineMixin]] = Field(None, description="""The gene product, gene, or complex that catalyzes the reaction""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Pathway(BiologicalProcess):
    
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PhysiologicalProcess(BiologicalProcess):
    
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Behavior(BiologicalProcess):
    
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class OrganismAttribute(Attribute):
    """
    describes a characteristic of an organismal entity.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class PhenotypicQuality(OrganismAttribute):
    """
    A property of a phenotype
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class Inheritance(OrganismAttribute):
    """
    The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""may often be an organism attribute""")
    


@dataclass(config=PydanticConfig)
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class IndividualOrganism(OrganismalEntity):
    """
    An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class StudyPopulation(PopulationOfIndividualOrganisms):
    """
    A group of people banded together or treated as a group as participants in a research study.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Disease(DiseaseOrPhenotypicFeature):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    A combination of entity and quality that makes up a phenotyping statement.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class BehavioralFeature(PhenotypicFeature):
    """
    A phenotypic feature which is behavioral in nature.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Cell(AnatomicalEntity):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class CellLine(OrganismalEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GrossAnatomicalStructure(AnatomicalEntity):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalEntityOrGeneOrGeneProduct:
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    None
    


@dataclass(config=PydanticConfig)
class ChemicalEntityOrProteinOrPolypeptide:
    """
    A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    None
    


@dataclass(config=PydanticConfig)
class ChemicalEntity(NamedThing):
    """
    A chemical entity is a physical entity that pertains to chemistry or biochemistry.
    """
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MolecularEntity(ChemicalEntity):
    """
    A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
    """
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SmallMolecule(MolecularEntity):
    """
    A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).
    """
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalMixture(ChemicalEntity):
    """
    A chemical mixture is a chemical entity composed of two or more molecular entities.
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class NucleicAcidEntity(MolecularEntity):
    """
    A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class MolecularMixture(ChemicalMixture):
    """
    A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry.
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ComplexMolecularMixture(ChemicalMixture):
    """
    A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown concentration and stoichiometry.
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ProcessedMaterial(ChemicalMixture):
    """
    A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a material entity that is created or changed during material processing.
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Drug(MolecularMixture):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EnvironmentalFoodContaminant(ChemicalEntity):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class FoodAdditive(ChemicalEntity):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Nutrient(ChemicalEntity):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Macronutrient(Nutrient):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Micronutrient(Nutrient):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Vitamin(Micronutrient):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Food(ChemicalMixture):
    """
    A substance consumed by a living organism as a source of nutrition
    """
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MacromolecularMachineMixin:
    """
    A union of gene locus, gene product, and macromolecular complex mixin. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    name: Optional[str] = Field(None, description="""genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name""")
    


@dataclass(config=PydanticConfig)
class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


@dataclass(config=PydanticConfig)
class Gene(BiologicalEntity):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    symbol: Optional[str] = Field(None, description="""Symbol for a particular thing""")
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class GeneProductMixin(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


@dataclass(config=PydanticConfig)
class GeneProductIsoformMixin(GeneProductMixin):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


@dataclass(config=PydanticConfig)
class MacromolecularComplexMixin(MacromolecularMachineMixin):
    """
    A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


@dataclass(config=PydanticConfig)
class Genome(BiologicalEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class Exon(NucleicAcidEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class Transcript(NucleicAcidEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class CodingSequence(NucleicAcidEntity):
    
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class Polypeptide(BiologicalEntity):
    """
    A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Protein(Polypeptide):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class NucleicAcidSequenceMotif(BiologicalEntity):
    """
    A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class RNAProduct(Transcript):
    
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class NoncodingRNAProduct(RNAProduct):
    
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class MicroRNA(NoncodingRNAProduct):
    
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class SiRNA(NoncodingRNAProduct):
    """
    A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
    """
    synonym: Optional[List[str]] = Field(None, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[ChemicalRole]] = Field(None, description="""	A role is particular behaviour which a material entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class GeneGroupingMixin:
    """
    any grouping of multiple genes or gene products
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    


@dataclass(config=PydanticConfig)
class ProteinDomain(BiologicalEntity):
    """
    A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ProteinFamily(BiologicalEntity):
    
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneFamily(BiologicalEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Zygosity(Attribute):
    
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class Genotype(BiologicalEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
    """
    has_zygosity: Optional[Zygosity] = Field(None)
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class Haplotype(BiologicalEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class SequenceVariant(BiologicalEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    has_gene: Optional[List[str]] = Field(None, description="""Each allele can be associated with any number of genes""")
    has_biological_sequence: Optional[str] = Field(None, description="""The state of the sequence w.r.t a reference sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class Snv(SequenceVariant):
    """
    SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
    """
    has_gene: Optional[List[str]] = Field(None, description="""connects an entity associated with one or more genes""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class ReagentTargetedGene(BiologicalEntity):
    """
    A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class ClinicalAttribute(Attribute):
    """
    Attributes relating to a clinical manifestation
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class ClinicalMeasurement(ClinicalAttribute):
    """
    A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class ClinicalModifier(ClinicalAttribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology, with respect to severity, laterality, and other aspects
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class ClinicalCourse(ClinicalAttribute):
    """
    The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class Onset(ClinicalCourse):
    """
    The age group in which (disease) symptom manifestations appear
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ClinicalTrial(ClinicalEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ClinicalIntervention(ClinicalEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ClinicalFinding(PhenotypicFeature):
    """
    this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[ClinicalAttribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Hospitalization(ClinicalIntervention):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: OntologyClass = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    source: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class Case(IndividualOrganism):
    """
    An individual (human) organism that has a patient role in some clinical context.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class Cohort(StudyPopulation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ExposureEvent:
    """
    A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class GenomicBackgroundExposure:
    """
    A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


@dataclass(config=PydanticConfig)
class PathologicalEntityMixin:
    """
    A pathological (abnormal) structure or process.
    """
    None
    


@dataclass(config=PydanticConfig)
class PathologicalProcess(BiologicalProcess):
    """
    A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
    """
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PathologicalProcessExposure:
    """
    A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalStructure(AnatomicalEntity):
    """
    An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalExposure:
    """
    An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureExposure:
    """
    A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class ChemicalExposure:
    """
    A chemical exposure is an intake of a particular chemical entity.
    """
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class ComplexChemicalExposure:
    """
    A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
    """
    None
    


@dataclass(config=PydanticConfig)
class DrugExposure(ChemicalExposure):
    """
    A drug exposure is an intake of a particular drug.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    


@dataclass(config=PydanticConfig)
class DrugToGeneInteractionExposure(DrugExposure):
    """
    drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    


@dataclass(config=PydanticConfig)
class Treatment(NamedThing):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures
    """
    has_drug: Optional[List[str]] = Field(None, description="""connects an entity to one or more drugs""")
    has_device: Optional[List[str]] = Field(None, description="""connects an entity to one or more (medical) devices""")
    has_procedure: Optional[List[str]] = Field(None, description="""connects an entity to one or more (medical) procedures""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(None, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class BioticExposure:
    """
    An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class EnvironmentalExposure:
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class GeographicExposure(EnvironmentalExposure):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class BehavioralExposure:
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class SocioeconomicExposure:
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    


@dataclass(config=PydanticConfig)
class Outcome:
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes.
    """
    None
    


@dataclass(config=PydanticConfig)
class PathologicalProcessOutcome:
    """
    An outcome resulting from an exposure event which is the manifestation of a pathological process.
    """
    None
    


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalOutcome:
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure.
    """
    None
    


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureOutcome:
    """
    Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype.
    """
    None
    


@dataclass(config=PydanticConfig)
class BehavioralOutcome:
    """
    An outcome resulting from an exposure event which is the manifestation of human behavior.
    """
    None
    


@dataclass(config=PydanticConfig)
class HospitalizationOutcome:
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) hospitalization.
    """
    None
    


@dataclass(config=PydanticConfig)
class MortalityOutcome:
    """
    An outcome of death from resulting from an exposure event.
    """
    None
    


@dataclass(config=PydanticConfig)
class EpidemiologicalOutcome:
    """
    An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
    """
    None
    


@dataclass(config=PydanticConfig)
class SocioeconomicOutcome:
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event
    """
    None
    


@dataclass(config=PydanticConfig)
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None, description="""rdf:type of biolink:Association should be fixed at rdf:Statement""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    subject: str = Field(None, description="""information content entity which an agent has helped realise""")
    predicate: str = Field(None, description="""generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'""")
    object: str = Field(None, description="""agent helping to realise the given entity (e.g. such as a publication)""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""child genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""the relationship type used to connect genotype to gene""")
    object: str = Field(None, description="""gene implicated in genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""the relationship type used to connect genotype to gene""")
    object: str = Field(None, description="""gene implicated in genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
    """
    subject: GeneOrGeneProduct = Field(None, description="""the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOrGeneProduct = Field(None, description="""the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """
    subject: GeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""homology relationship type""")
    object: GeneOrGeneProduct = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneExpressionMixin:
    """
    Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.
    """
    quantifier_qualifier: Optional[OntologyClass] = Field(None, description="""Optional quantitative value indicating degree of expression.""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    


@dataclass(config=PydanticConfig)
class GeneToGeneCoexpressionAssociation(GeneToGeneAssociation):
    """
    Indicates that two genes are co-expressed, generally under the same conditions.
    """
    quantifier_qualifier: Optional[OntologyClass] = Field(None, description="""A measurable quantity for the object of the association""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    subject: GeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOrGeneProduct = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    subject: GeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""interaction relationship type""")
    object: GeneOrGeneProduct = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PairwiseMolecularInteraction(PairwiseGeneToGeneInteraction):
    """
    An interaction at the molecular level between two physical entities
    """
    interacting_molecules_category: Optional[OntologyClass] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""interaction relationship type""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""identifier for the interaction. This may come from an interaction database such as IMEX.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class CellLineToEntityAssociationMixin:
    """
    An relationship between a cell line and another entity
    """
    None
    


@dataclass(config=PydanticConfig)
class ChemicalEntityToEntityAssociationMixin:
    """
    An interaction between a chemical entity and another entity
    """
    None
    


@dataclass(config=PydanticConfig)
class DrugToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a drug and another entity
    """
    None
    


@dataclass(config=PydanticConfig)
class ChemicalToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a chemical entity and another entity
    """
    None
    


@dataclass(config=PydanticConfig)
class CaseToEntityAssociationMixin:
    """
    An abstract association for use where the case is the subject
    """
    None
    


@dataclass(config=PydanticConfig)
class ChemicalToChemicalAssociation(Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
    """
    subject: ChemicalEntityOrGeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the chemical element that is the target of the statement""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ReactionToParticipantAssociation(ChemicalToChemicalAssociation):
    
    stoichiometry: Optional[int] = Field(None, description="""the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.""")
    reaction_direction: Optional[ReactionDirectionEnum] = Field(None, description="""the direction of a reaction as constrained by the direction_enum (ie: left_to_right, neutral, etc.)""")
    reaction_side: Optional[ReactionSideEnum] = Field(None, description="""the side of a reaction being modeled (ie: left or right)""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ReactionToCatalystAssociation(ReactionToParticipantAssociation):
    
    stoichiometry: Optional[int] = Field(None, description="""the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.""")
    reaction_direction: Optional[ReactionDirectionEnum] = Field(None, description="""the direction of a reaction as constrained by the direction_enum (ie: left_to_right, neutral, etc.)""")
    reaction_side: Optional[ReactionSideEnum] = Field(None, description="""the side of a reaction being modeled (ie: left or right)""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOrGeneProduct = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
  IF
  R has-input C1 AND
  R has-output C2 AND
  R enabled-by P AND
  R type Reaction
  THEN
  C1 derives-into C2 <<catalyst qualifier P>>
    """
    catalyst_qualifier: Optional[List[MacromolecularMachineMixin]] = Field(None, description="""this connects the derivation edge to the chemical entity that catalyzes the reaction that causes the subject chemical to transform into the object chemical.""")
    subject: str = Field(None, description="""the upstream chemical entity""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the downstream chemical entity""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway.
    """
    subject: str = Field(None, description="""the chemical entity that is affecting the pathway""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the pathway that is affected by the chemical""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product.
    """
    subject: ChemicalEntityOrGeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOrGeneProduct = Field(None, description="""the gene or gene product that is affected by the chemical.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DrugToGeneAssociation(Association):
    """
    An interaction between a drug and a gene or gene product.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOrGeneProduct = Field(None, description="""the gene or gene product that is affected by the drug""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MaterialSampleToEntityAssociationMixin:
    """
    An association between a material sample and something.
    """
    None
    


@dataclass(config=PydanticConfig)
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity from which it is derived.
    """
    subject: str = Field(None, description="""the material sample being described""")
    predicate: str = Field(None, description="""derivation relationship""")
    object: str = Field(None, description="""the material entity the sample was derived from. This may be another material sample, or any other material entity, including for example an organism, a geographic feature, or some environmental material.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class DiseaseToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class EntityToExposureEventAssociationMixin:
    """
    An association between some entity and an exposure event.
    """
    None
    


@dataclass(config=PydanticConfig)
class DiseaseToExposureEventAssociation(Association):
    """
    An association between an exposure event and a disease.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: ExposureEvent = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ExposureEventToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class EntityToOutcomeAssociationMixin:
    """
    An association between some entity and an outcome
    """
    None
    


@dataclass(config=PydanticConfig)
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    has_population_context: Optional[str] = Field(None, description="""a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.""")
    has_temporal_context: Optional[str] = Field(None, description="""a constraint of time placed upon the truth value of an association.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: Outcome = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class FrequencyQualifierMixin:
    """
    Qualifier for frequency type associations
    """
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class EntityToFeatureOrDiseaseQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to disease or phenotype associations.
    """
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class EntityToPhenotypicFeatureAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class InformationContentEntityToNamedThingAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EntityToDiseaseAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a disease
    """
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureToLocationAssociation(Association):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""anatomical entity in which the disease or feature is found.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EntityToDiseaseOrPhenotypicFeatureAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
    """
    subject: ChemicalEntityOrGeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the disease or phenotype that is affected by the chemical""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a material sample and a disease or phenotype.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GenotypeToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    """
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""genotype that is associated with the phenotypic feature""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class ExposureEventToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
    """
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: ExposureEvent = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
    """
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
    """
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
    """
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""behavior that is the subject of the association""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""behavioral feature that is the object of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class GeneToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class VariantToEntityAssociationMixin:
    
    None
    


@dataclass(config=PydanticConfig)
class GeneToPhenotypicFeatureAssociation(Association):
    
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: GeneOrGeneProduct = Field(None, description="""gene in which variation is correlated with the phenotypic feature""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class GeneToDiseaseAssociation(Association):
    
    subject: GeneOrGeneProduct = Field(None, description="""gene in which variation is correlated with the disease, may be protective or causative or associative, or as a model""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class DruggableGeneToDiseaseAssociation(GeneToDiseaseAssociation):
    
    subject: GeneOrGeneProduct = Field(None, description="""gene in which variation is correlated with the disease in a protective manner, or if the product produced by the gene can be targeted by a small molecule and this leads to a protective or improving disease state.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[DruggableGeneCategoryEnum]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class VariantToGeneAssociation(Association):
    """
    An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class VariantToGeneExpressionAssociation(VariantToGeneAssociation):
    """
    An association between a variant and expression of a gene (i.e. e-QTL)
    """
    quantifier_qualifier: Optional[OntologyClass] = Field(None, description="""A measurable quantity for the object of the association""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    has_count: Optional[int] = Field(None, description="""number in object population that carry a particular allele, aka allele count""")
    has_total: Optional[int] = Field(None, description="""number all populations that carry a particular allele, aka allele number""")
    has_quotient: Optional[float] = Field(None, description="""frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency""")
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    subject: str = Field(None, description="""an allele that has a certain frequency in a given population""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the population that is observed to have the frequency""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    subject: str = Field(None, description="""the population that form the subject of the association""")
    predicate: str = Field(None, description="""A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used""")
    object: str = Field(None, description="""the population that form the object of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class VariantToPhenotypicFeatureAssociation(Association):
    
    sex_qualifier: Optional[BiologicalSex] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""a sequence variant in which the allele state is associated in some way with the phenotype state""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class VariantToDiseaseAssociation(Association):
    
    subject: str = Field(None, description="""a sequence variant in which the allele state is associated in some way with the disease state""")
    predicate: str = Field(None, description="""E.g. is pathogenic for""")
    object: str = Field(None, description="""a disease that is associated with that variant""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class GenotypeToDiseaseAssociation(Association):
    
    subject: str = Field(None, description="""a genotype that is associated in some way with a disease state""")
    predicate: str = Field(None, description="""E.g. is pathogenic for""")
    object: str = Field(None, description="""a disease that is associated with that genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class ModelToDiseaseAssociationMixin:
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
    """
    None
    


@dataclass(config=PydanticConfig)
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    
    subject: GeneOrGeneProduct = Field(None, description="""A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class VariantAsAModelOfDiseaseAssociation(VariantToDiseaseAssociation):
    
    subject: str = Field(None, description="""A variant that has a role in modeling the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class GenotypeAsAModelOfDiseaseAssociation(GenotypeToDiseaseAssociation):
    
    subject: str = Field(None, description="""A genotype that has a role in modeling the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class CellLineAsAModelOfDiseaseAssociation(CellLineToDiseaseOrPhenotypicFeatureAssociation):
    
    subject: str = Field(None, description="""A cell line derived from an organismal entity with a disease state that is used as a model of that disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class OrganismalEntityAsAModelOfDiseaseAssociation(Association):
    
    subject: str = Field(None, description="""A organismal entity (strain, breed) with a predisposition to a disease, or bred/created specifically to model a disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class OrganismToOrganismAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""An association between two individual organisms.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class TaxonToTaxonAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""An association between individuals of different taxa.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    
    sequence_variant_qualifier: Optional[str] = Field(None, description="""a qualifier used in an association with the variant""")
    subject: GeneOrGeneProduct = Field(None, description="""A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[SeverityValue] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[Onset] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


@dataclass(config=PydanticConfig)
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and a gene expression site, possibly qualified by stage/timing info.
    """
    stage_qualifier: Optional[str] = Field(None, description="""stage at which the gene is expressed in the site""")
    quantifier_qualifier: Optional[OntologyClass] = Field(None, description="""can be used to indicate magnitude, or also ranking""")
    subject: GeneOrGeneProduct = Field(None, description="""Gene or gene product positively within the specified anatomical entity (or subclass, i.e. cellular component) location.""")
    predicate: str = Field(None, description="""expression relationship""")
    object: str = Field(None, description="""location in which the gene is expressed""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
    """
    subject: str = Field(None, description="""variant that modulates the treatment of some disease""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""treatment whose efficacy is modulated by the subject variant""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.
    """
    subject: MacromolecularMachineMixin = Field(None, description="""gene, product or macromolecular complex mixin that has the function associated with the GO term""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOntologyClass = Field(None, description="""class describing the activity, process or localization of the gene product""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MacromolecularMachineToEntityAssociationMixin:
    """
    an association which has a macromolecular machine mixin as a subject
    """
    None
    


@dataclass(config=PydanticConfig)
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution.
    """
    subject: MacromolecularMachineMixin = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it.
    """
    subject: MacromolecularMachineMixin = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component.
    """
    subject: MacromolecularMachineMixin = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MolecularActivityToChemicalEntityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class MolecularActivityToMolecularActivityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneToGoTermAssociation(FunctionalAssociation):
    
    subject: str = Field(None, description="""gene, product or macromolecular complex that has the function associated with the GO term""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneOntologyClass = Field(None, description="""class describing the activity, process or localization of the gene product""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EntityToDiseaseAssociation(Association):
    
    FDA_approval_status: Optional[FDAApprovalStatusEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class EntityToPhenotypicFeatureAssociation(Association):
    
    FDA_approval_status: Optional[FDAApprovalStatusEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a nucleic acid entity it is localized to.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GenomicSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig.
    """
    start_interbase_coordinate: Optional[int] = Field(None, description="""The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).""")
    end_interbase_coordinate: Optional[int] = Field(None, description="""The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.""")
    genome_build: Optional[StrandEnum] = Field(None, description="""The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.""")
    strand: Optional[StrandEnum] = Field(None, description="""The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).""")
    phase: Optional[PhaseEnum] = Field(None, description="""The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: GeneProductMixin = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    subject: GeneOrGeneProduct = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""the direction is always from regulator to regulated""")
    object: GeneOrGeneProduct = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
    """
    subject: str = Field(None, description="""the part""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the whole""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship.
    """
    subject: str = Field(None, description="""the structure at a later time""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the structure at an earlier time""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class OrganismTaxonToEntityAssociation:
    """
    An association between an organism taxon and another entity
    """
    None
    


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonAssociation(Association):
    """
    A relationship between two organism taxon nodes
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonSpecialization(OrganismTaxonToOrganismTaxonAssociation):
    """
    A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo
    """
    subject: str = Field(None, description="""the more specific taxon""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the more general taxon""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonInteraction(OrganismTaxonToOrganismTaxonAssociation):
    """
    An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens
    """
    associated_environmental_context: Optional[str] = Field(None, description="""the environment in which the two taxa interact""")
    subject: str = Field(None, description="""the taxon that is the subject of the association""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the taxon that is the subject of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    


@dataclass(config=PydanticConfig)
class OrganismTaxonToEnvironmentAssociation(Association):
    
    subject: str = Field(None, description="""the taxon that is the subject of the association""")
    predicate: str = Field(None, description="""predicate describing the relationship between the taxon and the environment
 """)
    object: str = Field(None, description="""the environment in which the organism occurs""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[OntologyClass]] = Field(None, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(None, description="""connects an association to publications supporting the association""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[List[str]] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    original_knowledge_source: Optional[List[str]] = Field(None, description="""The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).""")
    primary_knowledge_source: Optional[List[str]] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(None, description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[str] = Field(None)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    source: Optional[str] = Field(None)
    has_attribute: Optional[List[Attribute]] = Field(None, description="""connects any entity to an attribute""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
OntologyClass.__pydantic_model__.update_forward_refs()
Annotation.__pydantic_model__.update_forward_refs()
QuantityValue.__pydantic_model__.update_forward_refs()
Attribute.__pydantic_model__.update_forward_refs()
ChemicalRole.__pydantic_model__.update_forward_refs()
BiologicalSex.__pydantic_model__.update_forward_refs()
PhenotypicSex.__pydantic_model__.update_forward_refs()
GenotypicSex.__pydantic_model__.update_forward_refs()
SeverityValue.__pydantic_model__.update_forward_refs()
RelationshipQuantifier.__pydantic_model__.update_forward_refs()
SensitivityQuantifier.__pydantic_model__.update_forward_refs()
SpecificityQuantifier.__pydantic_model__.update_forward_refs()
PathognomonicityQuantifier.__pydantic_model__.update_forward_refs()
FrequencyQuantifier.__pydantic_model__.update_forward_refs()
ChemicalOrDrugOrTreatment.__pydantic_model__.update_forward_refs()
Entity.__pydantic_model__.update_forward_refs()
NamedThing.__pydantic_model__.update_forward_refs()
RelationshipType.__pydantic_model__.update_forward_refs()
GeneOntologyClass.__pydantic_model__.update_forward_refs()
UnclassifiedOntologyClass.__pydantic_model__.update_forward_refs()
TaxonomicRank.__pydantic_model__.update_forward_refs()
OrganismTaxon.__pydantic_model__.update_forward_refs()
Event.__pydantic_model__.update_forward_refs()
AdministrativeEntity.__pydantic_model__.update_forward_refs()
Agent.__pydantic_model__.update_forward_refs()
InformationContentEntity.__pydantic_model__.update_forward_refs()
Dataset.__pydantic_model__.update_forward_refs()
DatasetDistribution.__pydantic_model__.update_forward_refs()
DatasetVersion.__pydantic_model__.update_forward_refs()
DatasetSummary.__pydantic_model__.update_forward_refs()
ConfidenceLevel.__pydantic_model__.update_forward_refs()
EvidenceType.__pydantic_model__.update_forward_refs()
InformationResource.__pydantic_model__.update_forward_refs()
Publication.__pydantic_model__.update_forward_refs()
Book.__pydantic_model__.update_forward_refs()
BookChapter.__pydantic_model__.update_forward_refs()
Serial.__pydantic_model__.update_forward_refs()
Article.__pydantic_model__.update_forward_refs()
PhysicalEssenceOrOccurrent.__pydantic_model__.update_forward_refs()
PhysicalEssence.__pydantic_model__.update_forward_refs()
PhysicalEntity.__pydantic_model__.update_forward_refs()
Occurrent.__pydantic_model__.update_forward_refs()
ActivityAndBehavior.__pydantic_model__.update_forward_refs()
Activity.__pydantic_model__.update_forward_refs()
Procedure.__pydantic_model__.update_forward_refs()
Phenomenon.__pydantic_model__.update_forward_refs()
Device.__pydantic_model__.update_forward_refs()
SubjectOfInvestigation.__pydantic_model__.update_forward_refs()
MaterialSample.__pydantic_model__.update_forward_refs()
PlanetaryEntity.__pydantic_model__.update_forward_refs()
EnvironmentalProcess.__pydantic_model__.update_forward_refs()
EnvironmentalFeature.__pydantic_model__.update_forward_refs()
GeographicLocation.__pydantic_model__.update_forward_refs()
GeographicLocationAtTime.__pydantic_model__.update_forward_refs()
BiologicalEntity.__pydantic_model__.update_forward_refs()
ThingWithTaxon.__pydantic_model__.update_forward_refs()
GenomicEntity.__pydantic_model__.update_forward_refs()
ChemicalSubstance.__pydantic_model__.update_forward_refs()
BiologicalProcessOrActivity.__pydantic_model__.update_forward_refs()
MolecularActivity.__pydantic_model__.update_forward_refs()
BiologicalProcess.__pydantic_model__.update_forward_refs()
Pathway.__pydantic_model__.update_forward_refs()
PhysiologicalProcess.__pydantic_model__.update_forward_refs()
Behavior.__pydantic_model__.update_forward_refs()
OrganismAttribute.__pydantic_model__.update_forward_refs()
PhenotypicQuality.__pydantic_model__.update_forward_refs()
Inheritance.__pydantic_model__.update_forward_refs()
OrganismalEntity.__pydantic_model__.update_forward_refs()
LifeStage.__pydantic_model__.update_forward_refs()
IndividualOrganism.__pydantic_model__.update_forward_refs()
PopulationOfIndividualOrganisms.__pydantic_model__.update_forward_refs()
StudyPopulation.__pydantic_model__.update_forward_refs()
DiseaseOrPhenotypicFeature.__pydantic_model__.update_forward_refs()
Disease.__pydantic_model__.update_forward_refs()
PhenotypicFeature.__pydantic_model__.update_forward_refs()
BehavioralFeature.__pydantic_model__.update_forward_refs()
AnatomicalEntity.__pydantic_model__.update_forward_refs()
CellularComponent.__pydantic_model__.update_forward_refs()
Cell.__pydantic_model__.update_forward_refs()
CellLine.__pydantic_model__.update_forward_refs()
GrossAnatomicalStructure.__pydantic_model__.update_forward_refs()
ChemicalEntityOrGeneOrGeneProduct.__pydantic_model__.update_forward_refs()
ChemicalEntityOrProteinOrPolypeptide.__pydantic_model__.update_forward_refs()
ChemicalEntity.__pydantic_model__.update_forward_refs()
MolecularEntity.__pydantic_model__.update_forward_refs()
SmallMolecule.__pydantic_model__.update_forward_refs()
ChemicalMixture.__pydantic_model__.update_forward_refs()
NucleicAcidEntity.__pydantic_model__.update_forward_refs()
MolecularMixture.__pydantic_model__.update_forward_refs()
ComplexMolecularMixture.__pydantic_model__.update_forward_refs()
ProcessedMaterial.__pydantic_model__.update_forward_refs()
Drug.__pydantic_model__.update_forward_refs()
EnvironmentalFoodContaminant.__pydantic_model__.update_forward_refs()
FoodAdditive.__pydantic_model__.update_forward_refs()
Nutrient.__pydantic_model__.update_forward_refs()
Macronutrient.__pydantic_model__.update_forward_refs()
Micronutrient.__pydantic_model__.update_forward_refs()
Vitamin.__pydantic_model__.update_forward_refs()
Food.__pydantic_model__.update_forward_refs()
MacromolecularMachineMixin.__pydantic_model__.update_forward_refs()
GeneOrGeneProduct.__pydantic_model__.update_forward_refs()
Gene.__pydantic_model__.update_forward_refs()
GeneProductMixin.__pydantic_model__.update_forward_refs()
GeneProductIsoformMixin.__pydantic_model__.update_forward_refs()
MacromolecularComplexMixin.__pydantic_model__.update_forward_refs()
Genome.__pydantic_model__.update_forward_refs()
Exon.__pydantic_model__.update_forward_refs()
Transcript.__pydantic_model__.update_forward_refs()
CodingSequence.__pydantic_model__.update_forward_refs()
Polypeptide.__pydantic_model__.update_forward_refs()
Protein.__pydantic_model__.update_forward_refs()
ProteinIsoform.__pydantic_model__.update_forward_refs()
NucleicAcidSequenceMotif.__pydantic_model__.update_forward_refs()
RNAProduct.__pydantic_model__.update_forward_refs()
RNAProductIsoform.__pydantic_model__.update_forward_refs()
NoncodingRNAProduct.__pydantic_model__.update_forward_refs()
MicroRNA.__pydantic_model__.update_forward_refs()
SiRNA.__pydantic_model__.update_forward_refs()
GeneGroupingMixin.__pydantic_model__.update_forward_refs()
ProteinDomain.__pydantic_model__.update_forward_refs()
ProteinFamily.__pydantic_model__.update_forward_refs()
GeneFamily.__pydantic_model__.update_forward_refs()
Zygosity.__pydantic_model__.update_forward_refs()
Genotype.__pydantic_model__.update_forward_refs()
Haplotype.__pydantic_model__.update_forward_refs()
SequenceVariant.__pydantic_model__.update_forward_refs()
Snv.__pydantic_model__.update_forward_refs()
ReagentTargetedGene.__pydantic_model__.update_forward_refs()
ClinicalAttribute.__pydantic_model__.update_forward_refs()
ClinicalMeasurement.__pydantic_model__.update_forward_refs()
ClinicalModifier.__pydantic_model__.update_forward_refs()
ClinicalCourse.__pydantic_model__.update_forward_refs()
Onset.__pydantic_model__.update_forward_refs()
ClinicalEntity.__pydantic_model__.update_forward_refs()
ClinicalTrial.__pydantic_model__.update_forward_refs()
ClinicalIntervention.__pydantic_model__.update_forward_refs()
ClinicalFinding.__pydantic_model__.update_forward_refs()
Hospitalization.__pydantic_model__.update_forward_refs()
SocioeconomicAttribute.__pydantic_model__.update_forward_refs()
Case.__pydantic_model__.update_forward_refs()
Cohort.__pydantic_model__.update_forward_refs()
ExposureEvent.__pydantic_model__.update_forward_refs()
GenomicBackgroundExposure.__pydantic_model__.update_forward_refs()
PathologicalEntityMixin.__pydantic_model__.update_forward_refs()
PathologicalProcess.__pydantic_model__.update_forward_refs()
PathologicalProcessExposure.__pydantic_model__.update_forward_refs()
PathologicalAnatomicalStructure.__pydantic_model__.update_forward_refs()
PathologicalAnatomicalExposure.__pydantic_model__.update_forward_refs()
DiseaseOrPhenotypicFeatureExposure.__pydantic_model__.update_forward_refs()
ChemicalExposure.__pydantic_model__.update_forward_refs()
ComplexChemicalExposure.__pydantic_model__.update_forward_refs()
DrugExposure.__pydantic_model__.update_forward_refs()
DrugToGeneInteractionExposure.__pydantic_model__.update_forward_refs()
Treatment.__pydantic_model__.update_forward_refs()
BioticExposure.__pydantic_model__.update_forward_refs()
EnvironmentalExposure.__pydantic_model__.update_forward_refs()
GeographicExposure.__pydantic_model__.update_forward_refs()
BehavioralExposure.__pydantic_model__.update_forward_refs()
SocioeconomicExposure.__pydantic_model__.update_forward_refs()
Outcome.__pydantic_model__.update_forward_refs()
PathologicalProcessOutcome.__pydantic_model__.update_forward_refs()
PathologicalAnatomicalOutcome.__pydantic_model__.update_forward_refs()
DiseaseOrPhenotypicFeatureOutcome.__pydantic_model__.update_forward_refs()
BehavioralOutcome.__pydantic_model__.update_forward_refs()
HospitalizationOutcome.__pydantic_model__.update_forward_refs()
MortalityOutcome.__pydantic_model__.update_forward_refs()
EpidemiologicalOutcome.__pydantic_model__.update_forward_refs()
SocioeconomicOutcome.__pydantic_model__.update_forward_refs()
Association.__pydantic_model__.update_forward_refs()
ContributorAssociation.__pydantic_model__.update_forward_refs()
GenotypeToGenotypePartAssociation.__pydantic_model__.update_forward_refs()
GenotypeToGeneAssociation.__pydantic_model__.update_forward_refs()
GenotypeToVariantAssociation.__pydantic_model__.update_forward_refs()
GeneToGeneAssociation.__pydantic_model__.update_forward_refs()
GeneToGeneHomologyAssociation.__pydantic_model__.update_forward_refs()
GeneExpressionMixin.__pydantic_model__.update_forward_refs()
GeneToGeneCoexpressionAssociation.__pydantic_model__.update_forward_refs()
PairwiseGeneToGeneInteraction.__pydantic_model__.update_forward_refs()
PairwiseMolecularInteraction.__pydantic_model__.update_forward_refs()
CellLineToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
ChemicalEntityToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
DrugToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
ChemicalToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
CaseToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
ChemicalToChemicalAssociation.__pydantic_model__.update_forward_refs()
ReactionToParticipantAssociation.__pydantic_model__.update_forward_refs()
ReactionToCatalystAssociation.__pydantic_model__.update_forward_refs()
ChemicalToChemicalDerivationAssociation.__pydantic_model__.update_forward_refs()
ChemicalToPathwayAssociation.__pydantic_model__.update_forward_refs()
ChemicalToGeneAssociation.__pydantic_model__.update_forward_refs()
DrugToGeneAssociation.__pydantic_model__.update_forward_refs()
MaterialSampleToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
MaterialSampleDerivationAssociation.__pydantic_model__.update_forward_refs()
DiseaseToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
EntityToExposureEventAssociationMixin.__pydantic_model__.update_forward_refs()
DiseaseToExposureEventAssociation.__pydantic_model__.update_forward_refs()
ExposureEventToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
EntityToOutcomeAssociationMixin.__pydantic_model__.update_forward_refs()
ExposureEventToOutcomeAssociation.__pydantic_model__.update_forward_refs()
FrequencyQualifierMixin.__pydantic_model__.update_forward_refs()
EntityToFeatureOrDiseaseQualifiersMixin.__pydantic_model__.update_forward_refs()
EntityToPhenotypicFeatureAssociationMixin.__pydantic_model__.update_forward_refs()
InformationContentEntityToNamedThingAssociation.__pydantic_model__.update_forward_refs()
EntityToDiseaseAssociationMixin.__pydantic_model__.update_forward_refs()
DiseaseOrPhenotypicFeatureToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
DiseaseOrPhenotypicFeatureToLocationAssociation.__pydantic_model__.update_forward_refs()
EntityToDiseaseOrPhenotypicFeatureAssociationMixin.__pydantic_model__.update_forward_refs()
CellLineToDiseaseOrPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
ChemicalToDiseaseOrPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
GenotypeToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
GenotypeToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
ExposureEventToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
DiseaseToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
CaseToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
BehaviorToBehavioralFeatureAssociation.__pydantic_model__.update_forward_refs()
GeneToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
VariantToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
GeneToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
GeneToDiseaseAssociation.__pydantic_model__.update_forward_refs()
DruggableGeneToDiseaseAssociation.__pydantic_model__.update_forward_refs()
VariantToGeneAssociation.__pydantic_model__.update_forward_refs()
VariantToGeneExpressionAssociation.__pydantic_model__.update_forward_refs()
VariantToPopulationAssociation.__pydantic_model__.update_forward_refs()
PopulationToPopulationAssociation.__pydantic_model__.update_forward_refs()
VariantToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
VariantToDiseaseAssociation.__pydantic_model__.update_forward_refs()
GenotypeToDiseaseAssociation.__pydantic_model__.update_forward_refs()
ModelToDiseaseAssociationMixin.__pydantic_model__.update_forward_refs()
GeneAsAModelOfDiseaseAssociation.__pydantic_model__.update_forward_refs()
VariantAsAModelOfDiseaseAssociation.__pydantic_model__.update_forward_refs()
GenotypeAsAModelOfDiseaseAssociation.__pydantic_model__.update_forward_refs()
CellLineAsAModelOfDiseaseAssociation.__pydantic_model__.update_forward_refs()
OrganismalEntityAsAModelOfDiseaseAssociation.__pydantic_model__.update_forward_refs()
OrganismToOrganismAssociation.__pydantic_model__.update_forward_refs()
TaxonToTaxonAssociation.__pydantic_model__.update_forward_refs()
GeneHasVariantThatContributesToDiseaseAssociation.__pydantic_model__.update_forward_refs()
GeneToExpressionSiteAssociation.__pydantic_model__.update_forward_refs()
SequenceVariantModulatesTreatmentAssociation.__pydantic_model__.update_forward_refs()
FunctionalAssociation.__pydantic_model__.update_forward_refs()
MacromolecularMachineToEntityAssociationMixin.__pydantic_model__.update_forward_refs()
MacromolecularMachineToMolecularActivityAssociation.__pydantic_model__.update_forward_refs()
MacromolecularMachineToBiologicalProcessAssociation.__pydantic_model__.update_forward_refs()
MacromolecularMachineToCellularComponentAssociation.__pydantic_model__.update_forward_refs()
MolecularActivityToChemicalEntityAssociation.__pydantic_model__.update_forward_refs()
MolecularActivityToMolecularActivityAssociation.__pydantic_model__.update_forward_refs()
GeneToGoTermAssociation.__pydantic_model__.update_forward_refs()
EntityToDiseaseAssociation.__pydantic_model__.update_forward_refs()
EntityToPhenotypicFeatureAssociation.__pydantic_model__.update_forward_refs()
SequenceAssociation.__pydantic_model__.update_forward_refs()
GenomicSequenceLocalization.__pydantic_model__.update_forward_refs()
SequenceFeatureRelationship.__pydantic_model__.update_forward_refs()
TranscriptToGeneRelationship.__pydantic_model__.update_forward_refs()
GeneToGeneProductRelationship.__pydantic_model__.update_forward_refs()
ExonToTranscriptRelationship.__pydantic_model__.update_forward_refs()
GeneRegulatoryRelationship.__pydantic_model__.update_forward_refs()
AnatomicalEntityToAnatomicalEntityAssociation.__pydantic_model__.update_forward_refs()
AnatomicalEntityToAnatomicalEntityPartOfAssociation.__pydantic_model__.update_forward_refs()
AnatomicalEntityToAnatomicalEntityOntogenicAssociation.__pydantic_model__.update_forward_refs()
OrganismTaxonToEntityAssociation.__pydantic_model__.update_forward_refs()
OrganismTaxonToOrganismTaxonAssociation.__pydantic_model__.update_forward_refs()
OrganismTaxonToOrganismTaxonSpecialization.__pydantic_model__.update_forward_refs()
OrganismTaxonToOrganismTaxonInteraction.__pydantic_model__.update_forward_refs()
OrganismTaxonToEnvironmentAssociation.__pydantic_model__.update_forward_refs()

