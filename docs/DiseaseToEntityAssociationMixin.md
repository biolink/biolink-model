# Class: DiseaseToEntityAssociationMixin



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:DiseaseToEntityAssociationMixin](https://w3id.org/biolink/vocab/DiseaseToEntityAssociationMixin)



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
name: disease to entity association mixin
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: disease class
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    values_from:
    - mondo
    - omim
    - orphanet
    - ncit
    - doid
    range: disease
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: disease to entity association mixin
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: disease class
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    values_from:
    - mondo
    - omim
    - orphanet
    - ncit
    - doid
    range: disease
defining_slots:
- subject

```
</details>