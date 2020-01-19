---
parent: Classes
title: biolink:MaterialSample
grand_parent: Browse Biolink Model
---

# Type: MaterialSample


A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]

URI: [biolink:MaterialSample](https://w3id.org/biolink/vocab/MaterialSample)

OBI:0000747
{: .mapping-label }

SIO:001050
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Attribute]<has%20attribute%200..*-%20\[MaterialSample&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[MaterialSampleDerivationAssociation]-%20subject%201..1>\[MaterialSample],%20\[MaterialSampleToThingAssociation]-%20subject%201..1>\[MaterialSample],%20\[MaterialSample]uses%20-.->\[SubjectOfInvestigation],%20\[MaterialSample]uses%20-.->\[PhysicalEntity],%20\[NamedThing]^-\[MaterialSample])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [SubjectOfInvestigation](SubjectOfInvestigation.md) - An entity that has the role of being studied in an investigation, study, or experiment
 *  mixin: [PhysicalEntity](PhysicalEntity.md) - An entity that has physical properties such as mass, volume, or charge

## Referenced by class

 *  **[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)** *[material sample derivation association➞subject](material_sample_derivation_association_subject.md)*  <sub>REQ</sub>  **[MaterialSample](MaterialSample.md)**
 *  **[MaterialSampleToThingAssociation](MaterialSampleToThingAssociation.md)** *[material sample to thing association➞subject](material_sample_to_thing_association_subject.md)*  <sub>REQ</sub>  **[MaterialSample](MaterialSample.md)**

## Attributes


### Own

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | biospecimen |
|  | | sample |
|  | | biosample |
|  | | physical sample |
| **Mappings:** | | OBI:0000747 |
|  | | SIO:001050 |

