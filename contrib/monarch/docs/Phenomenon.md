# Class: phenomenon


a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

URI: [http://bioentity.io/vocab/Phenomenon](http://bioentity.io/vocab/Phenomenon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Phenomenon|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_participant(i):string%20%3F;has_input(i):string%20%3F]-%20precedes(i)%20%3F>\[Occurrent],%20\[Phenomenon]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[Phenomenon]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Occurrent]^-\[Phenomenon])
## Mappings

 * [UMLSSG:PHEN](http://purl.obolibrary.org/obo/UMLSSG_PHEN)
## Inheritance

 *  is_a: [Occurrent](Occurrent.md) - A processual entity
## Children

## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has alternate identifier](has_alternate_identifier.md)
    * Description: An alternate identifier for the entity, provided by the source database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [has input](has_input.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: **string**
    * inherited from: [Occurrent](Occurrent.md)
 * [has participant](has_participant.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process 
    * range: **string**
    * inherited from: [Occurrent](Occurrent.md)
 * [has synonym](has_synonym.md)
    * Description: Alternate labels for an entity
    * range: [name](name.md) *subsets*: (translator_minimal)*
    * inherited from: [NamedThing](NamedThing.md)
 * [has xref](has_xref.md)
    * Description: A database cross-reference for the entity, provided by a separate database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [precedes](precedes.md) *subsets*: (translator_minimal)
    * Description: holds between two processes, where one completes before the other begins
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
