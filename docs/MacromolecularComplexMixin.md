# Class: MacromolecularComplexMixin
_A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:MacromolecularComplexMixin](https://w3id.org/biolink/vocab/MacromolecularComplexMixin)




## Inheritance

* [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * **MacromolecularComplexMixin**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name](name.md) | [symbol_type](symbol_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |


## Usages



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* INTACT

* GO

* PR

* REACT










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: macromolecular complex mixin
id_prefixes:
- INTACT
- GO
- PR
- REACT
exact_mappings:
- GO:0032991
- WIKIDATA:Q22325163
description: A stable assembly of two or more macromolecules, i.e. proteins, nucleic
  acids, carbohydrates or lipids, in which at least one component is a protein and
  the constituent parts function together.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: macromolecular machine mixin
mixin: true

```
</details>

### Induced

<details>
```yaml
name: macromolecular complex mixin
id_prefixes:
- INTACT
- GO
- PR
- REACT
exact_mappings:
- GO:0032991
- WIKIDATA:Q22325163
description: A stable assembly of two or more macromolecules, i.e. proteins, nucleic
  acids, carbohydrates or lipids, in which at least one component is a protein and
  the constituent parts function together.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: macromolecular machine mixin
mixin: true
attributes:
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: macromolecular complex mixin
    range: symbol type

```
</details>