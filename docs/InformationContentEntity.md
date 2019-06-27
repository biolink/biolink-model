
# Class: information content entity


a piece of information that typically describes some piece of biology or is used as support.

URI: [biolink:InformationContentEntity](https://w3id.org/biolink/vocab/InformationContentEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[InformationContentEntity|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[Publication],%20\[InformationContentEntity]^-\[EvidenceType],%20\[InformationContentEntity]^-\[ConfidenceLevel],%20\[NamedThing]^-\[InformationContentEntity])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
 * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
 * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.

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
