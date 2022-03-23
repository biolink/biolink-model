# Class: BioticExposure
_An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses)._





URI: [biolink:BioticExposure](https://w3id.org/biolink/vocab/BioticExposure)




## Inheritance

* **BioticExposure** [ exposure event]




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
name: biotic exposure
aliases:
- viral exposure
- bacterial exposure
description: An external biotic exposure is an intake of (sometimes pathological)
  biological organisms (including viruses).
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: biotic exposure
aliases:
- viral exposure
- bacterial exposure
description: An external biotic exposure is an intake of (sometimes pathological)
  biological organisms (including viruses).
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
attributes:
  timepoint:
    name: timepoint
    aliases:
    - duration
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: biotic exposure
    range: time type

```
</details>