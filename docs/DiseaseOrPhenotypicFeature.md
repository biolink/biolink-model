---
layout: default
---

## disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [http://bioentity.io/vocab/DiseaseOrPhenotypicFeature](http://bioentity.io/vocab/DiseaseOrPhenotypicFeature)


![img](http://yuml.me/diagram/nofunky/class/[biological entity|]^-[disease or phenotypic feature|in taxon], [disease or phenotypic feature|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings


## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children

 *  child: [disease](Disease.html)
 *  child: [phenotypic feature](PhenotypicFeature.html)

## Used in

 *  class: [treatment](Treatment.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
 *  class: [disease to thing association](DiseaseToThingAssociation.html) references: [disease](Disease.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [disease](Disease.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [variant to disease association](VariantToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [disease](Disease.html)

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
