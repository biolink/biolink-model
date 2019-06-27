
# Class: population of individual organisms


A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

URI: [biolink:PopulationOfIndividualOrganisms](https://w3id.org/biolink/vocab/PopulationOfIndividualOrganisms)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[PopulationOfIndividualOrganisms|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[PopulationToPopulationAssociation]-%20object%201..1>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20subject%201..1>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20object%201..1>\[PopulationOfIndividualOrganisms],%20\[PopulationOfIndividualOrganisms]uses%20-.->\[ThingWithTaxon],%20\[OrganismalEntity]^-\[PopulationOfIndividualOrganisms])

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon

## Referenced by class

 *  **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[object](population_to_population_association_object.md)*  <sub>REQ</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[subject](population_to_population_association_subject.md)*  <sub>REQ</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[object](variant_to_population_association_object.md)*  <sub>REQ</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)
