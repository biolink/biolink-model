# Class: genotype to variant association


Any association between a genotype and a sequence variant.

URI: http://bioentity.io/vocab/GenotypeToVariantAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GenotypeToVariantAssociation],%20\[GenotypeToVariantAssociation]-%20relation>\[RelationshipType],%20\[GenotypeToVariantAssociation]-%20subject>\[Genotype],%20\[GenotypeToVariantAssociation]-%20object>\[SequenceVariant],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: [relation](relation.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genotype](Genotype.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * inherited from: [object](object.md)
