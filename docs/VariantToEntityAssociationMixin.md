# Class: VariantToEntityAssociationMixin



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:VariantToEntityAssociationMixin](https://w3id.org/biolink/vocab/VariantToEntityAssociationMixin)



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
name: variant to entity association mixin
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: variant annotation
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: a sequence variant in which the allele state is associated with some
      other entity
    examples:
    - value: ClinVar:38077
      description: ClinVar representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    - value: ClinGen:CA024716
      description: chr13:g.32921033G>C (hg19) in ClinGen
    range: sequence variant
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: variant to entity association mixin
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: variant annotation
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: a sequence variant in which the allele state is associated with some
      other entity
    examples:
    - value: ClinVar:38077
      description: ClinVar representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    - value: ClinGen:CA024716
      description: chr13:g.32921033G>C (hg19) in ClinGen
    range: sequence variant
defining_slots:
- subject

```
</details>