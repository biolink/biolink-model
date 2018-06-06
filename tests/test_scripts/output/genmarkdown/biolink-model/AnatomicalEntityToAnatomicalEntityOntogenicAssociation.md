# Class: anatomical entity to anatomical entity ontogenic association


A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship

URI: [http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation](http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20publications(i)%20*>\[Publication],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20relation>\[RelationshipType])
## Mappings

## Inheritance

 *  is_a: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * __Local__
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: develops from
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
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
