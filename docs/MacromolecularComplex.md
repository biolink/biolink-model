---
layout: default
---

## macromolecular complex


None

URI: [http://bioentity.io/vocab/MacromolecularComplex](http://bioentity.io/vocab/MacromolecularComplex)


![img](http://yuml.me/diagram/nofunky/class/[molecular entity|in taxon]^-[macromolecular complex|], [macromolecular complex|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [GO:0032991](http://purl.obolibrary.org/obo/GO_0032991)
 * [SIO:010046](http://semanticscience.org/resource/SIO_010046)
 * [WD:Q22325163](http://purl.obolibrary.org/obo/WD_Q22325163)

## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)

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
