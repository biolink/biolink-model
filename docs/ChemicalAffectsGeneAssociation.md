---
parent: Associations
title: biolink:ChemicalAffectsGeneAssociation
grand_parent: Classes
layout: default
---

# Class: ChemicalAffectsGeneAssociation


Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.)

URI: [biolink:ChemicalAffectsGeneAssociation](https://w3id.org/biolink/vocab/ChemicalAffectsGeneAssociation)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OrganismTaxon],[OntologyClass],[InformationResource],[GeneOrGeneProduct],[EvidenceType],[ChemicalEntity],[OrganismTaxon]%3Cspecies%20context%20qualifier%200..1-%20[ChemicalAffectsGeneAssociation%7Csubject_form_or_variant_qualifier:ChemicalOrGeneOrGeneProductFormOrVariantEnum%20%3F;subject_part_qualifier:GeneOrGeneProductOrChemicalPartQualifierEnum%20%3F;subject_derivative_qualifier:ChemicalEntityDerivativeEnum%20%3F;subject_aspect_qualifier:GeneOrGeneProductOrChemicalPartQualifierEnum%20%3F;subject_direction_qualifier:DirectionQualifierEnum%20%3F;object_form_or_variant_qualifier:ChemicalOrGeneOrGeneProductFormOrVariantEnum%20%3F;object_part_qualifier:GeneOrGeneProductOrChemicalPartQualifierEnum%20%3F;object_aspect_qualifier:GeneOrGeneProductOrChemicalPartQualifierEnum%20%3F;causal_mechanism_qualifier:CausalMechanismQualifierEnum%20%3F;qualified_predicate:string%20%3F;predicate:predicate_type;object_direction_qualifier:DirectionQualifierEnum%20%3F;negated(i):boolean%20%3F;timepoint(i):time_type%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[GeneOrGeneProduct]%3Cobject%201..1-++[ChemicalAffectsGeneAssociation],[ChemicalEntity]%3Csubject%201..1-%20[ChemicalAffectsGeneAssociation],[AnatomicalEntity]%3Canatomical%20context%20qualifier%200..1-%20[ChemicalAffectsGeneAssociation],[AnatomicalEntity]%3Cobject%20context%20qualifier%200..1-%20[ChemicalAffectsGeneAssociation],[AnatomicalEntity]%3Csubject%20context%20qualifier%200..1-%20[ChemicalAffectsGeneAssociation],[Association]%5E-[ChemicalAffectsGeneAssociation],[Attribute],[Association],[AnatomicalEntity])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [anatomical context qualifier](anatomical_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or subcellular location).
     * Range: [AnatomicalContextQualifierEnum](AnatomicalContextQualifierEnum.md)
 * [causal mechanism qualifier](causal_mechanism_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
     * Range: [String](types/String.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object aspect qualifier](object_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object context qualifier](object_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object direction qualifier](object_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [DirectionQualifierEnum](DirectionQualifierEnum.md)
 * [object form or variant qualifier](object_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object part qualifier](object_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [qualified predicate](qualified_predicate.md)  <sub>0..1</sub>
     * Description: Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
     * Range: [String](types/String.md)
 * [species context qualifier](species_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
     * Range: [OrganismTaxon](OrganismTaxon.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject aspect qualifier](subject_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject context qualifier](subject_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject derivative qualifier](subject_derivative_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject direction qualifier](subject_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject part qualifier](subject_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

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
     * Description: One or more publications that report the statement expressed in an Association, or provide information used as  evidence supporting this statement.
     * Range: [Publication](Publication.md)
 * [has evidence](has_evidence.md)  <sub>0..\*</sub>
     * Description: connects an association to an instance of supporting evidence
     * Range: [EvidenceType](EvidenceType.md)
 * [knowledge source](knowledge_source.md)  <sub>0..1</sub>
     * Description: An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
     * Range: [InformationResource](InformationResource.md)
 * [primary knowledge source](primary_knowledge_source.md)  <sub>0..1</sub>
     * Description: The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to caputre non-primary sources.
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
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Domain for slot:

 * [anatomical context qualifier](anatomical_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or subcellular location).
     * Range: [AnatomicalContextQualifierEnum](AnatomicalContextQualifierEnum.md)
 * [causal mechanism qualifier](causal_mechanism_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
     * Range: [String](types/String.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object aspect qualifier](object_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object context qualifier](object_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object direction qualifier](object_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [DirectionQualifierEnum](DirectionQualifierEnum.md)
 * [object form or variant qualifier](object_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object part qualifier](object_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [qualified predicate](qualified_predicate.md)  <sub>0..1</sub>
     * Description: Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
     * Range: [String](types/String.md)
 * [species context qualifier](species_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
     * Range: [OrganismTaxon](OrganismTaxon.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject aspect qualifier](subject_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject context qualifier](subject_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject derivative qualifier](subject_derivative_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject direction qualifier](subject_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject part qualifier](subject_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
