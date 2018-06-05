# Class: attribute


A property or characteristic of an entity

URI: http://bioentity.io/vocab/Attribute

![img](http://yuml.me/diagram/nofunky/class/\[Attribute]^-\[BiologicalSex],%20\[Attribute]^-\[ClinicalModifier],%20\[Attribute]^-\[FrequencyValue],%20\[Attribute]^-\[Onset],%20\[Attribute]^-\[SeverityValue],%20\[Attribute]^-\[Zygosity],%20\[Attribute]-%20subclass_of%20%3F>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass],%20)
## Mappings

 * [PATO:0000001](http://purl.obolibrary.org/obo/PATO_0000001)
## Inheritance

 *  mixin: [ontology class](OntologyClass.md)
## Children

 *  child: [zygosity](Zygosity.md)
 *  child: [frequency value](FrequencyValue.md)
 *  child: [onset](Onset.md)
 *  child: [biological sex](BiologicalSex.md)
 *  child: [severity value](SeverityValue.md)
 *  child: [clinical modifier](ClinicalModifier.md)
## Used in

 *  class: [attribute](Attribute.md) references: [zygosity](Zygosity.md)
 *  class: [attribute](Attribute.md) references: [frequency value](FrequencyValue.md)
 *  class: [attribute](Attribute.md) references: [onset](Onset.md)
 *  class: [attribute](Attribute.md) references: [biological sex](BiologicalSex.md)
 *  class: [attribute](Attribute.md) references: [severity value](SeverityValue.md)
 *  class: [attribute](Attribute.md) references: [clinical modifier](ClinicalModifier.md)
## Fields

 * _[subclass of](subclass_of.md) *subsets: translator_minimal*_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [ontology class](OntologyClass.md)
    * inherited from: [related to](related_to.md)
