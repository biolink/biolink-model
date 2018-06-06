# Class: entity to phenotypic feature association




URI: [http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation](http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation)

![img](images/EntityToPhenotypicFeatureAssociation.png)
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
## Used in

 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
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
 * _[description](description.md) *subsets: translator_minimal*_
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
