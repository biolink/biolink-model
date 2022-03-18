# Class: GeneGroupingMixin
_any grouping of multiple genes or gene products_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneGroupingMixin](https://w3id.org/biolink/vocab/GeneGroupingMixin)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | [Gene](Gene.md) | 0..* | connects an entity with one or more gene or gene products  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene grouping mixin
description: any grouping of multiple genes or gene products
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- has gene or gene product

```
</details>

### Induced

<details>
```yaml
name: gene grouping mixin
description: any grouping of multiple genes or gene products
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
attributes:
  has gene or gene product:
    name: has gene or gene product
    description: connects an entity with one or more gene or gene products
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: has_gene_or_gene_product
    owner: gene grouping mixin
    range: gene

```
</details>