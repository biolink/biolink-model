# Class: molecular interaction


An interaction at the molecular level between two physical entities

URI: http://bioentity.io/vocab/MolecularInteraction

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[MolecularInteraction],%20\[MolecularInteraction]-%20subject>\[MolecularEntity],%20\[MolecularInteraction]-%20relation>\[RelationshipType],%20\[MolecularInteraction]-%20object>\[MolecularEntity],%20\[MolecularInteraction]-%20interacting_molecules_category%20%3F>\[OntologyClass],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md)
## Used in

 *  class: [molecular interaction](MolecularInteraction.md) references: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [molecular entity](MolecularEntity.md) [required]
    * inherited from: [subject](subject.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: [molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*
    * Example: [RO:0002447](http://purl.obolibrary.org/obo/RO_0002447) the subject molecular phosphorylates the object molecule
    * inherited from: [relation](relation.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [molecular entity](MolecularEntity.md) [required]
    * inherited from: [object](object.md)
 * _[interacting molecules category](interacting_molecules_category.md)_
    * range: [ontology class](OntologyClass.md)
    * Example: [MI:1048](http://purl.obolibrary.org/obo/MI_1048) smallmolecule-protein
