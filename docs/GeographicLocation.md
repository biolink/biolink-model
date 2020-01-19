---
parent: Classes
title: biolink:GeographicLocation
grand_parent: Browse Biolink Model
---

# Type: GeographicLocation


a location that can be described in lat/long coordinates

URI: [biolink:GeographicLocation](https://w3id.org/biolink/vocab/GeographicLocation)

UMLSSG:GEOG
{: .mapping-label }

UMLSST:geoa
{: .mapping-label }

UMLSSC:T083
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeographicLocation&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[GeographicLocationAtTime],%20\[PlanetaryEntity]^-\[GeographicLocation])

---


## Parents

 *  is_a: [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet

## Children

 * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time

## Referenced by class


## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | UMLSSG:GEOG |
|  | | UMLSST:geoa |
|  | | UMLSSC:T083 |

