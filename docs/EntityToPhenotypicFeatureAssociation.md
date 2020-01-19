---
parent: Classes
title: biolink:EntityToPhenotypicFeatureAssociation
grand_parent: Browse Biolink Model
---

# Type: EntityToPhenotypicFeatureAssociation




URI: [biolink:EntityToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[EntityToPhenotypicFeatureAssociation&#124;relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[EntityToPhenotypicFeatureAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[EntityToPhenotypicFeatureAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[EntityToPhenotypicFeatureAssociation],%20\[NamedThing]<subject(i)%201..1-%20\[EntityToPhenotypicFeatureAssociation],%20\[PhenotypicFeature]<object%201..1-%20\[EntityToPhenotypicFeatureAssociation],%20\[EntityToPhenotypicFeatureAssociation]uses%20-.->\[EntityToFeatureOrDiseaseQualifiers],%20\[VariantToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[GenotypeToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[GeneToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[ExposureEventToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[DiseaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[CaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation])

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

 * [entity to phenotypic feature association➞object](entity_to_phenotypic_feature_association_object.md)  <sub>REQ</sub>
    * range: [PhenotypicFeature](PhenotypicFeature.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)

### Domain for slot:

 * [entity to phenotypic feature association➞description](entity_to_phenotypic_feature_association_description.md)  <sub>OPT</sub>
    * range: [NarrativeText](types/NarrativeText.md)
 * [entity to phenotypic feature association➞object](entity_to_phenotypic_feature_association_object.md)  <sub>REQ</sub>
    * range: [PhenotypicFeature](PhenotypicFeature.md)
