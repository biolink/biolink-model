---
parent: Associations
title: biolink:VariantToPopulationAssociation
grand_parent: Classes
layout: default
---

# Class: VariantToPopulationAssociation


An association between a variant and a population, where the variant has particular frequency in the population

URI: [biolink:VariantToPopulationAssociation](https://w3id.org/biolink/vocab/VariantToPopulationAssociation)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PopulationOfIndividualOrganisms]%3Cobject%201..1-%20[VariantToPopulationAssociation%7Chas_quotient:double%20%3F;has_count:integer%20%3F;has_total:integer%20%3F;has_percentage:double%20%3F;frequency_qualifier:frequency_value%20%3F;predicate(i):predicate_type;negated(i):boolean%20%3F;original_knowledge_source(i):string%20%3F;timepoint(i):time_type%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):string%20%3F],[SequenceVariant]%3Csubject%201..1-%20[VariantToPopulationAssociation],[VariantToPopulationAssociation]uses%20-.-%3E[VariantToEntityAssociationMixin],[VariantToPopulationAssociation]uses%20-.-%3E[FrequencyQuantifier],[VariantToPopulationAssociation]uses%20-.-%3E[FrequencyQualifierMixin],[Association]%5E-[VariantToPopulationAssociation],[VariantToEntityAssociationMixin],[SequenceVariant],[Publication],[PopulationOfIndividualOrganisms],[OntologyClass],[InformationResource],[FrequencyQuantifier],[FrequencyQualifierMixin],[EvidenceType],[Attribute],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)
 *  mixin: [FrequencyQuantifier](FrequencyQuantifier.md)
 *  mixin: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations

## Referenced by class


## Attributes


### Own

 * [has count](has_count.md)  <sub>0..1</sub>
     * Description: number of things with a particular property
     * Range: [Integer](types/Integer.md)
 * [has quotient](has_quotient.md)  <sub>0..1</sub>
     * Range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>0..1</sub>
     * Description: total number of things in a particular reference set
     * Range: [Integer](types/Integer.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
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
 * [knowledge source](knowledge_source.md)  <sub>0..1</sub>
     * Description: An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
     * Range: [InformationResource](InformationResource.md)
 * [original knowledge source](original_knowledge_source.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [primary knowledge source](primary_knowledge_source.md)  <sub>0..1</sub>
     * Description: The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).
     * Range: [InformationResource](InformationResource.md)
 * [aggregator knowledge source](aggregator_knowledge_source.md)  <sub>0..\*</sub>
     * Description: An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
     * Range: [InformationResource](InformationResource.md)
 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..\*</sub>
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
     * Range: [String](types/String.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * Range: [FrequencyValue](types/FrequencyValue.md)

### Inherited from frequency quantifier:

 * [has count](has_count.md)  <sub>0..1</sub>
     * Description: number of things with a particular property
     * Range: [Integer](types/Integer.md)
 * [has total](has_total.md)  <sub>0..1</sub>
     * Description: total number of things in a particular reference set
     * Range: [Integer](types/Integer.md)
 * [has quotient](has_quotient.md)  <sub>0..1</sub>
     * Range: [Double](types/Double.md)
 * [has percentage](has_percentage.md)  <sub>0..1</sub>
     * Description: equivalent to has quotient multiplied by 100
     * Range: [Double](types/Double.md)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Domain for slot:

 * [has count](has_count.md)  <sub>0..1</sub>
     * Description: number of things with a particular property
     * Range: [Integer](types/Integer.md)
 * [has quotient](has_quotient.md)  <sub>0..1</sub>
     * Range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>0..1</sub>
     * Description: total number of things in a particular reference set
     * Range: [Integer](types/Integer.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)