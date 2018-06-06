# Class: clinical entity


Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities

URI: [http://bioentity.io/vocab/ClinicalEntity](http://bioentity.io/vocab/ClinicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[ClinicalEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F],%20\[ClinicalEntity]^-\[ClinicalIntervention],%20\[ClinicalEntity]^-\[ClinicalTrial],%20\[ClinicalEntity]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

## Inheritance

 *  is_a: [named thing](NamedThing.md) - a databased entity or concept/class
## Children

 *  child: [clinical intervention](ClinicalIntervention.md)
 *  child: [clinical trial](ClinicalTrial.md)
## Used in

 *  class: [clinical entity](ClinicalEntity.md) references: [clinical intervention](ClinicalIntervention.md)
 *  class: [clinical entity](ClinicalEntity.md) references: [clinical trial](ClinicalTrial.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
