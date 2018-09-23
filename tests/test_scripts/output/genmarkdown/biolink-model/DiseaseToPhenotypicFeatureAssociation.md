# Class: disease to phenotypic feature association


An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way

URI: [http://bioentity.io/vocab/DiseaseToPhenotypicFeatureAssociation](http://bioentity.io/vocab/DiseaseToPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DiseaseToPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;systematic_synonym(i):label_type%20%3F;subject(i):string;negated(i):boolean%20%3F;association_slot(i):string%20%3F;description(i):narrative_text%20%3F]-%20object(i)>\[PhenotypicFeature],%20\[DiseaseToPhenotypicFeatureAssociation]-%20sex%20qualifier(i)%20%3F>\[BiologicalSex],%20\[DiseaseToPhenotypicFeatureAssociation]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[DiseaseToPhenotypicFeatureAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[DiseaseToPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[DiseaseToPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[DiseaseToPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[DiseaseToPhenotypicFeatureAssociation]-%20relation(i)>\[RelationshipType],%20\[DiseaseToPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[DiseaseToPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DiseaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[DiseaseToPhenotypicFeatureAssociation]uses%20-.->\[DiseaseToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [DiseaseToThingAssociation](DiseaseToThingAssociation.md)
## Children

## Fields

 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * inherited from: [Association](Association.md)
 * [onset qualifier](onset_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
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
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
 * [severity qualifier](severity_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * [sex qualifier](sex_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)
    * inherited from: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [subject](subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * inherited from: [Association](Association.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
