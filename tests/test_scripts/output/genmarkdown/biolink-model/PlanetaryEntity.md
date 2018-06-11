# Class: planetary entity


Any entity or process that exists at the level of the whole planet

URI: [http://bioentity.io/vocab/PlanetaryEntity](http://bioentity.io/vocab/PlanetaryEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PlanetaryEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PlanetaryEntity]^-\[GeographicLocationAtTime],%20\[PlanetaryEntity]^-\[GeographicLocation],%20\[PlanetaryEntity]^-\[EnvironmentalProcess],%20\[PlanetaryEntity]^-\[EnvironmentalFeature],%20\[NamedThing]^-\[PlanetaryEntity])
## Mappings

## Inheritance

 *  is_a: named thing
## Children

 * environmental feature
 * environmental process
 * geographic location
 * geographic location at time
## Used in

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
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
