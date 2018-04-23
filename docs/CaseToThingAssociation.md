---
layout: default
---

## case to thing association


An abstract association for use where the case is the subject

URI: [http://bioentity.io/vocab/CaseToThingAssociation](http://bioentity.io/vocab/CaseToThingAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[case to thing association|], [case to thing association|]-association type >[ontology class|], [case to thing association|]-subject >[case|], [individual organism|in taxon]^-[case|], [case|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [case to thing association|]-relation >[relationship type|], [case to thing association|]-qualifiers >[ontology class|], [case to thing association|]-publications >[publication|], [information content entity|]^-[publication|], [case to thing association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html)


## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _the case (e.g. patient) that has the property_
    * __range__: [case](Case.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: None [required]
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
