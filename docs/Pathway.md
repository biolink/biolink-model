---
layout: default
---

## pathway


None

URI: [http://bioentity.io/vocab/Pathway](http://bioentity.io/vocab/Pathway)


![img](http://yuml.me/diagram/nofunky/class/[biological process|]^-[pathway|])
## Mappings

 * [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)
 * [SIO:010526](http://semanticscience.org/resource/SIO_010526)
 * [PW:0000001](http://purl.obolibrary.org/obo/PW_0000001)
 * [WD:Q4915012](http://purl.obolibrary.org/obo/WD_Q4915012)

## Inheritance

 *  is_a: [biological process](BiologicalProcess.html)

## Children


## Used in

 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [pathway](Pathway.html)

## Fields

 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
