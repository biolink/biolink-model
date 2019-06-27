
# Class: biological sex




URI: [biolink:BiologicalSex](https://w3id.org/biolink/vocab/BiologicalSex)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EntityToPhenotypicFeatureAssociation]-%20sex%20qualifier%200..1>\[BiologicalSex|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[BiologicalSex]^-\[PhenotypicSex],%20\[BiologicalSex]^-\[GenotypicSex],%20\[Attribute]^-\[BiologicalSex])

## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity

## Children

 * [GenotypicSex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
 * [PhenotypicSex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.

## Referenced by class

 *  **[EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)** *[sex qualifier](sex_qualifier.md)*  <sub>OPT</sub>  **[BiologicalSex](BiologicalSex.md)**

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
