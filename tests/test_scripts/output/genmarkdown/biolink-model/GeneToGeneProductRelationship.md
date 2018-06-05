# Class: gene to gene product relationship


A gene is transcribed and potentially translated to a gene product

URI: http://bioentity.io/vocab/GeneToGeneProductRelationship

![img](http://yuml.me/diagram/nofunky/class/\[SequenceFeatureRelationship]^-\[GeneToGeneProductRelationship],%20\[GeneToGeneProductRelationship]-%20subject>\[Gene],%20\[GeneToGeneProductRelationship]-%20object>\[GeneProduct],%20\[GeneToGeneProductRelationship]-%20relation>\[RelationshipType],%20)
## Mappings

## Inheritance

 *  is_a: [sequence feature relationship](SequenceFeatureRelationship.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene](Gene.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene product](GeneProduct.md) [required]
    * inherited from: [object](object.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: [has gene product](has_gene_product.md) *subsets: translator_minimal*
    * inherited from: [relation](relation.md)
