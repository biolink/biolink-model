# Class: attribute


A property or characteristic of an entity

URI: [http://bioentity.io/vocab/Attribute](http://bioentity.io/vocab/Attribute)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Attribute]^-\[BiologicalSex],%20\[Attribute]^-\[ClinicalModifier],%20\[Attribute]^-\[FrequencyValue],%20\[Attribute]^-\[Onset],%20\[Attribute]^-\[SeverityValue],%20\[Attribute]^-\[Zygosity],%20\[Attribute]-%20subclass%20of%20%3F>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass])
## Mappings

 * [PATO:0000001](http://purl.obolibrary.org/obo/PATO_0000001)
## Inheritance

 *  mixin: [ontology class](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
## Children

 *  child: [frequency value](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 *  child: [clinical modifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 *  child: [severity value](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 *  child: [onset](Onset.md) - The age group in which manifestations appear
 *  child: [zygosity](Zygosity.md)
 *  child: [biological sex](BiologicalSex.md)
## Used in

 *  class: [attribute](Attribute.md) references: [frequency value](FrequencyValue.md)
 *  class: [attribute](Attribute.md) references: [clinical modifier](ClinicalModifier.md)
 *  class: [attribute](Attribute.md) references: [severity value](SeverityValue.md)
 *  class: [attribute](Attribute.md) references: [onset](Onset.md)
 *  class: [attribute](Attribute.md) references: [zygosity](Zygosity.md)
 *  class: [attribute](Attribute.md) references: [biological sex](BiologicalSex.md)
## Fields

 * _[subclass of](subclass_of.md) *subsets: translator_minimal*_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [ontology class](OntologyClass.md)
    * __Local__
