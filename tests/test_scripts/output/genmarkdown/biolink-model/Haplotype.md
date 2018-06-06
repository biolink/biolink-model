# Class: haplotype


A set of zero or more Alleles on a single instance of a Sequence[VMC]

URI: [http://bioentity.io/vocab/Haplotype](http://bioentity.io/vocab/Haplotype)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GenomicEntity]^-\[Haplotype|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F],%20\[Haplotype]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Haplotype]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[Haplotype]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[Haplotype]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Haplotype]-%20in%20taxon(i)%20%3F>\[OrganismTaxon])
## Mappings

 * [GENO:0000871](http://purl.obolibrary.org/obo/GENO_0000871)
 * [VMC:Haplotype](http://purl.obolibrary.org/obo/VMC_Haplotype)
## Inheritance

 *  is_a: [genomic entity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
## Children

## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
