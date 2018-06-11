# Class: procedure


A series of actions conducted in a certain order or manner

URI: [http://bioentity.io/vocab/Procedure](http://bioentity.io/vocab/Procedure)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Procedure|has_participant(i):string%20%3F;has_input(i):string%20%3F]-%20precedes(i)%20%3F>\[Occurrent],%20\[Procedure]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[Occurrent]^-\[Procedure])
## Mappings

 * [UMLSSG:PROC](http://purl.obolibrary.org/obo/UMLSSG_PROC)
## Inheritance

 *  is_a: occurrent
## Children

## Fields

 * _has input_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: **string**
    * inherited from: occurrent
 * _has participant_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: **string**
    * inherited from: occurrent
 * _precedes_
    * _holds between two processes, where one completes before the other begins_
    * range: occurrent
    * inherited from: occurrent
 * _regulates, process to process_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: occurrent
    * inherited from: occurrent
