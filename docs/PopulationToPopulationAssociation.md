
# Type: population to population association


An association between a two populations

URI: [biolink:PopulationToPopulationAssociation](https://w3id.org/biolink/vocab/PopulationToPopulationAssociation)


![img](images/PopulationToPopulationAssociation.svg)

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [population to population association➞object](population_to_population_association_object.md)  <sub>REQ</sub>
    * Description: the population that form the object of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [population to population association➞relation](population_to_population_association_relation.md)  <sub>REQ</sub>
    * Description: A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [population to population association➞subject](population_to_population_association_subject.md)  <sub>REQ</sub>
    * Description: the population that form the subject of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)

### Inherited from association:

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
