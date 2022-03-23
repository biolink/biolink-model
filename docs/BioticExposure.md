---
parent: Other Classes
title: biolink:BioticExposure
grand_parent: Classes
layout: default
---

# Class: BioticExposure


An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).

URI: [biolink:BioticExposure](https://w3id.org/biolink/vocab/BioticExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEvent],[BioticExposure%7Ctimepoint:time_type%20%3F]uses%20-.-%3E[ExposureEvent])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | viral exposure |
|  | | bacterial exposure |

