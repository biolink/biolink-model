---
parent: Class Mixins
title: biolink:Occurrent
grand_parent: Classes
layout: default
---

# Class: Occurrent


A processual entity.

URI: [biolink:Occurrent](https://w3id.org/biolink/vocab/Occurrent)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEssenceOrOccurrent],[Phenomenon]uses%20-.-%3E[Occurrent],[MolecularActivity]uses%20-.-%3E[Occurrent],[EnvironmentalProcess]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]uses%20-.-%3E[Occurrent],[BiologicalProcess]uses%20-.-%3E[Occurrent],[Occurrent]%5E-[ActivityAndBehavior],[PhysicalEssenceOrOccurrent]%5E-[Occurrent],[Phenomenon],[NamedThing],[MolecularActivity],[EnvironmentalProcess],[BiologicalProcessOrActivity],[BiologicalProcess],[ActivityAndBehavior])

---


## Parents

 *  is_a: [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) - Either a physical or processual entity.

## Children

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world

## Mixin for

 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) (mixin)  - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
 * [EnvironmentalProcess](EnvironmentalProcess.md) (mixin) 
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.
 * [Phenomenon](Phenomenon.md) (mixin)  - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

## Referenced by class

 *  **[MolecularActivity](MolecularActivity.md)** *[actively involved in](actively_involved_in.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[capable of](capable_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[consumed by](consumed_by.md)*  <sub>0..1</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[is catalyst of](is_catalyst_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[is input of](is_input_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[is output of](is_output_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[is substrate of](is_substrate_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[NamedThing](NamedThing.md)** *[participates in](participates_in.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[preceded by](preceded_by.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[precedes](precedes.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process negatively regulated by process](process_negatively_regulated_by_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process negatively regulates process](process_negatively_regulates_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process positively regulated by process](process_positively_regulated_by_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process positively regulates process](process_positively_regulates_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process regulated by process](process_regulated_by_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[process regulates process](process_regulates_process.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[temporally related to](temporally_related_to.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | BFO:0000003 |

