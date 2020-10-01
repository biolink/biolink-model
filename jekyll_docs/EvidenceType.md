---
parent: Classes
title: biolink:EvidenceType
grand_parent: Browse Biolink Model
layout: default
---

# Type: EvidenceType


Class of evidence that supports an association

URI: [biolink:EvidenceType](https://w3id.org/biolink/vocab/EvidenceType)

ECO:0000000
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[InformationContentEntity],[InformationContentEntity]%5E-[EvidenceType%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[Association])

---


## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.

## Referenced by class

 *  **[Association](Association.md)** *[has evidence](has_evidence.md)*  <sub>OPT</sub>  **[EvidenceType](EvidenceType.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | evidence code |
| **Mappings:** | | ECO:0000000 |

