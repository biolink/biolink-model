---
parent: Other Classes
title: biolink:DiseaseOrPhenotypicFeatureExposure
grand_parent: Classes
layout: default
---

# Class: DiseaseOrPhenotypicFeatureExposure


A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.

URI: [biolink:DiseaseOrPhenotypicFeatureExposure](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PathologicalEntityMixin],[ExposureEvent],[DiseaseOrPhenotypicFeatureExposure%7Ctimepoint:time_type%20%3F]uses%20-.-%3E[ExposureEvent],[DiseaseOrPhenotypicFeatureExposure]uses%20-.-%3E[PathologicalEntityMixin])

---


## Uses Mixins

 *  mixin: [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 *  mixin: [PathologicalEntityMixin](PathologicalEntityMixin.md) - A pathological (abnormal) structure or process.

## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)
