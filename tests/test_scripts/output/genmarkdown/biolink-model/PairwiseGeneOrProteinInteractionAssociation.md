# Class: pairwise gene or protein interaction association


An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

URI: http://bioentity.io/vocab/PairwiseGeneOrProteinInteractionAssociation

![img](http://yuml.me/diagram/nofunky/class/\[GeneToGeneAssociation]^-\[PairwiseGeneOrProteinInteractionAssociation],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20relation>\[RelationshipType],%20\[PairwiseGeneOrProteinInteractionAssociation]uses%20-.->\[MolecularInteraction],%20)
## Mappings

## Inheritance

 *  is_a: [gene to gene association](GeneToGeneAssociation.md)
 *  mixin: [molecular interaction](MolecularInteraction.md)
## Children

## Used in

## Fields

 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: [molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*
    * inherited from: [relation](relation.md)
