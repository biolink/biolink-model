# Class: thing with taxon


A mixin that can be used on any entity with a taxon

URI: http://bioentity.io/vocab/ThingWithTaxon

![img](http://yuml.me/diagram/nofunky/class/)
## Mappings

## Inheritance

## Children

 *  mixin: [life stage](LifeStage.md)
 *  mixin: [molecular entity](MolecularEntity.md)
 *  mixin: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  mixin: [anatomical entity](AnatomicalEntity.md)
 *  mixin: [biosample](Biosample.md)
 *  mixin: [individual organism](IndividualOrganism.md)
 *  mixin: [population of individual organisms](PopulationOfIndividualOrganisms.md)
## Used in

 *  class: [thing with taxon](ThingWithTaxon.md) references: [life stage](LifeStage.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [molecular entity](MolecularEntity.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [biosample](Biosample.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [individual organism](IndividualOrganism.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [population of individual organisms](PopulationOfIndividualOrganisms.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
