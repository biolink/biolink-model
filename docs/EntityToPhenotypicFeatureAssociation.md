---
parent: Classes
title: biolink:EntityToPhenotypicFeatureAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Class: EntityToPhenotypicFeatureAssociation




URI: [biolink:EntityToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Publication],[Provider],[PhenotypicFeature],[OntologyClass],[Onset],[NamedThing],[FrequencyValue],[PhenotypicFeature]%3Cobject%201..1-%20[EntityToPhenotypicFeatureAssociation%7Cdescription:narrative_text%20%3F;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[BiologicalSex]%3Csex%20qualifier%200..1-%20[EntityToPhenotypicFeatureAssociation],[EntityToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToFeatureOrDiseaseQualifiers],[VariantToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[GeneToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[ExposureEventToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[DiseaseToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToPhenotypicFeatureAssociation],[Association]%5E-[EntityToPhenotypicFeatureAssociation],[VariantToPhenotypicFeatureAssociation],[GenotypeToPhenotypicFeatureAssociation],[GeneToPhenotypicFeatureAssociation],[ExposureEventToPhenotypicFeatureAssociation],[EntityToFeatureOrDiseaseQualifiers],[DiseaseToPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation],[BiologicalSex],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) (mixin)  - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) (mixin) 
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) (mixin)  - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [entity to phenotypic feature association➞description](entity_to_phenotypic_feature_association_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [entity to phenotypic feature association➞object](entity_to_phenotypic_feature_association_object.md)  <sub>REQ</sub>
    * Description: phenotypic class
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * Example:    
    * Example:    
    * Example:    
 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)

### Inherited from entity to feature or disease qualifiers:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)

### Domain for slot:

 * [entity to phenotypic feature association➞description](entity_to_phenotypic_feature_association_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [entity to phenotypic feature association➞object](entity_to_phenotypic_feature_association_object.md)  <sub>REQ</sub>
    * Description: phenotypic class
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * Example:    
    * Example:    
    * Example:    
