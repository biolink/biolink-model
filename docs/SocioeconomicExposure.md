---
parent: Other Classes
title: biolink:SocioeconomicExposure
grand_parent: Classes
layout: default
---

# Class: SocioeconomicExposure


A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).

URI: [biolink:SocioeconomicExposure](https://w3id.org/biolink/vocab/SocioeconomicExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SocioeconomicAttribute]%3Chas%20attribute%201..%2A-%20[SocioeconomicExposure%7Ctimepoint:time_type%20%3F],[SocioeconomicExposure]uses%20-.-%3E[ExposureEvent],[SocioeconomicAttribute],[ExposureEvent])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Referenced by class


## Attributes


### Own

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

### Domain for slot:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)
