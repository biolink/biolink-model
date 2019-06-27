
# Class: case


An individual organism that has a patient role in some clinical context.

URI: [biolink:Case](https://w3id.org/biolink/vocab/Case)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Case|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[CaseToThingAssociation]-%20subject%201..1>\[Case],%20\[IndividualOrganism]^-\[Case])

## Parents

 *  is_a: [IndividualOrganism](IndividualOrganism.md)

## Referenced by class

 *  **[CaseToThingAssociation](CaseToThingAssociation.md)** *[subject](case_to_thing_association_subject.md)*  <sub>REQ</sub>  **[Case](Case.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)
