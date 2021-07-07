---
parent: Other Classes
title: biolink:PathologicalAnatomicalExposure
grand_parent: Classes
layout: default
---

# Class: PathologicalAnatomicalExposure


An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.

URI: [biolink:PathologicalAnatomicalExposure](https://w3id.org/biolink/vocab/PathologicalAnatomicalExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PathologicalAnatomicalExposure%7Ctimepoint:time_type%20%3F]uses%20-.-%3E[ExposureEvent],[ExposureEvent])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)
