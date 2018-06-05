# Class: genotype to thing association




URI: http://bioentity.io/vocab/GenotypeToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GenotypeToThingAssociation],%20\[GenotypeToThingAssociation]-%20subject>\[Genotype],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [genotype to thing association](GenotypeToThingAssociation.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genotype](Genotype.md) [required]
    * inherited from: [subject](subject.md)
