---
layout: default
---

## disease


None

URI: [http://bioentity.io/vocab/Disease](http://bioentity.io/vocab/Disease)
## Mappings

 * [MONDO:0000001](http://purl.obolibrary.org/obo/MONDO_0000001)

## Inheritance

 *  is_a: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)

## Children


## Used in

 *  class: [entity to disease association](EntityToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [disease to thing association](DiseaseToThingAssociation.html) references: [disease](Disease.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [disease](Disease.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [disease to phenotypic feature denormalized association](DiseaseToPhenotypicFeatureDenormalizedAssociation.html) references: [disease](Disease.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
