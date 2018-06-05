# Class: gene to go term association




URI: http://bioentity.io/vocab/GeneToGoTermAssociation

![img](http://yuml.me/diagram/nofunky/class/\[FunctionalAssociation]^-\[GeneToGoTermAssociation],%20\[GeneToGoTermAssociation]-%20subject>\[MolecularEntity],%20\[GeneToGoTermAssociation]-%20object>\[GeneOntologyClass],%20)
## Mappings

 * [http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association](http://purl.obolibrary.org/obo/http_//bio2rdf.org/wormbase_vocabulary_Gene-GO-Association)
## Inheritance

 *  is_a: [functional association](FunctionalAssociation.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [molecular entity](MolecularEntity.md) [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene ontology class](GeneOntologyClass.md) [required]
    * Example: [GO:0016301](http://purl.obolibrary.org/obo/GO_0016301) kinase activity
    * inherited from: [object](object.md)
