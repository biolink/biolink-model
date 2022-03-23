---
parent: Class Mixins
title: biolink:ExposureEvent
grand_parent: Classes
layout: default
---

# Class: ExposureEvent


A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

URI: [biolink:ExposureEvent](https://w3id.org/biolink/vocab/ExposureEvent)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEventToPhenotypicFeatureAssociation],[EntityToExposureEventAssociationMixin]++-%20object%201..1%3E[ExposureEvent%7Ctimepoint:time_type%20%3F],[ExposureEventToPhenotypicFeatureAssociation]++-%20subject%201..1%3E[ExposureEvent],[Treatment]uses%20-.-%3E[ExposureEvent],[SocioeconomicExposure]uses%20-.-%3E[ExposureEvent],[PathologicalProcessExposure]uses%20-.-%3E[ExposureEvent],[PathologicalAnatomicalExposure]uses%20-.-%3E[ExposureEvent],[GeographicExposure]uses%20-.-%3E[ExposureEvent],[GenomicBackgroundExposure]uses%20-.-%3E[ExposureEvent],[EnvironmentalExposure]uses%20-.-%3E[ExposureEvent],[DrugExposure]uses%20-.-%3E[ExposureEvent],[DiseaseOrPhenotypicFeatureExposure]uses%20-.-%3E[ExposureEvent],[ChemicalExposure]uses%20-.-%3E[ExposureEvent],[BioticExposure]uses%20-.-%3E[ExposureEvent],[BehavioralExposure]uses%20-.-%3E[ExposureEvent],[Treatment],[SocioeconomicExposure],[PathologicalProcessExposure],[PathologicalAnatomicalExposure],[GeographicExposure],[GenomicBackgroundExposure],[EnvironmentalExposure],[EntityToExposureEventAssociationMixin],[DrugExposure],[DiseaseOrPhenotypicFeatureExposure],[ChemicalExposure],[BioticExposure],[BehavioralExposure])

---


## Mixin for

 * [BehavioralExposure](BehavioralExposure.md) (mixin)  - A behavioral exposure is a factor relating to behavior impacting an individual.
 * [BioticExposure](BioticExposure.md) (mixin)  - An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
 * [ChemicalExposure](ChemicalExposure.md) (mixin)  - A chemical exposure is an intake of a particular chemical entity.
 * [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) (mixin)  - A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer.
 * [DrugExposure](DrugExposure.md) (mixin)  - A drug exposure is an intake of a particular drug.
 * [EnvironmentalExposure](EnvironmentalExposure.md) (mixin)  - A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [GeographicExposure](GeographicExposure.md) (mixin)  - A geographic exposure is a factor relating to geographic proximity to some impactful entity.
 * [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) (mixin)  - An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
 * [PathologicalProcessExposure](PathologicalProcessExposure.md) (mixin)  - A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
 * [SocioeconomicExposure](SocioeconomicExposure.md) (mixin)  - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
 * [Treatment](Treatment.md) (mixin)  - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures

## Referenced by class

 *  **[EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md)** *[object](object.md)*  <sub>1..1</sub>  **[ExposureEvent](ExposureEvent.md)**
 *  **[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ExposureEvent](ExposureEvent.md)**

## Attributes


### Own

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | exposure |
|  | | experimental condition |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | XCO:0000000 |

