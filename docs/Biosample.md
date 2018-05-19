---
layout: default
---

## biosample


None

URI: [http://bioentity.io/vocab/Biosample](http://bioentity.io/vocab/Biosample)


![img](http://yuml.me/diagram/nofunky/class/[organismal entity|]^-[biosample|in taxon], [biosample|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SIO:001050](http://semanticscience.org/resource/SIO_001050)

## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children

 *  child: [cell line](CellLine.html)

## Used in

 *  class: [cell line to thing association](CellLineToThingAssociation.html) references: [cell line](CellLine.html)
 *  class: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.html) references: [cell line](CellLine.html)
 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)

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
 * [in taxon](in_taxon.html) *subsets: translator_minimal*
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
