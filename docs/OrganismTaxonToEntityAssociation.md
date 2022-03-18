# Class: OrganismTaxonToEntityAssociation
_An association between an organism taxon and another entity_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:OrganismTaxonToEntityAssociation](https://w3id.org/biolink/vocab/OrganismTaxonToEntityAssociation)



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
name: organism taxon to entity association
description: An association between an organism taxon and another entity
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: organism taxon that is the subject of the association
    range: organism taxon
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: organism taxon to entity association
description: An association between an organism taxon and another entity
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: organism taxon that is the subject of the association
    range: organism taxon
defining_slots:
- subject

```
</details>