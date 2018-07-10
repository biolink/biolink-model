# Class: population of individual organisms




URI: [http://bioentity.io/vocab/PopulationOfIndividualOrganisms](http://bioentity.io/vocab/PopulationOfIndividualOrganisms)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PopulationOfIndividualOrganisms|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;uri(i):uri%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PopulationOfIndividualOrganisms]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[PopulationToPopulationAssociation]-%20object(i)>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20subject(i)>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20object(i)>\[PopulationOfIndividualOrganisms],%20\[PopulationOfIndividualOrganisms]uses%20-.->\[ThingWithTaxon],%20\[OrganismalEntity]^-\[PopulationOfIndividualOrganisms])
## Mappings

 * [SIO:001061](http://semanticscience.org/resource/SIO_001061)
 * [PCO:0000001](http://purl.obolibrary.org/obo/PCO_0000001)
## Inheritance

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

## Used in

 *  class: **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[population to population association.object](population_to_population_association_object.md)* **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  class: **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[population to population association.subject](population_to_population_association_subject.md)* **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  class: **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association.object](variant_to_population_association_object.md)* **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
## Fields

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
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [uri](uri.md)
    * Description: URI expansion of CURIE
    * range: [uri](uri.md)
    * inherited from: [NamedThing](NamedThing.md)
