# Class: activity and behavior


Activity or behavior of any independent integral living, organization or mechanical actor in the world

URI: [http://w3id.org/biolink/vocab/ActivityAndBehavior](http://w3id.org/biolink/vocab/ActivityAndBehavior)

![img](images/ActivityAndBehavior.png)
## Mappings

 * [UMLSSG:ACTI](http://purl.obolibrary.org/obo/UMLSSG_ACTI)
 * [UMLSSC:T051](http://purl.obolibrary.org/obo/UMLSSC_T051)
 * [UMLSST:evnt](http://purl.obolibrary.org/obo/UMLSST_evnt)
 * [UMLSSC:T052](http://purl.obolibrary.org/obo/UMLSSC_T052)
 * [UMLSST:acty](http://purl.obolibrary.org/obo/UMLSST_acty)
 * [UMLSSC:T053](http://purl.obolibrary.org/obo/UMLSSC_T053)
 * [UMLSST:bhvr](http://purl.obolibrary.org/obo/UMLSST_bhvr)
 * [UMLSSC:T054](http://purl.obolibrary.org/obo/UMLSSC_T054)
 * [UMLSST:socb](http://purl.obolibrary.org/obo/UMLSST_socb)
 * [UMLSSC:T055](http://purl.obolibrary.org/obo/UMLSSC_T055)
 * [UMLSST:inbe](http://purl.obolibrary.org/obo/UMLSST_inbe)
 * [UMLSSC:T056](http://purl.obolibrary.org/obo/UMLSSC_T056)
 * [UMLSST:dora](http://purl.obolibrary.org/obo/UMLSST_dora)
 * [UMLSSC:T057](http://purl.obolibrary.org/obo/UMLSSC_T057)
 * [UMLSST:ocac](http://purl.obolibrary.org/obo/UMLSST_ocac)
 * [UMLSSC:T064](http://purl.obolibrary.org/obo/UMLSSC_T064)
 * [UMLSST:gora](http://purl.obolibrary.org/obo/UMLSST_gora)
 * [UMLSSC:T066](http://purl.obolibrary.org/obo/UMLSSC_T066)
 * [UMLSST:mcha](http://purl.obolibrary.org/obo/UMLSST_mcha)
## Inheritance

 *  is_a: [Occurrent](Occurrent.md) - A processual entity
## Children

## Fields

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
 * [has input](has_input.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [has participant](has_participant.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process 
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Occurrent](Occurrent.md)
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
 * [synonym](synonym.md) *subsets*: (translator_minimal)
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
