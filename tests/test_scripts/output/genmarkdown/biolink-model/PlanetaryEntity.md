# Class: planetary entity


Any entity or process that exists at the level of the whole planet

URI: [http://bioentity.io/vocab/PlanetaryEntity](http://bioentity.io/vocab/PlanetaryEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[PlanetaryEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F],%20\[PlanetaryEntity]^-\[EnvironmentalFeature],%20\[PlanetaryEntity]^-\[EnvironmentalProcess],%20\[PlanetaryEntity]^-\[GeographicLocation],%20\[PlanetaryEntity]^-\[GeographicLocationAtTime],%20\[PlanetaryEntity]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

## Inheritance

 *  is_a: [named thing](NamedThing.md) - a databased entity or concept/class
## Children

 *  child: [environmental feature](EnvironmentalFeature.md)
 *  child: [environmental process](EnvironmentalProcess.md)
 *  child: [geographic location](GeographicLocation.md) - a location that can be described in lat/long coordinates
 *  child: [geographic location at time](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
## Used in

## Fields

 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
