# Class: genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: http://bioentity.io/vocab/GenotypeToGenotypePartAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[GenotypeToGenotypePartAssociation]-%20relation>\[RelationshipType],%20\[GenotypeToGenotypePartAssociation]-%20subject>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20object>\[Genotype],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: has variant part
    * inherited from: [relation](relation.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genotype](Genotype.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genotype](Genotype.md) [required]
    * inherited from: [object](object.md)
