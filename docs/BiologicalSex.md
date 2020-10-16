---
parent: Classes
title: biolink:BiologicalSex
grand_parent: Browse Biolink Model
layout: default
---

# Type: BiologicalSex




URI: [biolink:BiologicalSex](https://w3id.org/biolink/vocab/BiologicalSex)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[PhenotypicSex],[OntologyClass],[NamedThing],[GenotypicSex],[EntityToPhenotypicFeatureAssociation]-%20sex%20qualifier%200..1%3E[BiologicalSex%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[BiologicalSex]%5E-[PhenotypicSex],[BiologicalSex]%5E-[GenotypicSex],[Attribute]%5E-[BiologicalSex],[EntityToPhenotypicFeatureAssociation],[Attribute],[Association])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Children

 * [GenotypicSex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
 * [PhenotypicSex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.

## Referenced by class

 *  **[Association](Association.md)** *[sex qualifier](sex_qualifier.md)*  <sub>OPT</sub>  **[BiologicalSex](BiologicalSex.md)**

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

### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
