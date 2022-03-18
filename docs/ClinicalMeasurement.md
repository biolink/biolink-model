# Class: ClinicalMeasurement
_A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot._





URI: [biolink:ClinicalMeasurement](https://w3id.org/biolink/vocab/ClinicalMeasurement)




## Inheritance

* [Annotation](Annotation.md)
    * [Attribute](Attribute.md) [ ontology class]
        * [ClinicalAttribute](ClinicalAttribute.md)
            * **ClinicalMeasurement**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [has_attribute_type](has_attribute_type.md) | [OntologyClass](OntologyClass.md) | 1..1 | connects an attribute to a class that describes it  | . |
| [has_quantitative_value](has_quantitative_value.md) | [QuantityValue](QuantityValue.md) | 0..* | connects an attribute to a value  | . |
| [has_qualitative_value](has_qualitative_value.md) | [NamedThing](NamedThing.md) | 0..1 | connects an attribute to a value  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [source](source.md) | [label_type](label_type.md) | 0..1 | a lightweight analog to the association class 'provided by' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: clinical measurement
exact_mappings:
- EFO:0001444
description: A clinical measurement is a special kind of attribute which results from
  a laboratory observation from a subject individual or sample. Measurements can be
  connected to their subject by the 'has attribute' slot.
from_schema: https://w3id.org/biolink/biolink-model
is_a: clinical attribute
slot_usage:
  has attribute type:
    name: has attribute type
    values_from:
    - EFO
    - LOINC
    multivalued: false
    required: true

```
</details>

### Induced

<details>
```yaml
name: clinical measurement
exact_mappings:
- EFO:0001444
description: A clinical measurement is a special kind of attribute which results from
  a laboratory observation from a subject individual or sample. Measurements can be
  connected to their subject by the 'has attribute' slot.
from_schema: https://w3id.org/biolink/biolink-model
is_a: clinical attribute
slot_usage:
  has attribute type:
    name: has attribute type
    values_from:
    - EFO
    - LOINC
    multivalued: false
    required: true
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
    owner: clinical measurement
    range: label type
  has attribute type:
    name: has attribute type
    description: connects an attribute to a class that describes it
    from_schema: https://w3id.org/biolink/biolink-model
    values_from:
    - EFO
    - LOINC
    domain: attribute
    multivalued: false
    alias: has_attribute_type
    owner: clinical measurement
    range: ontology class
    required: true
  has quantitative value:
    name: has quantitative value
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: true
    alias: has_quantitative_value
    owner: clinical measurement
    range: quantity value
  has qualitative value:
    name: has qualitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: false
    alias: has_qualitative_value
    owner: clinical measurement
    range: named thing
  iri:
    name: iri
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    alias: iri
    owner: clinical measurement
    range: iri type
  source:
    name: source
    description: a lightweight analog to the association class 'provided by' slot,
      which is the string name, or the authoritative (i.e. database) namespace, designating
      the origin of the entity to which the slot belongs.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: clinical measurement
    range: label type

```
</details>