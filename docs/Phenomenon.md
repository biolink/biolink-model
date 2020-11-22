---
parent: Entities
title: biolink:Phenomenon
grand_parent: Classes
layout: default
---

# Class: Phenomenon


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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Phenomenon%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B]uses%20-.-%3E[Occurrent],[NamedThing]%5E-[Phenomenon],[Occurrent],[NamedThing])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
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

