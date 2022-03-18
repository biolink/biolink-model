# Class: FrequencyQualifierMixin
_Qualifier for frequency type associations_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:FrequencyQualifierMixin](https://w3id.org/biolink/vocab/FrequencyQualifierMixin)




## Inheritance

* **FrequencyQualifierMixin**
    * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [frequency_qualifier](frequency_qualifier.md) | [frequency_value](frequency_value.md) | 0..1 | a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: frequency qualifier mixin
description: Qualifier for frequency type associations
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- frequency qualifier

```
</details>

### Induced

<details>
```yaml
name: frequency qualifier mixin
description: Qualifier for frequency type associations
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
attributes:
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: frequency_qualifier
    owner: frequency qualifier mixin
    range: frequency value

```
</details>