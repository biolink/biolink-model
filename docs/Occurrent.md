
# Class: occurrent


A processual entity

URI: [biolink:Occurrent](https://w3id.org/biolink/vocab/Occurrent)

![img](images/Occurrent.png)

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner

## Mixin for

 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) (mixin)  - Either an individual molecular activity, or a collection of causally connected molecular activities
 * [EnvironmentalProcess](EnvironmentalProcess.md) (mixin) 
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[actively involved in](actively_involved_in.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[capable of](capable_of.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[negatively regulates, process to process](negatively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[participates in](participates_in.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[positively regulates, process to process](positively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[precedes](precedes.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[regulates, process to process](regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**

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

### Domain for slot:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)
    * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an output of the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [has participant](has_participant.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [negatively regulates, process to process](negatively_regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [Occurrent](Occurrent.md)
 * [positively regulates, process to process](positively_regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [Occurrent](Occurrent.md)
 * [precedes](precedes.md)  <sub>0..*</sub>
    * Description: holds between two processes, where one completes before the other begins
    * range: [Occurrent](Occurrent.md)
    * in subsets: (translator_minimal)
 * [regulates, process to process](regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [Occurrent](Occurrent.md)
