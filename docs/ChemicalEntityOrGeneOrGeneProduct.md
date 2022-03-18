# Class: ChemicalEntityOrGeneOrGeneProduct
_A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:ChemicalEntityOrGeneOrGeneProduct](https://w3id.org/biolink/vocab/ChemicalEntityOrGeneOrGeneProduct)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject](subject.md) | range | chemical entity or gene or gene product |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | chemical entity or gene or gene product |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject](subject.md) | range | chemical entity or gene or gene product |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [subject](subject.md) | range | chemical entity or gene or gene product |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical entity or gene or gene product
description: A union of chemical entities and children, and gene or gene product.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true

```
</details>

### Induced

<details>
```yaml
name: chemical entity or gene or gene product
description: A union of chemical entities and children, and gene or gene product.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true

```
</details>