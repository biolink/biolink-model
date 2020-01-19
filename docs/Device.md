---
parent: Classes
title: biolink:Device
grand_parent: Browse Biolink Model
---

# Type: Device


A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment

URI: [biolink:Device](https://w3id.org/biolink/vocab/Device)

UMLSSG:DEVI
{: .mapping-label }

UMLSSC:T074
{: .mapping-label }

UMLSST:medd
{: .mapping-label }

UMLSSC:T075
{: .mapping-label }

UMLSST:resd
{: .mapping-label }

UMLSSC:T203
{: .mapping-label }

UMLSST:drdd
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[Device&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

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
| **Mappings:** | | UMLSSG:DEVI |
|  | | UMLSSC:T074 |
|  | | UMLSST:medd |
|  | | UMLSSC:T075 |
|  | | UMLSST:resd |
|  | | UMLSSC:T203 |
|  | | UMLSST:drdd |

