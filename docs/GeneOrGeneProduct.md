# Class: GeneOrGeneProduct
_A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneOrGeneProduct](https://w3id.org/biolink/vocab/GeneOrGeneProduct)




## Inheritance

* [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * **GeneOrGeneProduct**
        * [GeneProductMixin](GeneProductMixin.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name](name.md) | [symbol_type](symbol_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object](object.md) | range | gene or gene product |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object](object.md) | range | gene or gene product |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object](object.md) | range | gene or gene product |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject](subject.md) | range | gene or gene product |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object](object.md) | range | gene or gene product |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object](object.md) | range | gene or gene product |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [object](object.md) | range | gene or gene product |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object](object.md) | range | gene or gene product |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject](subject.md) | range | gene or gene product |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [subject](subject.md) | range | gene or gene product |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [object](object.md) | range | gene or gene product |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEMBL.TARGET

* IUPHAR.FAMILY










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene or gene product
id_prefixes:
- CHEMBL.TARGET
- IUPHAR.FAMILY
description: A union of gene loci or gene products. Frequently an identifier for one
  will be used as proxy for another
from_schema: https://w3id.org/biolink/biolink-model
is_a: macromolecular machine mixin
mixin: true

```
</details>

### Induced

<details>
```yaml
name: gene or gene product
id_prefixes:
- CHEMBL.TARGET
- IUPHAR.FAMILY
description: A union of gene loci or gene products. Frequently an identifier for one
  will be used as proxy for another
from_schema: https://w3id.org/biolink/biolink-model
is_a: macromolecular machine mixin
mixin: true
attributes:
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: gene or gene product
    range: symbol type

```
</details>