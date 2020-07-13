---
parent: Classes
title: biolink:RelationshipType
grand_parent: Browse Biolink Model
layout: default
---

# Type: RelationshipType


An OWL property used as an edge label

URI: [biolink:RelationshipType](https://w3id.org/biolink/vocab/RelationshipType)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass]%5E-[RelationshipType|id(i):string;name(i):label_type;category(i):category_type%20%2B],[OntologyClass])

---


## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Attributes


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
