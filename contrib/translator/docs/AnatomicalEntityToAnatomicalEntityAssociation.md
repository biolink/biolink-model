# Class: anatomical entity to anatomical entity association




URI: [http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation](http://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntityToAnatomicalEntityAssociation|id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20publications(i)%20*>\[Publication],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20relation(i)>\[RelationshipType],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20object>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityPartOfAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
 * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
## Used in

## Fields

 * [anatomical entity to anatomical entity association.object](anatomical_entity_to_anatomical_entity_association_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [anatomical entity to anatomical entity association.subject](anatomical_entity_to_anatomical_entity_association_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
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
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
