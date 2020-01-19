---
parent: Classes
title: biolink:Disease
grand_parent: Browse Biolink Model
---

# Type: Disease




URI: [biolink:Disease](https://w3id.org/biolink/vocab/Disease)

MONDO:0000001
{: .mapping-label }

WD:Q12136
{: .mapping-label }

SIO:010299
{: .mapping-label }

UMLSSG:DISO
{: .mapping-label }

UMLSSC:T019
{: .mapping-label }

UMLSST:cgab
{: .mapping-label }

UMLSSC:T020
{: .mapping-label }

UMLSST:acab
{: .mapping-label }

UMLSSC:T037
{: .mapping-label }

UMLSST:inpo
{: .mapping-label }

UMLSSC:T046
{: .mapping-label }

UMLSST:patf
{: .mapping-label }

UMLSSC:T047
{: .mapping-label }

UMLSST:dsyn
{: .mapping-label }

UMLSSC:T048
{: .mapping-label }

UMLSST:mobd
{: .mapping-label }

UMLSSC:T049
{: .mapping-label }

UMLSST:comd
{: .mapping-label }

UMLSSC:T184
{: .mapping-label }

UMLSST:sosy
{: .mapping-label }

UMLSSC:T190
{: .mapping-label }

UMLSST:anab
{: .mapping-label }

UMLSSC:T191
{: .mapping-label }

UMLSST:neop
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Disease&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DiseaseToExposureAssociation]-%20subject%201..1>\[Disease],%20\[DiseaseToThingAssociation]-%20subject%201..1>\[Disease],%20\[DiseaseOrPhenotypicFeature]^-\[Disease])

---


## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

## Referenced by class

 *  **[DiseaseToExposureAssociation](DiseaseToExposureAssociation.md)** *[disease to exposure association➞subject](disease_to_exposure_association_subject.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**
 *  **[DiseaseToThingAssociation](DiseaseToThingAssociation.md)** *[disease to thing association➞subject](disease_to_thing_association_subject.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**
 *  **[EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)** *[entity to disease association➞object](entity_to_disease_association_object.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**
 *  **[NamedThing](NamedThing.md)** *[manifestation of](manifestation_of.md)*  <sub>0..*</sub>  **[Disease](Disease.md)**

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
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | condition |
|  | | disorder |
|  | | medical condition |
| **Mappings:** | | MONDO:0000001 |
|  | | WD:Q12136 |
|  | | SIO:010299 |
|  | | UMLSSG:DISO |
|  | | UMLSSC:T019 |
|  | | UMLSST:cgab |
|  | | UMLSSC:T020 |
|  | | UMLSST:acab |
|  | | UMLSSC:T037 |
|  | | UMLSST:inpo |
|  | | UMLSSC:T046 |
|  | | UMLSST:patf |
|  | | UMLSSC:T047 |
|  | | UMLSST:dsyn |
|  | | UMLSSC:T048 |
|  | | UMLSST:mobd |
|  | | UMLSSC:T049 |
|  | | UMLSST:comd |
|  | | UMLSSC:T184 |
|  | | UMLSST:sosy |
|  | | UMLSSC:T190 |
|  | | UMLSST:anab |
|  | | UMLSSC:T191 |
|  | | UMLSST:neop |

