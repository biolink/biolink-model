# Class: occurrent


A processual entity

URI: [http://bioentity.io/vocab/Occurrent](http://bioentity.io/vocab/Occurrent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent|has_participant:string%20%3F;has_input:string%20%3F]^-\[ActivityAndBehavior],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[Procedure],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[Occurrent]-%20precedes%20%3F>\[Occurrent])
## Mappings

 * [BFO:0000003](http://purl.obolibrary.org/obo/BFO_0000003)
## Inheritance

## Children

 *  child: [activity and behavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 *  child: [procedure](Procedure.md) - A series of actions conducted in a certain order or manner
 *  child: [phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 *  mixin: [biological process](BiologicalProcess.md) - One or more causally connected executions of molecular functions
 *  mixin: [molecular activity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.
 *  mixin: [environmental process](EnvironmentalProcess.md)
## Used in

 *  class: [occurrent](Occurrent.md) references: [activity and behavior](ActivityAndBehavior.md)
 *  class: [occurrent](Occurrent.md) references: [procedure](Procedure.md)
 *  class: [occurrent](Occurrent.md) references: [molecular activity](MolecularActivity.md)
 *  class: [occurrent](Occurrent.md) references: [phenomenon](Phenomenon.md)
 *  class: [occurrent](Occurrent.md) references: [biological process](BiologicalProcess.md)
 *  class: [occurrent](Occurrent.md) references: [environmental process](EnvironmentalProcess.md)
## Fields

 * _[regulates, process to process](regulates_process_to_process.md)_
    * range: [occurrent](Occurrent.md)
    * __Local__
 * _[has participant](has_participant.md) *subsets: translator_minimal*_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: string
    * __Local__
 * _[has input](has_input.md) *subsets: translator_minimal*_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: string
    * __Local__
 * _[precedes](precedes.md) *subsets: translator_minimal*_
    * _holds between two processes, where one completes before the other begins_
    * range: [occurrent](Occurrent.md)
    * __Local__
