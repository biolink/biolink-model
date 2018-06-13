# Class: occurrent


A processual entity

URI: [http://bioentity.io/vocab/Occurrent](http://bioentity.io/vocab/Occurrent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent|has_participant:string%20%3F;has_input:string%20%3F]-%20precedes%20%3F>\[Occurrent],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[NamedThing]-%20actively%20involved%20in(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20capable%20of(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20participates%20in(i)%20%3F>\[Occurrent],%20\[Occurrent]-%20precedes%20%3F>\[Occurrent],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[MolecularActivity]uses%20-.->\[Occurrent],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[Occurrent]^-\[Procedure],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[ActivityAndBehavior])
## Mappings

 * [BFO:0000003](http://purl.obolibrary.org/obo/BFO_0000003)
## Inheritance

## Children

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [EnvironmentalProcess](EnvironmentalProcess.md) (mixin) 
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.
## Used in

 *  class: **[NamedThing](NamedThing.md)** *[actively involved in](actively_involved_in.md)* **[Occurrent](Occurrent.md)**
 *  class: **[NamedThing](NamedThing.md)** *[capable of](capable_of.md)* **[Occurrent](Occurrent.md)**
 *  class: **[NamedThing](NamedThing.md)** *[participates in](participates_in.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[precedes](precedes.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[regulates, process to process](regulates_process_to_process.md)* **[Occurrent](Occurrent.md)**
## Fields

 * _[has input](has_input.md) *subsets*: (translator_minimal)_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: **string**
    * __Local__
 * _[has participant](has_participant.md) *subsets*: (translator_minimal)_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: **string**
    * __Local__
 * _[precedes](precedes.md) *subsets*: (translator_minimal)_
    * _holds between two processes, where one completes before the other begins_
    * range: [Occurrent](Occurrent.md)
    * __Local__
 * _[regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: [Occurrent](Occurrent.md)
    * __Local__
