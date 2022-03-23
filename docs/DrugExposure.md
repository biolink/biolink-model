---
parent: Other Classes
title: biolink:DrugExposure
grand_parent: Classes
layout: default
---

# Class: DrugExposure


A drug exposure is an intake of a particular drug.

URI: [biolink:DrugExposure](https://w3id.org/biolink/vocab/DrugExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[ExposureEvent],[DrugToGeneInteractionExposure],[DrugExposure%7Ctimepoint(i):time_type%20%3F]uses%20-.-%3E[ExposureEvent],[DrugExposure]%5E-[DrugToGeneInteractionExposure],[ChemicalExposure]%5E-[DrugExposure],[ChemicalExposure])

---


## Parents

 *  is_a: [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical entity.

## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Children

 * [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) - drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.

## Referenced by class


## Attributes


### Inherited from chemical exposure:

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
| **Aliases:** | | drug intake |
|  | | drug dose |
|  | | medication intake |
| **Exact Mappings:** | | ECTO:0000509 |
| **Broad Mappings:** | | SIO:001005 |

