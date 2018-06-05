# Class: gene to gene association


abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.

URI: http://bioentity.io/vocab/GeneToGeneAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GeneToGeneAssociation],%20\[GeneToGeneAssociation]^-\[GeneToGeneHomologyAssociation],%20\[GeneToGeneAssociation]^-\[PairwiseGeneOrProteinInteractionAssociation],%20\[GeneToGeneAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20object>\[GeneOrGeneProduct],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  child: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md)
 *  child: [gene to gene homology association](GeneToGeneHomologyAssociation.md)
## Used in

 *  class: [gene to gene association](GeneToGeneAssociation.md) references: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md)
 *  class: [gene to gene association](GeneToGeneAssociation.md) references: [gene to gene homology association](GeneToGeneHomologyAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [object](object.md)
