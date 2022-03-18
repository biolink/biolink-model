# Class: GenotypeToEntityAssociationMixin



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GenotypeToEntityAssociationMixin](https://w3id.org/biolink/vocab/GenotypeToEntityAssociationMixin)



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
name: genotype to entity association mixin
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: genotype that is the subject of the association
    range: genotype
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: genotype to entity association mixin
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: genotype that is the subject of the association
    range: genotype
defining_slots:
- subject

```
</details>