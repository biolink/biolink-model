
# Class: frequency value


describes the frequency of occurrence of an event or condition

URI: [biolink:FrequencyValue](https://w3id.org/biolink/vocab/FrequencyValue)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FrequencyQualifierMixin]-%20frequency%20qualifier%200..1>\[FrequencyValue|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[Attribute]^-\[FrequencyValue])

## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity

## Referenced by class

 *  **[FrequencyQualifierMixin](FrequencyQualifierMixin.md)** *[frequency qualifier](frequency_qualifier.md)*  <sub>OPT</sub>  **[FrequencyValue](FrequencyValue.md)**

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
