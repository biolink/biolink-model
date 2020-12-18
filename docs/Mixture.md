---
parent: Class Mixins
title: biolink:Mixture
grand_parent: Classes
layout: default
---

# Class: Mixture


The physical combination of two or more molecular entities in which the identities are retained and are mixed in the form of solutions, suspensions and colloids.

URI: [biolink:Mixture](https://w3id.org/biolink/vocab/Mixture)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalSubstance]%3Chas%20constituent%200..%2A-%20[Mixture],[ProcessedMaterial]uses%20-.-%3E[Mixture],[Food]uses%20-.-%3E[Mixture],[Drug]uses%20-.-%3E[Mixture],[ComplexChemicalExposure]uses%20-.-%3E[Mixture],[ProcessedMaterial],[Food],[Drug],[ComplexChemicalExposure],[ChemicalSubstance])

---


## Mixin for

 * [ComplexChemicalExposure](ComplexChemicalExposure.md) (mixin)  - A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
 * [Drug](Drug.md) (mixin)  - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 * [Food](Food.md) (mixin)  - A substance consumed by a living organism as a source of nutrition
 * [ProcessedMaterial](ProcessedMaterial.md) (mixin)  - A chemical substance (often a mixture) processed for consumption for nutritional, medical or technical use.

## Referenced by class


## Attributes


### Own

 * [has constituent](has_constituent.md)  <sub>0..*</sub>
    * Description: one or more chemical substances within a mixture
    * range: [ChemicalSubstance](ChemicalSubstance.md)
