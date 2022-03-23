# Class: ExposureEvent
_A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:ExposureEvent](https://w3id.org/biolink/vocab/ExposureEvent)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object](object.md) | range | exposure event |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | exposure event |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: exposure event
aliases:
- exposure
- experimental condition
exact_mappings:
- XCO:0000000
description: A (possibly time bounded) incidence of a feature of the environment of
  an organism that influences one or more phenotypic features of that organism, potentially
  mediated by genes
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- timepoint

```
</details>

### Induced

<details>
```yaml
name: exposure event
aliases:
- exposure
- experimental condition
exact_mappings:
- XCO:0000000
description: A (possibly time bounded) incidence of a feature of the environment of
  an organism that influences one or more phenotypic features of that organism, potentially
  mediated by genes
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
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
    owner: exposure event
    range: time type

```
</details>