---
layout: default
---

## cellular component


A location in or around a cell

URI: [http://bioentity.io/vocab/CellularComponent](http://bioentity.io/vocab/CellularComponent)


![img](http://yuml.me/diagram/nofunky/class/[anatomical entity|in taxon]^-[cellular component|], [cellular component|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)
 * [SIO:001400](http://semanticscience.org/resource/SIO_001400)
 * [WD:Q5058355](http://purl.obolibrary.org/obo/WD_Q5058355)

## Inheritance

 *  is_a: [anatomical entity](AnatomicalEntity.html)

## Children



## Fields

 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
