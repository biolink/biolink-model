# Class: PathologicalProcessExposure
_A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease._





URI: [biolink:PathologicalProcessExposure](https://w3id.org/biolink/vocab/PathologicalProcessExposure)




## Inheritance

* **PathologicalProcessExposure** [ exposure event]




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
name: pathological process exposure
description: A pathological process, when viewed as an exposure, representing a precondition,
  leading to or influencing an outcome, e.g. autoimmunity leading to disease.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: pathological process exposure
description: A pathological process, when viewed as an exposure, representing a precondition,
  leading to or influencing an outcome, e.g. autoimmunity leading to disease.
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
    owner: pathological process exposure
    range: time type

```
</details>