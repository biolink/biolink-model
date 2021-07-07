---
parent: Other Classes
title: biolink:EnvironmentalExposure
grand_parent: Classes
layout: default
---

# Class: EnvironmentalExposure


A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.

URI: [biolink:EnvironmentalExposure](https://w3id.org/biolink/vocab/EnvironmentalExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeographicExposure],[ExposureEvent],[EnvironmentalExposure%7Ctimepoint:time_type%20%3F]uses%20-.-%3E[ExposureEvent],[EnvironmentalExposure]%5E-[GeographicExposure])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Children

 * [GeographicExposure](GeographicExposure.md) - A geographic exposure is a factor relating to geographic proximity to some impactful entity.

## Referenced by class


## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)
