# Class: pairwise gene or protein interaction association


An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

URI: [http://bioentity.io/vocab/PairwiseGeneOrProteinInteractionAssociation](http://bioentity.io/vocab/PairwiseGeneOrProteinInteractionAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PairwiseGeneOrProteinInteractionAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20interacting%20molecules%20category(i)%20%3F>\[OntologyClass],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20object(i)>\[MolecularEntity],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20subject(i)>\[MolecularEntity],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20publications(i)%20*>\[Publication],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PairwiseGeneOrProteinInteractionAssociation]-%20relation>\[RelationshipType],%20\[PairwiseGeneOrProteinInteractionAssociation]uses%20-.->\[MolecularInteraction],%20\[GeneToGeneAssociation]^-\[PairwiseGeneOrProteinInteractionAssociation])
## Mappings

## Inheritance

 *  is_a: gene to gene association
 *  mixin: molecular interaction
## Children

## Used in

## Fields

 * _pairwise gene or protein interaction association relation_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: relationship type [required]
    * edge label: molecularly interacts with
    * __Local__
 * _association slot_
    * _any slot that relates an association to another entity_
    * range: **string**
    * inherited from: association
 * _association type_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: ontology class
    * inherited from: association
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _gene to gene association object_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: gene or gene product [required]
    * inherited from: gene to gene association
 * _gene to gene association subject_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: gene or gene product [required]
    * inherited from: gene to gene association
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _molecular interaction interacting molecules category_
    * range: ontology class
    * Example: [MI:1048](http://purl.obolibrary.org/obo/MI_1048) smallmolecule-protein
    * inherited from: molecular interaction
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _negated_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * inherited from: association
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _provided by_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: provider
    * inherited from: association
 * _publications_
    * _connects an association to publications supporting the association_
    * range: publication*
    * inherited from: association
 * _qualifiers_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: ontology class*
    * inherited from: association
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
