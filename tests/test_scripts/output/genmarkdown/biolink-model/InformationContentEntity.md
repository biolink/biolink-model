# Class: information content entity


a piece of information that typically describes some piece of biology or is used as support.

URI: [http://bioentity.io/vocab/InformationContentEntity](http://bioentity.io/vocab/InformationContentEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[InformationContentEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F],%20\[InformationContentEntity]^-\[Association],%20\[InformationContentEntity]^-\[ConfidenceLevel],%20\[InformationContentEntity]^-\[EvidenceType],%20\[InformationContentEntity]^-\[Publication],%20\[InformationContentEntity]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

 * [IAO:0000030](http://purl.obolibrary.org/obo/IAO_0000030)
 * [UMLSSG:CONC](http://purl.obolibrary.org/obo/UMLSSG_CONC)
## Inheritance

 *  is_a: [named thing](NamedThing.md) - a databased entity or concept/class
## Children

 *  child: [publication](Publication.md) - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
 *  child: [evidence type](EvidenceType.md) - Class of evidence that supports an association
 *  child: [confidence level](ConfidenceLevel.md) - Level of confidence in a statement
 *  child: [association](Association.md) - A typed association between two entities, supported by evidence
## Used in

 *  class: [information content entity](InformationContentEntity.md) references: [publication](Publication.md)
 *  class: [information content entity](InformationContentEntity.md) references: [evidence type](EvidenceType.md)
 *  class: [information content entity](InformationContentEntity.md) references: [confidence level](ConfidenceLevel.md)
 *  class: [information content entity](InformationContentEntity.md) references: [association](Association.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
