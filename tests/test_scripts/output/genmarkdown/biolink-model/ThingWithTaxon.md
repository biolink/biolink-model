# Class: thing with taxon


A mixin that can be used on any entity with a taxon

URI: [http://bioentity.io/vocab/ThingWithTaxon](http://bioentity.io/vocab/ThingWithTaxon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ThingWithTaxon]-%20in%20taxon%20%3F>\[OrganismTaxon])
## Mappings

## Inheritance

## Children

 *  mixin: [biosample](Biosample.md)
 *  mixin: [anatomical entity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
 *  mixin: [individual organism](IndividualOrganism.md)
 *  mixin: [population of individual organisms](PopulationOfIndividualOrganisms.md)
 *  mixin: [life stage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
 *  mixin: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
 *  mixin: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
## Used in

 *  class: [thing with taxon](ThingWithTaxon.md) references: [biosample](Biosample.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [individual organism](IndividualOrganism.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [population of individual organisms](PopulationOfIndividualOrganisms.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [life stage](LifeStage.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [molecular entity](MolecularEntity.md)
 *  class: [thing with taxon](ThingWithTaxon.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
