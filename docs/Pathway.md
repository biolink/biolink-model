
# Type: pathway




URI: [biolink:Pathway](https://w3id.org/biolink/vocab/Pathway)


![img](images/Pathway.svg)

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

## Referenced by class

 *  **[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)** *[chemical to pathway association➞object](chemical_to_pathway_association_object.md)*  <sub>REQ</sub>  **[Pathway](Pathway.md)**

## Attributes


### Inherited from biological process:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an output of the process
    * range: [NamedThing](NamedThing.md)
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
| **Mappings:** | | GO:0007165 |
|  | | SIO:010526 |
|  | | PW:0000001 |
|  | | WIKIDATA:Q4915012 |

