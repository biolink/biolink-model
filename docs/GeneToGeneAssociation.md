# Class: gene to gene association


abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.

URI: [http://bioentity.io/vocab/GeneToGeneAssociation](http://bioentity.io/vocab/GeneToGeneAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[GeneToGeneAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[GeneToGeneAssociation]^-\[GeneToGeneHomologyAssociation],%20\[GeneToGeneAssociation]^-\[PairwiseGeneOrProteinInteractionAssociation],%20\[GeneToGeneAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneToGeneAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToGeneAssociation]-%20relation(i)>\[RelationshipType],%20\[GeneToGeneAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToGeneAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneToGeneAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneToGeneAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20object>\[GeneOrGeneProduct])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  child: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
 *  child: [gene to gene homology association](GeneToGeneHomologyAssociation.md) - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
## Used in

 *  class: [gene to gene association](GeneToGeneAssociation.md) references: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md)
 *  class: [gene to gene association](GeneToGeneAssociation.md) references: [gene to gene homology association](GeneToGeneHomologyAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
