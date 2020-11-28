---
parent: Associations
title: biolink:GeneHasVariantThatContributesToDiseaseAssociation
grand_parent: Classes
layout: default
---

# Class: GeneHasVariantThatContributesToDiseaseAssociation




URI: [biolink:GeneHasVariantThatContributesToDiseaseAssociation](https://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[SequenceVariant],[Publication],[OntologyClass],[Onset],[NamedThing],[GeneToDiseaseAssociation],[GeneOrGeneProduct],[GeneOrGeneProduct]%3Csubject%201..1-%20[GeneHasVariantThatContributesToDiseaseAssociation%7Cid(i):string;predicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F],[SequenceVariant]%3Csequence%20variant%20qualifier%200..1-%20[GeneHasVariantThatContributesToDiseaseAssociation],[GeneToDiseaseAssociation]%5E-[GeneHasVariantThatContributesToDiseaseAssociation],[FrequencyValue],[Attribute],[Agent])

---


## Parents

 *  is_a: [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)

## Referenced by class


## Attributes


### Own

 * [gene has variant that contributes to disease association➞subject](gene_has_variant_that_contributes_to_disease_association_subject.md)  <sub>REQ</sub>
    * Description: A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [sequence variant qualifier](sequence_variant_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in an association with the variant
    * range: [SequenceVariant](SequenceVariant.md)

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

### Domain for slot:

 * [gene has variant that contributes to disease association➞subject](gene_has_variant_that_contributes_to_disease_association_subject.md)  <sub>REQ</sub>
    * Description: A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
