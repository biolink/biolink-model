---
parent: Classes
title: biolink:Attribute
grand_parent: Browse Biolink Model
---

# Type: Attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)

SIO:000614
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<has%20qualitative%20value%200..1-%20\[Attribute&#124;id:identifier_type;name:label_type;category:iri_type%20%2B],%20\[QuantityValue]<has%20quantitative%20value%200..*-++\[Attribute],%20\[OntologyClass]<has%20attribute%20type%200..1-%20\[Attribute],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[Attribute]^-\[Zygosity],%20\[Attribute]^-\[SeverityValue],%20\[Attribute]^-\[Onset],%20\[Attribute]^-\[FrequencyValue],%20\[Attribute]^-\[ClinicalModifier],%20\[Attribute]^-\[BiologicalSex],%20\[AbstractEntity]^-\[Attribute])

---


## Parents

 *  is_a: [AbstractEntity](AbstractEntity.md) - Any thing that is not a process or a physical mass-bearing entity

## Uses Mixins

 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Children

 * [BiologicalSex](BiologicalSex.md)
 * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Onset](Onset.md) - The age group in which manifestations appear
 * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 * [Zygosity](Zygosity.md)

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:000614 |
| **In Subsets:** | | samples |

