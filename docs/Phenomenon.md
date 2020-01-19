---
parent: Classes
title: biolink:Phenomenon
grand_parent: Browse Biolink Model
---

# Type: Phenomenon


a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

URI: [biolink:Phenomenon](https://w3id.org/biolink/vocab/Phenomenon)

UMLSSG:PHEN
{: .mapping-label }

UMLSSC:T034
{: .mapping-label }

UMLSST:lbtr
{: .mapping-label }

UMLSSC:T038
{: .mapping-label }

UMLSST:biof
{: .mapping-label }

UMLSSC:T067
{: .mapping-label }

UMLSST:phpr
{: .mapping-label }

UMLSSC:T068
{: .mapping-label }

UMLSST:hcpp
{: .mapping-label }

UMLSSC:T069
{: .mapping-label }

UMLSST:eehu
{: .mapping-label }

UMLSSC:T070
{: .mapping-label }

UMLSST:npop
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent]^-\[Phenomenon&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

---


## Parents

 *  is_a: [Occurrent](Occurrent.md) - A processual entity

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
| **Mappings:** | | UMLSSG:PHEN |
|  | | UMLSSC:T034 |
|  | | UMLSST:lbtr |
|  | | UMLSSC:T038 |
|  | | UMLSST:biof |
|  | | UMLSSC:T067 |
|  | | UMLSST:phpr |
|  | | UMLSSC:T068 |
|  | | UMLSST:hcpp |
|  | | UMLSSC:T069 |
|  | | UMLSST:eehu |
|  | | UMLSSC:T070 |
|  | | UMLSST:npop |

