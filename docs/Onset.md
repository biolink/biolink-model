---
parent: Classes
title: biolink:Onset
grand_parent: Browse Biolink Model
layout: default
---

# Type: Onset


The age group in which manifestations appear

URI: [biolink:Onset](https://w3id.org/biolink/vocab/Onset)

HP:0003674
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[OntologyClass],[EntityToFeatureOrDiseaseQualifiers]-%20onset%20qualifier%200..1%3E[Onset%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[ClinicalCourse]%5E-[Onset],[NamedThing],[EntityToFeatureOrDiseaseQualifiers],[ClinicalCourse],[Association])

---


## Parents

 *  is_a: [ClinicalCourse](ClinicalCourse.md) - The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual

## Referenced by class

 *  **[Association](Association.md)** *[onset qualifier](onset_qualifier.md)*  <sub>OPT</sub>  **[Onset](Onset.md)**

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

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | HP:0003674 |

