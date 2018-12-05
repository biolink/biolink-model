# Class: clinical modifier


Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects

URI: [http://w3id.org/biolink/vocab/ClinicalModifier](http://w3id.org/biolink/vocab/ClinicalModifier)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalModifier|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20subclass%20of(i)%20%3F>\[OntologyClass],%20\[ClinicalModifier]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Association]-%20clinical%20modifier%20qualifier(i)%20%3F>\[ClinicalModifier],%20\[Attribute]^-\[ClinicalModifier])
## Mappings

 * [HP:0012823](http://purl.obolibrary.org/obo/HP_0012823)
## Inheritance

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity
## Children

## Used in

 *  class: **[Association](Association.md)** *[clinical modifier qualifier](clinical_modifier_qualifier.md)* **[ClinicalModifier](ClinicalModifier.md)**
## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has alternate identifier](has_alternate_identifier.md)
    * Description: An alternate identifier for the entity, provided by the source database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [has synonym](has_synonym.md)
    * Description: Alternate labels for an entity
    * range: [name](name.md) *subsets*: (translator_minimal)*
    * inherited from: [NamedThing](NamedThing.md)
 * [has xref](has_xref.md)
    * Description: A database cross-reference for the entity, provided by a separate database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [subclass of](subclass_of.md) *subsets*: (translator_minimal)
    * Description: holds between two classes where the domain class is a specialization of the range class
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [OntologyClass](OntologyClass.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
