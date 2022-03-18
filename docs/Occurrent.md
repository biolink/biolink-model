# Class: Occurrent
_A processual entity._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:Occurrent](https://w3id.org/biolink/vocab/Occurrent)




## Inheritance

* [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md)
    * **Occurrent**
        * [ActivityAndBehavior](ActivityAndBehavior.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_input](has_input.md) | domain | occurrent |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_output](has_output.md) | domain | occurrent |
| [MolecularActivity](MolecularActivity.md) | [has_input](has_input.md) | domain | occurrent |
| [MolecularActivity](MolecularActivity.md) | [has_output](has_output.md) | domain | occurrent |
| [BiologicalProcess](BiologicalProcess.md) | [has_input](has_input.md) | domain | occurrent |
| [BiologicalProcess](BiologicalProcess.md) | [has_output](has_output.md) | domain | occurrent |
| [Pathway](Pathway.md) | [has_input](has_input.md) | domain | occurrent |
| [Pathway](Pathway.md) | [has_output](has_output.md) | domain | occurrent |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_input](has_input.md) | domain | occurrent |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_output](has_output.md) | domain | occurrent |
| [Behavior](Behavior.md) | [has_input](has_input.md) | domain | occurrent |
| [Behavior](Behavior.md) | [has_output](has_output.md) | domain | occurrent |
| [PathologicalProcess](PathologicalProcess.md) | [has_input](has_input.md) | domain | occurrent |
| [PathologicalProcess](PathologicalProcess.md) | [has_output](has_output.md) | domain | occurrent |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: occurrent
exact_mappings:
- BFO:0000003
description: A processual entity.
from_schema: https://w3id.org/biolink/biolink-model
is_a: physical essence or occurrent
mixin: true

```
</details>

### Induced

<details>
```yaml
name: occurrent
exact_mappings:
- BFO:0000003
description: A processual entity.
from_schema: https://w3id.org/biolink/biolink-model
is_a: physical essence or occurrent
mixin: true

```
</details>