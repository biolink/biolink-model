# Class: biosample to thing association


An association between a biosample and something

URI: http://bioentity.io/vocab/BiosampleToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[BiosampleToThingAssociation],%20\[BiosampleToThingAssociation]-%20subject>\[Biosample],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
## Used in

 *  class: [biosample to thing association](BiosampleToThingAssociation.md) references: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [biosample](Biosample.md) [required]
    * inherited from: [subject](subject.md)
