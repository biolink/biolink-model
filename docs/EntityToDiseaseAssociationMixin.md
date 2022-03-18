# Class: EntityToDiseaseAssociationMixin
_mixin class for any association whose object (target node) is a disease_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:EntityToDiseaseAssociationMixin](https://w3id.org/biolink/vocab/EntityToDiseaseAssociationMixin)




## Inheritance

* [FrequencyQualifierMixin](FrequencyQualifierMixin.md)
    * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)
        * **EntityToDiseaseAssociationMixin**




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
name: entity to disease association mixin
description: mixin class for any association whose object (target node) is a disease
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity to feature or disease qualifiers mixin
mixin: true
slot_usage:
  object:
    name: object
    description: disease
    examples:
    - value: MONDO:0020066
      description: Ehlers-Danlos syndrome
    range: disease
defining_slots:
- object

```
</details>

### Induced

<details>
```yaml
name: entity to disease association mixin
description: mixin class for any association whose object (target node) is a disease
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity to feature or disease qualifiers mixin
mixin: true
slot_usage:
  object:
    name: object
    description: disease
    examples:
    - value: MONDO:0020066
      description: Ehlers-Danlos syndrome
    range: disease
attributes:
  severity qualifier:
    name: severity qualifier
    description: a qualifier used in a phenotypic association to state how severe
      the phenotype is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: severity_qualifier
    owner: entity to disease association mixin
    range: severity value
  onset qualifier:
    name: onset qualifier
    description: a qualifier used in a phenotypic association to state when the phenotype
      appears is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: onset_qualifier
    owner: entity to disease association mixin
    range: onset
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: frequency_qualifier
    owner: entity to disease association mixin
    range: frequency value
defining_slots:
- object

```
</details>