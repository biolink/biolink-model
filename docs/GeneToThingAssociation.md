# Class: gene to thing association




URI: http://bioentity.io/vocab/GeneToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GeneToThingAssociation],%20\[GeneToThingAssociation]-%20subject>\[GeneOrGeneProduct],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [gene to disease association](GeneToDiseaseAssociation.md)
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [gene to thing association](GeneToThingAssociation.md) references: [gene to disease association](GeneToDiseaseAssociation.md)
 *  class: [gene to thing association](GeneToThingAssociation.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [subject](subject.md)
