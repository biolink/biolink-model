
# Class: organism taxon




URI: [biolink:OrganismTaxon](https://w3id.org/biolink/vocab/OrganismTaxon)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ThingWithTaxon]-%20in%20taxon%200..*>\[OrganismTaxon|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[OntologyClass]^-\[OrganismTaxon])

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **[ThingWithTaxon](ThingWithTaxon.md)** *[in taxon](in_taxon.md)*  <sub>0..*</sub>  **[OrganismTaxon](OrganismTaxon.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
