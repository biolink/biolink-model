# Class: anatomical entity to anatomical entity ontogenic association


A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship

URI: [http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation](http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation|id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20publications(i)%20*>\[Publication],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20relation>\[RelationshipType],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation])
## Mappings

## Inheritance

 *  is_a: [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
## Children

## Used in

## Fields

 * [anatomical entity to anatomical entity ontogenic association.object](anatomical_entity_to_anatomical_entity_ontogenic_association_object.md)
    * Description: the structure at an earlier time
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [anatomical entity to anatomical entity ontogenic association.relation](anatomical_entity_to_anatomical_entity_ontogenic_association_relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * __Local__
 * [anatomical entity to anatomical entity ontogenic association.subject](anatomical_entity_to_anatomical_entity_ontogenic_association_subject.md)
    * Description: the structure at a later time
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
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
