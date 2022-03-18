# Class: GeneExpressionMixin
_Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneExpressionMixin](https://w3id.org/biolink/vocab/GeneExpressionMixin)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [quantifier_qualifier](quantifier_qualifier.md) | [OntologyClass](OntologyClass.md) | 0..1 | Optional quantitative value indicating degree of expression.  | . |
| [expression_site](expression_site.md) | [AnatomicalEntity](AnatomicalEntity.md) | 0..1 | location in which gene or protein expression takes place. May be cell, tissue, or organ.  | . |
| [stage_qualifier](stage_qualifier.md) | [LifeStage](LifeStage.md) | 0..1 | stage during which gene or protein expression of takes place.  | . |
| [phenotypic_state](phenotypic_state.md) | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | 0..1 | in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene expression mixin
description: Observed gene expression intensity, context (site, stage) and associated
  phenotypic status within which the expression occurs.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- quantifier qualifier
- expression site
- stage qualifier
- phenotypic state
slot_usage:
  quantifier qualifier:
    name: quantifier qualifier
    description: Optional quantitative value indicating degree of expression.

```
</details>

### Induced

<details>
```yaml
name: gene expression mixin
description: Observed gene expression intensity, context (site, stage) and associated
  phenotypic status within which the expression occurs.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  quantifier qualifier:
    name: quantifier qualifier
    description: Optional quantitative value indicating degree of expression.
attributes:
  quantifier qualifier:
    name: quantifier qualifier
    description: Optional quantitative value indicating degree of expression.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: quantifier_qualifier
    owner: gene expression mixin
    range: ontology class
  expression site:
    name: expression site
    description: location in which gene or protein expression takes place. May be
      cell, tissue, or organ.
    examples:
    - value: UBERON:0002037
      description: cerebellum
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: expression_site
    owner: gene expression mixin
    range: anatomical entity
  stage qualifier:
    name: stage qualifier
    description: stage during which gene or protein expression of takes place.
    examples:
    - value: UBERON:0000069
      description: larval stage
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: stage_qualifier
    owner: gene expression mixin
    range: life stage
  phenotypic state:
    name: phenotypic state
    description: in experiments (e.g. gene expression) assaying diseased or unhealthy
      tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues,
      use XXX.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: phenotypic_state
    owner: gene expression mixin
    range: disease or phenotypic feature

```
</details>