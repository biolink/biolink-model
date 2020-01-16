---
parent: "Browse Biolink Model"
title: biolink:ActivityAndBehavior
---

# Type: ActivityAndBehavior


Activity or behavior of any independent integral living, organization or mechanical actor in the world

URI: [biolink:ActivityAndBehavior](https://w3id.org/biolink/vocab/ActivityAndBehavior)

UMLSSG:ACTI
{: .mappinglabel }

UMLSSC:T051
{: .mappinglabel }

UMLSST:evnt
{: .mappinglabel }

UMLSSC:T052
{: .mappinglabel }

UMLSST:acty
{: .mappinglabel }

UMLSSC:T053
{: .mappinglabel }

UMLSST:bhvr
{: .mappinglabel }

UMLSSC:T054
{: .mappinglabel }

UMLSST:socb
{: .mappinglabel }

UMLSSC:T055
{: .mappinglabel }

UMLSST:inbe
{: .mappinglabel }

UMLSSC:T056
{: .mappinglabel }

UMLSST:dora
{: .mappinglabel }

UMLSSC:T057
{: .mappinglabel }

UMLSST:ocac
{: .mappinglabel }

UMLSSC:T064
{: .mappinglabel }

UMLSST:gora
{: .mappinglabel }

UMLSSC:T066
{: .mappinglabel }

UMLSST:mcha
{: .mappinglabel }

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Occurrent]^-\[ActivityAndBehavior&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

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
| **Mappings:** | | UMLSSG:ACTI |
|  | | UMLSSC:T051 |
|  | | UMLSST:evnt |
|  | | UMLSSC:T052 |
|  | | UMLSST:acty |
|  | | UMLSSC:T053 |
|  | | UMLSST:bhvr |
|  | | UMLSSC:T054 |
|  | | UMLSST:socb |
|  | | UMLSSC:T055 |
|  | | UMLSST:inbe |
|  | | UMLSSC:T056 |
|  | | UMLSST:dora |
|  | | UMLSSC:T057 |
|  | | UMLSST:ocac |
|  | | UMLSSC:T064 |
|  | | UMLSST:gora |
|  | | UMLSSC:T066 |
|  | | UMLSST:mcha |

