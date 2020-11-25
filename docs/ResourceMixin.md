---
parent: Class Mixins
title: biolink:ResourceMixin
grand_parent: Classes
layout: default
---

# Class: ResourceMixin




URI: [biolink:ResourceMixin](https://w3id.org/biolink/vocab/ResourceMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]uses%20-.-%3E[ResourceMixin%7Ciri:iri_type%20%3F;name:label_type%20%3F;source:label_type%20%3F],[Attribute]uses%20-.-%3E[ResourceMixin],[NamedThing],[Attribute])

---


## Mixin for

 * [Attribute](Attribute.md) (mixin)  - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 * [NamedThing](NamedThing.md) (mixin)  - a databased entity or concept/class

## Referenced by class


## Attributes


### Own

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
