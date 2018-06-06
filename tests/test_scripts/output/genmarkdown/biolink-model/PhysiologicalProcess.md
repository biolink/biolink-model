# Class: physiological process




URI: [http://bioentity.io/vocab/PhysiologicalProcess](http://bioentity.io/vocab/PhysiologicalProcess)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalProcess]^-\[PhysiologicalProcess|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_participant(i):string%20%3F;has_input(i):string%20%3F],%20\[PhysiologicalProcess]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PhysiologicalProcess]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[PhysiologicalProcess]-%20precedes(i)%20%3F>\[Occurrent])
## Mappings

 * [UMLSSG:PHYS](http://purl.obolibrary.org/obo/UMLSSG_PHYS)
## Inheritance

 *  is_a: [biological process](BiologicalProcess.md) - One or more causally connected executions of molecular functions
## Children

## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[regulates, process to process](regulates_process_to_process.md)_
    * range: [occurrent](Occurrent.md)
    * inherited from: [occurrent](Occurrent.md)
 * _[precedes](precedes.md) *subsets: translator_minimal*_
    * _holds between two processes, where one completes before the other begins_
    * range: [occurrent](Occurrent.md)
    * inherited from: [occurrent](Occurrent.md)
