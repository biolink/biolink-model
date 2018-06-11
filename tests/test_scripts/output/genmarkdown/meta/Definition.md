# Class: definition


definition base class

URI: [http://bioentity.io/vocab/Definition](http://bioentity.io/vocab/Definition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Definition|mixin:boolean%20%3F;abstract:boolean%20%3F;local_names:string%20*;values_from:string%20*;symmetric:boolean%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*]++-%20examples(i)%20*>\[Example],%20\[Definition]-%20subclass_of%20%3F>\[Definition],%20\[Definition]-%20union_of%20*>\[Definition],%20\[Definition]-%20mixins%20*>\[Definition],%20\[Definition]-%20is_a%20%3F>\[Definition],%20\[Definition]-%20is_a%20%3F>\[Definition],%20\[Definition]-%20mixins%20*>\[Definition],%20\[Definition]-%20subclass_of%20%3F>\[Definition],%20\[Definition]-%20union_of%20*>\[Definition],%20\[Definition]^-\[SlotDefinition],%20\[Definition]^-\[SchemaDefinition],%20\[Definition]^-\[ClassDefinition],%20\[Element]^-\[Definition])
## Mappings

## Inheritance

 *  is_a: element
## Children

 * class definition
 * schema definition
 * slot definition
## Used in

 *  class: **definition** *is_a* **definition**
 *  class: **definition** *mixins* **definition**
 *  class: **definition** *subclass_of* **definition**
 *  class: **definition** *union_of* **definition**
## Fields

 * _abstract_
    * _An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored_
    * range: **boolean**
    * __Local__
 * _is_a_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: definition
    * __Local__
 * _local_names_
    * _map from local identifier to slot_
    * range: **string***
    * __Local__
 * _mixin_
    * _Used only as a mixin -- cannot be instantiated on its own._
    * range: **boolean**
    * __Local__
 * _mixins_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: definition*
    * __Local__
 * _subclass_of_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: definition
    * __Local__
 * _symmetric_
    * _Symmetric slot_
    * range: **boolean**
    * __Local__
 * _union_of_
    * _list of class or slot definitions that are combined to create the union class_
    * range: definition*
    * __Local__
 * _values_from_
    * _identifies the possible uri's of the range_
    * range: **string***
    * __Local__
 * _aliases_
    * range: **string***
    * inherited from: element
 * _alt_descriptions_
    * range: **string***
    * inherited from: element
 * _comment_
    * _Comment about an element_
    * range: **string**
    * inherited from: element
 * _description_
    * _a description_
    * range: **string**
    * inherited from: element
 * _examples_
    * _Example of usage for a slot or class_
    * range: example*
    * inherited from: element
 * _flags_
    * _State information and other details_
    * range: **string***
    * inherited from: element
 * _from_schema_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * range: **string**
    * inherited from: element
 * _id_prefixes_
    * range: **string***
    * inherited from: element
 * _in_subset_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * range: **string***
    * inherited from: element
 * _mappings_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: **string***
    * inherited from: element
 * _name_
    * _a unique key that identifies a slot, type or class in a schema_
    * range: **string**
    * inherited from: element
 * _note_
    * _Notes about an element_
    * range: **string**
    * inherited from: element
 * _prefixes_
    * _list of ID/CURIE prefixes applicable to that element_
    * range: **string***
    * inherited from: element
 * _see_also_
    * range: **string**
    * inherited from: element
 * _singular_name_
    * _a name that is used in the singular form_
    * range: **string**
    * inherited from: element
