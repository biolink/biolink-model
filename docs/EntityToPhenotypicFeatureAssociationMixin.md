# Class: EntityToPhenotypicFeatureAssociationMixin



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:EntityToPhenotypicFeatureAssociationMixin](https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociationMixin)




## Inheritance

* [FrequencyQualifierMixin](FrequencyQualifierMixin.md)
    * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)
        * **EntityToPhenotypicFeatureAssociationMixin**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [sex_qualifier](sex_qualifier.md) | [BiologicalSex](BiologicalSex.md) | 0..1 | a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.  | . |
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
name: entity to phenotypic feature association mixin
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity to feature or disease qualifiers mixin
mixin: true
slots:
- sex qualifier
slot_usage:
  object:
    name: object
    examples:
    - value: HP:0002487
      description: Hyperkinesis
    - value: WBPhenotype:0000180
      description: axon morphology variant
    - value: MP:0001569
      description: abnormal circulating bilirubin level
    values_from:
    - upheno
    - hp
    - mp
    - wbphenotype
    range: phenotypic feature
defining_slots:
- object

```
</details>

### Induced

<details>
```yaml
name: entity to phenotypic feature association mixin
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity to feature or disease qualifiers mixin
mixin: true
slot_usage:
  object:
    name: object
    examples:
    - value: HP:0002487
      description: Hyperkinesis
    - value: WBPhenotype:0000180
      description: axon morphology variant
    - value: MP:0001569
      description: abnormal circulating bilirubin level
    values_from:
    - upheno
    - hp
    - mp
    - wbphenotype
    range: phenotypic feature
attributes:
  sex qualifier:
    name: sex qualifier
    description: a qualifier used in a phenotypic association to state whether the
      association is specific to a particular sex.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: sex_qualifier
    owner: entity to phenotypic feature association mixin
    range: biological sex
  severity qualifier:
    name: severity qualifier
    description: a qualifier used in a phenotypic association to state how severe
      the phenotype is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: severity_qualifier
    owner: entity to phenotypic feature association mixin
    range: severity value
  onset qualifier:
    name: onset qualifier
    description: a qualifier used in a phenotypic association to state when the phenotype
      appears is in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: onset_qualifier
    owner: entity to phenotypic feature association mixin
    range: onset
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: frequency_qualifier
    owner: entity to phenotypic feature association mixin
    range: frequency value
defining_slots:
- object

```
</details>