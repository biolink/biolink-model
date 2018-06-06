# Class: geographic location


a location that can be described in lat/long coordinates

URI: [http://bioentity.io/vocab/GeographicLocation](http://bioentity.io/vocab/GeographicLocation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PlanetaryEntity]^-\[GeographicLocation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;latitude:float%20%3F;longitude:float%20%3F],%20\[GeographicLocation]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

 * [UMLSSG:GEOG](http://purl.obolibrary.org/obo/UMLSSG_GEOG)
## Inheritance

 *  is_a: [planetary entity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
## Children

## Fields

 * _[latitude](latitude.md)_
    * _latitude_
    * range: float
    * __Local__
 * _[longitude](longitude.md)_
    * _longitude_
    * range: float
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
