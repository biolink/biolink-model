---
parent: Class Mixins
title: biolink:ChemicalOrDrugOrTreatment
grand_parent: Classes
layout: default
---

# Class: ChemicalOrDrugOrTreatment




URI: [biolink:ChemicalOrDrugOrTreatment](https://w3id.org/biolink/vocab/ChemicalOrDrugOrTreatment)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature],[Treatment]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[Drug]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[ChemicalEntity]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[Treatment],[Drug],[ChemicalEntity])

---


## Mixin for

 * [ChemicalEntity](ChemicalEntity.md) (mixin)  - A chemical entity is a physical entity that pertains to chemistry or biochemistry.
 * [Drug](Drug.md) (mixin)  - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 * [Treatment](Treatment.md) (mixin)  - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures

## Referenced by class

 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[approved for treatment by](approved_for_treatment_by.md)*  <sub>0..\*</sub>  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[is diagnosed by](is_diagnosed_by.md)*  <sub>0..\*</sub>  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[treated by](treated_by.md)*  <sub>0..\*</sub>  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)**

## Attributes

