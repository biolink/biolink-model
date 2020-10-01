
# Type: physiological process




URI: [biolink:PhysiologicalProcess](https://w3id.org/biolink/vocab/PhysiologicalProcess)


![img](images/PhysiologicalProcess.svg)

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

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
| **Aliases:** | | physiology |
| **Mappings:** | | UMLSSG:PHYS |
|  | | UMLSSC:T032 |
|  | | UMLSST:orga |
|  | | UMLSSC:T039 |
|  | | UMLSST:phsf |
|  | | UMLSSC:T040 |
|  | | UMLSST:orgf |
|  | | UMLSSC:T041 |
|  | | UMLSST:menp |
|  | | UMLSSC:T042 |
|  | | UMLSST:ortf |
|  | | UMLSSC:T043 |
|  | | UMLSST:celf |
|  | | UMLSSC:T045 |
|  | | UMLSST:genf |
|  | | UMLSSC:T201 |
|  | | UMLSST:clna |

