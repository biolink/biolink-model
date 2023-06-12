---
parent: Class Mixins
title: biolink:FrequencyQuantifier
grand_parent: Classes
layout: default
---

# Class: FrequencyQuantifier




URI: [biolink:FrequencyQuantifier](https://w3id.org/biolink/vocab/FrequencyQuantifier)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipQuantifier],[VariantToPopulationAssociation]uses%20-.-%3E[FrequencyQuantifier%7Chas_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;has_percentage:double%20%3F],[EntityToPhenotypicFeatureAssociationMixin]uses%20-.-%3E[FrequencyQuantifier],[RelationshipQuantifier]%5E-[FrequencyQuantifier],[VariantToPopulationAssociation],[EntityToPhenotypicFeatureAssociationMixin])

---


## Parents

 *  is_a: [RelationshipQuantifier](RelationshipQuantifier.md)

## Mixin for

 * [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) (mixin) 
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [has count](has_count.md)  <sub>0..1</sub>
     * Description: number of things with a particular property
     * Range: [Integer](types/Integer.md)
 * [has percentage](has_percentage.md)  <sub>0..1</sub>
     * Description: equivalent to has quotient multiplied by 100
     * Range: [Double](types/Double.md)
 * [has quotient](has_quotient.md)  <sub>0..1</sub>
     * Range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>0..1</sub>
     * Description: total number of things in a particular reference set
     * Range: [Integer](types/Integer.md)