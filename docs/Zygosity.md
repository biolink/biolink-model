---
parent: Other Classes
title: biolink:Zygosity
grand_parent: Classes
layout: default
---

# Class: Zygosity




URI: [biolink:Zygosity](https://w3id.org/biolink/vocab/Zygosity)

GENO:0000133
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Genotype]++-%20has%20zygosity%200..1%3E[Zygosity],[Attribute]%5E-[Zygosity],[QuantityValue],[OntologyClass],[NamedThing],[Genotype],[GenomicEntity],[Attribute])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Referenced by class

 *  **[GenomicEntity](GenomicEntity.md)** *[has zygosity](has_zygosity.md)*  <sub>OPT</sub>  **[Zygosity](Zygosity.md)**

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
| **Mappings:** | | GENO:0000133 |

