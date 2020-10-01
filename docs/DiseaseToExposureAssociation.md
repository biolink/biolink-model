
# Type: disease to exposure association


An association between an exposure event and a disease

URI: [biolink:DiseaseToExposureAssociation](https://w3id.org/biolink/vocab/DiseaseToExposureAssociation)


![img](images/DiseaseToExposureAssociation.svg)

## Parents

 *  is_a: [DiseaseToThingAssociation](DiseaseToThingAssociation.md)

## Referenced by class


## Attributes


### Own

 * [disease to exposure association➞object](disease_to_exposure_association_object.md)  <sub>REQ</sub>
    * range: [ExposureEvent](ExposureEvent.md)
 * [disease to exposure association➞subject](disease_to_exposure_association_subject.md)  <sub>REQ</sub>
    * range: [Disease](Disease.md)

### Inherited from disease to thing association:

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
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
