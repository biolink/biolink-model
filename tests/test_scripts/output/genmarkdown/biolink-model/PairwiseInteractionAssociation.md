# Class: pairwise interaction association


An interaction at the molecular level between two physical entities

URI: [http://bioentity.io/vocab/PairwiseInteractionAssociation](http://bioentity.io/vocab/PairwiseInteractionAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PairwiseInteractionAssociation|id:identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[PairwiseInteractionAssociation]-%20publications(i)%20*>\[Publication],%20\[PairwiseInteractionAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[PairwiseInteractionAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[PairwiseInteractionAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PairwiseInteractionAssociation]-%20interacting%20molecules%20category%20%3F>\[OntologyClass],%20\[PairwiseInteractionAssociation]-%20object>\[MolecularEntity],%20\[PairwiseInteractionAssociation]-%20relation>\[RelationshipType],%20\[PairwiseInteractionAssociation]-%20subject>\[MolecularEntity],%20\[PairwiseGeneToGeneInteraction]uses%20-.->\[PairwiseInteractionAssociation],%20\[Association]^-\[PairwiseInteractionAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) (mixin)  - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
## Used in

## Fields

 * [pairwise interaction association.interacting molecules category](interacting_molecules_category.md)
    * range: [OntologyClass](OntologyClass.md)
    * __Local__
 * [pairwise interaction association.id](pairwise_interaction_association_id.md) *subsets*: (translator_minimal)
    * Description: identifier for the interaction. This may come from an interaction database such as IMEX.
    * range: [IdentifierType](IdentifierType.md)
    * __Local__
 * [pairwise interaction association.object](pairwise_interaction_association_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [MolecularEntity](MolecularEntity.md) [required]
    * __Local__
 * [pairwise interaction association.relation](pairwise_interaction_association_relation.md)
    * Description: interaction relationship type
    * range: [RelationshipType](RelationshipType.md) [required]
    * edge label: [molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)
    * __Local__
 * [pairwise interaction association.subject](pairwise_interaction_association_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [MolecularEntity](MolecularEntity.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
