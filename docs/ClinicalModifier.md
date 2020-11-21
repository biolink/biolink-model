---
parent: Other Classes
title: biolink:ClinicalModifier
grand_parent: Classes
layout: default
---

# Class: ClinicalModifier


Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, and other aspects

URI: [biolink:ClinicalModifier](https://w3id.org/biolink/vocab/ClinicalModifier)

HP:0012823
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[OntologyClass],[NamedThing],[Attribute]%5E-[ClinicalModifier],[Attribute],[Association])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Referenced by class

 *  **[Association](Association.md)** *[clinical modifier qualifier](clinical_modifier_qualifier.md)*  <sub>OPT</sub>  **[ClinicalModifier](ClinicalModifier.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | HP:0012823 |

