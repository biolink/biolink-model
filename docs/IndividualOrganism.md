---
parent: Classes
title: biolink:IndividualOrganism
grand_parent: Browse Biolink Model
---

# Type: IndividualOrganism




URI: [biolink:IndividualOrganism](https://w3id.org/biolink/vocab/IndividualOrganism)

SIO:010000
{: .mapping-label }

WD:Q795052
{: .mapping-label }

UMLSSG:LIVB
{: .mapping-label }

UMLSSC:T001
{: .mapping-label }

UMLSST:orgm
{: .mapping-label }

UMLSSC:T002
{: .mapping-label }

UMLSST:plnt
{: .mapping-label }

UMLSSC:T004
{: .mapping-label }

UMLSST:fngs
{: .mapping-label }

UMLSSC:T005
{: .mapping-label }

UMLSST:virs
{: .mapping-label }

UMLSSC:T007
{: .mapping-label }

UMLSST:bact
{: .mapping-label }

UMLSSC:T008
{: .mapping-label }

UMLSST:anim
{: .mapping-label }

UMLSSC:T010
{: .mapping-label }

UMLSST:vtbt
{: .mapping-label }

UMLSSC:T011
{: .mapping-label }

UMLSST:amph
{: .mapping-label }

UMLSSC:T012
{: .mapping-label }

UMLSST:bird
{: .mapping-label }

UMLSSC:T013
{: .mapping-label }

UMLSST:fish
{: .mapping-label }

UMLSSC:T014
{: .mapping-label }

UMLSST:rept
{: .mapping-label }

UMLSSC:T015
{: .mapping-label }

UMLSST:mamm
{: .mapping-label }

UMLSSC:T016
{: .mapping-label }

UMLSST:humn
{: .mapping-label }

UMLSSC:T096
{: .mapping-label }

UMLSST:grup
{: .mapping-label }

UMLSSC:T097
{: .mapping-label }

UMLSST:prog
{: .mapping-label }

UMLSSC:T099
{: .mapping-label }

UMLSST:famg
{: .mapping-label }

UMLSSC:T100
{: .mapping-label }

UMLSST:aggp
{: .mapping-label }

UMLSSC:T101
{: .mapping-label }

UMLSST:podg
{: .mapping-label }

UMLSSC:T194
{: .mapping-label }

UMLSST:arch
{: .mapping-label }

UMLSSC:T204
{: .mapping-label }

UMLSST:euka
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[IndividualOrganism&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[IndividualOrganism]uses%20-.->\[ThingWithTaxon],%20\[IndividualOrganism]^-\[Case],%20\[OrganismalEntity]^-\[IndividualOrganism])

---


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

