---
parent: Classes
title: biolink:MolecularActivity
grand_parent: Browse Biolink Model
layout: default
---

# Class: MolecularActivity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: [biolink:MolecularActivity](https://w3id.org/biolink/vocab/MolecularActivity)

GO:0003674
{: .mapping-label }

UMLSSC:T044
{: .mapping-label }

UMLSST:moft
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Occurrent],[MacromolecularMachine]%3Cenabled%20by%200..%2A-%20[MolecularActivity%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[ChemicalSubstance]%3Chas%20output%200..%2A-%20[MolecularActivity],[ChemicalSubstance]%3Chas%20input%200..%2A-%20[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1%3E[MolecularActivity],[MolecularActivity]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]%5E-[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachine],[ChemicalSubstance],[BiologicalProcessOrActivity])

---


## Identifier prefixes

 * GO
 * REACT
 * RHEA
 * MetaCyc
 * EC
 * KEGG

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Referenced by class

 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>REQ</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The gene product, gene, or complex that catalyzes the reaction
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the input for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the output for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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

### Domain for slot:

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The gene product, gene, or complex that catalyzes the reaction
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the input for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the output for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Mappings:** | | GO:0003674 |
|  | | UMLSSC:T044 |
|  | | UMLSST:moft |

