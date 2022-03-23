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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[ExposureEvent],[DrugExposure],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[ChemicalExposure%7Ctimepoint:time_type%20%3F],[ChemicalExposure]uses%20-.-%3E[ExposureEvent],[ChemicalExposure]%5E-[DrugExposure])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Children

 * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular drug.

## Referenced by class


## Attributes


### Own

 * [has quantitative value](has_quantitative_value.md)  <sub>0..\*</sub>
     * Description: connects an attribute to a value
     * Range: [QuantityValue](QuantityValue.md)
     * in subsets: (samples)

### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | ECTO:9000000 |
|  | | SIO:001399 |

