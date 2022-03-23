# Class: EnvironmentalExposure
_A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants._





URI: [biolink:EnvironmentalExposure](https://w3id.org/biolink/vocab/EnvironmentalExposure)




## Inheritance

* **EnvironmentalExposure** [ exposure event]
    * [GeographicExposure](GeographicExposure.md) [ exposure event]




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
name: environmental exposure
description: A environmental exposure is a factor relating to abiotic processes in
  the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution)
  and water-born contaminants.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: environmental exposure
description: A environmental exposure is a factor relating to abiotic processes in
  the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution)
  and water-born contaminants.
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
    owner: environmental exposure
    range: time type

```
</details>