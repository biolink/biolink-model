---
parent: Other Classes
title: biolink:GeographicExposure
grand_parent: Classes
layout: default
---

# Class: GeographicExposure


A geographic exposure is a factor relating to geographic proximity to some impactful entity.

URI: [biolink:GeographicExposure](https://w3id.org/biolink/vocab/GeographicExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeographicExposure%7Ctimepoint(i):time_type%20%3F]uses%20-.-%3E[ExposureEvent],[EnvironmentalExposure]%5E-[GeographicExposure],[ExposureEvent],[EnvironmentalExposure])

---


## Parents

 *  is_a: [EnvironmentalExposure](EnvironmentalExposure.md) - A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.

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
| **Close Mappings:** | | dcid:GeologicalEvent |
| **Narrow Mappings:** | | dcid:IceStoremEvent |
|  | | dcid:LakeEffectSnowEvent |
|  | | dcid:LandslideEvent |
|  | | dcid:MarineDenseFogEvent |
|  | | dcid:MarineLighteningEvent |
|  | | dcid:MarineStrongWindEvent |
|  | | dcid:MarineThunderstormWindEvent |
|  | | dcid:StormEvent |
|  | | dcid:StormSurgeTideEvent |
|  | | dcid:StrongWindEvent |
|  | | dcid:ThunderstormWindEvent |
|  | | dcid:TornadoEvent |
|  | | dcid:TropicalDepressionEvent |
|  | | dcid:WinterStoremEvent |

