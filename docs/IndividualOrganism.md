---
layout: default
---

## individual organism


None

URI: [http://bioentity.io/vocab/IndividualOrganism](http://bioentity.io/vocab/IndividualOrganism)


![img](http://yuml.me/diagram/nofunky/class/[organismal entity|]^-[individual organism|in taxon], [individual organism|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [SIO:010000](http://semanticscience.org/resource/SIO_010000)
 * [WD:Q795052](http://purl.obolibrary.org/obo/WD_Q795052)
 * [NCBITaxon:1](http://purl.obolibrary.org/obo/NCBITaxon_1)

## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children

 *  child: [case](Case.html)

## Used in

 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)

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
