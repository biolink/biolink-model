# Class: genotype to gene association


Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality

URI: http://bioentity.io/vocab/GenotypeToGeneAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GenotypeToGeneAssociation],%20\[GenotypeToGeneAssociation]-%20relation>\[RelationshipType],%20\[GenotypeToGeneAssociation]-%20subject>\[Genotype],%20\[GenotypeToGeneAssociation]-%20object>\[Gene],%20)
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
    * range: [gene](Gene.md) [required]
    * inherited from: [object](object.md)
