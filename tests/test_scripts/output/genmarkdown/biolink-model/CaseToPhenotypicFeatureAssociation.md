# Class: case to phenotypic feature association


An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype

URI: [http://bioentity.io/vocab/CaseToPhenotypicFeatureAssociation](http://bioentity.io/vocab/CaseToPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[CaseToPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;subject(i):string;negated(i):boolean%20%3F;object(i):string;association_slot(i):string%20%3F;frequency_qualifier:frequency_value%20%3F],%20\[CaseToPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[CaseToPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[CaseToPhenotypicFeatureAssociation]-%20relation(i)>\[RelationshipType],%20\[CaseToPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[CaseToPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[CaseToPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[CaseToPhenotypicFeatureAssociation]-%20frequency%20qualifier%20%3F>\[FrequencyValue],%20\[CaseToPhenotypicFeatureAssociation]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[CaseToPhenotypicFeatureAssociation]-%20onset%20qualifier%20%3F>\[Onset],%20\[CaseToPhenotypicFeatureAssociation]-%20sex%20qualifier%20%3F>\[BiologicalSex],%20\[CaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[CaseToPhenotypicFeatureAssociation]uses%20-.->\[CaseToThingAssociation])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [case to thing association](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
## Children

## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * __Local__
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * __Local__
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * __Local__
 * _[sex qualifier](sex_qualifier.md)_
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * range: [biological sex](BiologicalSex.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
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
