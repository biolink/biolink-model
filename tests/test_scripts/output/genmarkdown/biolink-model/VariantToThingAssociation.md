# Class: variant to thing association




URI: http://bioentity.io/vocab/VariantToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[VariantToThingAssociation],%20\[VariantToThingAssociation]-%20subject>\[SequenceVariant],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  mixin: [variant to disease association](VariantToDiseaseAssociation.md)
 *  mixin: [variant to population association](VariantToPopulationAssociation.md)
## Used in

 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to population association](VariantToPopulationAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * Example: [ClinVar:38077](http://purl.obolibrary.org/obo/ClinVar_38077) ClinVar representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    * Example: [ClinGen:CA024716](http://purl.obolibrary.org/obo/ClinGen_CA024716) chr13:g.32921033G>C (hg19) in ClinGen
    * inherited from: [subject](subject.md)
