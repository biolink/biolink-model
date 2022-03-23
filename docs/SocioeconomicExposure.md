# Class: SocioeconomicExposure
_A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty)._





URI: [biolink:SocioeconomicExposure](https://w3id.org/biolink/vocab/SocioeconomicExposure)




## Inheritance

* **SocioeconomicExposure** [ exposure event]




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
name: socioeconomic exposure
description: A socioeconomic exposure is a factor relating to social and financial
  status of an affected individual (e.g. poverty).
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
slot_usage:
  has attribute:
    name: has attribute
    range: socioeconomic attribute
    required: true

```
</details>

### Induced

<details>
```yaml
name: socioeconomic exposure
description: A socioeconomic exposure is a factor relating to social and financial
  status of an affected individual (e.g. poverty).
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
slot_usage:
  has attribute:
    name: has attribute
    range: socioeconomic attribute
    required: true
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
    owner: socioeconomic exposure
    range: time type

```
</details>