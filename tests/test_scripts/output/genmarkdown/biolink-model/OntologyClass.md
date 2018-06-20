# Class: ontology class


a concept or class in an ontology, vocabulary or thesaurus

URI: [http://bioentity.io/vocab/OntologyClass](http://bioentity.io/vocab/OntologyClass)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OntologyClass|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[OntologyClass]-%20subclass%20of%20%3F>\[OntologyClass],%20\[Association]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%20%3F>\[OntologyClass],%20\[MolecularInteraction]-%20interacting%20molecules%20category(i)%20%3F>\[OntologyClass],%20\[Association]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%20%3F>\[OntologyClass],%20\[OntologyClass]-%20subclass%20of%20%3F>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[OntologyClass]^-\[OrganismTaxon],%20\[OntologyClass]^-\[GeneOntologyClass],%20\[NamedThing]^-\[OntologyClass])
## Mappings

## Inheritance

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class
## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md)
 * [Attribute](Attribute.md) (mixin)  - A property or characteristic of an entity
## Used in

 *  class: **[Association](Association.md)** *[association type](association_type.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association.quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **None** *[has molecular consequence](has_molecular_consequence.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[MolecularInteraction](MolecularInteraction.md)** *[molecular interaction.interacting molecules category](interacting_molecules_category.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[Association](Association.md)** *[qualifiers](qualifiers.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[quantifier qualifier](quantifier_qualifier.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)* **[OntologyClass](OntologyClass.md)**
## Fields

 * _[subclass of](subclass_of.md) *subsets*: (translator_minimal)_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [OntologyClass](OntologyClass.md)
    * __Local__
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
