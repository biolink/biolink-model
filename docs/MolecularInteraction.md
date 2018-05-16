---
layout: default
---

## molecular interaction


An interaction at the molecular level between two physical entities

URI: [http://bioentity.io/vocab/MolecularInteraction](http://bioentity.io/vocab/MolecularInteraction)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[molecular interaction|], [molecular interaction|]-association type >[ontology class|], [molecular interaction|]-subject >[molecular entity|in taxon], [biological entity|]^-[molecular entity|in taxon], [molecular entity|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [molecular interaction|]-object >[molecular entity|in taxon], [molecular interaction|]-qualifiers >[ontology class|], [molecular interaction|]-publications >[publication|], [information content entity|]^-[publication|], [molecular interaction|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  mixin: [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.html)


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
    * __range__: [molecularly interacts with](molecularly_interacts_with.html) *subsets: translator_minimal* [required]
    * edge label: [molecularly interacts with](molecularly_interacts_with.html) *subsets: translator_minimal*
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
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
