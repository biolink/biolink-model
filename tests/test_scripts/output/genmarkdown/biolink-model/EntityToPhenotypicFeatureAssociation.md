# Class: entity to phenotypic feature association




URI: [http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation](http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[EntityToPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;systematic_synonym(i):label_type%20%3F;subject(i):string;negated(i):boolean%20%3F;association_slot(i):string%20%3F;frequency_qualifier:frequency_value%20%3F;description:narrative_text%20%3F],%20\[EntityToPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[EntityToPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[EntityToPhenotypicFeatureAssociation]-%20relation(i)>\[RelationshipType],%20\[EntityToPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[EntityToPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[EntityToPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[EntityToPhenotypicFeatureAssociation]-%20frequency%20qualifier%20%3F>\[FrequencyValue],%20\[EntityToPhenotypicFeatureAssociation]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[EntityToPhenotypicFeatureAssociation]-%20onset%20qualifier%20%3F>\[Onset],%20\[EntityToPhenotypicFeatureAssociation]-%20sex%20qualifier%20%3F>\[BiologicalSex],%20\[EntityToPhenotypicFeatureAssociation]-%20object>\[PhenotypicFeature])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
## Used in

## Fields

 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [phenotypic feature](PhenotypicFeature.md) [required]
    * Example: [HP:0002487](http://purl.obolibrary.org/obo/HP_0002487) Hyperkinesis
    * Example: [WBPhenotype:0000180](http://purl.obolibrary.org/obo/WBPhenotype_0000180) axon morphology variant
    * Example: [MP:0001569](http://purl.obolibrary.org/obo/MP_0001569) abnormal circulating bilirubin level
    * __Local__
 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * __Local__
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * __Local__
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * __Local__
 * _[sex qualifier](sex_qualifier.md)_
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * range: [biological sex](BiologicalSex.md)
    * __Local__
 * _[association slot](association_slot.md)_
    * _any slot that relates an association to another entity_
    * range: string
    * inherited from: [association](Association.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: [association](Association.md)
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[negated](negated.md)_
    * _if set to true, then the association is negated i.e. is not true_
    * range: boolean
    * inherited from: [association](Association.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: [association](Association.md)
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: [association](Association.md)
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: [association](Association.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: [association](Association.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * inherited from: [association](Association.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
