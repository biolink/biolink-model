# Class: PhenotypicQuality
_A property of a phenotype_





URI: [biolink:PhenotypicQuality](https://w3id.org/biolink/vocab/PhenotypicQuality)




## Inheritance

* [Annotation](Annotation.md)
    * [Attribute](Attribute.md) [ ontology class]
        * [OrganismAttribute](OrganismAttribute.md)
            * **PhenotypicQuality**




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
name: phenotypic quality
aliases:
- phenotypic properties
mappings:
- PATO:0000001
description: A property of a phenotype
examples:
- value: weight
from_schema: https://w3id.org/biolink/biolink-model
is_a: organism attribute

```
</details>

### Induced

<details>
```yaml
name: phenotypic quality
aliases:
- phenotypic properties
mappings:
- PATO:0000001
description: A property of a phenotype
examples:
- value: weight
from_schema: https://w3id.org/biolink/biolink-model
is_a: organism attribute
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
    owner: phenotypic quality
    range: label type
  has attribute type:
    name: has attribute type
    narrow_mappings:
    - LOINC:has_modality_type
    - LOINC:has_view_type
    description: connects an attribute to a class that describes it
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: attribute
    multivalued: false
    alias: has_attribute_type
    owner: phenotypic quality
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
    owner: phenotypic quality
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
    owner: phenotypic quality
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
    owner: phenotypic quality
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
    owner: phenotypic quality
    range: label type

```
</details>