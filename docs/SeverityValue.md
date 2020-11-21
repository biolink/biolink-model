---
parent: Other Classes
title: biolink:SeverityValue
grand_parent: Classes
layout: default
---

# Class: SeverityValue


describes the severity of a phenotypic feature or disease

URI: [biolink:SeverityValue](https://w3id.org/biolink/vocab/SeverityValue)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EntityToFeatureOrDiseaseQualifiersMixin]++-%20severity%20qualifier%200..1%3E[SeverityValue],[Attribute]%5E-[SeverityValue],[QuantityValue],[OntologyClass],[NamedThing],[EntityToFeatureOrDiseaseQualifiersMixin],[Attribute],[Association])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Referenced by class

 *  **[Association](Association.md)** *[severity qualifier](severity_qualifier.md)*  <sub>OPT</sub>  **[SeverityValue](SeverityValue.md)**

## Attributes


### Inherited from attribute:

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
