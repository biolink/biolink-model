# Class: DiseaseOrPhenotypicFeatureExposure
_A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer._





URI: [biolink:DiseaseOrPhenotypicFeatureExposure](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureExposure)




## Inheritance

* **DiseaseOrPhenotypicFeatureExposure** [ exposure event pathological entity mixin]




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
name: disease or phenotypic feature exposure
description: A disease or phenotypic feature state, when viewed as an exposure, represents
  an precondition, leading to or influencing an outcome, e.g. HIV predisposing an
  individual to infections; a relative deficiency of skin pigmentation predisposing
  an individual to skin cancer.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
- pathological entity mixin

```
</details>

### Induced

<details>
```yaml
name: disease or phenotypic feature exposure
description: A disease or phenotypic feature state, when viewed as an exposure, represents
  an precondition, leading to or influencing an outcome, e.g. HIV predisposing an
  individual to infections; a relative deficiency of skin pigmentation predisposing
  an individual to skin cancer.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
- pathological entity mixin
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
    owner: disease or phenotypic feature exposure
    range: time type

```
</details>