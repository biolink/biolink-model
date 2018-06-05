# Class: gene has variant that contributes to disease association




URI: http://bioentity.io/vocab/GeneHasVariantThatContributesToDiseaseAssociation

![img](http://yuml.me/diagram/nofunky/class/\[GeneToDiseaseAssociation]^-\[GeneHasVariantThatContributesToDiseaseAssociation],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence_variant_qualifier%20%3F>\[SequenceVariant],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20)
## Mappings

## Inheritance

 *  is_a: [gene to disease association](GeneToDiseaseAssociation.md)
## Children

## Used in

## Fields

 * _[sequence variant qualifier](sequence_variant_qualifier.md)_
    * _a qualifier used in an association where the variant_
    * range: [sequence variant](SequenceVariant.md)
    * inherited from: [association slot](association_slot.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [subject](subject.md)
