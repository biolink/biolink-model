
# Class: clinical entity


Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities

URI: [biolink:ClinicalEntity](https://w3id.org/biolink/vocab/ClinicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalEntity|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[ClinicalTrial],%20\[ClinicalEntity]^-\[ClinicalIntervention],%20\[NamedThing]^-\[ClinicalEntity])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ClinicalIntervention](ClinicalIntervention.md)
 * [ClinicalTrial](ClinicalTrial.md)

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
