---
layout: default
---

## anatomical entity to anatomical entity ontogenic association


A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship

URI: [http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation](http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation)


![img](http://yuml.me/diagram/nofunky/class/[anatomical entity to anatomical entity association|]^-[anatomical entity to anatomical entity ontogenic association|], [anatomical entity to anatomical entity ontogenic association|]-association type >[ontology class|], [anatomical entity to anatomical entity ontogenic association|]-subject >[anatomical entity|in taxon], [organismal entity|]^-[anatomical entity|in taxon], [anatomical entity|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [anatomical entity to anatomical entity ontogenic association|]-relation >[relationship type|], [anatomical entity to anatomical entity ontogenic association|]-object >[anatomical entity|in taxon], [anatomical entity to anatomical entity ontogenic association|]-qualifiers >[ontology class|], [anatomical entity to anatomical entity ontogenic association|]-publications >[publication|], [information content entity|]^-[publication|], [anatomical entity to anatomical entity ontogenic association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _the structure at a later time_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * edge label: 
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _the structure at an earlier time_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
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
 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
