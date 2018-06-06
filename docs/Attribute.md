# Class: attribute


A property or characteristic of an entity

URI: [http://bioentity.io/vocab/Attribute](http://bioentity.io/vocab/Attribute)

![img](images/Attribute.png)
## Mappings

 * [PATO:0000001](http://purl.obolibrary.org/obo/PATO_0000001)
## Inheritance

 *  mixin: [ontology class](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
## Children

 *  child: [biological sex](BiologicalSex.md)
 *  child: [clinical modifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 *  child: [onset](Onset.md) - The age group in which manifestations appear
 *  child: [zygosity](Zygosity.md)
 *  child: [severity value](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 *  child: [frequency value](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
## Used in

 *  class: [attribute](Attribute.md) references: [biological sex](BiologicalSex.md)
 *  class: [attribute](Attribute.md) references: [clinical modifier](ClinicalModifier.md)
 *  class: [attribute](Attribute.md) references: [onset](Onset.md)
 *  class: [attribute](Attribute.md) references: [zygosity](Zygosity.md)
 *  class: [attribute](Attribute.md) references: [severity value](SeverityValue.md)
 *  class: [attribute](Attribute.md) references: [frequency value](FrequencyValue.md)
## Fields

 * _[subclass of](subclass_of.md) *subsets: translator_minimal*_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [ontology class](OntologyClass.md)
    * __Local__
