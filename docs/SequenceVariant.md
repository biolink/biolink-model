# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [http://bioentity.io/vocab/SequenceVariant](http://bioentity.io/vocab/SequenceVariant)

![img](images/SequenceVariant.png)
## Mappings

 * [GENO:0000002](http://purl.obolibrary.org/obo/GENO_0000002)
 * [WD:Q15304597](http://purl.obolibrary.org/obo/WD_Q15304597)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)
## Inheritance

 *  is_a: [genomic entity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
## Children

## Used in

## Fields

 * _[has gene](has_gene.md)_
    * _Each allele can be associated with any number of genes_
    * range: string*
    * __Local__
 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [biological sequence](BiologicalSequence.md)
    * __Local__
 * _[id](id.md) *subsets: translator_minimal*_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * Example: [ZFIN:ZDB-ALT-980203-1091](http://purl.obolibrary.org/obo/ZFIN_ZDB-ALT-980203-1091) ti282a allele from ZFIN
    * Example: [ClinVarVariant:17681](http://purl.obolibrary.org/obo/ClinVarVariant_17681) NM_007294.3(BRCA1):c.2521C>T (p.Arg841Trp)
    * __Local__
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
