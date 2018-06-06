# Class: molecular entity


A gene, gene product, small molecule or macromolecule (including protein complex)

URI: [http://bioentity.io/vocab/MolecularEntity](http://bioentity.io/vocab/MolecularEntity)

![img](images/MolecularEntity.png)
## Mappings

 * [SIO:010004](http://semanticscience.org/resource/SIO_010004)
 * [WD:Q43460564](http://purl.obolibrary.org/obo/WD_Q43460564)
## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [genomic entity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
 *  child: [chemical substance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
 *  child: [gene family](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
## Used in

 *  class: [molecular entity](MolecularEntity.md) references: [genomic entity](GenomicEntity.md)
 *  class: [molecular entity](MolecularEntity.md) references: [chemical substance](ChemicalSubstance.md)
 *  class: [molecular entity](MolecularEntity.md) references: [gene family](GeneFamily.md)
## Fields

 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * __Local__
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * __Local__
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * __Local__
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
