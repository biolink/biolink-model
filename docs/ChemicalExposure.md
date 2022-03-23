# Class: ChemicalExposure
_A chemical exposure is an intake of a particular chemical entity._





URI: [biolink:ChemicalExposure](https://w3id.org/biolink/vocab/ChemicalExposure)




## Inheritance

* **ChemicalExposure** [ exposure event]
    * [DrugExposure](DrugExposure.md) [ exposure event]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_quantitative_value](has_quantitative_value.md) | [QuantityValue](QuantityValue.md) | 0..* | connects an attribute to a value  | . |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical exposure
exact_mappings:
- ECTO:9000000
- SIO:001399
description: A chemical exposure is an intake of a particular chemical entity.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
slots:
- has quantitative value

```
</details>

### Induced

<details>
```yaml
name: chemical exposure
exact_mappings:
- ECTO:9000000
- SIO:001399
description: A chemical exposure is an intake of a particular chemical entity.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
attributes:
  has quantitative value:
    name: has quantitative value
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: true
    alias: has_quantitative_value
    owner: chemical exposure
    range: quantity value
  timepoint:
    name: timepoint
    aliases:
    - duration
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: chemical exposure
    range: time type

```
</details>