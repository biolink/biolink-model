# Class: macromolecular machine to cellular component association


A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component

URI: http://bioentity.io/vocab/MacromolecularMachineToCellularComponentAssociation

![img](http://yuml.me/diagram/nofunky/class/\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation],%20\[MacromolecularMachineToCellularComponentAssociation]-%20object>\[CellularComponent],%20)
## Mappings

## Inheritance

 *  is_a: [functional association](FunctionalAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [cellular component](CellularComponent.md) [required]
    * inherited from: [object](object.md)
