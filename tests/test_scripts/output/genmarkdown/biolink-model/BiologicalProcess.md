# Class: biological process


One or more causally connected executions of molecular functions

URI: http://bioentity.io/vocab/BiologicalProcess

![img](http://yuml.me/diagram/nofunky/class/\[BiologicalProcessOrActivity]^-\[BiologicalProcess|has_participant:string%20%3F;has_input:string%20%3F],%20\[BiologicalProcess]^-\[Pathway],%20\[BiologicalProcess]^-\[PhysiologicalProcess],%20\[BiologicalProcess]-%20regulates_process_to_process%20%3F>\[Occurrent],%20\[BiologicalProcess]-%20precedes%20%3F>\[Occurrent],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20)
## Mappings

 * [GO:0008150](http://purl.obolibrary.org/obo/GO_0008150)
 * [SIO:000006](http://semanticscience.org/resource/SIO_000006)
 * [WD:Q2996394](http://purl.obolibrary.org/obo/WD_Q2996394)
## Inheritance

 *  is_a: [biological process or activity](BiologicalProcessOrActivity.md)
 *  mixin: [occurrent](Occurrent.md)
## Children

 *  child: [physiological process](PhysiologicalProcess.md)
 *  child: [pathway](Pathway.md)
## Used in

 *  class: [biological process](BiologicalProcess.md) references: [physiological process](PhysiologicalProcess.md)
 *  class: [biological process](BiologicalProcess.md) references: [biological process or activity](BiologicalProcessOrActivity.md)
 *  class: [biological process](BiologicalProcess.md) references: [pathway](Pathway.md)
## Fields

 * _[regulates, process to process](regulates_process_to_process.md)_
    * range: [occurrent](Occurrent.md)
    * inherited from: [regulates](regulates.md)
 * _[has participant](has_participant.md) *subsets: translator_minimal*_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: string
    * inherited from: [related to](related_to.md)
 * _[has input](has_input.md) *subsets: translator_minimal*_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: string
    * inherited from: [has participant](has_participant.md) *subsets: translator_minimal*
 * _[precedes](precedes.md) *subsets: translator_minimal*_
    * _holds between two processes, where one completes before the other begins_
    * range: [occurrent](Occurrent.md)
    * inherited from: [related to](related_to.md)
