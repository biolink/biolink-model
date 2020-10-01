
# Type: publication


Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.

URI: [biolink:Publication](https://w3id.org/biolink/vocab/Publication)


![img](images/Publication.svg)

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.

## Referenced by class

 *  **[Association](Association.md)** *[publications](publications.md)*  <sub>0..*</sub>  **[Publication](Publication.md)**

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
| **Mappings:** | | IAO:0000311 |
|  | | IAO:0000013 |
|  | | UMLSSC:T170 |
|  | | UMLSST:inpr |

