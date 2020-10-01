
# Type: pairwise interaction association


An interaction at the molecular level between two physical entities

URI: [biolink:PairwiseInteractionAssociation](https://w3id.org/biolink/vocab/PairwiseInteractionAssociation)


![img](images/PairwiseInteractionAssociation.svg)

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Mixin for

 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) (mixin)  - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

## Referenced by class


## Attributes


### Own

 * [pairwise interaction association➞id](pairwise_interaction_association_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database such as IMEX.
    * range: [String](types/String.md)
    * Example:    
 * [pairwise interaction association➞interacting molecules category](pairwise_interaction_association_interacting_molecules_category.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
    * Example:    
 * [pairwise interaction association➞object](pairwise_interaction_association_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise interaction association➞relation](pairwise_interaction_association_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
    * Example:    
 * [pairwise interaction association➞subject](pairwise_interaction_association_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)

### Inherited from association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
