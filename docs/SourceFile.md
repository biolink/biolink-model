---
parent: "Browse the BioLink Model"
---


# Class: source file




URI: [biolink:SourceFile](https://w3id.org/biolink/vocab/SourceFile)

![img](images/SourceFile.png)

## Parents

 *  is_a: [DataFile](DataFile.md)

## Referenced by class


## Attributes


### Own

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](String.md)

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

### Domain for slot:

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](String.md)
