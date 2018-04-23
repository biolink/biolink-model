---
layout: default
---

## cell


None

URI: [http://bioentity.io/vocab/Cell](http://bioentity.io/vocab/Cell)


![img](http://yuml.me/diagram/nofunky/class/[anatomical entity|in taxon]^-[cell|], [cell|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [GO:0005623](http://purl.obolibrary.org/obo/GO_0005623)
 * [SIO:010001](http://semanticscience.org/resource/SIO_010001)
 * [WD:Q7868](http://purl.obolibrary.org/obo/WD_Q7868)

## Inheritance

 *  is_a: [anatomical entity](AnatomicalEntity.html)

## Children



## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
