# Class: chemical to pathway association


An interaction between a chemical entity and a biological process or pathway

URI: http://bioentity.io/vocab/ChemicalToPathwayAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[ChemicalToPathwayAssociation],%20\[ChemicalToPathwayAssociation]-%20object>\[Pathway],%20\[ChemicalToPathwayAssociation]uses%20-.->\[ChemicalToThingAssociation],%20)
## Mappings

 * [SIO:001250](http://semanticscience.org/resource/SIO_001250)
## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [chemical to thing association](ChemicalToThingAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [pathway](Pathway.md) [required]
    * inherited from: [object](object.md)
