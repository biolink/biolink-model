---
parent: Classes
title: biolink:PhenotypicSex
grand_parent: Browse Biolink Model
layout: default
---

# Type: PhenotypicSex


An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.

URI: [biolink:PhenotypicSex](https://w3id.org/biolink/vocab/PhenotypicSex)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[BiologicalSex]%5E-[PhenotypicSex%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[OntologyClass],[NamedThing],[BiologicalSex])

---


## Parents

 *  is_a: [BiologicalSex](BiologicalSex.md)

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
