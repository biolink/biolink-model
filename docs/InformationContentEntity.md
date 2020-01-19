---
parent: Classes
title: biolink:InformationContentEntity
grand_parent: Browse Biolink Model
---

# Type: InformationContentEntity


a piece of information that typically describes some piece of biology or is used as support.

URI: [biolink:InformationContentEntity](https://w3id.org/biolink/vocab/InformationContentEntity)

IAO:0000030
{: .mapping-label }

UMLSSG:CONC
{: .mapping-label }

UMLSSC:T077
{: .mapping-label }

UMLSST:cnce
{: .mapping-label }

UMLSSC:T078
{: .mapping-label }

UMLSST:idcn
{: .mapping-label }

UMLSSC:T079
{: .mapping-label }

UMLSST:tmco
{: .mapping-label }

UMLSSC:T080
{: .mapping-label }

UMLSST:qlco
{: .mapping-label }

UMLSSC:T081
{: .mapping-label }

UMLSST:qnco
{: .mapping-label }

UMLSSC:T082
{: .mapping-label }

UMLSST:spco
{: .mapping-label }

UMLSSC:T089
{: .mapping-label }

UMLSST:rnlw
{: .mapping-label }

UMLSSC:T102
{: .mapping-label }

UMLSST:grpa
{: .mapping-label }

UMLSSC:T169
{: .mapping-label }

UMLSST:ftcn
{: .mapping-label }

UMLSSC:T171
{: .mapping-label }

UMLSST:lang
{: .mapping-label }

UMLSSC:T185
{: .mapping-label }

UMLSST:clas
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[InformationContentEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[Publication],%20\[InformationContentEntity]^-\[EvidenceType],%20\[InformationContentEntity]^-\[ConfidenceLevel],%20\[NamedThing]^-\[InformationContentEntity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
 * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
 * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.

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
| **Aliases:** | | information |
|  | | information artefact |
|  | | information entity |
| **Mappings:** | | IAO:0000030 |
|  | | UMLSSG:CONC |
|  | | UMLSSC:T077 |
|  | | UMLSST:cnce |
|  | | UMLSSC:T078 |
|  | | UMLSST:idcn |
|  | | UMLSSC:T079 |
|  | | UMLSST:tmco |
|  | | UMLSSC:T080 |
|  | | UMLSST:qlco |
|  | | UMLSSC:T081 |
|  | | UMLSST:qnco |
|  | | UMLSSC:T082 |
|  | | UMLSST:spco |
|  | | UMLSSC:T089 |
|  | | UMLSST:rnlw |
|  | | UMLSSC:T102 |
|  | | UMLSST:grpa |
|  | | UMLSSC:T169 |
|  | | UMLSST:ftcn |
|  | | UMLSSC:T171 |
|  | | UMLSST:lang |
|  | | UMLSSC:T185 |
|  | | UMLSST:clas |

