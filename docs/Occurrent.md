---
parent: Entities
title: biolink:Occurrent
grand_parent: Classes
layout: default
---

# Class: Occurrent


A processual entity

URI: [biolink:Occurrent](https://w3id.org/biolink/vocab/Occurrent)

BFO:0000003
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Procedure],[Phenomenon],[MolecularActivity]uses%20-.-%3E[Occurrent%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[EnvironmentalProcess]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]uses%20-.-%3E[Occurrent],[BiologicalProcess]uses%20-.-%3E[Occurrent],[Occurrent]%5E-[Procedure],[Occurrent]%5E-[Phenomenon],[Occurrent]%5E-[ActivityAndBehavior],[NamedThing]%5E-[Occurrent],[NamedThing],[MolecularActivity],[EnvironmentalProcess],[BiologicalProcessOrActivity],[BiologicalProcess],[ActivityAndBehavior])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner

## Mixin for

 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) (mixin)  - Either an individual molecular activity, or a collection of causally connected molecular activities
 * [EnvironmentalProcess](EnvironmentalProcess.md) (mixin) 
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[actively involved in](actively_involved_in.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[capable of](capable_of.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[negatively regulates, process to process](negatively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[participates in](participates_in.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[positively regulates, process to process](positively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[preceded by](preceded_by.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[precedes](precedes.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[regulates, process to process](regulates_process_to_process.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[temporally related to](temporally_related_to.md)*  <sub>0..*</sub>  **[Occurrent](Occurrent.md)**

## Attributes


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
| **Mappings:** | | BFO:0000003 |

