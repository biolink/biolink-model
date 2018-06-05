# Class: definition


definition base class

URI: http://bioentity.io/vocab/Definition

![img](http://yuml.me/diagram/nofunky/class/\[Element]^-\[Definition|mixin:boolean%20%3F;abstract:boolean%20%3F;local_names:string%20*;values_from:string%20*;symmetric:boolean%20%3F],%20\[Definition]^-\[ClassDefinition],%20\[Definition]^-\[SchemaDefinition],%20\[Definition]^-\[SlotDefinition],%20\[Definition]-%20is_a%20%3F>\[Definition],%20\[Definition]-%20mixins%20*>\[Definition],%20\[Definition]-%20union_of%20*>\[Definition],%20\[Definition]-%20subclass_of%20%3F>\[Definition],%20)
## Mappings

## Inheritance

 *  is_a: [element](Element.md)
## Children

 *  child: [slot definition](SlotDefinition.md)
 *  child: [class definition](ClassDefinition.md)
 *  child: [schema definition](SchemaDefinition.md)
## Used in

 *  class: [definition](Definition.md) references: [slot definition](SlotDefinition.md)
 *  class: [definition](Definition.md) references: [class definition](ClassDefinition.md)
 *  class: [definition](Definition.md) references: [schema definition](SchemaDefinition.md)
## Fields

 * _[is_a](is_a.md)_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: [definition](Definition.md)
 * _[mixin](mixin.md)_
    * _Used only as a mixin -- cannot be instantiated on its own._
    * range: boolean
 * _[mixins](mixins.md)_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: [definition](Definition.md)*
 * _[abstract](abstract.md)_
    * _An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored_
    * range: boolean
 * _[local_names](local_names.md)_
    * _map from local identifier to slot_
    * range: string*
 * _[union_of](union_of.md)_
    * _list of class or slot definitions that are combined to create the union class_
    * range: [definition](Definition.md)*
 * _[subclass_of](subclass_of.md)_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: [definition](Definition.md)
 * _[values_from](values_from.md)_
    * _identifies the possible uri's of the range_
    * range: string*
 * _[symmetric](symmetric.md)_
    * _Symmetric slot_
    * range: boolean
