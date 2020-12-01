---
parent: Other Classes
title: biolink:Entity
grand_parent: Classes
layout: default
---

# Class: Entity


Root Biolink Model class for all things and informational relationships, real or imagined.

URI: [biolink:Entity](https://w3id.org/biolink/vocab/Entity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Attribute]%3Chas%20attribute%200..%2A-++[Entity%7Cid:string;iri:iri_type%20%3F;category:category_type%20%2B;type:string%20%3F;name:label_type%20%3F;description:narrative_text%20%3F;source:label_type%20%3F],[Agent]%3Cprovided%20by%200..%2A-%20[Entity],[Entity]%5E-[NamedThing],[Entity]%5E-[Association],[Attribute],[Association],[Agent])

---


## Children

 * [Association](Association.md) - A typed association between two entities, supported by evidence
 * [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class


## Attributes


### Own

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a resource. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)
