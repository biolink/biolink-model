# Class: occurrent


A processual entity

URI: [http://bioentity.io/vocab/Occurrent](http://bioentity.io/vocab/Occurrent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent|has_participant:string%20%3F;has_input:string%20%3F]-%20precedes%20%3F>\[Occurrent],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[Occurrent]-%20precedes%20%3F>\[Occurrent],%20\[NamedThing]-%20capable%20of(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20participates%20in(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20actively%20involved%20in(i)%20%3F>\[Occurrent],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[MolecularActivity]uses%20-.->\[Occurrent],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[Occurrent]^-\[Procedure],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[ActivityAndBehavior])
## Mappings

 * [BFO:0000003](http://purl.obolibrary.org/obo/BFO_0000003)
## Inheritance

## Children

 * activity and behavior
 * phenomenon
 * procedure
 * biological process
 * environmental process
 * molecular activity
## Used in

 *  class: **named thing** *actively involved in* **occurrent**
 *  class: **named thing** *capable of* **occurrent**
 *  class: **named thing** *participates in* **occurrent**
 *  class: **occurrent** *precedes* **occurrent**
 *  class: **occurrent** *regulates, process to process* **occurrent**
## Fields

 * _has input_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: **string**
    * __Local__
 * _has participant_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: **string**
    * __Local__
 * _precedes_
    * _holds between two processes, where one completes before the other begins_
    * range: occurrent
    * __Local__
 * _regulates, process to process_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: occurrent
    * __Local__
