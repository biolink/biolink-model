---
parent: Classes
title: biolink:OntologyClass
grand_parent: Browse Biolink Model
---

# Type: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]-%20association%20type%200..1>\[OntologyClass&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1>\[OntologyClass],%20\[Attribute]-%20has%20attribute%20type%200..1>\[OntologyClass],%20\[Association]-%20qualifiers%200..*>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[OntologyClass]^-\[RelationshipType],%20\[OntologyClass]^-\[OrganismTaxon],%20\[OntologyClass]^-\[GeneOntologyClass],%20\[NamedThing]^-\[OntologyClass])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md)
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

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [subclass of](subclass_of.md)  <sub>0..*</sub>
    * Description: holds between two classes where the domain class is a specialization of the range class
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
