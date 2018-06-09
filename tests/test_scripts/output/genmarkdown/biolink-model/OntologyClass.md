# Class: ontology class


a concept or class in an ontology, vocabulary or thesaurus

URI: [http://bioentity.io/vocab/OntologyClass](http://bioentity.io/vocab/OntologyClass)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OntologyClass]^-\[GeneOntologyClass],%20\[OntologyClass]^-\[OrganismTaxon],%20\[OntologyClass]-%20subclass%20of%20%3F>\[OntologyClass])
## Mappings

## Inheritance

## Children

 *  child: [gene ontology class](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 *  child: [organism taxon](OrganismTaxon.md)
 *  mixin: [attribute](Attribute.md) - A property or characteristic of an entity
## Used in

 *  class: [association](Association.md) references: [ontology class](OntologyClass.md)
 *  class: [named thing](NamedThing.md) references: [ontology class](OntologyClass.md)
 *  class: [molecular interaction](MolecularInteraction.md) references: [ontology class](OntologyClass.md)
 *  class: [association](Association.md) references: [ontology class](OntologyClass.md)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.md) references: [ontology class](OntologyClass.md)
 *  class: [ontology class](OntologyClass.md) references: [ontology class](OntologyClass.md)
## Fields

 * _[subclass of](subclass_of.md) *subsets*: (translator_minimal)_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [ontology class](OntologyClass.md)
    * __Local__
