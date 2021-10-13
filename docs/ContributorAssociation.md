---
parent: Associations
title: biolink:ContributorAssociation
grand_parent: Classes
layout: default
---

# Class: ContributorAssociation


Any association between an entity (such as a publication) and various agents that contribute to its realisation

URI: [biolink:ContributorAssociation](https://w3id.org/biolink/vocab/ContributorAssociation)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[InformationContentEntity],[OntologyClass]%3Cqualifiers%200..%2A-++[ContributorAssociation%7Cpredicate:predicate_type;relation(i):string%20%3F;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Agent]%3Cobject%201..1-%20[ContributorAssociation],[InformationContentEntity]%3Csubject%201..1-%20[ContributorAssociation],[Association]%5E-[ContributorAssociation],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [contributor association➞object](contributor_association_object.md)  <sub>1..1</sub>
     * Description: agent helping to realise the given entity (e.g. such as a publication)
     * Range: [Agent](Agent.md)
 * [contributor association➞predicate](contributor_association_predicate.md)  <sub>1..1</sub>
     * Description: generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'
     * Range: [PredicateType](types/PredicateType.md)
 * [contributor association➞qualifiers](contributor_association_qualifiers.md)  <sub>0..\*</sub>
     * Description: this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'
     * Range: [OntologyClass](OntologyClass.md)
 * [contributor association➞subject](contributor_association_subject.md)  <sub>1..1</sub>
     * Description: information content entity which an agent has helped realise
     * Range: [InformationContentEntity](InformationContentEntity.md)

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
 * [association➞type](association_type.md)  <sub>0..1</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * Range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..\*</sub>
     * Range: [CategoryType](types/CategoryType.md)

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

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [contributor association➞object](contributor_association_object.md)  <sub>1..1</sub>
     * Description: agent helping to realise the given entity (e.g. such as a publication)
     * Range: [Agent](Agent.md)
 * [contributor association➞predicate](contributor_association_predicate.md)  <sub>1..1</sub>
     * Description: generally one of the predicate values 'provider', 'publisher', 'editor' or 'author'
     * Range: [PredicateType](types/PredicateType.md)
 * [contributor association➞qualifiers](contributor_association_qualifiers.md)  <sub>0..\*</sub>
     * Description: this field can be used to annotate special characteristics of an agent relationship, such as the fact that a given author agent of a publication is the 'corresponding author'
     * Range: [OntologyClass](OntologyClass.md)
 * [contributor association➞subject](contributor_association_subject.md)  <sub>1..1</sub>
     * Description: information content entity which an agent has helped realise
     * Range: [InformationContentEntity](InformationContentEntity.md)