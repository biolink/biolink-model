from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel as BaseModel, Field

metamodel_version = "None"
version = "3.2.0"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class AnatomicalContextQualifierEnum(str, Enum):
    
    
    dummy = "dummy"
    

class DirectionQualifierEnum(str, Enum):
    
    increased = "increased"
    upregulated = "upregulated"
    decreased = "decreased"
    downregulated = "downregulated"
    
    

class ChemicalEntityDerivativeEnum(str, Enum):
    
    metabolite = "metabolite"
    
    

class ChemicalOrGeneOrGeneProductFormOrVariantEnum(str, Enum):
    
    genetic_variant_form = "genetic_variant_form"
    modified_form = "modified_form"
    loss_of_function_variant_form = "loss_of_function_variant_form"
    gain_of_function_variant_form = "gain_of_function_variant_form"
    polymorphic_form = "polymorphic_form"
    snp_form = "snp_form"
    analog_form = "analog_form"
    
    

class GeneOrGeneProductOrChemicalPartQualifierEnum(str, Enum):
    
    number_3_prime_utr = "3_prime_utr"
    number_5_prime_utr = "5_prime_utr"
    polya_tail = "polya_tail"
    promoter = "promoter"
    enhancer = "enhancer"
    exon = "exon"
    intron = "intron"
    
    

class GeneOrGeneProductOrChemicalEntityAspectEnum(str, Enum):
    
    activity_or_abundance = "activity_or_abundance"
    abundance = "abundance"
    activity = "activity"
    expression = "expression"
    synthesis = "synthesis"
    degradation = "degradation"
    cleavage = "cleavage"
    hydrolysis = "hydrolysis"
    metabolic_processing = "metabolic_processing"
    mutation_rate = "mutation_rate"
    stability = "stability"
    folding = "folding"
    localization = "localization"
    transport = "transport"
    secretion = "secretion"
    uptake = "uptake"
    molecular_modification = "molecular_modification"
    acetylation = "acetylation"
    acylation = "acylation"
    alkylation = "alkylation"
    amination = "amination"
    carbamoylation = "carbamoylation"
    ethylation = "ethylation"
    glutathionylation = "glutathionylation"
    glycation = "glycation"
    glycosylation = "glycosylation"
    glucuronidation = "glucuronidation"
    n_linked_glycosylation = "n_linked_glycosylation"
    o_linked_glycosylation = "o_linked_glycosylation"
    hydroxylation = "hydroxylation"
    lipidation = "lipidation"
    farnesylation = "farnesylation"
    geranoylation = "geranoylation"
    myristoylation = "myristoylation"
    palmitoylation = "palmitoylation"
    prenylation = "prenylation"
    methylation = "methylation"
    nitrosation = "nitrosation"
    nucleotidylation = "nucleotidylation"
    phosphorylation = "phosphorylation"
    ribosylation = "ribosylation"
    ADP_ribosylation = "ADP-ribosylation"
    sulfation = "sulfation"
    sumoylation = "sumoylation"
    ubiquitination = "ubiquitination"
    oxidation = "oxidation"
    reduction = "reduction"
    carboxylation = "carboxylation"
    
    

class CausalMechanismQualifierEnum(str, Enum):
    
    binding = "binding"
    inhibition = "inhibition"
    antibody_inhibition = "antibody_inhibition"
    antagonism = "antagonism"
    molecular_channel_blockage = "molecular_channel_blockage"
    inverse_agonism = "inverse_agonism"
    negative_allosteric_modulation = "negative_allosteric_modulation"
    agonism = "agonism"
    molecular_channel_opening = "molecular_channel_opening"
    positive_allosteric_modulation = "positive_allosteric_modulation"
    potentiation = "potentiation"
    activation = "activation"
    inducer = "inducer"
    transcriptional_regulation = "transcriptional_regulation"
    signaling_mediated_control = "signaling_mediated_control"
    stabilization = "stabilization"
    stimulation = "stimulation"
    releasing_activity = "releasing_activity"
    
    

class LogicalInterpretationEnum(str, Enum):
    
    some_some = "some_some"
    all_some = "all_some"
    inverse_all_some = "inverse_all_some"
    
    

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
    
    na = "na"
    aa = "aa"
    
    

class DruggableGeneCategoryEnum(str, Enum):
    
    tclin = "tclin"
    tbio = "tbio"
    tchem = "tchem"
    tdark = "tdark"
    
    

class DrugAvailabilityEnum(str, Enum):
    
    over_the_counter = "over_the_counter"
    prescription = "prescription"
    
    

class DrugDeliveryEnum(str, Enum):
    
    inhalation = "inhalation"
    oral = "oral"
    absorption_through_the_skin = "absorption_through_the_skin"
    intravenous_injection = "intravenous_injection"
    
    

class FDAApprovalStatusEnum(str, Enum):
    
    discovery_and_development_phase = "discovery_and_development_phase"
    preclinical_research_phase = "preclinical_research_phase"
    fda_clinical_research_phase = "fda_clinical_research_phase"
    fda_review_phase_4 = "fda_review_phase_4"
    fda_post_market_safety_review = "fda_post_market_safety_review"
    fda_clinical_research_phase_1 = "fda_clinical_research_phase_1"
    fda_clinical_research_phase_2 = "fda_clinical_research_phase_2"
    fda_clinical_research_phase_3 = "fda_clinical_research_phase_3"
    fda_clinical_research_phase_4 = "fda_clinical_research_phase_4"
    fda_fast_track = "fda_fast_track"
    fda_breakthrough_therapy = "fda_breakthrough_therapy"
    fda_accelerated_approval = "fda_accelerated_approval"
    fda_priority_review = "fda_priority_review"
    regular_fda_approval = "regular_fda_approval"
    post_approval_withdrawal = "post_approval_withdrawal"
    
    

class FDAIDAAdverseEventEnum(str, Enum):
    
    life_threatening_adverse_event = "life_threatening_adverse_event"
    serious_adverse_event = "serious_adverse_event"
    suspected_adverse_reaction = "suspected_adverse_reaction"
    unexpected_adverse_event = "unexpected_adverse_event"
    
    

class MappingCollection(ConfiguredBaseModel):
    """
    A collection of deprecated mappings.
    """
    predicate_mappings: Optional[List[PredicateMapping]] = Field(None, description="""A collection of relationships that are not used in biolink, but have biolink patterns that can  be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3.""")
    


class PredicateMapping(ConfiguredBaseModel):
    """
    A deprecated predicate mapping object contains the deprecated predicate and an example of the rewiring that should be done to use a qualified statement in its place.
    """
    mapped_predicate: Optional[str] = Field(None, description="""The predicate that is being replaced by the fully qualified representation of predicate + subject and object  qualifiers.  Only to be used in test data and mapping data to help with the transition to the fully qualified predicate model. Not to be used in knowledge graphs.""")
    subject_aspect_qualifier: Optional[str] = Field(None)
    subject_direction_qualifier: Optional[DirectionQualifierEnum] = Field(None)
    subject_form_or_variant_qualifier: Optional[str] = Field(None)
    subject_part_qualifier: Optional[str] = Field(None)
    subject_derivative_qualifier: Optional[str] = Field(None)
    subject_context_qualifier: Optional[str] = Field(None)
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    qualified_predicate: Optional[str] = Field(None, description="""Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.""")
    object_aspect_qualifier: Optional[str] = Field(None)
    object_direction_qualifier: Optional[DirectionQualifierEnum] = Field(None)
    object_form_or_variant_qualifier: Optional[str] = Field(None)
    object_part_qualifier: Optional[str] = Field(None)
    object_derivative_qualifier: Optional[str] = Field(None)
    object_context_qualifier: Optional[str] = Field(None)
    causal_mechanism_qualifier: Optional[CausalMechanismQualifierEnum] = Field(None, description="""A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')""")
    anatomical_context_qualifier: Optional[AnatomicalContextQualifierEnum] = Field(None, description="""A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).""")
    species_context_qualifier: Optional[str] = Field(None, description="""A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.""")
    exact_match: Optional[List[str]] = Field(None, description="""holds between two entities that have strictly equivalent meanings, with a high degree of confidence""")
    narrow_match: Optional[List[str]] = Field(None, description="""a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.""")
    broad_match: Optional[List[str]] = Field(None, description="""a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.""")
    


class OntologyClass(ConfiguredBaseModel):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    


class Annotation(ConfiguredBaseModel):
    """
    Biolink Model root class for entity annotations.
    """
    None
    


class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    has_unit: Optional[str] = Field(None, description="""connects a quantity value to a unit""")
    has_numeric_value: Optional[float] = Field(None, description="""connects a quantity value to a number""")
    


class RelationshipQuantifier(ConfiguredBaseModel):
    
    None
    


class SensitivityQuantifier(RelationshipQuantifier):
    
    None
    


class SpecificityQuantifier(RelationshipQuantifier):
    
    None
    


class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
    """
    None
    


class FrequencyQuantifier(RelationshipQuantifier):
    
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    


class ChemicalOrDrugOrTreatment(ConfiguredBaseModel):
    
    None
    


class Entity(ConfiguredBaseModel):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:Entity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:NamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Attribute(NamedThing, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:Attribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalRole(Attribute):
    """
    	A role played by the molecular entity or part thereof within a chemical context.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ChemicalRole"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BiologicalSex(Attribute):
    
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:BiologicalSex"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:PhenotypicSex"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:GenotypicSex"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:SeverityValue"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    


class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    


class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:OrganismTaxon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Event(NamedThing):
    """
    Something that happens at a given place and time.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Event"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class AdministrativeEntity(NamedThing):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:AdministrativeEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    affiliation: Optional[List[str]] = Field(default_factory=list, description="""a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.""")
    address: Optional[str] = Field(None, description="""the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text \"blob\" containing all relevant details of the given location for fitness of purpose. For the moment, this \"address\" can include other contact details such as email and phone number(?).""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Agent"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""it is recommended that an author's 'name' property be formatted as \"surname, firstname initial.\"""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:InformationContentEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class StudyResult(InformationContentEntity):
    """
    A collection of data items from a study that are about a particular study subject or experimental unit (the  'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of this data as evidence.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:StudyResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Study(InformationContentEntity):
    """
    a detailed investigation and/or analysis
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Study"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class StudyVariable(InformationContentEntity):
    """
    a variable that is used as a measure in the investigation of a study
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:StudyVariable"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CommonDataElement(InformationContentEntity):
    """
    A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable  responses, used systematically across different sites, studies, or clinical trials to ensure consistent  data collection. Multiple CDEs (from one or more Collections) can be curated into Forms.  (https://cde.nlm.nih.gov/home)
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:CommonDataElement"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ConceptCountAnalysisResult(StudyResult):
    """
    A result of a concept count analysis.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ConceptCountAnalysisResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ObservedExpectedFrequencyAnalysisResult(StudyResult):
    """
    A result of a observed expected frequency analysis.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ObservedExpectedFrequencyAnalysisResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class RelativeFrequencyAnalysisResult(StudyResult):
    """
    A result of a relative frequency analysis.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:RelativeFrequencyAnalysisResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class TextMiningResult(StudyResult):
    """
    A result of text mining.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:TextMiningResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChiSquaredAnalysisResult(StudyResult):
    """
    A result of a chi squared analysis.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ChiSquaredAnalysisResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Dataset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:DatasetDistribution"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:DatasetVersion"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:DatasetSummary"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ConfidenceLevel"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:EvidenceType"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:InformationResource"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.
    """
    authors: Optional[List[str]] = Field(default_factory=list, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(default_factory=list, description="""When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Publication"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    authors: Optional[List[str]] = Field(default_factory=list, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(default_factory=list, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Books should have industry-standard identifier such as from ISBN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Book"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list, description="""Should generally be set to an ontology class defined term for 'book'.""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BookChapter(Publication):
    
    published_in: str = Field(None, description="""The enclosing parent book containing the chapter should have industry-standard identifier from ISBN.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    chapter: Optional[str] = Field(None, description="""chapter of a book""")
    authors: Optional[List[str]] = Field(default_factory=list, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(default_factory=list, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:BookChapter"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    iso_abbreviation: Optional[str] = Field(None, description="""Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    issue: Optional[str] = Field(None, description="""issue of a newspaper, a scientific journal or magazine for reference purpose""")
    authors: Optional[List[str]] = Field(default_factory=list, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(default_factory=list, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""Serials (journals) should have industry-standard identifier such as from ISSN.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Serial"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list, description="""Should generally be set to an ontology class defined term for 'serial' or 'journal'.""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Article(Publication):
    
    published_in: str = Field(None, description="""The enclosing parent serial containing the article should have industry-standard identifier from ISSN.""")
    iso_abbreviation: Optional[str] = Field(None, description="""Optional value, if used locally as a convenience, is set to the iso abbreviation of the 'published in' parent.""")
    volume: Optional[str] = Field(None, description="""volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication""")
    issue: Optional[str] = Field(None, description="""issue of a newspaper, a scientific journal or magazine for reference purpose""")
    authors: Optional[List[str]] = Field(default_factory=list, description="""connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as \"surname, firstname initial.\".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.""")
    pages: Optional[List[str]] = Field(default_factory=list, description="""page number of source referenced for statement or publication""")
    summary: Optional[str] = Field(None, description="""executive  summary of a publication""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""keywords tagging a publication""")
    mesh_terms: Optional[List[str]] = Field(None, description="""mesh terms tagging a publication""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Article"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PhysicalEssenceOrOccurrent(ConfiguredBaseModel):
    """
    Either a physical or processual entity.
    """
    None
    


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    None
    


class PhysicalEntity(PhysicalEssence, NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PhysicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    None
    


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    None
    


class Activity(ActivityAndBehavior, NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Activity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Procedure(ActivityAndBehavior, NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Procedure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Phenomenon(Occurrent, NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Phenomenon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Device"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SubjectOfInvestigation(ConfiguredBaseModel):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    None
    


class MaterialSample(SubjectOfInvestigation, PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MaterialSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PlanetaryEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EnvironmentalProcess(PlanetaryEntity, Occurrent):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:EnvironmentalProcess"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EnvironmentalFeature(PlanetaryEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:EnvironmentalFeature"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    latitude: Optional[float] = Field(None, description="""latitude""")
    longitude: Optional[float] = Field(None, description="""longitude""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:GeographicLocation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    latitude: Optional[float] = Field(None, description="""latitude""")
    longitude: Optional[float] = Field(None, description="""longitude""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:GeographicLocationAtTime"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ThingWithTaxon(ConfiguredBaseModel):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    


class BiologicalEntity(ThingWithTaxon, NamedThing):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:BiologicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenomicEntity(ConfiguredBaseModel):
    
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    


class EpigenomicEntity(ConfiguredBaseModel):
    
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    


class BiologicalProcessOrActivity(BiologicalEntity, Occurrent, OntologyClass):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
    """
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:BiologicalProcessOrActivity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MolecularActivity(BiologicalProcessOrActivity, Occurrent, OntologyClass):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""A chemical entity that is the input for the reaction""")
    has_output: Optional[List[str]] = Field(None, description="""A chemical entity that is the output for the reaction""")
    enabled_by: Optional[List[str]] = Field(None, description="""The gene product, gene, or complex that catalyzes the reaction""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MolecularActivity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BiologicalProcess(BiologicalProcessOrActivity, Occurrent, OntologyClass):
    """
    One or more causally connected executions of molecular functions
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:BiologicalProcess"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Pathway(BiologicalProcess, OntologyClass):
    
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Pathway"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PhysiologicalProcess(BiologicalProcess, OntologyClass):
    
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PhysiologicalProcess"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Behavior(BiologicalProcess, ActivityAndBehavior, OntologyClass):
    
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Behavior"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismAttribute(Attribute):
    """
    describes a characteristic of an organismal entity.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:OrganismAttribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PhenotypicQuality(OrganismAttribute):
    """
    A property of a phenotype
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:PhenotypicQuality"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneticInheritance(BiologicalEntity):
    """
    The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:GeneticInheritance"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismalEntity(BiologicalEntity, SubjectOfInvestigation):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:OrganismalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""may often be an organism attribute""")
    


class Virus(OrganismalEntity, SubjectOfInvestigation):
    """
    A virus is a microorganism that replicates itself as a microRNA and infects the host cell.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Virus"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CellularOrganism(OrganismalEntity, SubjectOfInvestigation):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:CellularOrganism"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:LifeStage"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class IndividualOrganism(OrganismalEntity, SubjectOfInvestigation):
    """
    An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:IndividualOrganism"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PopulationOfIndividualOrganisms(OrganismalEntity, SubjectOfInvestigation):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PopulationOfIndividualOrganisms"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class StudyPopulation(PopulationOfIndividualOrganisms):
    """
    A group of people banded together or treated as a group as participants in a research study.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:StudyPopulation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.  Please see definitions of phenotypic feature and disease in this model for their independent descriptions.  This class is helpful to enforce domains and ranges   that may involve either a disease or a phenotypic feature.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:DiseaseOrPhenotypicFeature"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Disease(DiseaseOrPhenotypicFeature):
    """
    A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Disease"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an  individual resulting from the interaction of its genotype with its molecular and physical environment.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PhenotypicFeature"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BehavioralFeature(PhenotypicFeature):
    """
    A phenotypic feature which is behavioral in nature.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:BehavioralFeature"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class AnatomicalEntity(OrganismalEntity, PhysicalEssence):
    """
    A subcellular location, cell type or gross anatomical part
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:AnatomicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:CellularComponent"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Cell(AnatomicalEntity):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Cell"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CellLine(OrganismalEntity, SubjectOfInvestigation):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:CellLine"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GrossAnatomicalStructure(AnatomicalEntity):
    
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:GrossAnatomicalStructure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalEntityOrGeneOrGeneProduct(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    None
    


class ChemicalEntityOrProteinOrPolypeptide(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    None
    


class ChemicalEntity(ChemicalEntityOrProteinOrPolypeptide, ChemicalEntityOrGeneOrGeneProduct, PhysicalEssence, NamedThing, ChemicalOrDrugOrTreatment):
    """
    A chemical entity is a physical entity that pertains to chemistry or biochemistry.
    """
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ChemicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MolecularEntity(ChemicalEntity):
    """
    A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
    """
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MolecularEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SmallMolecule(MolecularEntity):
    """
    A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).
    """
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:SmallMolecule"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ChemicalMixture"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class NucleicAcidEntity(MolecularEntity, GenomicEntity, ThingWithTaxon, PhysicalEssence, OntologyClass):
    """
    A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:NucleicAcidEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MolecularMixture"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ComplexMolecularMixture"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ProcessedMaterial"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Drug(MolecularMixture, ChemicalOrDrugOrTreatment, OntologyClass):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_supplement: Optional[str] = Field(None)
    highest_FDA_approval_status: Optional[str] = Field(None, description="""Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'""")
    drug_regulatory_status_world_wide: Optional[str] = Field(None, description="""An agglomeration of drug regulatory status worldwide. Not specific to FDA.""")
    routes_of_delivery: Optional[List[DrugDeliveryEnum]] = Field(None, description="""the method or process of administering a pharmaceutical compound to achieve a therapeutic effect in humans or animals.""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Drug"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EnvironmentalFoodContaminant(ChemicalEntity):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:EnvironmentalFoodContaminant"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class FoodAdditive(ChemicalEntity):
    
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:FoodAdditive"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Food"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MacromolecularMachineMixin(ConfiguredBaseModel):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    name: Optional[str] = Field(None, description="""genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name""")
    


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


class Gene(GeneOrGeneProduct, ChemicalEntityOrGeneOrGeneProduct, GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    symbol: Optional[str] = Field(None, description="""Symbol for a particular thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Gene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneProductMixin(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


class GeneProductIsoformMixin(GeneProductMixin):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    


class MacromolecularComplex(MacromolecularMachineMixin, BiologicalEntity):
    """
    A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MacromolecularComplex"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class NucleosomeModification(GeneProductIsoformMixin, EpigenomicEntity, GenomicEntity, BiologicalEntity):
    """
    A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:NucleosomeModification"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    


class Genome(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Genome"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Exon(NucleicAcidEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Exon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Transcript(NucleicAcidEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Transcript"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CodingSequence(NucleicAcidEntity):
    
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:CodingSequence"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Polypeptide(ChemicalEntityOrProteinOrPolypeptide, ChemicalEntityOrGeneOrGeneProduct, BiologicalEntity):
    """
    A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Polypeptide"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Protein(Polypeptide, GeneProductMixin):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Protein"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ProteinIsoform(Protein, GeneProductIsoformMixin):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ProteinIsoform"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PosttranslationalModification(GeneProductIsoformMixin, BiologicalEntity):
    """
    A chemical modification of a polypeptide or protein that occurs after translation.  e.g. polypeptide cleavage to form separate proteins, methylation or acetylation of histone tail amino acids,  protein ubiquitination.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PosttranslationalModification"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    


class NucleicAcidSequenceMotif(BiologicalEntity):
    """
    A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:NucleicAcidSequenceMotif"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class RNAProduct(Transcript, GeneProductMixin):
    
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:RNAProduct"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class RNAProductIsoform(RNAProduct, GeneProductIsoformMixin):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:RNAProductIsoform"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class NoncodingRNAProduct(RNAProduct):
    
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:NoncodingRNAProduct"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MicroRNA(NoncodingRNAProduct):
    
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:MicroRNA"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SiRNA(NoncodingRNAProduct):
    """
    A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
    """
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    is_metabolite: Optional[bool] = Field(None, description="""indicates whether a molecular entity is a metabolite""")
    trade_name: Optional[str] = Field(None)
    available_from: Optional[List[DrugAvailabilityEnum]] = Field(None)
    max_tolerated_dose: Optional[str] = Field(None, description="""The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.""")
    is_toxic: Optional[bool] = Field(None)
    has_chemical_role: Optional[List[str]] = Field(None, description="""A role is particular behaviour which a chemical entity may exhibit.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:SiRNA"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneGroupingMixin(ConfiguredBaseModel):
    """
    any grouping of multiple genes or gene products
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    


class ProteinDomain(GeneGroupingMixin, ChemicalEntityOrGeneOrGeneProduct, BiologicalEntity):
    """
    A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ProteinDomain"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ProteinFamily(GeneGroupingMixin, ChemicalEntityOrGeneOrGeneProduct, BiologicalEntity):
    
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ProteinFamily"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneFamily(GeneGroupingMixin, ChemicalEntityOrGeneOrGeneProduct, BiologicalEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:GeneFamily"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Zygosity(Attribute):
    
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:Zygosity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Genotype(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
    """
    has_zygosity: Optional[str] = Field(None)
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Genotype"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Haplotype(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Haplotype"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SequenceVariant(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.
    """
    has_gene: Optional[List[str]] = Field(None, description="""Each allele can be associated with any number of genes""")
    has_biological_sequence: Optional[str] = Field(None, description="""The state of the sequence w.r.t a reference sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:SequenceVariant"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Snv(SequenceVariant):
    """
    SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
    """
    has_gene: Optional[List[str]] = Field(None, description="""connects an entity associated with one or more genes""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Snv"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ReagentTargetedGene(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
    """
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ReagentTargetedGene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalAttribute(Attribute):
    """
    Attributes relating to a clinical manifestation
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ClinicalAttribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalMeasurement(ClinicalAttribute):
    """
    A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ClinicalMeasurement"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalModifier(ClinicalAttribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology, with respect to severity, laterality, and other aspects
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ClinicalModifier"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalCourse(ClinicalAttribute):
    """
    The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ClinicalCourse"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Onset(ClinicalCourse):
    """
    The age group in which (disease) symptom manifestations appear
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:Onset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
    """
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ClinicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalTrial(ClinicalEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ClinicalTrial"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalIntervention(ClinicalEntity):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ClinicalIntervention"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ClinicalFinding(PhenotypicFeature):
    """
    this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:ClinicalFinding"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Hospitalization(ClinicalIntervention):
    
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Hospitalization"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:SocioeconomicAttribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Case(IndividualOrganism, SubjectOfInvestigation):
    """
    An individual (human) organism that has a patient role in some clinical context.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Case"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Cohort(StudyPopulation, SubjectOfInvestigation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Cohort"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ExposureEvent(OntologyClass):
    """
    A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    


class GenomicBackgroundExposure(ExposureEvent, GeneGroupingMixin, GenomicEntity, ThingWithTaxon, PhysicalEssence, Attribute, OntologyClass):
    """
    A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:GenomicBackgroundExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PathologicalEntityMixin(ConfiguredBaseModel):
    """
    A pathological (abnormal) structure or process.
    """
    None
    


class PathologicalProcess(PathologicalEntityMixin, BiologicalProcess):
    """
    A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
    """
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    has_input: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an input into the process""")
    has_output: Optional[List[str]] = Field(None, description="""holds between a process and a continuant, where the continuant is an output of the process""")
    enabled_by: Optional[List[str]] = Field(None, description="""holds between a process and a physical entity, where the physical entity executes the process""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PathologicalProcess"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PathologicalProcessExposure(ExposureEvent, Attribute):
    """
    A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:PathologicalProcessExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PathologicalAnatomicalStructure(PathologicalEntityMixin, AnatomicalEntity):
    """
    An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:PathologicalAnatomicalStructure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PathologicalAnatomicalExposure(ExposureEvent, Attribute):
    """
    An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:PathologicalAnatomicalExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DiseaseOrPhenotypicFeatureExposure(PathologicalEntityMixin, ExposureEvent, Attribute):
    """
    A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:DiseaseOrPhenotypicFeatureExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalExposure(ExposureEvent, Attribute):
    """
    A chemical exposure is an intake of a particular chemical entity.
    """
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ChemicalExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ComplexChemicalExposure(Attribute):
    """
    A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:ComplexChemicalExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DrugExposure(ChemicalExposure, ExposureEvent):
    """
    A drug exposure is an intake of a particular drug.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:DrugExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DrugToGeneInteractionExposure(DrugExposure, GeneGroupingMixin):
    """
    drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
    """
    has_gene_or_gene_product: Optional[List[str]] = Field(None, description="""connects an entity with one or more gene or gene products""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:DrugToGeneInteractionExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class Treatment(ExposureEvent, NamedThing, ChemicalOrDrugOrTreatment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures
    """
    has_drug: Optional[List[str]] = Field(None, description="""connects an entity to one or more drugs""")
    has_device: Optional[List[str]] = Field(None, description="""connects an entity to one or more (medical) devices""")
    has_procedure: Optional[List[str]] = Field(None, description="""connects an entity to one or more (medical) procedures""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[str] = Field(["biolink:Treatment"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BioticExposure(ExposureEvent, Attribute):
    """
    An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:BioticExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EnvironmentalExposure(ExposureEvent, Attribute):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:EnvironmentalExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeographicExposure(EnvironmentalExposure, ExposureEvent):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:GeographicExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class BehavioralExposure(ExposureEvent, Attribute):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:BehavioralExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SocioeconomicExposure(ExposureEvent, Attribute):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
    """
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    has_attribute_type: str = Field(None, description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""Alternate CURIEs for a thing""")
    category: List[str] = Field(["biolink:SocioeconomicExposure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: List[str] = Field(None, description="""connects any entity to an attribute""")
    


class Outcome(ConfiguredBaseModel):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes.
    """
    None
    


class PathologicalProcessOutcome(Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of a pathological process.
    """
    None
    


class PathologicalAnatomicalOutcome(Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure.
    """
    None
    


class DiseaseOrPhenotypicFeatureOutcome(Outcome):
    """
    Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype.
    """
    None
    


class BehavioralOutcome(Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of human behavior.
    """
    None
    


class HospitalizationOutcome(Outcome):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) hospitalization.
    """
    None
    


class MortalityOutcome(Outcome):
    """
    An outcome of death from resulting from an exposure event.
    """
    None
    


class EpidemiologicalOutcome(Outcome):
    """
    An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
    """
    None
    


class SocioeconomicOutcome(Outcome):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event
    """
    None
    


class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:Association"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list, description="""rdf:type of biolink:Association should be fixed at rdf:Statement""")
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalEntityAssessesNamedThingAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalEntityAssessesNamedThingAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    subject: str = Field(None, description="""information content entity which an agent has helped realise""")
    predicate: str = Field(None, description="""generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'""")
    object: str = Field(None, description="""agent helping to realise the given entity (e.g. such as a publication)""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ContributorAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""child genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeToGenotypePartAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""the relationship type used to connect genotype to gene""")
    object: str = Field(None, description="""gene implicated in genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeToGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    subject: str = Field(None, description="""parent genotype""")
    predicate: str = Field(None, description="""the relationship type used to connect genotype to gene""")
    object: str = Field(None, description="""gene implicated in genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeToVariantAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
    """
    subject: str = Field(None, description="""the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""homology relationship type""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGeneHomologyAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneToGeneFamilyAssociation(Association):
    """
    Set membership of a gene in a family of genes related by common evolutionary ancestry usually inferred by sequence comparisons. The genes in a given family generally share common sequence motifs which generally map onto shared gene product structure-function relationships.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""membership of the gene in the given gene family.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGeneFamilyAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneExpressionMixin(ConfiguredBaseModel):
    """
    Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.
    """
    quantifier_qualifier: Optional[str] = Field(None, description="""Optional quantitative value indicating degree of expression.""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    


class GeneToGeneCoexpressionAssociation(GeneExpressionMixin, GeneToGeneAssociation):
    """
    Indicates that two genes are co-expressed, generally under the same conditions.
    """
    quantifier_qualifier: Optional[str] = Field(None, description="""A measurable quantity for the object of the association""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGeneCoexpressionAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""interaction relationship type""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:PairwiseGeneToGeneInteraction"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PairwiseMolecularInteraction(PairwiseGeneToGeneInteraction):
    """
    An interaction at the molecular level between two physical entities
    """
    interacting_molecules_category: Optional[str] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""interaction relationship type""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""identifier for the interaction. This may come from an interaction database such as IMEX.""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:PairwiseMolecularInteraction"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class CellLineToEntityAssociationMixin(ConfiguredBaseModel):
    """
    An relationship between a cell line and another entity
    """
    None
    


class ChemicalEntityToEntityAssociationMixin(ConfiguredBaseModel):
    """
    An interaction between a chemical entity and another entity
    """
    None
    


class DrugToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a drug and another entity
    """
    None
    


class ChemicalToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a chemical entity and another entity
    """
    None
    


class CaseToEntityAssociationMixin(ConfiguredBaseModel):
    """
    An abstract association for use where the case is the subject
    """
    None
    


class ChemicalToChemicalAssociation(ChemicalToEntityAssociationMixin, Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the chemical element that is the target of the statement""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalToChemicalAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ReactionToParticipantAssociation(ChemicalToChemicalAssociation):
    
    stoichiometry: Optional[int] = Field(None, description="""the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.""")
    reaction_direction: Optional[ReactionDirectionEnum] = Field(None, description="""the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)""")
    reaction_side: Optional[ReactionSideEnum] = Field(None, description="""the side of a reaction being modeled (ie: left or right)""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ReactionToParticipantAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ReactionToCatalystAssociation(ReactionToParticipantAssociation):
    
    stoichiometry: Optional[int] = Field(None, description="""the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers.""")
    reaction_direction: Optional[ReactionDirectionEnum] = Field(None, description="""the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)""")
    reaction_side: Optional[ReactionSideEnum] = Field(None, description="""the side of a reaction being modeled (ie: left or right)""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ReactionToCatalystAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    catalyst_qualifier: Optional[List[str]] = Field(None, description="""this connects the derivation edge to the chemical entity that catalyzes the reaction that causes the subject chemical to transform into the object chemical.""")
    subject: str = Field(None, description="""the upstream chemical entity""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the downstream chemical entity""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalToChemicalDerivationAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MolecularActivityToPathwayAssociation(Association):
    """
    Association that holds the relationship between a reaction and the pathway it participates in.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MolecularActivityToPathwayAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalToPathwayAssociation(ChemicalToEntityAssociationMixin, Association):
    """
    An interaction between a chemical entity and a biological process or pathway.
    """
    subject: str = Field(None, description="""the chemical entity that is affecting the pathway""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the pathway that is affected by the chemical""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalToPathwayAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class NamedThingAssociatedWithLikelihoodOfNamedThingAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:NamedThingAssociatedWithLikelihoodOfNamedThingAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalGeneInteractionAssociation(ChemicalToEntityAssociationMixin, Association):
    """
    describes a physical interaction between a chemical entity and a gene or gene product. Any biological or chemical effect resulting from such an interaction are out of scope, and covered by the ChemicalAffectsGeneAssociation type (e.g. impact of a chemical on the abundance, activity, structure, etc, of either participant in the interaction)
    """
    subject_form_or_variant_qualifier: Optional[ChemicalOrGeneOrGeneProductFormOrVariantEnum] = Field(None)
    subject_part_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    subject_derivative_qualifier: Optional[ChemicalEntityDerivativeEnum] = Field(None)
    subject_context_qualifier: Optional[str] = Field(None)
    object_form_or_variant_qualifier: Optional[ChemicalOrGeneOrGeneProductFormOrVariantEnum] = Field(None)
    object_part_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    object_context_qualifier: Optional[str] = Field(None)
    anatomical_context_qualifier: Optional[str] = Field(None, description="""A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalGeneInteractionAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalAffectsGeneAssociation(Association):
    """
    Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.)
    """
    subject_form_or_variant_qualifier: Optional[ChemicalOrGeneOrGeneProductFormOrVariantEnum] = Field(None)
    subject_part_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    subject_derivative_qualifier: Optional[ChemicalEntityDerivativeEnum] = Field(None)
    subject_aspect_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    subject_context_qualifier: Optional[str] = Field(None)
    subject_direction_qualifier: Optional[DirectionQualifierEnum] = Field(None)
    object_form_or_variant_qualifier: Optional[ChemicalOrGeneOrGeneProductFormOrVariantEnum] = Field(None)
    object_part_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    object_aspect_qualifier: Optional[GeneOrGeneProductOrChemicalPartQualifierEnum] = Field(None)
    object_context_qualifier: Optional[str] = Field(None)
    causal_mechanism_qualifier: Optional[CausalMechanismQualifierEnum] = Field(None, description="""A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')""")
    anatomical_context_qualifier: Optional[str] = Field(None, description="""A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location).""")
    qualified_predicate: Optional[str] = Field(None, description="""Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalAffectsGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DrugToGeneAssociation(DrugToEntityAssociationMixin, Association):
    """
    An interaction between a drug and a gene or gene product.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the gene or gene product that is affected by the drug""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DrugToGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MaterialSampleToEntityAssociationMixin(ConfiguredBaseModel):
    """
    An association between a material sample and something.
    """
    None
    


class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity from which it is derived.
    """
    subject: str = Field(None, description="""the material sample being described""")
    predicate: str = Field(None, description="""derivation relationship""")
    object: str = Field(None, description="""the material entity the sample was derived from. This may be another material sample, or any other material entity, including for example an organism, a geographic feature, or some environmental material.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MaterialSampleDerivationAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DiseaseToEntityAssociationMixin(ConfiguredBaseModel):
    
    None
    


class EntityToExposureEventAssociationMixin(ConfiguredBaseModel):
    """
    An association between some entity and an exposure event.
    """
    None
    


class DiseaseToExposureEventAssociation(EntityToExposureEventAssociationMixin, DiseaseToEntityAssociationMixin, Association):
    """
    An association between an exposure event and a disease.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DiseaseToExposureEventAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EntityToOutcomeAssociationMixin(ConfiguredBaseModel):
    """
    An association between some entity and an outcome
    """
    None
    


class ExposureEventToOutcomeAssociation(EntityToOutcomeAssociationMixin, Association):
    """
    An association between an exposure event and an outcome.
    """
    population_context_qualifier: Optional[str] = Field(None, description="""a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.""")
    temporal_context_qualifier: Optional[str] = Field(None, description="""a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ExposureEventToOutcomeAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class FrequencyQualifierMixin(ConfiguredBaseModel):
    """
    Qualifier for frequency type associations
    """
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class EntityToFeatureOrDiseaseQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to disease or phenotype associations.
    """
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class EntityToPhenotypicFeatureAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin, FrequencyQuantifier):
    
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class InformationContentEntityToNamedThingAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:InformationContentEntityToNamedThingAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EntityToDiseaseAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a disease
    """
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class DiseaseOrPhenotypicFeatureToEntityAssociationMixin(ConfiguredBaseModel):
    
    None
    


class DiseaseOrPhenotypicFeatureToLocationAssociation(DiseaseOrPhenotypicFeatureToEntityAssociationMixin, Association):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""anatomical entity in which the disease or feature is found.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DiseaseOrPhenotypicFeatureToLocationAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation(DiseaseOrPhenotypicFeatureToEntityAssociationMixin, Association):
    """
    An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""genetic inheritance associated with the specified disease or phenotypic feature.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EntityToDiseaseOrPhenotypicFeatureAssociationMixin(ConfiguredBaseModel):
    
    None
    


class CellLineToDiseaseOrPhenotypicFeatureAssociation(EntityToDiseaseOrPhenotypicFeatureAssociationMixin, CellLineToEntityAssociationMixin, Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalToDiseaseOrPhenotypicFeatureAssociation(EntityToDiseaseOrPhenotypicFeatureAssociationMixin, ChemicalToEntityAssociationMixin, Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the disease or phenotype that is affected by the chemical""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(EntityToDiseaseOrPhenotypicFeatureAssociationMixin, ChemicalToEntityAssociationMixin, Association):
    """
    This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary undesirable effect.
    """
    FDA_adverse_event_level: Optional[FDAIDAAdverseEventEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation(ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation, EntityToDiseaseOrPhenotypicFeatureAssociationMixin, ChemicalToEntityAssociationMixin):
    """
    This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary, typically (but not always) undesirable effect.
    """
    FDA_adverse_event_level: Optional[FDAIDAAdverseEventEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(EntityToDiseaseOrPhenotypicFeatureAssociationMixin, MaterialSampleToEntityAssociationMixin, Association):
    """
    An association between a material sample and a disease or phenotype.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GenotypeToEntityAssociationMixin(ConfiguredBaseModel):
    
    None
    


class GenotypeToPhenotypicFeatureAssociation(GenotypeToEntityAssociationMixin, EntityToPhenotypicFeatureAssociationMixin, Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    """
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""genotype that is associated with the phenotypic feature""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class ExposureEventToPhenotypicFeatureAssociation(EntityToPhenotypicFeatureAssociationMixin, Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
    """
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ExposureEventToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class DiseaseToPhenotypicFeatureAssociation(EntityToPhenotypicFeatureAssociationMixin, DiseaseToEntityAssociationMixin, Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
    """
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DiseaseToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class CaseToPhenotypicFeatureAssociation(EntityToPhenotypicFeatureAssociationMixin, CaseToEntityAssociationMixin, Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
    """
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:CaseToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class BehaviorToBehavioralFeatureAssociation(EntityToPhenotypicFeatureAssociationMixin, Association):
    """
    An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
    """
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""behavior that is the subject of the association""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""behavioral feature that is the object of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:BehaviorToBehavioralFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class GeneToEntityAssociationMixin(ConfiguredBaseModel):
    
    None
    


class GeneToPathwayAssociation(GeneToEntityAssociationMixin, Association):
    """
    An interaction between a gene or gene product and a biological process or pathway.
    """
    subject: str = Field(None, description="""the gene or gene product entity that participates or influences the pathway""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the pathway that includes or is affected by the gene or gene product""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToPathwayAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class VariantToEntityAssociationMixin(ConfiguredBaseModel):
    
    None
    


class GeneToPhenotypicFeatureAssociation(GeneToEntityAssociationMixin, EntityToPhenotypicFeatureAssociationMixin, Association):
    
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""gene in which variation is correlated with the phenotypic feature""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class GeneToDiseaseAssociation(GeneToEntityAssociationMixin, EntityToDiseaseAssociationMixin, Association):
    
    subject: str = Field(None, description="""gene in which variation is correlated with the disease, may be protective or causative or associative, or as a model""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class DruggableGeneToDiseaseAssociation(GeneToDiseaseAssociation, GeneToEntityAssociationMixin, EntityToDiseaseAssociationMixin):
    
    subject: str = Field(None, description="""gene in which variation is correlated with the disease in a protective manner, or if the product produced by the gene can be targeted by a small molecule and this leads to a protective or improving disease state.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[DruggableGeneCategoryEnum]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:DruggableGeneToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class VariantToGeneAssociation(VariantToEntityAssociationMixin, Association):
    """
    An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantToGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class VariantToGeneExpressionAssociation(VariantToGeneAssociation, GeneExpressionMixin):
    """
    An association between a variant and expression of a gene (i.e. e-QTL)
    """
    quantifier_qualifier: Optional[str] = Field(None, description="""A measurable quantity for the object of the association""")
    expression_site: Optional[str] = Field(None, description="""location in which gene or protein expression takes place. May be cell, tissue, or organ.""")
    stage_qualifier: Optional[str] = Field(None, description="""stage during which gene or protein expression of takes place.""")
    phenotypic_state: Optional[str] = Field(None, description="""in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.""")
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantToGeneExpressionAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class VariantToPopulationAssociation(VariantToEntityAssociationMixin, FrequencyQualifierMixin, Association, FrequencyQuantifier):
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
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantToPopulationAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    subject: str = Field(None, description="""the population that form the subject of the association""")
    predicate: str = Field(None, description="""A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used""")
    object: str = Field(None, description="""the population that form the object of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:PopulationToPopulationAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class VariantToPhenotypicFeatureAssociation(VariantToEntityAssociationMixin, EntityToPhenotypicFeatureAssociationMixin, Association):
    
    sex_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.""")
    subject: str = Field(None, description="""a sequence variant in which the allele state is associated in some way with the phenotype state""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    has_count: Optional[int] = Field(None, description="""number of things with a particular property""")
    has_total: Optional[int] = Field(None, description="""total number of things in a particular reference set""")
    has_quotient: Optional[float] = Field(None)
    has_percentage: Optional[float] = Field(None, description="""equivalent to has quotient multiplied by 100""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class VariantToDiseaseAssociation(VariantToEntityAssociationMixin, EntityToDiseaseAssociationMixin, Association):
    
    subject: str = Field(None, description="""a sequence variant in which the allele state is associated in some way with the disease state""")
    predicate: str = Field(None, description="""E.g. is pathogenic for""")
    object: str = Field(None, description="""a disease that is associated with that variant""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class GenotypeToDiseaseAssociation(GenotypeToEntityAssociationMixin, EntityToDiseaseAssociationMixin, Association):
    
    subject: str = Field(None, description="""a genotype that is associated in some way with a disease state""")
    predicate: str = Field(None, description="""E.g. is pathogenic for""")
    object: str = Field(None, description="""a disease that is associated with that genotype""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class ModelToDiseaseAssociationMixin(ConfiguredBaseModel):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
    """
    None
    


class GeneAsAModelOfDiseaseAssociation(ModelToDiseaseAssociationMixin, GeneToDiseaseAssociation, EntityToDiseaseAssociationMixin):
    
    subject: str = Field(None, description="""A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneAsAModelOfDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class VariantAsAModelOfDiseaseAssociation(ModelToDiseaseAssociationMixin, VariantToDiseaseAssociation, EntityToDiseaseAssociationMixin):
    
    subject: str = Field(None, description="""A variant that has a role in modeling the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:VariantAsAModelOfDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class GenotypeAsAModelOfDiseaseAssociation(ModelToDiseaseAssociationMixin, GenotypeToDiseaseAssociation, EntityToDiseaseAssociationMixin):
    
    subject: str = Field(None, description="""A genotype that has a role in modeling the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenotypeAsAModelOfDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class CellLineAsAModelOfDiseaseAssociation(ModelToDiseaseAssociationMixin, CellLineToDiseaseOrPhenotypicFeatureAssociation, EntityToDiseaseAssociationMixin):
    
    subject: str = Field(None, description="""A cell line derived from an organismal entity with a disease state that is used as a model of that disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:CellLineAsAModelOfDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class OrganismalEntityAsAModelOfDiseaseAssociation(ModelToDiseaseAssociationMixin, EntityToDiseaseAssociationMixin, Association):
    
    subject: str = Field(None, description="""A organismal entity (strain, breed) with a predisposition to a disease, or bred/created specifically to model a disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismalEntityAsAModelOfDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class OrganismToOrganismAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""An association between two individual organisms.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismToOrganismAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class TaxonToTaxonAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""An association between individuals of different taxa.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:TaxonToTaxonAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    
    subject_form_or_variant_qualifier: Optional[str] = Field(None)
    subject: str = Field(None, description="""A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneHasVariantThatContributesToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    severity_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how severe the phenotype is in the subject""")
    onset_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state when the phenotype appears is in the subject""")
    frequency_qualifier: Optional[str] = Field(None, description="""a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject""")
    


class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and a gene expression site, possibly qualified by stage/timing info.
    """
    stage_qualifier: Optional[str] = Field(None, description="""stage at which the gene is expressed in the site""")
    quantifier_qualifier: Optional[str] = Field(None, description="""can be used to indicate magnitude, or also ranking""")
    subject: str = Field(None, description="""Gene or gene product positively within the specified anatomical entity (or subclass, i.e. cellular component) location.""")
    predicate: str = Field(None, description="""expression relationship""")
    object: str = Field(None, description="""location in which the gene is expressed""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToExpressionSiteAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
    """
    subject: str = Field(None, description="""variant that modulates the treatment of some disease""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""treatment whose efficacy is modulated by the subject variant""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:SequenceVariantModulatesTreatmentAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.
    """
    subject: str = Field(None, description="""gene, product or macromolecular complex that has the function associated with the GO term""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""class describing the activity, process or localization of the gene product""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:FunctionalAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MacromolecularMachineToEntityAssociationMixin(ConfiguredBaseModel):
    """
    an association which has a macromolecular machine mixin as a subject
    """
    None
    


class MacromolecularMachineToMolecularActivityAssociation(MacromolecularMachineToEntityAssociationMixin, FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MacromolecularMachineToMolecularActivityAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MacromolecularMachineToBiologicalProcessAssociation(MacromolecularMachineToEntityAssociationMixin, FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MacromolecularMachineToBiologicalProcessAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MacromolecularMachineToCellularComponentAssociation(MacromolecularMachineToEntityAssociationMixin, FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MacromolecularMachineToCellularComponentAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MolecularActivityToChemicalEntityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MolecularActivityToChemicalEntityAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class MolecularActivityToMolecularActivityAssociation(Association):
    """
    Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:MolecularActivityToMolecularActivityAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneToGoTermAssociation(FunctionalAssociation):
    
    subject: str = Field(None, description="""gene, product or macromolecular complex that has the function associated with the GO term""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""class describing the activity, process or localization of the gene product""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGoTermAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EntityToDiseaseAssociation(Association):
    
    FDA_approval_status: Optional[FDAApprovalStatusEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:EntityToDiseaseAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class EntityToPhenotypicFeatureAssociation(Association):
    
    FDA_approval_status: Optional[FDAApprovalStatusEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:EntityToPhenotypicFeatureAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SequenceAssociation(Association):
    """
    An association between a sequence feature and a nucleic acid entity it is localized to.
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:SequenceAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


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
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GenomicSequenceLocalization"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:SequenceFeatureRelationship"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:TranscriptToGeneRelationship"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:GeneToGeneProductRelationship"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ExonToTranscriptRelationship"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation(Association):
    """
    A regulatory relationship between two genes
    """
    object_direction_qualifier: Optional[DirectionQualifierEnum] = Field(None)
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""the direction is always from regulator to regulated""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:AnatomicalEntityToAnatomicalEntityAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
    """
    subject: str = Field(None, description="""the part""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the whole""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship.
    """
    subject: str = Field(None, description="""the structure at a later time""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the structure at an earlier time""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismTaxonToEntityAssociation(ConfiguredBaseModel):
    """
    An association between an organism taxon and another entity
    """
    None
    


class OrganismTaxonToOrganismTaxonAssociation(OrganismTaxonToEntityAssociation, Association):
    """
    A relationship between two organism taxon nodes
    """
    subject: str = Field(None, description="""connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismTaxonToOrganismTaxonAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismTaxonToOrganismTaxonSpecialization(OrganismTaxonToOrganismTaxonAssociation):
    """
    A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo
    """
    subject: str = Field(None, description="""the more specific taxon""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the more general taxon""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismTaxonToOrganismTaxonSpecialization"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismTaxonToOrganismTaxonInteraction(OrganismTaxonToOrganismTaxonAssociation):
    """
    An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens
    """
    associated_environmental_context: Optional[str] = Field(None, description="""the environment in which the two taxa interact""")
    subject: str = Field(None, description="""the taxon that is the subject of the association""")
    predicate: str = Field(None, description="""A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.""")
    object: str = Field(None, description="""the taxon that is the subject of the association""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismTaxonToOrganismTaxonInteraction"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    


class OrganismTaxonToEnvironmentAssociation(OrganismTaxonToEntityAssociation, Association):
    
    subject: str = Field(None, description="""the taxon that is the subject of the association""")
    predicate: str = Field(None, description="""predicate describing the relationship between the taxon and the environment""")
    object: str = Field(None, description="""the environment in which the organism occurs""")
    negated: Optional[bool] = Field(None, description="""if set to true, then the association is negated i.e. is not true""")
    qualifiers: Optional[List[str]] = Field(default_factory=list, description="""connects an association to qualifiers that modify or qualify the meaning of that association""")
    publications: Optional[List[str]] = Field(default_factory=list, description="""One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.""")
    has_evidence: Optional[List[str]] = Field(None, description="""connects an association to an instance of supporting evidence""")
    knowledge_source: Optional[str] = Field(None, description="""An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.""")
    primary_knowledge_source: Optional[str] = Field(None, description="""The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  \"aggregator knowledge source\" can be used to caputre non-primary sources.""")
    aggregator_knowledge_source: Optional[List[str]] = Field(None, description="""An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.""")
    timepoint: Optional[str] = Field(None, description="""a point in time""")
    original_subject: Optional[str] = Field(None, description="""used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_predicate: Optional[str] = Field(None, description="""used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.""")
    original_object: Optional[str] = Field(None, description="""used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.""")
    id: str = Field(None, description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: Optional[List[str]] = Field(["biolink:OrganismTaxonToEnvironmentAssociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
MappingCollection.update_forward_refs()
PredicateMapping.update_forward_refs()
OntologyClass.update_forward_refs()
Annotation.update_forward_refs()
QuantityValue.update_forward_refs()
RelationshipQuantifier.update_forward_refs()
SensitivityQuantifier.update_forward_refs()
SpecificityQuantifier.update_forward_refs()
PathognomonicityQuantifier.update_forward_refs()
FrequencyQuantifier.update_forward_refs()
ChemicalOrDrugOrTreatment.update_forward_refs()
Entity.update_forward_refs()
NamedThing.update_forward_refs()
Attribute.update_forward_refs()
ChemicalRole.update_forward_refs()
BiologicalSex.update_forward_refs()
PhenotypicSex.update_forward_refs()
GenotypicSex.update_forward_refs()
SeverityValue.update_forward_refs()
RelationshipType.update_forward_refs()
TaxonomicRank.update_forward_refs()
OrganismTaxon.update_forward_refs()
Event.update_forward_refs()
AdministrativeEntity.update_forward_refs()
Agent.update_forward_refs()
InformationContentEntity.update_forward_refs()
StudyResult.update_forward_refs()
Study.update_forward_refs()
StudyVariable.update_forward_refs()
CommonDataElement.update_forward_refs()
ConceptCountAnalysisResult.update_forward_refs()
ObservedExpectedFrequencyAnalysisResult.update_forward_refs()
RelativeFrequencyAnalysisResult.update_forward_refs()
TextMiningResult.update_forward_refs()
ChiSquaredAnalysisResult.update_forward_refs()
Dataset.update_forward_refs()
DatasetDistribution.update_forward_refs()
DatasetVersion.update_forward_refs()
DatasetSummary.update_forward_refs()
ConfidenceLevel.update_forward_refs()
EvidenceType.update_forward_refs()
InformationResource.update_forward_refs()
Publication.update_forward_refs()
Book.update_forward_refs()
BookChapter.update_forward_refs()
Serial.update_forward_refs()
Article.update_forward_refs()
PhysicalEssenceOrOccurrent.update_forward_refs()
PhysicalEssence.update_forward_refs()
PhysicalEntity.update_forward_refs()
Occurrent.update_forward_refs()
ActivityAndBehavior.update_forward_refs()
Activity.update_forward_refs()
Procedure.update_forward_refs()
Phenomenon.update_forward_refs()
Device.update_forward_refs()
SubjectOfInvestigation.update_forward_refs()
MaterialSample.update_forward_refs()
PlanetaryEntity.update_forward_refs()
EnvironmentalProcess.update_forward_refs()
EnvironmentalFeature.update_forward_refs()
GeographicLocation.update_forward_refs()
GeographicLocationAtTime.update_forward_refs()
ThingWithTaxon.update_forward_refs()
BiologicalEntity.update_forward_refs()
GenomicEntity.update_forward_refs()
EpigenomicEntity.update_forward_refs()
BiologicalProcessOrActivity.update_forward_refs()
MolecularActivity.update_forward_refs()
BiologicalProcess.update_forward_refs()
Pathway.update_forward_refs()
PhysiologicalProcess.update_forward_refs()
Behavior.update_forward_refs()
OrganismAttribute.update_forward_refs()
PhenotypicQuality.update_forward_refs()
GeneticInheritance.update_forward_refs()
OrganismalEntity.update_forward_refs()
Virus.update_forward_refs()
CellularOrganism.update_forward_refs()
LifeStage.update_forward_refs()
IndividualOrganism.update_forward_refs()
PopulationOfIndividualOrganisms.update_forward_refs()
StudyPopulation.update_forward_refs()
DiseaseOrPhenotypicFeature.update_forward_refs()
Disease.update_forward_refs()
PhenotypicFeature.update_forward_refs()
BehavioralFeature.update_forward_refs()
AnatomicalEntity.update_forward_refs()
CellularComponent.update_forward_refs()
Cell.update_forward_refs()
CellLine.update_forward_refs()
GrossAnatomicalStructure.update_forward_refs()
ChemicalEntityOrGeneOrGeneProduct.update_forward_refs()
ChemicalEntityOrProteinOrPolypeptide.update_forward_refs()
ChemicalEntity.update_forward_refs()
MolecularEntity.update_forward_refs()
SmallMolecule.update_forward_refs()
ChemicalMixture.update_forward_refs()
NucleicAcidEntity.update_forward_refs()
MolecularMixture.update_forward_refs()
ComplexMolecularMixture.update_forward_refs()
ProcessedMaterial.update_forward_refs()
Drug.update_forward_refs()
EnvironmentalFoodContaminant.update_forward_refs()
FoodAdditive.update_forward_refs()
Food.update_forward_refs()
MacromolecularMachineMixin.update_forward_refs()
GeneOrGeneProduct.update_forward_refs()
Gene.update_forward_refs()
GeneProductMixin.update_forward_refs()
GeneProductIsoformMixin.update_forward_refs()
MacromolecularComplex.update_forward_refs()
NucleosomeModification.update_forward_refs()
Genome.update_forward_refs()
Exon.update_forward_refs()
Transcript.update_forward_refs()
CodingSequence.update_forward_refs()
Polypeptide.update_forward_refs()
Protein.update_forward_refs()
ProteinIsoform.update_forward_refs()
PosttranslationalModification.update_forward_refs()
NucleicAcidSequenceMotif.update_forward_refs()
RNAProduct.update_forward_refs()
RNAProductIsoform.update_forward_refs()
NoncodingRNAProduct.update_forward_refs()
MicroRNA.update_forward_refs()
SiRNA.update_forward_refs()
GeneGroupingMixin.update_forward_refs()
ProteinDomain.update_forward_refs()
ProteinFamily.update_forward_refs()
GeneFamily.update_forward_refs()
Zygosity.update_forward_refs()
Genotype.update_forward_refs()
Haplotype.update_forward_refs()
SequenceVariant.update_forward_refs()
Snv.update_forward_refs()
ReagentTargetedGene.update_forward_refs()
ClinicalAttribute.update_forward_refs()
ClinicalMeasurement.update_forward_refs()
ClinicalModifier.update_forward_refs()
ClinicalCourse.update_forward_refs()
Onset.update_forward_refs()
ClinicalEntity.update_forward_refs()
ClinicalTrial.update_forward_refs()
ClinicalIntervention.update_forward_refs()
ClinicalFinding.update_forward_refs()
Hospitalization.update_forward_refs()
SocioeconomicAttribute.update_forward_refs()
Case.update_forward_refs()
Cohort.update_forward_refs()
ExposureEvent.update_forward_refs()
GenomicBackgroundExposure.update_forward_refs()
PathologicalEntityMixin.update_forward_refs()
PathologicalProcess.update_forward_refs()
PathologicalProcessExposure.update_forward_refs()
PathologicalAnatomicalStructure.update_forward_refs()
PathologicalAnatomicalExposure.update_forward_refs()
DiseaseOrPhenotypicFeatureExposure.update_forward_refs()
ChemicalExposure.update_forward_refs()
ComplexChemicalExposure.update_forward_refs()
DrugExposure.update_forward_refs()
DrugToGeneInteractionExposure.update_forward_refs()
Treatment.update_forward_refs()
BioticExposure.update_forward_refs()
EnvironmentalExposure.update_forward_refs()
GeographicExposure.update_forward_refs()
BehavioralExposure.update_forward_refs()
SocioeconomicExposure.update_forward_refs()
Outcome.update_forward_refs()
PathologicalProcessOutcome.update_forward_refs()
PathologicalAnatomicalOutcome.update_forward_refs()
DiseaseOrPhenotypicFeatureOutcome.update_forward_refs()
BehavioralOutcome.update_forward_refs()
HospitalizationOutcome.update_forward_refs()
MortalityOutcome.update_forward_refs()
EpidemiologicalOutcome.update_forward_refs()
SocioeconomicOutcome.update_forward_refs()
Association.update_forward_refs()
ChemicalEntityAssessesNamedThingAssociation.update_forward_refs()
ContributorAssociation.update_forward_refs()
GenotypeToGenotypePartAssociation.update_forward_refs()
GenotypeToGeneAssociation.update_forward_refs()
GenotypeToVariantAssociation.update_forward_refs()
GeneToGeneAssociation.update_forward_refs()
GeneToGeneHomologyAssociation.update_forward_refs()
GeneToGeneFamilyAssociation.update_forward_refs()
GeneExpressionMixin.update_forward_refs()
GeneToGeneCoexpressionAssociation.update_forward_refs()
PairwiseGeneToGeneInteraction.update_forward_refs()
PairwiseMolecularInteraction.update_forward_refs()
CellLineToEntityAssociationMixin.update_forward_refs()
ChemicalEntityToEntityAssociationMixin.update_forward_refs()
DrugToEntityAssociationMixin.update_forward_refs()
ChemicalToEntityAssociationMixin.update_forward_refs()
CaseToEntityAssociationMixin.update_forward_refs()
ChemicalToChemicalAssociation.update_forward_refs()
ReactionToParticipantAssociation.update_forward_refs()
ReactionToCatalystAssociation.update_forward_refs()
ChemicalToChemicalDerivationAssociation.update_forward_refs()
MolecularActivityToPathwayAssociation.update_forward_refs()
ChemicalToPathwayAssociation.update_forward_refs()
NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.update_forward_refs()
ChemicalGeneInteractionAssociation.update_forward_refs()
ChemicalAffectsGeneAssociation.update_forward_refs()
DrugToGeneAssociation.update_forward_refs()
MaterialSampleToEntityAssociationMixin.update_forward_refs()
MaterialSampleDerivationAssociation.update_forward_refs()
DiseaseToEntityAssociationMixin.update_forward_refs()
EntityToExposureEventAssociationMixin.update_forward_refs()
DiseaseToExposureEventAssociation.update_forward_refs()
EntityToOutcomeAssociationMixin.update_forward_refs()
ExposureEventToOutcomeAssociation.update_forward_refs()
FrequencyQualifierMixin.update_forward_refs()
EntityToFeatureOrDiseaseQualifiersMixin.update_forward_refs()
EntityToPhenotypicFeatureAssociationMixin.update_forward_refs()
InformationContentEntityToNamedThingAssociation.update_forward_refs()
EntityToDiseaseAssociationMixin.update_forward_refs()
DiseaseOrPhenotypicFeatureToEntityAssociationMixin.update_forward_refs()
DiseaseOrPhenotypicFeatureToLocationAssociation.update_forward_refs()
DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.update_forward_refs()
EntityToDiseaseOrPhenotypicFeatureAssociationMixin.update_forward_refs()
CellLineToDiseaseOrPhenotypicFeatureAssociation.update_forward_refs()
ChemicalToDiseaseOrPhenotypicFeatureAssociation.update_forward_refs()
ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.update_forward_refs()
ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.update_forward_refs()
MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.update_forward_refs()
GenotypeToEntityAssociationMixin.update_forward_refs()
GenotypeToPhenotypicFeatureAssociation.update_forward_refs()
ExposureEventToPhenotypicFeatureAssociation.update_forward_refs()
DiseaseToPhenotypicFeatureAssociation.update_forward_refs()
CaseToPhenotypicFeatureAssociation.update_forward_refs()
BehaviorToBehavioralFeatureAssociation.update_forward_refs()
GeneToEntityAssociationMixin.update_forward_refs()
GeneToPathwayAssociation.update_forward_refs()
VariantToEntityAssociationMixin.update_forward_refs()
GeneToPhenotypicFeatureAssociation.update_forward_refs()
GeneToDiseaseAssociation.update_forward_refs()
DruggableGeneToDiseaseAssociation.update_forward_refs()
VariantToGeneAssociation.update_forward_refs()
VariantToGeneExpressionAssociation.update_forward_refs()
VariantToPopulationAssociation.update_forward_refs()
PopulationToPopulationAssociation.update_forward_refs()
VariantToPhenotypicFeatureAssociation.update_forward_refs()
VariantToDiseaseAssociation.update_forward_refs()
GenotypeToDiseaseAssociation.update_forward_refs()
ModelToDiseaseAssociationMixin.update_forward_refs()
GeneAsAModelOfDiseaseAssociation.update_forward_refs()
VariantAsAModelOfDiseaseAssociation.update_forward_refs()
GenotypeAsAModelOfDiseaseAssociation.update_forward_refs()
CellLineAsAModelOfDiseaseAssociation.update_forward_refs()
OrganismalEntityAsAModelOfDiseaseAssociation.update_forward_refs()
OrganismToOrganismAssociation.update_forward_refs()
TaxonToTaxonAssociation.update_forward_refs()
GeneHasVariantThatContributesToDiseaseAssociation.update_forward_refs()
GeneToExpressionSiteAssociation.update_forward_refs()
SequenceVariantModulatesTreatmentAssociation.update_forward_refs()
FunctionalAssociation.update_forward_refs()
MacromolecularMachineToEntityAssociationMixin.update_forward_refs()
MacromolecularMachineToMolecularActivityAssociation.update_forward_refs()
MacromolecularMachineToBiologicalProcessAssociation.update_forward_refs()
MacromolecularMachineToCellularComponentAssociation.update_forward_refs()
MolecularActivityToChemicalEntityAssociation.update_forward_refs()
MolecularActivityToMolecularActivityAssociation.update_forward_refs()
GeneToGoTermAssociation.update_forward_refs()
EntityToDiseaseAssociation.update_forward_refs()
EntityToPhenotypicFeatureAssociation.update_forward_refs()
SequenceAssociation.update_forward_refs()
GenomicSequenceLocalization.update_forward_refs()
SequenceFeatureRelationship.update_forward_refs()
TranscriptToGeneRelationship.update_forward_refs()
GeneToGeneProductRelationship.update_forward_refs()
ExonToTranscriptRelationship.update_forward_refs()
ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.update_forward_refs()
AnatomicalEntityToAnatomicalEntityAssociation.update_forward_refs()
AnatomicalEntityToAnatomicalEntityPartOfAssociation.update_forward_refs()
AnatomicalEntityToAnatomicalEntityOntogenicAssociation.update_forward_refs()
OrganismTaxonToEntityAssociation.update_forward_refs()
OrganismTaxonToOrganismTaxonAssociation.update_forward_refs()
OrganismTaxonToOrganismTaxonSpecialization.update_forward_refs()
OrganismTaxonToOrganismTaxonInteraction.update_forward_refs()
OrganismTaxonToEnvironmentAssociation.update_forward_refs()

