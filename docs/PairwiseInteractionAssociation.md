# Class: pairwise interaction association


An interaction at the molecular level between two physical entities

URI: [biolink:PairwiseInteractionAssociation](https://w3id.org/biolink/vocab/PairwiseInteractionAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalModifier]<clinical%20modifier%20qualifier(i)%200..1-%20\[PairwiseInteractionAssociation|id:identifier_type;relation:iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F;edge_label(i):label_type%20%3F],%20\[EvidenceType]<has%20evidence(i)%200..1-%20\[PairwiseInteractionAssociation],%20\[ConfidenceLevel]<has%20confidence%20level(i)%200..1-%20\[PairwiseInteractionAssociation],%20\[Provider]<provided%20by(i)%200..1-%20\[PairwiseInteractionAssociation],%20\[Publication]<publications(i)%200..*-%20\[PairwiseInteractionAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[PairwiseInteractionAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[PairwiseInteractionAssociation],%20\[OntologyClass]<interacting%20molecules%20category%200..1-%20\[PairwiseInteractionAssociation],%20\[MolecularEntity]<object%201..1-%20\[PairwiseInteractionAssociation],%20\[MolecularEntity]<subject%201..1-%20\[PairwiseInteractionAssociation],%20\[PairwiseGeneToGeneInteraction]uses%20-.->\[PairwiseInteractionAssociation],%20\[Association]^-\[PairwiseInteractionAssociation])
## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) (mixin)  - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
## Used by

## Fields

 * [association slot](association_slot.md)  <sub>OPT</sub>
    * Description: any slot that relates an association to another entity
    * range: [String](String.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [interacting molecules category](interacting_molecules_category.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [pairwise interaction association.id](pairwise_interaction_association_id.md)  <sub>REQ</sub>
    * range: [IdentifierType](IdentifierType.md)
 * [pairwise interaction association.object](pairwise_interaction_association_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise interaction association.relation](pairwise_interaction_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [pairwise interaction association.subject](pairwise_interaction_association_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
