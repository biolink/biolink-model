
# Type: confidence level


Level of confidence in a statement

URI: [biolink:ConfidenceLevel](https://w3id.org/biolink/vocab/ConfidenceLevel)


![img](images/ConfidenceLevel.svg)

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.

## Referenced by class

 *  **[Association](Association.md)** *[has confidence level](has_confidence_level.md)*  <sub>OPT</sub>  **[ConfidenceLevel](ConfidenceLevel.md)**

## Attributes


### Inherited from information content entity:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | CIO:0000028 |
|  | | SEPIO:0000167 |
|  | | SEPIO:0000187 |

