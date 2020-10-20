---
parent: Entities
title: biolink:BiologicalProcess
grand_parent: Classes
layout: default
---

# Class: BiologicalProcess


One or more causally connected executions of molecular functions

URI: [biolink:BiologicalProcess](https://w3id.org/biolink/vocab/BiologicalProcess)

GO:0008150
{: .mapping-label }

SIO:000006
{: .mapping-label }

WIKIDATA:Q2996394
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhysiologicalProcess],[PhysicalEntity],[Pathway],[Occurrent],[NamedThing],[MacromolecularMachineToBiologicalProcessAssociation],[BiologicalProcessOrActivity],[MacromolecularMachineToBiologicalProcessAssociation]-%20object%201..1%3E[BiologicalProcess%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[BiologicalProcess]uses%20-.-%3E[Occurrent],[BiologicalProcess]%5E-[PhysiologicalProcess],[BiologicalProcess]%5E-[Pathway],[BiologicalProcessOrActivity]%5E-[BiologicalProcess])

---


## Identifier prefixes

 * GO
 * REACT
 * MetaCyc
 * KEGG

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Children

 * [Pathway](Pathway.md)
 * [PhysiologicalProcess](PhysiologicalProcess.md)

## Referenced by class

 *  **[MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md)** *[macromolecular machine to biological process association➞object](macromolecular_machine_to_biological_process_association_object.md)*  <sub>REQ</sub>  **[BiologicalProcess](BiologicalProcess.md)**

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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0008150 |
|  | | SIO:000006 |
|  | | WIKIDATA:Q2996394 |

