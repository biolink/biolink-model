# Class: macromolecular machine to biological process association


A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: http://bioentity.io/vocab/MacromolecularMachineToBiologicalProcessAssociation

![img](http://yuml.me/diagram/nofunky/class/\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20object>\[BiologicalProcess],%20)
## Mappings

## Inheritance

 *  is_a: [functional association](FunctionalAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [biological process](BiologicalProcess.md) [required]
    * inherited from: [object](object.md)
