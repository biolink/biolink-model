
# Type: source file




URI: [biolink:SourceFile](https://w3id.org/biolink/vocab/SourceFile)


![img](images/SourceFile.svg)

## Parents

 *  is_a: [DataFile](DataFile.md)

## Referenced by class


## Attributes


### Own

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from data file:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
