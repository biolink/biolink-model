---
parent: Associations
title: biolink:GenotypeToDiseaseAssociation
grand_parent: Classes
layout: default
---

# Class: GenotypeToDiseaseAssociation




URI: [biolink:GenotypeToDiseaseAssociation](https://w3id.org/biolink/vocab/GenotypeToDiseaseAssociation)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Publication],[OntologyClass],[Onset],[NamedThing],[GenotypeToEntityAssociationMixin],[NamedThing]%3Cobject%201..1-%20[GenotypeToDiseaseAssociation%7Cpredicate:predicate_type;frequency_qualifier:frequency_value%20%3F;relation(i):string%20%3F;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing]%3Csubject%201..1-%20[GenotypeToDiseaseAssociation],[GenotypeToDiseaseAssociation]uses%20-.-%3E[GenotypeToEntityAssociationMixin],[GenotypeToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[GenotypeToDiseaseAssociation]%5E-[GenotypeAsAModelOfDiseaseAssociation],[Association]%5E-[GenotypeToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[EvidenceType],[EntityToDiseaseAssociationMixin],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md)
 *  mixin: [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease

## Children

 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)

## Referenced by class


## Attributes


### Own

 * [genotype to disease association➞object](genotype_to_disease_association_object.md)  <sub>1..1</sub>
     * Description: a disease that is associated with that genotype
     * Range: [NamedThing](NamedThing.md)
     * Example: MONDO:0016419 hereditary breast cancer
 * [genotype to disease association➞predicate](genotype_to_disease_association_predicate.md)  <sub>1..1</sub>
     * Description: E.g. is pathogenic for
     * Range: [PredicateType](types/PredicateType.md)
 * [genotype to disease association➞subject](genotype_to_disease_association_subject.md)  <sub>1..1</sub>
     * Description: a genotype that is associated in some way with a disease state
     * Range: [NamedThing](NamedThing.md)

### Inherited from association:

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [negated](negated.md)  <sub>0..1</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: connects an association to publications supporting the association
     * Range: [Publication](Publication.md)
 * [has evidence](has_evidence.md)  <sub>0..\*</sub>
     * Description: connects an association to an instance of supporting evidence
     * Range: [EvidenceType](EvidenceType.md)
 * [association➞type](association_type.md)  <sub>0..1</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * Range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Description: a lightweight analog to the association class 'provided by' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from entity to feature or disease qualifiers mixin:

 * [severity qualifier](severity_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * Range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * Range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * Range: [FrequencyValue](types/FrequencyValue.md)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)
     * in subsets: (translator_minimal,samples)

### Domain for slot:

 * [genotype to disease association➞object](genotype_to_disease_association_object.md)  <sub>1..1</sub>
     * Description: a disease that is associated with that genotype
     * Range: [NamedThing](NamedThing.md)
     * Example: MONDO:0016419 hereditary breast cancer
 * [genotype to disease association➞predicate](genotype_to_disease_association_predicate.md)  <sub>1..1</sub>
     * Description: E.g. is pathogenic for
     * Range: [PredicateType](types/PredicateType.md)
 * [genotype to disease association➞subject](genotype_to_disease_association_subject.md)  <sub>1..1</sub>
     * Description: a genotype that is associated in some way with a disease state
     * Range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | TODO decide no how to model pathogenicity |

