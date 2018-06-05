# Class: occurrent


A processual entity

URI: http://bioentity.io/vocab/Occurrent

![img](http://yuml.me/diagram/nofunky/class/\[Occurrent]^-\[ActivityAndBehavior],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[Procedure],%20)
## Mappings

 * [BFO:0000003](http://purl.obolibrary.org/obo/BFO_0000003)
## Inheritance

## Children

 *  child: [phenomenon](Phenomenon.md)
 *  child: [procedure](Procedure.md)
 *  child: [activity and behavior](ActivityAndBehavior.md)
 *  mixin: [molecular activity](MolecularActivity.md)
 *  mixin: [biological process](BiologicalProcess.md)
 *  mixin: [environmental process](EnvironmentalProcess.md)
## Used in

 *  class: [occurrent](Occurrent.md) references: [phenomenon](Phenomenon.md)
 *  class: [occurrent](Occurrent.md) references: [environmental process](EnvironmentalProcess.md)
 *  class: [occurrent](Occurrent.md) references: [procedure](Procedure.md)
 *  class: [occurrent](Occurrent.md) references: [activity and behavior](ActivityAndBehavior.md)
 *  class: [occurrent](Occurrent.md) references: [molecular activity](MolecularActivity.md)
 *  class: [occurrent](Occurrent.md) references: [biological process](BiologicalProcess.md)
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
    * __Local__
 * _[precedes](precedes.md) *subsets: translator_minimal*_
    * _holds between two processes, where one completes before the other begins_
    * range: [occurrent](Occurrent.md)
    * inherited from: [related to](related_to.md)
