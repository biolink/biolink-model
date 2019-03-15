# Class: occurrent


A processual entity

URI: [http://w3id.org/biolink/vocab/Occurrent](http://w3id.org/biolink/vocab/Occurrent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;synonym(i):label_type%20*;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Occurrent]-%20precedes%20%3F>\[Occurrent],%20\[Occurrent]-%20has%20input%20%3F>\[NamedThing],%20\[Occurrent]-%20has%20participant%20%3F>\[NamedThing],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[NamedThing]-%20actively%20involved%20in(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20capable%20of(i)%20%3F>\[Occurrent],%20\[Occurrent]-%20negatively%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[NamedThing]-%20participates%20in(i)%20%3F>\[Occurrent],%20\[Occurrent]-%20positively%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[Occurrent]-%20precedes%20%3F>\[Occurrent],%20\[Occurrent]-%20regulates,%20process%20to%20process%20%3F>\[Occurrent],%20\[MolecularActivity]uses%20-.->\[Occurrent],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[Occurrent]^-\[Procedure],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[ActivityAndBehavior],%20\[NamedThing]^-\[Occurrent])
## Mappings

 * [BFO:0000003](http://purl.obolibrary.org/obo/BFO_0000003)
## Inheritance

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class
## Children

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [EnvironmentalProcess](EnvironmentalProcess.md) (mixin) 
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.
## Used in

 *  class: **[NamedThing](NamedThing.md)** *[actively involved in](actively_involved_in.md)* **[Occurrent](Occurrent.md)**
 *  class: **[NamedThing](NamedThing.md)** *[capable of](capable_of.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[negatively regulates, process to process](negatively_regulates_process_to_process.md)* **[Occurrent](Occurrent.md)**
 *  class: **[NamedThing](NamedThing.md)** *[participates in](participates_in.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[positively regulates, process to process](positively_regulates_process_to_process.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[precedes](precedes.md)* **[Occurrent](Occurrent.md)**
 *  class: **[Occurrent](Occurrent.md)** *[regulates, process to process](regulates_process_to_process.md)* **[Occurrent](Occurrent.md)**
## Fields

 * [has input](has_input.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * [has participant](has_participant.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process 
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * [precedes](precedes.md) *subsets*: (translator_minimal)
    * Description: holds between two processes, where one completes before the other begins
    * range: [Occurrent](Occurrent.md)
    * __Local__
 * [regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [Occurrent](Occurrent.md)
    * __Local__
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
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
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [synonym](synonym.md) *subsets*: (translator_minimal)
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
