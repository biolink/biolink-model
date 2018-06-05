# Class: macromolecular machine to molecular activity association


A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution

URI: http://bioentity.io/vocab/MacromolecularMachineToMolecularActivityAssociation

![img](http://yuml.me/diagram/nofunky/class/\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation],%20\[MacromolecularMachineToMolecularActivityAssociation]-%20object>\[MolecularActivity],%20)
## Mappings

## Inheritance

 *  is_a: [functional association](FunctionalAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [molecular activity](MolecularActivity.md) [required]
    * inherited from: [object](object.md)
