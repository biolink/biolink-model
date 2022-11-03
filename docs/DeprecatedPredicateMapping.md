---
parent: Other Classes
title: biolink:DeprecatedPredicateMapping
grand_parent: Classes
layout: default
---

# Class: DeprecatedPredicateMapping


A deprecated predicate mapping object contains the deprecated predicate and an example of the rewiring that should be done to use a qualified statement in its place.

URI: [biolink:DeprecatedPredicateMapping](https://w3id.org/biolink/vocab/DeprecatedPredicateMapping)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[NamedThing]%3Cbroad%20match%200..%2A-%20[DeprecatedPredicateMapping%7Cmapped_predicate:string%20%3F;subject_aspect_qualifier:string%20%3F;subject_direction_qualifier:string%20%3F;subject_form_or_variant_qualifier:string%20%3F;subject_part_qualifier:string%20%3F;subject_derivative_qualifier:string%20%3F;subject_context_qualifier:string%20%3F;predicate:predicate_type;qualified_predicate:string%20%3F;object_aspect_qualifier:string%20%3F;object_direction_qualifier:DirectionQualifierEnum%20%3F;object_form_or_variant_qualifier:string%20%3F;object_part_qualifier:string%20%3F;object_derivative_qualifier:string%20%3F;object_context_qualifier:string%20%3F;causal_mechanism_qualifier:string%20%3F;anatomical_context_qualifier:AnatomicalContextQualifierEnum%20%3F],[NamedThing]%3Cnarrow%20match%200..%2A-%20[DeprecatedPredicateMapping],[NamedThing]%3Cexact%20match%200..%2A-%20[DeprecatedPredicateMapping],[OrganismTaxon]%3Cspecies%20context%20qualifier%200..1-%20[DeprecatedPredicateMapping],[DeprecatedMappingCollection]++-%20deprecated%20predicate%20mappings%200..%2A%3E[DeprecatedPredicateMapping],[DeprecatedMappingCollection])

---


## Referenced by class

 *  **None** *[deprecated predicate mappings](deprecated_predicate_mappings.md)*  <sub>0..\*</sub>  **[DeprecatedPredicateMapping](DeprecatedPredicateMapping.md)**

## Attributes


### Own

 * [broad match](broad_match.md)  <sub>0..\*</sub>
     * Description: a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [exact match](exact_match.md)  <sub>0..\*</sub>
     * Description: holds between two entities that have strictly equivalent meanings, with a high degree of confidence
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [mapped predicate](mapped_predicate.md)  <sub>0..1</sub>
     * Description: The predicate that is being replaced by the fully qualified representation of predicate + subject and object  qualifiers.  Only to be used in test data and mapping data to help with the transition to the fully qualified predicate model. Not to be used in knowledge graphs.
     * Range: [String](types/String.md)
 * [narrow match](narrow_match.md)  <sub>0..\*</sub>
     * Description: a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [object derivative qualifier](object_derivative_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [species context qualifier](species_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
     * Range: [OrganismTaxon](OrganismTaxon.md)

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

### Inherited from chemical affects gene association:

 * [subject form or variant qualifier](subject_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject part qualifier](subject_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject derivative qualifier](subject_derivative_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject aspect qualifier](subject_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject context qualifier](subject_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [subject direction qualifier](subject_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object form or variant qualifier](object_form_or_variant_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object part qualifier](object_part_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object aspect qualifier](object_aspect_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object context qualifier](object_context_qualifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [causal mechanism qualifier](causal_mechanism_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
     * Range: [String](types/String.md)
 * [anatomical context qualifier](anatomical_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or subcellular location).
     * Range: [AnatomicalContextQualifierEnum](AnatomicalContextQualifierEnum.md)
 * [qualified predicate](qualified_predicate.md)  <sub>0..1</sub>
     * Description: Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading.
     * Range: [String](types/String.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object direction qualifier](object_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [DirectionQualifierEnum](DirectionQualifierEnum.md)
 * [species context qualifier](species_context_qualifier.md)  <sub>0..1</sub>
     * Description: A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place.
     * Range: [OrganismTaxon](OrganismTaxon.md)

### Inherited from chemical entity or gene or gene product regulates gene association:

 * [object direction qualifier](object_direction_qualifier.md)  <sub>0..1</sub>
     * Range: [DirectionQualifierEnum](DirectionQualifierEnum.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
