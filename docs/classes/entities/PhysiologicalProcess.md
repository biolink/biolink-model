---
parent: Entities
title: biolink:PhysiologicalProcess
grand_parent: Classes
layout: default
---

# Class: PhysiologicalProcess




URI: [biolink:PhysiologicalProcess](https://w3id.org/biolink/vocab/PhysiologicalProcess)

UMLSSG:PHYS
{: .mapping-label }

UMLSSC:T032
{: .mapping-label }

UMLSST:orga
{: .mapping-label }

UMLSSC:T039
{: .mapping-label }

UMLSST:phsf
{: .mapping-label }

UMLSSC:T040
{: .mapping-label }

UMLSST:orgf
{: .mapping-label }

UMLSSC:T041
{: .mapping-label }

UMLSST:menp
{: .mapping-label }

UMLSSC:T042
{: .mapping-label }

UMLSST:ortf
{: .mapping-label }

UMLSSC:T043
{: .mapping-label }

UMLSST:celf
{: .mapping-label }

UMLSSC:T045
{: .mapping-label }

UMLSST:genf
{: .mapping-label }

UMLSSC:T201
{: .mapping-label }

UMLSST:clna
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BiologicalProcess]%5E-[PhysiologicalProcess%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[PhysicalEntity],[NamedThing],[BiologicalProcess])

---


## Identifier prefixes

 * GO
 * REACT

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

## Attributes


### Inherited from biological process or activity:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [PhysicalEntity](PhysicalEntity.md)
    * in subsets: (translator_minimal)

### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

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
| **Aliases:** | | physiology |
| **Mappings:** | | UMLSSG:PHYS |
|  | | UMLSSC:T032 |
|  | | UMLSST:orga |
|  | | UMLSSC:T039 |
|  | | UMLSST:phsf |
|  | | UMLSSC:T040 |
|  | | UMLSST:orgf |
|  | | UMLSSC:T041 |
|  | | UMLSST:menp |
|  | | UMLSSC:T042 |
|  | | UMLSST:ortf |
|  | | UMLSSC:T043 |
|  | | UMLSST:celf |
|  | | UMLSSC:T045 |
|  | | UMLSST:genf |
|  | | UMLSSC:T201 |
|  | | UMLSST:clna |

