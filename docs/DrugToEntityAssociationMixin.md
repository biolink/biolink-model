# Class: DrugToEntityAssociationMixin
_An interaction between a drug and another entity_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:DrugToEntityAssociationMixin](https://w3id.org/biolink/vocab/DrugToEntityAssociationMixin)




## Inheritance

* [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md)
    * **DrugToEntityAssociationMixin**




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
name: drug to entity association mixin
description: An interaction between a drug and another entity
from_schema: https://w3id.org/biolink/biolink-model
is_a: chemical entity to entity association mixin
mixin: true
slot_usage:
  subject:
    name: subject
    description: the drug that is an interactor
    range: drug
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: drug to entity association mixin
description: An interaction between a drug and another entity
from_schema: https://w3id.org/biolink/biolink-model
is_a: chemical entity to entity association mixin
mixin: true
slot_usage:
  subject:
    name: subject
    description: the drug that is an interactor
    range: drug
defining_slots:
- subject

```
</details>