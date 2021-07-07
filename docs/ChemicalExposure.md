---
parent: Other Classes
title: biolink:ChemicalExposure
grand_parent: Classes
layout: default
---

# Class: ChemicalExposure


A chemical exposure is an intake of a particular chemical entity.

URI: [biolink:ChemicalExposure](https://w3id.org/biolink/vocab/ChemicalExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEvent],[DrugExposure],[ChemicalExposure%7Ctimepoint:time_type%20%3F]uses%20-.-%3E[ExposureEvent],[ChemicalExposure]%5E-[DrugExposure])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Children

 * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular drug.

## Referenced by class


## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | ECTO:9000000 |
|  | | SIO:001399 |

