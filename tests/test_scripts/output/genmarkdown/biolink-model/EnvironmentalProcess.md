# Class: environmental process




URI: [http://bioentity.io/vocab/EnvironmentalProcess](http://bioentity.io/vocab/EnvironmentalProcess)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EnvironmentalProcess|has_participant(i):string%20%3F;has_input(i):string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[EnvironmentalProcess]-%20precedes(i)%20%3F>\[Occurrent],%20\[EnvironmentalProcess]-%20regulates,%20process%20to%20process(i)%20%3F>\[Occurrent],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20\[PlanetaryEntity]^-\[EnvironmentalProcess])
## Mappings

 * [ENVO:02500000](http://purl.obolibrary.org/obo/ENVO_02500000)
## Inheritance

 *  is_a: planetary entity
 *  mixin: occurrent
## Children

## Fields

 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _has input_
    * _holds between a process and a continuant, where the continuant is an input into the process_
    * range: **string**
    * inherited from: occurrent
 * _has participant_
    * _holds between a process and a continuant, where the continuant is somehow involved in the process _
    * range: **string**
    * inherited from: occurrent
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _precedes_
    * _holds between two processes, where one completes before the other begins_
    * range: occurrent
    * inherited from: occurrent
 * _regulates, process to process_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: occurrent
    * inherited from: occurrent
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
