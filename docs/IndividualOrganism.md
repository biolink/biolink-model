---
parent: "Browse Biolink Model"
title: biolink:IndividualOrganism
---

# Type: IndividualOrganism




URI: [biolink:IndividualOrganism](https://w3id.org/biolink/vocab/IndividualOrganism)

SIO:010000
{: .mappinglabel }

WD:Q795052
{: .mappinglabel }

UMLSSG:LIVB
{: .mappinglabel }

UMLSSC:T001
{: .mappinglabel }

UMLSST:orgm
{: .mappinglabel }

UMLSSC:T002
{: .mappinglabel }

UMLSST:plnt
{: .mappinglabel }

UMLSSC:T004
{: .mappinglabel }

UMLSST:fngs
{: .mappinglabel }

UMLSSC:T005
{: .mappinglabel }

UMLSST:virs
{: .mappinglabel }

UMLSSC:T007
{: .mappinglabel }

UMLSST:bact
{: .mappinglabel }

UMLSSC:T008
{: .mappinglabel }

UMLSST:anim
{: .mappinglabel }

UMLSSC:T010
{: .mappinglabel }

UMLSST:vtbt
{: .mappinglabel }

UMLSSC:T011
{: .mappinglabel }

UMLSST:amph
{: .mappinglabel }

UMLSSC:T012
{: .mappinglabel }

UMLSST:bird
{: .mappinglabel }

UMLSSC:T013
{: .mappinglabel }

UMLSST:fish
{: .mappinglabel }

UMLSSC:T014
{: .mappinglabel }

UMLSST:rept
{: .mappinglabel }

UMLSSC:T015
{: .mappinglabel }

UMLSST:mamm
{: .mappinglabel }

UMLSSC:T016
{: .mappinglabel }

UMLSST:humn
{: .mappinglabel }

UMLSSC:T096
{: .mappinglabel }

UMLSST:grup
{: .mappinglabel }

UMLSSC:T097
{: .mappinglabel }

UMLSST:prog
{: .mappinglabel }

UMLSSC:T099
{: .mappinglabel }

UMLSST:famg
{: .mappinglabel }

UMLSSC:T100
{: .mappinglabel }

UMLSST:aggp
{: .mappinglabel }

UMLSSC:T101
{: .mappinglabel }

UMLSST:podg
{: .mappinglabel }

UMLSSC:T194
{: .mappinglabel }

UMLSST:arch
{: .mappinglabel }

UMLSSC:T204
{: .mappinglabel }

UMLSST:euka
{: .mappinglabel }

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[IndividualOrganism&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[IndividualOrganism]uses%20-.->\[ThingWithTaxon],%20\[IndividualOrganism]^-\[Case],%20\[OrganismalEntity]^-\[IndividualOrganism])

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon

## Children

 * [Case](Case.md) - An individual organism that has a patient role in some clinical context.

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:010000 |
|  | | WD:Q795052 |
|  | | UMLSSG:LIVB |
|  | | UMLSSC:T001 |
|  | | UMLSST:orgm |
|  | | UMLSSC:T002 |
|  | | UMLSST:plnt |
|  | | UMLSSC:T004 |
|  | | UMLSST:fngs |
|  | | UMLSSC:T005 |
|  | | UMLSST:virs |
|  | | UMLSSC:T007 |
|  | | UMLSST:bact |
|  | | UMLSSC:T008 |
|  | | UMLSST:anim |
|  | | UMLSSC:T010 |
|  | | UMLSST:vtbt |
|  | | UMLSSC:T011 |
|  | | UMLSST:amph |
|  | | UMLSSC:T012 |
|  | | UMLSST:bird |
|  | | UMLSSC:T013 |
|  | | UMLSST:fish |
|  | | UMLSSC:T014 |
|  | | UMLSST:rept |
|  | | UMLSSC:T015 |
|  | | UMLSST:mamm |
|  | | UMLSSC:T016 |
|  | | UMLSST:humn |
|  | | UMLSSC:T096 |
|  | | UMLSST:grup |
|  | | UMLSSC:T097 |
|  | | UMLSST:prog |
|  | | UMLSSC:T099 |
|  | | UMLSST:famg |
|  | | UMLSSC:T100 |
|  | | UMLSST:aggp |
|  | | UMLSSC:T101 |
|  | | UMLSST:podg |
|  | | UMLSSC:T194 |
|  | | UMLSST:arch |
|  | | UMLSSC:T204 |
|  | | UMLSST:euka |

