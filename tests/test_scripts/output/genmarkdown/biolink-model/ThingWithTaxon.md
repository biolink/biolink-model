# Class: thing with taxon


A mixin that can be used on any entity with a taxon

URI: [http://bioentity.io/vocab/ThingWithTaxon](http://bioentity.io/vocab/ThingWithTaxon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ThingWithTaxon]-%20in%20taxon%20%3F>\[OrganismTaxon])
## Mappings

## Inheritance

## Children

 *  mixin: [anatomical entity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
 *  mixin: [biosample](Biosample.md)
 *  mixin: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 *  mixin: [individual organism](IndividualOrganism.md)
 *  mixin: [life stage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
 *  mixin: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
 *  mixin: [population of individual organisms](PopulationOfIndividualOrganisms.md)
## Used in

## Fields

 * _[in taxon](in_taxon.md) *subsets*: (translator_minimal)_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
