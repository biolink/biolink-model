---
parent: Class Mixins
title: biolink:GeneExpressionMixin
grand_parent: Classes
layout: default
---

# Class: GeneExpressionMixin


Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.

URI: [biolink:GeneExpressionMixin](https://w3id.org/biolink/vocab/GeneExpressionMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[LifeStage],[DiseaseOrPhenotypicFeature]%3Cphenotypic%20state%200..1-%20[GeneExpressionMixin],[LifeStage]%3Cstage%20qualifier%200..1-%20[GeneExpressionMixin],[AnatomicalEntity]%3Cexpression%20site%200..1-%20[GeneExpressionMixin],[OntologyClass]%3Cquantifier%20qualifier%200..1-%20[GeneExpressionMixin],[VariantToGeneExpressionAssociation]uses%20-.-%3E[GeneExpressionMixin],[GeneToGeneCoexpressionAssociation]uses%20-.-%3E[GeneExpressionMixin],[VariantToGeneExpressionAssociation],[GeneToGeneCoexpressionAssociation],[DiseaseOrPhenotypicFeature],[AnatomicalEntity])

---


## Mixin for

 * [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) (mixin)  - Indicates that two genes are co-expressed, generally under the same conditions.
 * [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) (mixin)  - An association between a variant and expression of a gene (i.e. e-QTL)

## Referenced by class


## Attributes


### Own

 * [expression site](expression_site.md)  <sub>0..1</sub>
     * Description: location in which gene or protein expression takes place. May be cell, tissue, or organ.
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
     * Example: UBERON:0002037 cerebellum
 * [quantifier qualifier](quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: A measurable quantity for the object of the association
     * Range: [OntologyClass](OntologyClass.md)
 * [phenotypic state](phenotypic_state.md)  <sub>0..1</sub>
     * Description: in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.
     * Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

### Inherited from gene to expression site association:

 * [stage qualifier](stage_qualifier.md)  <sub>0..1</sub>
     * Description: stage during which gene or protein expression of takes place.
     * Range: [LifeStage](LifeStage.md)
     * Example: UBERON:0000069 larval stage
 * [quantifier qualifier](quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: A measurable quantity for the object of the association
     * Range: [OntologyClass](OntologyClass.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)

### Domain for slot:

 * [quantifier qualifier](quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: A measurable quantity for the object of the association
     * Range: [OntologyClass](OntologyClass.md)
