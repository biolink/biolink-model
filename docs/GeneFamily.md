---
layout: default
---

## gene family


any grouping of multiple genes or gene products related by common descent

URI: [http://bioentity.io/vocab/GeneFamily](http://bioentity.io/vocab/GeneFamily)


![img](http://yuml.me/diagram/nofunky/class/[molecular entity|in taxon]^-[gene family|], [gene family|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SIO:001380](http://semanticscience.org/resource/SIO_001380)
 * [NCIT:C20130](http://purl.obolibrary.org/obo/NCIT_C20130)
 * [WD:Q417841](http://purl.obolibrary.org/obo/WD_Q417841)

## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)
 *  mixin: [gene grouping](GeneGrouping.html)

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
 * [in taxon](in_taxon.html) *subsets: translator_minimal*
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
