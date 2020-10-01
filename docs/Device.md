
# Type: device


A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment

URI: [biolink:Device](https://w3id.org/biolink/vocab/Device)


![img](images/Device.svg)

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Attributes


### Inherited from named thing:

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
| **Mappings:** | | UMLSSG:DEVI |
|  | | UMLSSC:T074 |
|  | | UMLSST:medd |
|  | | UMLSSC:T075 |
|  | | UMLSST:resd |
|  | | UMLSSC:T203 |
|  | | UMLSST:drdd |

