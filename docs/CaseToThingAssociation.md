# Class: case to thing association


An abstract association for use where the case is the subject

URI: http://bioentity.io/vocab/CaseToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[CaseToThingAssociation],%20\[CaseToThingAssociation]-%20subject>\[Case],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [case to thing association](CaseToThingAssociation.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [case](Case.md) [required]
    * inherited from: [subject](subject.md)
