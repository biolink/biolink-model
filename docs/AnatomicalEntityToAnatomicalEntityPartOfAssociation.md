
# Type: anatomical entity to anatomical entity part of association


A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

URI: [biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation](https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation)


![img](images/AnatomicalEntityToAnatomicalEntityPartOfAssociation.svg)

## Parents

 *  is_a: [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)

## Referenced by class


## Attributes


### Own

 * [anatomical entity to anatomical entity part of association➞object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)  <sub>REQ</sub>
    * Description: the whole
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity to anatomical entity part of association➞relation](anatomical_entity_to_anatomical_entity_part_of_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [anatomical entity to anatomical entity part of association➞subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)  <sub>REQ</sub>
    * Description: the part
    * range: [AnatomicalEntity](AnatomicalEntity.md)

### Inherited from anatomical entity to anatomical entity association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
