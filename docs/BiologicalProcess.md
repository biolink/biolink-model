---
parent: Classes
title: biolink:BiologicalProcess
grand_parent: Browse Biolink Model
---

# Type: BiologicalProcess


One or more causally connected executions of molecular functions

URI: [biolink:BiologicalProcess](https://w3id.org/biolink/vocab/BiologicalProcess)

GO:0008150
{: .mapping-label }

SIO:000006
{: .mapping-label }

WD:Q2996394
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MacromolecularMachineToBiologicalProcessAssociation]-%20object%201..1>\[BiologicalProcess&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcess]^-\[PhysiologicalProcess],%20\[BiologicalProcess]^-\[Pathway],%20\[BiologicalProcessOrActivity]^-\[BiologicalProcess])

---


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
| **Mappings:** | | GO:0008150 |
|  | | SIO:000006 |
|  | | WD:Q2996394 |

