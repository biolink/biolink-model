---
parent: Entities
title: biolink:BiologicalProcessOrActivity
grand_parent: Classes
layout: default
---

# Class: BiologicalProcessOrActivity


Either an individual molecular activity, or a collection of causally connected molecular activities

URI: [biolink:BiologicalProcessOrActivity](https://w3id.org/biolink/vocab/BiologicalProcessOrActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[Occurrent],[NamedThing],[MolecularActivity],[PhysicalEntity]%3Cenabled%20by%200..%2A-%20[BiologicalProcessOrActivity%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[NamedThing]%3Chas%20output%200..%2A-%20[BiologicalProcessOrActivity],[NamedThing]%3Chas%20input%200..%2A-%20[BiologicalProcessOrActivity],[BiologicalProcessOrActivity]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]%5E-[MolecularActivity],[BiologicalProcessOrActivity]%5E-[BiologicalProcess],[BiologicalEntity]%5E-[BiologicalProcessOrActivity],[BiologicalProcess],[BiologicalEntity])

---


## Identifier prefixes

 * GO
 * REACT

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Children

 * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
 * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[PhysicalEntity](PhysicalEntity.md)** *[enables](enables.md)*  <sub>0..*</sub>  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)**

## Attributes


### Own

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [PhysicalEntity](PhysicalEntity.md)
    * in subsets: (translator_minimal)

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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [PhysicalEntity](PhysicalEntity.md)
    * in subsets: (translator_minimal)
