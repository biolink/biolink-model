---
parent: Class Mixins
title: biolink:GeneOrGeneProduct
grand_parent: Classes
layout: default
---

# Class: GeneOrGeneProduct


A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another

URI: [biolink:GeneOrGeneProduct](https://w3id.org/biolink/vocab/GeneOrGeneProduct)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReactionToCatalystAssociation],[MacromolecularMachineMixin],[GeneToPathwayAssociation],[GeneToGeneHomologyAssociation],[GeneToGeneAssociation],[GeneToExpressionSiteAssociation],[GeneToEntityAssociationMixin],[GeneToDiseaseOrPhenotypicFeatureAssociation],[GeneProductMixin],[ChemicalAffectsGeneAssociation]++-%20object%201..1%3E[GeneOrGeneProduct%7Cname(i):symbol_type%20%3F],[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[ChemicalGeneInteractionAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[DrugToGeneAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[DruggableGeneToDiseaseAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneAsAModelOfDiseaseAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneHasVariantThatContributesToDiseaseAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToDiseaseOrPhenotypicFeatureAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToEntityAssociationMixin]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToExpressionSiteAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToGeneAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[GeneToGeneAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToGeneHomologyAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[GeneToGeneHomologyAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[GeneToPathwayAssociation]++-%20subject%201..1%3E[GeneOrGeneProduct],[ReactionToCatalystAssociation]++-%20object%201..1%3E[GeneOrGeneProduct],[Gene]uses%20-.-%3E[GeneOrGeneProduct],[GeneOrGeneProduct]%5E-[GeneProductMixin],[MacromolecularMachineMixin]%5E-[GeneOrGeneProduct],[GeneHasVariantThatContributesToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[Gene],[DruggableGeneToDiseaseAssociation],[DrugToGeneAssociation],[ChemicalGeneInteractionAssociation],[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation],[ChemicalAffectsGeneAssociation],[CellularComponent],[BiologicalProcess],[AnatomicalEntity])

---


## Identifier prefixes

 * CHEMBL.TARGET
 * IUPHAR.FAMILY

## Parents

 *  is_a: [MacromolecularMachineMixin](MacromolecularMachineMixin.md) - A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

## Children

 * [GeneProductMixin](GeneProductMixin.md) - The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.

## Mixin for

 * [Gene](Gene.md) (mixin)  - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.

## Referenced by class

 *  **[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[coexpressed with](coexpressed_with.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[DrugToGeneAssociation](DrugToGeneAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[expresses](expresses.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToPathwayAssociation](GeneToPathwayAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[CellularComponent](CellularComponent.md)** *[has active component](has_active_component.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has negative upstream actor](has_negative_upstream_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has negative upstream or within actor](has_negative_upstream_or_within_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has positive upstream actor](has_positive_upstream_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has positive upstream or within actor](has_positive_upstream_or_within_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has upstream actor](has_upstream_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[BiologicalProcess](BiologicalProcess.md)** *[has upstream or within actor](has_upstream_or_within_actor.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in cell population with](in_cell_population_with.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in complex with](in_complex_with.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in pathway with](in_pathway_with.md)*  <sub>0..\*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**

## Attributes


### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
