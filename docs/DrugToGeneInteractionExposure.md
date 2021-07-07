---
parent: Other Classes
title: biolink:DrugToGeneInteractionExposure
grand_parent: Classes
layout: default
---

# Class: DrugToGeneInteractionExposure


drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.

URI: [biolink:DrugToGeneInteractionExposure](https://w3id.org/biolink/vocab/DrugToGeneInteractionExposure)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneGroupingMixin],[Gene],[DrugToGeneInteractionExposure%7Ctimepoint(i):time_type%20%3F]uses%20-.-%3E[GeneGroupingMixin],[DrugExposure]%5E-[DrugToGeneInteractionExposure],[DrugExposure])

---


## Parents

 *  is_a: [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular drug.

## Uses Mixins

 *  mixin: [GeneGroupingMixin](GeneGroupingMixin.md) - any grouping of multiple genes or gene products

## Attributes


### Inherited from exposure event:

 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

### Inherited from gene grouping mixin:

 * [has gene or gene product](has_gene_or_gene_product.md)  <sub>0..\*</sub>
     * Description: connects an entity with one or more gene or gene products
     * Range: [Gene](Gene.md)
