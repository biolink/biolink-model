# Class: gene family


any grouping of multiple genes or gene products related by common descent

URI: [http://bioentity.io/vocab/GeneFamily](http://bioentity.io/vocab/GeneFamily)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneFamily|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;isa_partof_closure_label(i):string%20*;regulates_closure_label(i):string%20*]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[GeneFamily]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[GeneFamily]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[GeneFamily]-%20regulates%20closure(i)%20*>\[RelationshipType],%20\[GeneFamily]-%20isa%20partof%20closure(i)%20*>\[OntologyClass],%20\[GeneFamily]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[GeneFamily]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneFamily]uses%20-.->\[GeneGrouping],%20\[MolecularEntity]^-\[GeneFamily])
## Mappings

 * [SIO:001380](http://semanticscience.org/resource/SIO_001380)
 * [NCIT:C20130](http://purl.obolibrary.org/obo/NCIT_C20130)
 * [WD:Q417841](http://purl.obolibrary.org/obo/WD_Q417841)
## Inheritance

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
 *  mixin: [GeneGrouping](GeneGrouping.md) - any grouping of multiple genes or gene products
## Children

## Fields

 * [biomarker for](biomarker_for.md) *subsets*: (translator_minimal)
    * Description: holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [in taxon](in_taxon.md) *subsets*: (translator_minimal)
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [isa partof closure](isa_partof_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [isa partof closure label](isa_partof_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: **string***
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)
    * Description: holds between two entities that make physical contact as part of some interaction
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [regulates closure](regulates_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
    * range: [RelationshipType](RelationshipType.md)*
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [regulates closure label](regulates_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: **string***
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [regulates, entity to entity](regulates_entity_to_entity.md) *subsets*: (translator_minimal)
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
