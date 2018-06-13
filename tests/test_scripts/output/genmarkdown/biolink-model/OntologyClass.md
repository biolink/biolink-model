# Class: ontology class


a concept or class in an ontology, vocabulary or thesaurus

URI: [http://bioentity.io/vocab/OntologyClass](http://bioentity.io/vocab/OntologyClass)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OntologyClass]-%20subclass%20of%20%3F>\[OntologyClass],%20\[Association]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[NamedThing]-%20has%20molecular%20consequence(i)%20%3F>\[OntologyClass],%20\[MolecularInteraction]-%20interacting%20molecules%20category(i)%20%3F>\[OntologyClass],%20\[Association]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%20%3F>\[OntologyClass],%20\[OntologyClass]-%20subclass%20of%20%3F>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[OntologyClass]^-\[OrganismTaxon],%20\[OntologyClass]^-\[GeneOntologyClass])
## Mappings

## Inheritance

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md)
 * [Attribute](Attribute.md) (mixin)  - A property or characteristic of an entity
## Used in

 *  class: **[Association](Association.md)** *[association type](association_type.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[MolecularInteraction](MolecularInteraction.md)** *[molecular interaction.interacting molecules category](molecular_interaction_interacting_molecules_category.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[Association](Association.md)** *[qualifiers](qualifiers.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[quantifier qualifier](quantifier_qualifier.md)* **[OntologyClass](OntologyClass.md)**
 *  class: **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)* **[OntologyClass](OntologyClass.md)**
## Fields

 * _[subclass of](subclass_of.md) *subsets*: (translator_minimal)_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [OntologyClass](OntologyClass.md)
    * __Local__
