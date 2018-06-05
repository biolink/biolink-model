# Class: chemical to gene association


An interaction between a chemical entity and a gene or gene product

URI: http://bioentity.io/vocab/ChemicalToGeneAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[ChemicalToGeneAssociation],%20\[ChemicalToGeneAssociation]-%20object>\[GeneOrGeneProduct],%20\[ChemicalToGeneAssociation]uses%20-.->\[ChemicalToThingAssociation],%20)
## Mappings

 * [SIO:001257](http://semanticscience.org/resource/SIO_001257)
## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [chemical to thing association](ChemicalToThingAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [object](object.md)
