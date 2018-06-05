# Class: cell line to disease or phenotypic feature association


An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype

URI: http://bioentity.io/vocab/CellLineToDiseaseOrPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject>\[DiseaseOrPhenotypicFeature],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[CellLineToThingAssociation],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [cell line to thing association](CellLineToThingAssociation.md)
 *  mixin: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * inherited from: [subject](subject.md)
