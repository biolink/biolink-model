
# Class: organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [biolink:OrganismalEntity](https://w3id.org/biolink/vocab/OrganismalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[PopulationOfIndividualOrganisms],%20\[OrganismalEntity]^-\[LifeStage],%20\[OrganismalEntity]^-\[IndividualOrganism],%20\[OrganismalEntity]^-\[Biosample],%20\[OrganismalEntity]^-\[AnatomicalEntity],%20\[BiologicalEntity]^-\[OrganismalEntity])

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Children

 * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
 * [Biosample](Biosample.md)
 * [IndividualOrganism](IndividualOrganism.md)
 * [LifeStage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

## Referenced by class


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
