---
layout: default
---

## pairwise gene or protein interaction association


An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

URI: [http://bioentity.io/vocab/PairwiseGeneOrProteinInteractionAssociation](http://bioentity.io/vocab/PairwiseGeneOrProteinInteractionAssociation)


![img](http://yuml.me/diagram/nofunky/class/[gene to gene association|]^-[pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-association type >[ontology class|], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-subject >[molecular entity|in taxon], [biological entity|]^-[molecular entity|in taxon], [molecular entity|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-object >[molecular entity|in taxon], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-qualifiers >[ontology class|], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-publications >[publication|], [information content entity|]^-[publication|], [pairwise gene or protein interaction association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [gene to gene association](GeneToGeneAssociation.html)
 *  mixin: [molecular interaction](MolecularInteraction.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [molecular entity](MolecularEntity.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _interaction relationship type_
    * __range__: [molecularly interacts with](molecularly_interacts_with.html) [required]
    * subproperty_of: [RO:0002436](http://purl.obolibrary.org/obo/RO_0002436)
    * Example: [RO:0002447](http://purl.obolibrary.org/obo/RO_0002447) the subject molecular phosphorylates the object molecule
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [molecular entity](MolecularEntity.html) [required]
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
