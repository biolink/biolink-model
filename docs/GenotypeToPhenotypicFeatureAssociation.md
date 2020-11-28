---
parent: Associations
title: biolink:GenotypeToPhenotypicFeatureAssociation
grand_parent: Classes
layout: default
---

# Class: GenotypeToPhenotypicFeatureAssociation


Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment

URI: [biolink:GenotypeToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/GenotypeToPhenotypicFeatureAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingToPhenotypicFeatureAssociationMixin],[SeverityValue],[Publication],[OntologyClass],[Onset],[NamedThing],[GenotypeToThingAssociationMixin],[Genotype]%3Csubject%201..1-%20[GenotypeToPhenotypicFeatureAssociation%7Cpredicate:predicate_type;description:narrative_text%20%3F;id(i):string;relation(i):uriorcurie;negated(i):boolean%20%3F],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[ThingToPhenotypicFeatureAssociationMixin],[GenotypeToPhenotypicFeatureAssociation]uses%20-.-%3E[GenotypeToThingAssociationMixin],[Association]%5E-[GenotypeToPhenotypicFeatureAssociation],[Genotype],[FrequencyValue],[BiologicalSex],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [ThingToPhenotypicFeatureAssociationMixin](ThingToPhenotypicFeatureAssociationMixin.md)
 *  mixin: [GenotypeToThingAssociationMixin](GenotypeToThingAssociationMixin.md)

## Referenced by class


## Attributes


### Own

 * [genotype to phenotypic feature association➞predicate](genotype_to_phenotypic_feature_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [genotype to phenotypic feature association➞subject](genotype_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * Description: genotype that is associated with the phenotypic feature
    * range: [Genotype](Genotype.md)

### Inherited from association:

 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)

### Inherited from entity to feature or disease qualifiers mixin:

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

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from thing to phenotypic feature association mixin:

 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)
 * [thing to phenotypic feature association mixin➞description](thing_to_phenotypic_feature_association_mixin_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [thing to phenotypic feature association mixin➞object](thing_to_phenotypic_feature_association_mixin_object.md)  <sub>REQ</sub>
    * Description: phenotypic class
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * Example:    
    * Example:    
    * Example:    

### Domain for slot:

 * [genotype to phenotypic feature association➞predicate](genotype_to_phenotypic_feature_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [genotype to phenotypic feature association➞subject](genotype_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * Description: genotype that is associated with the phenotypic feature
    * range: [Genotype](Genotype.md)
