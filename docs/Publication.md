---
parent: Classes
title: biolink:Publication
grand_parent: Browse Biolink Model
---

# Type: Publication


Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.

URI: [biolink:Publication](https://w3id.org/biolink/vocab/Publication)

IAO:0000311
{: .mapping-label }

UMLSSC:T170
{: .mapping-label }

UMLSST:inpr
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]-%20publications%200..*>\[Publication&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[InformationContentEntity]^-\[Publication])

---


## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.

## Referenced by class

 *  **[Association](Association.md)** *[publications](publications.md)*  <sub>0..*</sub>  **[Publication](Publication.md)**

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
| **Aliases:** | | reference |
| **Mappings:** | | IAO:0000311 |
|  | | UMLSSC:T170 |
|  | | UMLSST:inpr |

