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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[LifeStage],[DiseaseOrPhenotypicFeature]%3Cphenotypic%20state%200..1-%20[GeneExpressionMixin],[LifeStage]%3Cstage%20qualifier%200..1-%20[GeneExpressionMixin],[AnatomicalEntity]%3Cexpression%20site%200..1-%20[GeneExpressionMixin],[OntologyClass]%3Cquantifier%20qualifier%200..1-++[GeneExpressionMixin],[VariantToGeneExpressionAssociation]uses%20-.-%3E[GeneExpressionMixin],[GeneToGeneCoexpressionAssociation]uses%20-.-%3E[GeneExpressionMixin],[VariantToGeneExpressionAssociation],[GeneToGeneCoexpressionAssociation],[DiseaseOrPhenotypicFeature],[AnatomicalEntity])

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
 * [gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: Optional quantitative value indicating degree of expression.
     * Range: [OntologyClass](OntologyClass.md)
 * [phenotypic state](phenotypic_state.md)  <sub>0..1</sub>
     * Description: in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.
     * Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

### Inherited from gene to expression site association:

 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>0..1</sub>
     * Description: stage at which the gene is expressed in the site
     * Range: [LifeStage](LifeStage.md)
     * Example: UBERON:0000069 larval stage
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: can be used to indicate magnitude, or also ranking
     * Range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>1..1</sub>
     * Description: gene in which variation is correlated with the phenotypic feature
     * Range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>1..1</sub>
     * Description: location in which the gene is expressed
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
     * Example: UBERON:0002037 cerebellum
 * [gene to expression site association➞predicate](gene_to_expression_site_association_predicate.md)  <sub>1..1</sub>
     * Description: expression relationship
     * Range: [PredicateType](types/PredicateType.md)

### Domain for slot:

 * [gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)  <sub>0..1</sub>
     * Description: Optional quantitative value indicating degree of expression.
     * Range: [OntologyClass](OntologyClass.md)