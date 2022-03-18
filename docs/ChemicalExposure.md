# Class: ChemicalExposure
_A chemical exposure is an intake of a particular chemical entity._





URI: [biolink:ChemicalExposure](https://w3id.org/biolink/vocab/ChemicalExposure)




## Inheritance

* **ChemicalExposure** [ exposure event]
    * [DrugExposure](DrugExposure.md) [ exposure event]




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
name: chemical exposure
exact_mappings:
- ECTO:9000000
- SIO:001399
description: A chemical exposure is an intake of a particular chemical entity.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event

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
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: chemical exposure
    range: time type

```
</details>