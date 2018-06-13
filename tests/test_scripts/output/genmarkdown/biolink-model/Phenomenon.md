# Class: phenomenon


a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

URI: [http://bioentity.io/vocab/Phenomenon](http://bioentity.io/vocab/Phenomenon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Phenomenon|has_participant(i):string%20%3F;has_input(i):string%20%3F]-%20precedes(i)%20%3F>\[Occurrent],%20\[Phenomenon]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[Occurrent]^-\[Phenomenon])
## Mappings

 * [UMLSSG:PHEN](http://purl.obolibrary.org/obo/UMLSSG_PHEN)
## Inheritance

 *  is_a: [Occurrent](Occurrent.md) - A processual entity
## Children

## Fields

 * _[has input](has_input.md) *subsets*: (translator_minimal)_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: **string**
    * inherited from: [Occurrent](Occurrent.md)
 * _[has participant](has_participant.md) *subsets*: (translator_minimal)_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: **string**
    * inherited from: [Occurrent](Occurrent.md)
 * _[precedes](precedes.md) *subsets*: (translator_minimal)_
    * _holds between two processes, where one completes before the other begins_
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
 * _[regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
