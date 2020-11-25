---
parent: Class Mixins
title: biolink:AttributeMixin
grand_parent: Classes
layout: default
---

# Class: AttributeMixin




URI: [biolink:AttributeMixin](https://w3id.org/biolink/vocab/AttributeMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]%3Chas%20attribute%200..%2A-++[AttributeMixin],[NamedThing]uses%20-.-%3E[AttributeMixin],[Association]uses%20-.-%3E[AttributeMixin],[NamedThing],[Attribute],[Association])

---


## Mixin for

 * [Association](Association.md) (mixin)  - A typed association between two entities, supported by evidence
 * [NamedThing](NamedThing.md) (mixin)  - a databased entity or concept/class

## Referenced by class


## Attributes


### Own

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)
