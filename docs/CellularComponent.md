
# Type: cellular component


A location in or around a cell

URI: [biolink:CellularComponent](https://w3id.org/biolink/vocab/CellularComponent)


![img](images/CellularComponent.svg)

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part

## Referenced by class

 *  **[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)** *[macromolecular machine to cellular component association➞object](macromolecular_machine_to_cellular_component_association_object.md)*  <sub>REQ</sub>  **[CellularComponent](CellularComponent.md)**

## Attributes


### Inherited from anatomical entity:

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
| **Mappings:** | | GO:0005575 |
|  | | SIO:001400 |
|  | | WIKIDATA:Q5058355 |
|  | | UMLSSC:T026 |
|  | | UMLSST:celc |

