# Class: molecular activity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: http://bioentity.io/vocab/MolecularActivity

![img](http://yuml.me/diagram/nofunky/class/\[BiologicalProcessOrActivity]^-\[MolecularActivity|has_participant:string%20%3F;has_input:string%20%3F],%20\[MolecularActivity]-%20regulates_process_to_process%20%3F>\[Occurrent],%20\[MolecularActivity]-%20precedes%20%3F>\[Occurrent],%20\[MolecularActivity]uses%20-.->\[Occurrent],%20)
## Mappings

 * [GO:0003674](http://purl.obolibrary.org/obo/GO_0003674)
## Inheritance

 *  is_a: [biological process or activity](BiologicalProcessOrActivity.md)
 *  mixin: [occurrent](Occurrent.md)
## Children

## Used in

 *  class: [molecular activity](MolecularActivity.md) references: [biological process or activity](BiologicalProcessOrActivity.md)
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
