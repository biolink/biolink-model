---
layout: default
---

## phenotypic feature


None

URI: [http://bioentity.io/vocab/PhenotypicFeature](http://bioentity.io/vocab/PhenotypicFeature)


![img](http://yuml.me/diagram/nofunky/class/[disease or phenotypic feature|in taxon]^-[phenotypic feature|], [phenotypic feature|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [UPHENO:0001001](http://purl.obolibrary.org/obo/UPHENO_0001001)
 * [SIO:010056](http://semanticscience.org/resource/SIO_010056)
 * [WD:Q169872](http://purl.obolibrary.org/obo/WD_Q169872)

## Inheritance

 *  is_a: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)

## Children


## Used in

 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)

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
