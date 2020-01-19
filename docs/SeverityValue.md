---
parent: Classes
title: biolink:SeverityValue
grand_parent: Browse Biolink Model
---

# Type: SeverityValue


describes the severity of a phenotypic feature or disease

URI: [biolink:SeverityValue](https://w3id.org/biolink/vocab/SeverityValue)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<has%20qualitative%20value(i)%200..1-%20\[SeverityValue&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[QuantityValue]<has%20quantitative%20value(i)%200..*-++\[SeverityValue],%20\[OntologyClass]<has%20attribute%20type(i)%200..1-%20\[SeverityValue],%20\[Attribute]^-\[SeverityValue])

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
    * inherited from: [Attribute](Attribute.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * inherited from: [Attribute](Attribute.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
