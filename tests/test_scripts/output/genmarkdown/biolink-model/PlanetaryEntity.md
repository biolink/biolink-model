# Class: planetary entity


Any entity or process that exists at the level of the whole planet

URI: [http://bioentity.io/vocab/PlanetaryEntity](http://bioentity.io/vocab/PlanetaryEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[PlanetaryEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F],%20\[PlanetaryEntity]^-\[EnvironmentalFeature],%20\[PlanetaryEntity]^-\[EnvironmentalProcess],%20\[PlanetaryEntity]^-\[GeographicLocation],%20\[PlanetaryEntity]^-\[GeographicLocationAtTime],%20\[PlanetaryEntity]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

## Inheritance

 *  is_a: [named thing](NamedThing.md) - a databased entity or concept/class
## Children

 *  child: [geographic location](GeographicLocation.md) - a location that can be described in lat/long coordinates
 *  child: [environmental process](EnvironmentalProcess.md)
 *  child: [geographic location at time](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
 *  child: [environmental feature](EnvironmentalFeature.md)
## Used in

 *  class: [planetary entity](PlanetaryEntity.md) references: [geographic location](GeographicLocation.md)
 *  class: [planetary entity](PlanetaryEntity.md) references: [environmental process](EnvironmentalProcess.md)
 *  class: [planetary entity](PlanetaryEntity.md) references: [geographic location at time](GeographicLocationAtTime.md)
 *  class: [planetary entity](PlanetaryEntity.md) references: [environmental feature](EnvironmentalFeature.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
