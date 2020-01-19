---
parent: Classes
title: biolink:Procedure
grand_parent: Browse Biolink Model
---

# Type: Procedure


A series of actions conducted in a certain order or manner

URI: [biolink:Procedure](https://w3id.org/biolink/vocab/Procedure)

UMLSSG:PROC
{: .mapping-label }

UMLSSC:T058
{: .mapping-label }

UMLSST:hlca
{: .mapping-label }

UMLSSC:T059
{: .mapping-label }

UMLSST:lbpr
{: .mapping-label }

UMLSSC:T060
{: .mapping-label }

UMLSST:diap
{: .mapping-label }

UMLSSC:T061
{: .mapping-label }

UMLSST:topp
{: .mapping-label }

UMLSSC:T062
{: .mapping-label }

UMLSST:resa
{: .mapping-label }

UMLSSC:T063
{: .mapping-label }

UMLSST:mbrt
{: .mapping-label }

UMLSSC:T065
{: .mapping-label }

UMLSST:edac
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent]^-\[Procedure&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

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
| **Mappings:** | | UMLSSG:PROC |
|  | | UMLSSC:T058 |
|  | | UMLSST:hlca |
|  | | UMLSSC:T059 |
|  | | UMLSST:lbpr |
|  | | UMLSSC:T060 |
|  | | UMLSST:diap |
|  | | UMLSSC:T061 |
|  | | UMLSST:topp |
|  | | UMLSSC:T062 |
|  | | UMLSST:resa |
|  | | UMLSSC:T063 |
|  | | UMLSST:mbrt |
|  | | UMLSSC:T065 |
|  | | UMLSST:edac |

