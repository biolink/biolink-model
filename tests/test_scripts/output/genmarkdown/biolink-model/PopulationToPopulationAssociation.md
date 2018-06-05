# Class: population to population association


An association between a two populations

URI: http://bioentity.io/vocab/PopulationToPopulationAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[PopulationToPopulationAssociation],%20\[PopulationToPopulationAssociation]-%20subject>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20relation>\[RelationshipType],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [population of individual organisms](PopulationOfIndividualOrganisms.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [population of individual organisms](PopulationOfIndividualOrganisms.md) [required]
    * inherited from: [object](object.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: [relation](relation.md)
