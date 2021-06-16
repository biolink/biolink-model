---
parent: Associations
title: biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation
grand_parent: Classes
layout: default
---

# Class: AnatomicalEntityToAnatomicalEntityPartOfAssociation


A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

URI: [biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation](https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[Attribute],[AnatomicalEntity]%3Cobject%201..1-%20[AnatomicalEntityToAnatomicalEntityPartOfAssociation%7Cpredicate:predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[AnatomicalEntity]%3Csubject%201..1-%20[AnatomicalEntityToAnatomicalEntityPartOfAssociation],[AnatomicalEntityToAnatomicalEntityAssociation]%5E-[AnatomicalEntityToAnatomicalEntityPartOfAssociation],[AnatomicalEntityToAnatomicalEntityAssociation],[AnatomicalEntity],[Agent])

---


## Parents

 *  is_a: [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)

## Referenced by class


## Attributes


### Own

 * [anatomical entity to anatomical entity part of association➞object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)  <sub>REQ</sub>
     * Description: the whole
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity to anatomical entity part of association➞predicate](anatomical_entity_to_anatomical_entity_part_of_association_predicate.md)  <sub>REQ</sub>
     * Range: [PredicateType](types/PredicateType.md)
 * [anatomical entity to anatomical entity part of association➞subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)  <sub>REQ</sub>
     * Description: the part
     * Range: [AnatomicalEntity](AnatomicalEntity.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
     * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: connects an association to publications supporting the association
     * Range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * Range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..\*</sub>
     * Range: [CategoryType](types/CategoryType.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
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
 * [type](type.md)  <sub>OPT</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [anatomical entity to anatomical entity part of association➞object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)  <sub>REQ</sub>
     * Description: the whole
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity to anatomical entity part of association➞predicate](anatomical_entity_to_anatomical_entity_part_of_association_predicate.md)  <sub>REQ</sub>
     * Range: [PredicateType](types/PredicateType.md)
 * [anatomical entity to anatomical entity part of association➞subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)  <sub>REQ</sub>
     * Description: the part
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
