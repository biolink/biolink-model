# Class: cell line to thing association


An relationship between a cell line and another entity

URI: http://bioentity.io/vocab/CellLineToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[CellLineToThingAssociation],%20\[CellLineToThingAssociation]-%20subject>\[CellLine],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
## Used in

 *  class: [cell line to thing association](CellLineToThingAssociation.md) references: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [cell line](CellLine.md) [required]
    * inherited from: [subject](subject.md)
