---
layout: default
---

## treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [http://bioentity.io/vocab/Treatment](http://bioentity.io/vocab/Treatment)


![img](http://yuml.me/diagram/nofunky/class/[environment|]^-[treatment|treats;has exposure parts], [treatment|treats;has exposure parts]-treats >[disease or phenotypic feature|in taxon], [biological entity|]^-[disease or phenotypic feature|in taxon], [disease or phenotypic feature|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [treatment|treats;has exposure parts]-has exposure parts >[drug exposure|], [environment|]^-[drug exposure|])
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://semanticscience.org/resource/SIO_001398)

## Inheritance

 *  is_a: [environment](Environment.html)

## Children


## Used in

 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [treatment](Treatment.html)

## Fields

 * [treats](treats.html)
    * _holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat _
    * __range__: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) [required]
    * __Local__
 * [has exposure parts](has_exposure_parts.html)
    * __range__: [drug exposure](DrugExposure.html) [required]
    * __Local__
 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
