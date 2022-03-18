# Class: MaterialSampleToEntityAssociationMixin
_An association between a material sample and something._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:MaterialSampleToEntityAssociationMixin](https://w3id.org/biolink/vocab/MaterialSampleToEntityAssociationMixin)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: material sample to entity association mixin
description: An association between a material sample and something.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the material sample being described
    range: material sample
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: material sample to entity association mixin
description: An association between a material sample and something.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the material sample being described
    range: material sample
defining_slots:
- subject

```
</details>