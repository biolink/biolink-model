---
layout: default
---

## geographic location at time


a location that can be described in lat/long coordinates, for a particular time

URI: [http://bioentity.io/vocab/GeographicLocationAtTime](http://bioentity.io/vocab/GeographicLocationAtTime)


![img](http://yuml.me/diagram/nofunky/class/[planetary entity|]^-[geographic location at time|latitude;longitude;timepoint])
## Mappings


## Inheritance

 *  is_a: [planetary entity](PlanetaryEntity.html)

## Children



## Fields

 * [latitude](latitude.html)
    * _latitude_
    * __range__: xsd:float
    * __Local__
 * [longitude](longitude.html)
    * _longitude_
    * __range__: xsd:float
    * __Local__
 * [timepoint](timepoint.html)
    * _a point in time_
    * __range__: time type
    * __Local__
 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
