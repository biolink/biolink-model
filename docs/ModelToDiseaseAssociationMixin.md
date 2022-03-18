# Class: ModelToDiseaseAssociationMixin
_This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:ModelToDiseaseAssociationMixin](https://w3id.org/biolink/vocab/ModelToDiseaseAssociationMixin)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: model to disease association mixin
description: This mixin is used for any association class for which the subject (source
  node) plays the role of a 'model', in that it recapitulates some features of the
  disease in a way that is useful for studying the disease outside a patient carrying
  the disease
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: The entity that serves as the model of the disease. This may be an
      organism, a strain of organism, a genotype or variant that exhibits similar
      features, or a gene that when mutated exhibits features of the disease
  predicate:
    name: predicate
    description: The relationship to the disease
    subproperty_of: model of

```
</details>

### Induced

<details>
```yaml
name: model to disease association mixin
description: This mixin is used for any association class for which the subject (source
  node) plays the role of a 'model', in that it recapitulates some features of the
  disease in a way that is useful for studying the disease outside a patient carrying
  the disease
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: The entity that serves as the model of the disease. This may be an
      organism, a strain of organism, a genotype or variant that exhibits similar
      features, or a gene that when mutated exhibits features of the disease
  predicate:
    name: predicate
    description: The relationship to the disease
    subproperty_of: model of

```
</details>