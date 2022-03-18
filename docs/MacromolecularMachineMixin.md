# Class: MacromolecularMachineMixin
_A union of gene locus, gene product, and macromolecular complex mixin. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:MacromolecularMachineMixin](https://w3id.org/biolink/vocab/MacromolecularMachineMixin)




## Inheritance

* **MacromolecularMachineMixin**
    * [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * [MacromolecularComplexMixin](MacromolecularComplexMixin.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name](name.md) | [symbol_type](symbol_type.md) | 0..1 | genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MolecularActivity](MolecularActivity.md) | [enabled_by](enabled_by.md) | range | macromolecular machine mixin |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [catalyst_qualifier](catalyst_qualifier.md) | range | macromolecular machine mixin |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject](subject.md) | range | macromolecular machine mixin |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject](subject.md) | domain | macromolecular machine mixin |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject](subject.md) | range | macromolecular machine mixin |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject](subject.md) | domain | macromolecular machine mixin |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject](subject.md) | range | macromolecular machine mixin |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject](subject.md) | domain | macromolecular machine mixin |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject](subject.md) | range | macromolecular machine mixin |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: macromolecular machine mixin
description: A union of gene locus, gene product, and macromolecular complex mixin.
  These are the basic units of function in a cell. They either carry out individual
  biological activities, or they encode molecules which do this.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- name
slot_usage:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    range: symbol type

```
</details>

### Induced

<details>
```yaml
name: macromolecular machine mixin
description: A union of gene locus, gene product, and macromolecular complex mixin.
  These are the basic units of function in a cell. They either carry out individual
  biological activities, or they encode molecules which do this.
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slot_usage:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    range: symbol type
attributes:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: macromolecular machine mixin
    range: symbol type

```
</details>