# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: http://bioentity.io/vocab/SequenceVariant

![img](http://yuml.me/diagram/nofunky/class/\[GenomicEntity]^-\[SequenceVariant|has_gene:string%20*;has_biological_sequence:biological_sequence%20%3F;id:identifier_type%20%3F],%20)
## Mappings

 * [GENO:0000002](http://purl.obolibrary.org/obo/GENO_0000002)
 * [WD:Q15304597](http://purl.obolibrary.org/obo/WD_Q15304597)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)
## Inheritance

 *  is_a: [genomic entity](GenomicEntity.md)
## Children

## Used in

## Fields

 * _[has gene](has_gene.md)_
    * _Each allele can be associated with any number of genes_
    * range: string*
 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [biological sequence](BiologicalSequence.md)
    * inherited from: [has biological sequence](has_biological_sequence.md)
 * _[id](id.md) *subsets: translator_minimal*_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * Example: [ZFIN:ZDB-ALT-980203-1091](http://purl.obolibrary.org/obo/ZFIN_ZDB-ALT-980203-1091) ti282a allele from ZFIN
    * Example: [ClinVarVariant:17681](http://purl.obolibrary.org/obo/ClinVarVariant_17681) NM_007294.3(BRCA1):c.2521C>T (p.Arg841Trp)
    * inherited from: [id](id.md) *subsets: translator_minimal*
