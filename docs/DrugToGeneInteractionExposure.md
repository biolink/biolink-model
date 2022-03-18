# Class: DrugToGeneInteractionExposure
_drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome._





URI: [biolink:DrugToGeneInteractionExposure](https://w3id.org/biolink/vocab/DrugToGeneInteractionExposure)




## Inheritance

* [ChemicalExposure](ChemicalExposure.md) [ exposure event]
    * [DrugExposure](DrugExposure.md) [ exposure event]
        * **DrugToGeneInteractionExposure** [ gene grouping mixin]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | [Gene](Gene.md) | 0..* | connects an entity with one or more gene or gene products  | . |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: drug to gene interaction exposure
description: drug to gene interaction exposure is a drug exposure is where the interactions
  of the drug with specific genes are known to constitute an 'exposure' to the organism,
  leading to or influencing an outcome.
from_schema: https://w3id.org/biolink/biolink-model
is_a: drug exposure
mixins:
- gene grouping mixin

```
</details>

### Induced

<details>
```yaml
name: drug to gene interaction exposure
description: drug to gene interaction exposure is a drug exposure is where the interactions
  of the drug with specific genes are known to constitute an 'exposure' to the organism,
  leading to or influencing an outcome.
from_schema: https://w3id.org/biolink/biolink-model
is_a: drug exposure
mixins:
- gene grouping mixin
attributes:
  has gene or gene product:
    name: has gene or gene product
    description: connects an entity with one or more gene or gene products
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: has_gene_or_gene_product
    owner: drug to gene interaction exposure
    range: gene
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: drug to gene interaction exposure
    range: time type

```
</details>