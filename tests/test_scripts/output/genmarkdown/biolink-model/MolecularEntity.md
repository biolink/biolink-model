# Class: molecular entity


A gene, gene product, small molecule or macromolecule (including protein complex)

URI: http://bioentity.io/vocab/MolecularEntity

![img](http://yuml.me/diagram/nofunky/class/\[BiologicalEntity]^-\[MolecularEntity],%20\[MolecularEntity]^-\[ChemicalSubstance],%20\[MolecularEntity]^-\[GeneFamily],%20\[MolecularEntity]^-\[GenomicEntity],%20\[MolecularEntity]-%20molecularly_interacts_with%20%3F>\[MolecularEntity],%20\[MolecularEntity]-%20regulates_entity_to_entity%20%3F>\[MolecularEntity],%20\[MolecularEntity]-%20biomarker_for%20%3F>\[DiseaseOrPhenotypicFeature],%20\[MolecularEntity]-%20in_taxon%20%3F>\[OrganismTaxon],%20\[MolecularEntity]uses%20-.->\[ThingWithTaxon],%20)
## Mappings

 * [SIO:010004](http://semanticscience.org/resource/SIO_010004)
 * [WD:Q43460564](http://purl.obolibrary.org/obo/WD_Q43460564)
## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md)
## Children

 *  child: [chemical substance](ChemicalSubstance.md)
 *  child: [genomic entity](GenomicEntity.md)
 *  child: [gene family](GeneFamily.md)
## Used in

 *  class: [molecular entity](MolecularEntity.md) references: [chemical substance](ChemicalSubstance.md)
 *  class: [molecular entity](MolecularEntity.md) references: [genomic entity](GenomicEntity.md)
 *  class: [molecular entity](MolecularEntity.md) references: [gene family](GeneFamily.md)
## Fields

 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [physically interacts with](physically_interacts_with.md) *subsets: translator_minimal*
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [regulates](regulates.md)
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [correlated with](correlated_with.md) *subsets: translator_minimal*
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
