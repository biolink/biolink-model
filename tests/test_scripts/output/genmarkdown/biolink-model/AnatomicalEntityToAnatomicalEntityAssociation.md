# Class: anatomical entity to anatomical entity association




URI: http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityPartOfAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20object>\[AnatomicalEntity],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  child: [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)
 *  child: [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)
## Used in

 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md) references: [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md) references: [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * inherited from: [object](object.md)
