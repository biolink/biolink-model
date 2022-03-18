# Class: EntityToFeatureOrDiseaseQualifiersMixin
_Qualifiers for entity to disease or phenotype associations._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:EntityToFeatureOrDiseaseQualifiersMixin](https://w3id.org/biolink/vocab/EntityToFeatureOrDiseaseQualifiersMixin)




## Inheritance

* [FrequencyQualifierMixin](FrequencyQualifierMixin.md)
    * **EntityToFeatureOrDiseaseQualifiersMixin**
        * [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)
        * [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [severity_qualifier](severity_qualifier.md) | [SeverityValue](SeverityValue.md) | 0..1 | a qualifier used in a phenotypic association to state how severe the phenotype is in the subject  | . |
| [onset_qualifier](onset_qualifier.md) | [Onset](Onset.md) | 0..1 | a qualifier used in a phenotypic association to state when the phenotype appears is in the subject  | . |
| [frequency_qualifier](frequency_qualifier.md) | [frequency_value](frequency_value.md) | 0..1 | a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: entity to feature or disease qualifiers mixin
description: Qualifiers for entity to disease or phenotype associations.
from_schema: https://w3id.org/biolink/biolink-model
is_a: frequency qualifier mixin
mixin: true
slots:
- severity qualifier
- onset qualifier

```
</details>

### Induced

<details>
```yaml
name: entity to feature or disease qualifiers mixin
description: Qualifiers for entity to disease or phenotype associations.
from_schema: https://w3id.org/biolink/biolink-model
is_a: frequency qualifier mixin
mixin: true
attributes:
  severity qualifier:
    name: severity qualifier
    description: a qualifier used in a phenotypic association to state how severe
      the phenotype is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: severity_qualifier
    owner: entity to feature or disease qualifiers mixin
    range: severity value
  onset qualifier:
    name: onset qualifier
    description: a qualifier used in a phenotypic association to state when the phenotype
      appears is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: onset_qualifier
    owner: entity to feature or disease qualifiers mixin
    range: onset
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: frequency_qualifier
    owner: entity to feature or disease qualifiers mixin
    range: frequency value

```
</details>