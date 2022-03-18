# Class: DrugExposure
_A drug exposure is an intake of a particular drug._





URI: [biolink:DrugExposure](https://w3id.org/biolink/vocab/DrugExposure)




## Inheritance

* [ChemicalExposure](ChemicalExposure.md) [ exposure event]
    * **DrugExposure** [ exposure event]
        * [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) [ gene grouping mixin]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: drug exposure
aliases:
- drug intake
- drug dose
- medication intake
exact_mappings:
- ECTO:0000509
broad_mappings:
- SIO:001005
description: A drug exposure is an intake of a particular drug.
from_schema: https://w3id.org/biolink/biolink-model
is_a: chemical exposure
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: drug exposure
aliases:
- drug intake
- drug dose
- medication intake
exact_mappings:
- ECTO:0000509
broad_mappings:
- SIO:001005
description: A drug exposure is an intake of a particular drug.
from_schema: https://w3id.org/biolink/biolink-model
is_a: chemical exposure
mixins:
- exposure event
attributes:
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: drug exposure
    range: time type

```
</details>