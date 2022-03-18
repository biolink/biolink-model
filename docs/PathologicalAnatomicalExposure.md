# Class: PathologicalAnatomicalExposure
_An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome._





URI: [biolink:PathologicalAnatomicalExposure](https://w3id.org/biolink/vocab/PathologicalAnatomicalExposure)




## Inheritance

* **PathologicalAnatomicalExposure** [ exposure event]




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
name: pathological anatomical exposure
description: An abnormal anatomical structure, when viewed as an exposure, representing
  an precondition, leading to or influencing an outcome, e.g. thrombosis leading to
  an ischemic disease outcome.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: pathological anatomical exposure
description: An abnormal anatomical structure, when viewed as an exposure, representing
  an precondition, leading to or influencing an outcome, e.g. thrombosis leading to
  an ischemic disease outcome.
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
    owner: pathological anatomical exposure
    range: time type

```
</details>