# Class: anatomical entity to anatomical entity part of association


A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

URI: [http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation](http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation)

![img](images/AnatomicalEntityToAnatomicalEntityPartOfAssociation.png)
## Mappings

## Inheritance

 *  is_a: [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
## Children

## Used in

## Fields

 * [anatomical entity to anatomical entity part of association.object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)
    * Description: the whole
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [anatomical entity to anatomical entity part of association.relation](anatomical_entity_to_anatomical_entity_part_of_association_relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * edge label: [part of](part_of.md) *subsets*: (translator_minimal)
    * __Local__
 * [anatomical entity to anatomical entity part of association.subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)
    * Description: the part
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
