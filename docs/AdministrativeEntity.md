---
parent: Classes
title: biolink:AdministrativeEntity
grand_parent: Browse Biolink Model
layout: default
---

# Type: AdministrativeEntity




URI: [biolink:AdministrativeEntity](https://w3id.org/biolink/vocab/AdministrativeEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AdministrativeEntity%7Cid(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]%5E-[Provider],%20[NamedThing]%5E-[AdministrativeEntity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [Provider](Provider.md) - person, group, organization or project that provides a piece of information

## Referenced by class


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
