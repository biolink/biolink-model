# Class: CaseToEntityAssociationMixin
_An abstract association for use where the case is the subject_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:CaseToEntityAssociationMixin](https://w3id.org/biolink/vocab/CaseToEntityAssociationMixin)



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
name: case to entity association mixin
description: An abstract association for use where the case is the subject
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the case (e.g. patient) that has the property
    range: case
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: case to entity association mixin
description: An abstract association for use where the case is the subject
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the case (e.g. patient) that has the property
    range: case
defining_slots:
- subject

```
</details>