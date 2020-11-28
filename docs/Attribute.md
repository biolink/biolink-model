---
parent: Other Classes
title: biolink:Attribute
grand_parent: Classes
layout: default
---

# Class: Attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[SeverityValue],[ResourceMixin],[QuantityValue],[OntologyClass],[NamedThing],[Inheritance],[FrequencyValue],[ClinicalModifier],[ClinicalCourse],[BiologicalSex],[NamedThing]%3Chas%20qualitative%20value%200..1-%20[Attribute%7Cname:label_type%20%3F;iri:iri_type%20%3F;source:label_type%20%3F],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[Attribute],[OntologyClass]%3Chas%20attribute%20type%201..1-%20[Attribute],[AttributeMixin]++-%20has%20attribute%200..%2A%3E[Attribute],[Attribute]uses%20-.-%3E[ResourceMixin],[Attribute]%5E-[Zygosity],[Attribute]%5E-[SeverityValue],[Attribute]%5E-[Inheritance],[Attribute]%5E-[FrequencyValue],[Attribute]%5E-[ClinicalModifier],[Attribute]%5E-[ClinicalCourse],[Attribute]%5E-[BiologicalSex],[AbstractEntity]%5E-[Attribute],[AttributeMixin],[AbstractEntity])

---


## Identifier prefixes

 * EDAM-DATA
 * EDAM-FORMAT
 * EDAM-OPERATION
 * EDAM-TOPIC

## Parents

 *  is_a: [AbstractEntity](AbstractEntity.md) - Any thing that is not a process or a physical mass-bearing entity

## Uses Mixins

 *  mixin: [ResourceMixin](ResourceMixin.md)

## Children

 * [BiologicalSex](BiologicalSex.md)
 * [ClinicalCourse](ClinicalCourse.md) - The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
 * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, and other aspects
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Inheritance](Inheritance.md) - The pattern in which a particular genetic trait or disorder is passed from one generation to the next
 * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 * [Zygosity](Zygosity.md)

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has attribute type](has_attribute_type.md)  <sub>REQ</sub>
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

### Inherited from resource mixin:

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has attribute type](has_attribute_type.md)  <sub>REQ</sub>
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
| **In Subsets:** | | samples |
| **Exact Mappings:** | | SIO:000614 |

