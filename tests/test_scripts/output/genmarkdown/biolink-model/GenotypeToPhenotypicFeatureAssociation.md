# Class: genotype to phenotypic feature association


Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment

URI: [http://bioentity.io/vocab/GenotypeToPhenotypicFeatureAssociation](http://bioentity.io/vocab/GenotypeToPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GenotypeToPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F;description(i):narrative_text%20%3F]-%20object(i)>\[PhenotypicFeature],%20\[GenotypeToPhenotypicFeatureAssociation]-%20sex%20qualifier(i)%20%3F>\[BiologicalSex],%20\[GenotypeToPhenotypicFeatureAssociation]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[GenotypeToPhenotypicFeatureAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[GenotypeToPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GenotypeToPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[GenotypeToPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GenotypeToPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GenotypeToPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GenotypeToPhenotypicFeatureAssociation]-%20subject>\[Genotype],%20\[GenotypeToPhenotypicFeatureAssociation]-%20relation>\[RelationshipType],%20\[GenotypeToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[GenotypeToPhenotypicFeatureAssociation]uses%20-.->\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
## Children

## Used in

## Fields

 * _[genotype to phenotypic feature association.relation](genotype_to_phenotypic_feature_association_relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [RelationshipType](RelationshipType.md) [required]
    * edge label: [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * __Local__
 * _[genotype to phenotypic feature association.subject](genotype_to_phenotypic_feature_association_subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [Genotype](Genotype.md) [required]
    * __Local__
 * _[association slot](association_slot.md)_
    * _any slot that relates an association to another entity_
    * range: **string**
    * inherited from: [Association](Association.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[negated](negated.md)_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: **string** [required]
    * inherited from: [Association](Association.md)
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [Onset](Onset.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * _[sex qualifier](sex_qualifier.md)_
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * range: [BiologicalSex](BiologicalSex.md)
    * inherited from: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
