# Class: QuantityValue
_A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value_





URI: [biolink:QuantityValue](https://w3id.org/biolink/vocab/QuantityValue)




## Inheritance

* [Annotation](Annotation.md)
    * **QuantityValue**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_unit](has_unit.md) | [unit](unit.md) | 0..1 | connects a quantity value to a unit  | . |
| [has_numeric_value](has_numeric_value.md) | [double](double.md) | 0..1 | connects a quantity value to a number  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QuantityValue](QuantityValue.md) | [has_unit](has_unit.md) | domain | quantity value |
| [QuantityValue](QuantityValue.md) | [has_numeric_value](has_numeric_value.md) | domain | quantity value |
| [Attribute](Attribute.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [BiologicalSex](BiologicalSex.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [PhenotypicSex](PhenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [GenotypicSex](GenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [SeverityValue](SeverityValue.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [OrganismAttribute](OrganismAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [Inheritance](Inheritance.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [Zygosity](Zygosity.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [ClinicalModifier](ClinicalModifier.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [ClinicalCourse](ClinicalCourse.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [Onset](Onset.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [ChemicalExposure](ChemicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [DrugExposure](DrugExposure.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_quantitative_value](has_quantitative_value.md) | range | quantity value |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: quantity value
description: A value of an attribute that is quantitative and measurable, expressed
  as a combination of a unit and a numeric value
from_schema: https://w3id.org/biolink/biolink-model
is_a: annotation
slots:
- has unit
- has numeric value

```
</details>

### Induced

<details>
```yaml
name: quantity value
description: A value of an attribute that is quantitative and measurable, expressed
  as a combination of a unit and a numeric value
from_schema: https://w3id.org/biolink/biolink-model
is_a: annotation
attributes:
  has unit:
    name: has unit
    exact_mappings:
    - qud:unit
    - IAO:0000039
    close_mappings:
    - EFO:0001697
    - UO-PROPERTY:is_unit_of
    narrow_mappings:
    - SNOMED:has_concentration_strength_denominator_unit
    - SNOMED:has_concentration_strength_numerator_unit
    - SNOMED:has_presentation_strength_denominator_unit
    - SNOMED:has_presentation_strength_numerator_unit
    - SNOMED:has_unit_of_presentation
    description: connects a quantity value to a unit
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: quantity value
    multivalued: false
    alias: has_unit
    owner: quantity value
    range: unit
  has numeric value:
    name: has numeric value
    exact_mappings:
    - qud:quantityValue
    description: connects a quantity value to a number
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: quantity value
    multivalued: false
    alias: has_numeric_value
    owner: quantity value
    range: double

```
</details>