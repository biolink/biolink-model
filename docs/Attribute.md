
# Class: attribute


A property or characteristic of an entity

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Attribute|id:identifier_type;name:label_type;category:iri_type%20%2B]uses%20-.->\[OntologyClass],%20\[Attribute]^-\[Zygosity],%20\[Attribute]^-\[SeverityValue],%20\[Attribute]^-\[Onset],%20\[Attribute]^-\[FrequencyValue],%20\[Attribute]^-\[ClinicalModifier],%20\[Attribute]^-\[BiologicalSex])

## Uses Mixins

 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Children

 * [BiologicalSex](BiologicalSex.md)
 * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Onset](Onset.md) - The age group in which manifestations appear
 * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 * [Zygosity](Zygosity.md)

## Referenced by class


## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * in subsets: (translator_minimal)
