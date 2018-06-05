# Class: environmental process




URI: http://bioentity.io/vocab/EnvironmentalProcess

![img](http://yuml.me/diagram/nofunky/class/\[PlanetaryEntity]^-\[EnvironmentalProcess|has_participant:string%20%3F;has_input:string%20%3F],%20\[EnvironmentalProcess]-%20regulates_process_to_process%20%3F>\[Occurrent],%20\[EnvironmentalProcess]-%20precedes%20%3F>\[Occurrent],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20)
## Mappings

 * [ENVO:02500000](http://purl.obolibrary.org/obo/ENVO_02500000)
## Inheritance

 *  is_a: [planetary entity](PlanetaryEntity.md)
 *  mixin: [occurrent](Occurrent.md)
## Children

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
