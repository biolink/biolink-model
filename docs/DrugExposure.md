---
parent: Entities
title: biolink:DrugExposure
grand_parent: Classes
layout: default
---

# Class: DrugExposure


A drug exposure is an intake of a particular chemical substance

URI: [biolink:DrugExposure](https://w3id.org/biolink/vocab/DrugExposure)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Treatment],[NamedThing],[ChemicalSubstance]%3Chas%20drug%201..%2A-%20[DrugExposure%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Treatment]-%20has%20part%201..%2A%3E[DrugExposure],[ChemicalExposure]%5E-[DrugExposure],[ChemicalSubstance],[ChemicalExposure],[Attribute],[Agent])

---


## Parents

 *  is_a: [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical substance

## Referenced by class

 *  **[Treatment](Treatment.md)** *[treatment➞has part](treatment_has_part.md)*  <sub>1..*</sub>  **[DrugExposure](DrugExposure.md)**

## Attributes


### Own

 * [drug exposure➞has drug](drug_exposure_has_drug.md)  <sub>1..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a resource. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [drug exposure➞has drug](drug_exposure_has_drug.md)  <sub>1..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | drug intake |
|  | | drug dose |
| **Exact Mappings:** | | ECTO:0000509 |
| **Broad Mappings:** | | SIO:001005 |

