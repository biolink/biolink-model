# Class: phenomenon


a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

URI: [http://bioentity.io/vocab/Phenomenon](http://bioentity.io/vocab/Phenomenon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent]^-\[Phenomenon|has_participant(i):string%20%3F;has_input(i):string%20%3F],%20\[Phenomenon]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[Phenomenon]-%20precedes(i)%20%3F>\[Occurrent])
## Mappings

 * [UMLSSG:PHEN](http://purl.obolibrary.org/obo/UMLSSG_PHEN)
## Inheritance

 *  is_a: [occurrent](Occurrent.md) - A processual entity
## Children

## Fields

 * _[regulates, process to process](regulates_process_to_process.md)_
    * range: [occurrent](Occurrent.md)
    * inherited from: [occurrent](Occurrent.md)
 * _[precedes](precedes.md) *subsets: translator_minimal*_
    * _holds between two processes, where one completes before the other begins_
    * range: [occurrent](Occurrent.md)
    * inherited from: [occurrent](Occurrent.md)
