---
parent: Classes
title: biolink:OntologyClass
grand_parent: Browse Biolink Model
layout: default
---

# Type: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[PairwiseInteractionAssociation],[OrganismTaxon],[Association]-%20association%20type%200..1%3E[OntologyClass|id(i):string;name(i):label_type;category(i):category_type%20%2B],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[Attribute]-%20has%20attribute%20type%200..1%3E[OntologyClass],[PairwiseInteractionAssociation]-%20interacting%20molecules%20category(i)%200..1%3E[OntologyClass],[Association]-%20qualifiers%200..*%3E[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[Attribute]uses%20-.-%3E[OntologyClass],[OntologyClass]%5E-[RelationshipType],[OntologyClass]%5E-[OrganismTaxon],[OntologyClass]%5E-[GeneOntologyClass],[NamedThing]%5E-[OntologyClass],[NamedThing],[GeneToExpressionSiteAssociation],[GeneOntologyClass],[Attribute],[Association])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md) - A classification of a set of organisms. Examples: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label

## Mixin for

 * [Attribute](Attribute.md) (mixin)  - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Referenced by class

 *  **[Association](Association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Attribute](Attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[PairwiseInteractionAssociation](PairwiseInteractionAssociation.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
