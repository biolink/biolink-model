---
parent: Classes
title: biolink:ExposureEvent
grand_parent: Browse Biolink Model
---

# Type: ExposureEvent


A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

URI: [biolink:ExposureEvent](https://w3id.org/biolink/vocab/ExposureEvent)

SIO:000955
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DiseaseToExposureAssociation]-%20object%201..1>\[ExposureEvent&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExposureEventToPhenotypicFeatureAssociation]-%20subject%201..1>\[ExposureEvent],%20\[ExposureEvent]^-\[Treatment],%20\[ExposureEvent]^-\[ChemicalExposure],%20\[BiologicalEntity]^-\[ExposureEvent])

---


## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Children

 * [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical substance
 * [Treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

## Referenced by class

 *  **[DiseaseToExposureAssociation](DiseaseToExposureAssociation.md)** *[disease to exposure association➞object](disease_to_exposure_association_object.md)*  <sub>REQ</sub>  **[ExposureEvent](ExposureEvent.md)**
 *  **[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md)** *[exposure event to phenotypic feature association➞subject](exposure_event_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[ExposureEvent](ExposureEvent.md)**

## Attributes


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

### Domain for slot:

 * [has receptor](has_receptor.md)  <sub>OPT</sub>
    * Description: the organism or organism part being exposed
    * range: [OrganismalEntity](OrganismalEntity.md)
 * [has route](has_route.md)  <sub>OPT</sub>
    * Description: the process that results in the stressor coming into direct contact with the receptor
    * range: [String](types/String.md)
 * [has stressor](has_stressor.md)  <sub>OPT</sub>
    * Description: the process or entity that the receptor is being exposed to
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | environment |
|  | | exposure |
|  | | experimental condition |
| **Mappings:** | | SIO:000955 |

