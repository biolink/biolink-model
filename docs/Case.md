---
layout: default
---

## case


An individual organism that has a patient role in some clinical context.

URI: [http://bioentity.io/vocab/Case](http://bioentity.io/vocab/Case)


![img](http://yuml.me/diagram/nofunky/class/[individual organism|in taxon]^-[case|], [case|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings


## Inheritance

 *  is_a: [individual organism](IndividualOrganism.html)

## Children


## Used in

 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)

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
