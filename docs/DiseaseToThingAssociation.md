---
layout: default
---

## disease to thing association


None

URI: [http://bioentity.io/vocab/DiseaseToThingAssociation](http://bioentity.io/vocab/DiseaseToThingAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association]^-[disease to thing association], [disease to thing association]-association type >[ontology class], [disease to thing association]-subject >[disease], [disease or phenotypic feature]^-[disease], [disease]-in taxon >[organism taxon], [ontology class]^-[organism taxon], [disease to thing association]-relation >[relationship type], [disease to thing association]-qualifiers >[ontology class], [disease to thing association]-publications >[publication], [information content entity]^-[publication], [disease to thing association]-provided by >[provider], [administrative entity]^-[provider])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html)


## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _disease class_
    * __range__: [disease](Disease.html) [required]
    * Example: [MONDO:0017314](http://purl.obolibrary.org/obo/MONDO_0017314) Ehlers-Danlos syndrome, vascular type
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
