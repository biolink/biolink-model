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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEssenceOrOccurrent],[BiologicalProcessOrActivity]++-%20has%20input%200..%2A%3E[Occurrent],[BiologicalProcessOrActivity]++-%20has%20output%200..%2A%3E[Occurrent],[Phenomenon]uses%20-.-%3E[Occurrent],[MolecularActivity]uses%20-.-%3E[Occurrent],[EnvironmentalProcess]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]uses%20-.-%3E[Occurrent],[BiologicalProcess]uses%20-.-%3E[Occurrent],[Occurrent]%5E-[ActivityAndBehavior],[PhysicalEssenceOrOccurrent]%5E-[Occurrent],[Phenomenon],[MolecularActivity],[EnvironmentalProcess],[BiologicalProcessOrActivity],[BiologicalProcess],[ActivityAndBehavior])

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

 *  **[MolecularActivity](MolecularActivity.md)** *[actively involves](actively_involves.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[can be carried out by](can_be_carried_out_by.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[capable of](capable_of.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[consumes](consumes.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[has input](has_input.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[has output](has_output.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[has participant](has_participant.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[preceded by](preceded_by.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[precedes](precedes.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**
 *  **[Occurrent](Occurrent.md)** *[temporally related to](temporally_related_to.md)*  <sub>0..\*</sub>  **[Occurrent](Occurrent.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | BFO:0000003 |

