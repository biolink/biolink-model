# Class: functional association


An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

URI: http://bioentity.io/vocab/FunctionalAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[FunctionalAssociation],%20\[FunctionalAssociation]^-\[GeneToGoTermAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation],%20\[FunctionalAssociation]-%20subject>\[MacromolecularMachine],%20\[FunctionalAssociation]-%20object>\[GeneOntologyClass],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  child: [gene to go term association](GeneToGoTermAssociation.md)
 *  child: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.md)
 *  child: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.md)
 *  child: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.md)
## Used in

 *  class: [functional association](FunctionalAssociation.md) references: [gene to go term association](GeneToGoTermAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [macromolecular machine](MacromolecularMachine.md) [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene ontology class](GeneOntologyClass.md) [required]
    * Example: [GO:0016301](http://purl.obolibrary.org/obo/GO_0016301) kinase activity
    * Example: [GO:0045211](http://purl.obolibrary.org/obo/GO_0045211) postsynaptic membrane
    * inherited from: [object](object.md)
