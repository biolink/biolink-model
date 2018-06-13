# Class: slot definition


A property or slot

URI: [http://bioentity.io/vocab/SlotDefinition](http://bioentity.io/vocab/SlotDefinition)

![img](images/SlotDefinition.png)
## Mappings

## Inheritance

 *  is_a: definition
## Children

## Used in

 *  class: **class definition** *defining_slots* **slot definition**
 *  class: **slot definition** *inverse* **slot definition**
 *  class: **schema definition** *slot definitions* **slot definition**
 *  class: **class definition** *slot_usage* **slot definition**
 *  class: **class definition** *slots* **slot definition**
 *  class: **slot definition** *subproperty_of* **slot definition**
## Fields

 * _alias_
    * _A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference_
    * range: **string**
    * __Local__
 * _definitional_
    * _slot is a defining slot -- injection into the defining_slots list_
    * range: **boolean**
    * __Local__
 * _domain_
    * _The class to which this slot applies._
    * range: class definition
    * __Local__
 * _identifier_
    * _True means that this slot must be unique across the collection of slots_
    * range: **boolean**
    * __Local__
 * _inlined_
    * _if true then the value of this slot is inlined (i.e. a nested object) rather linked by key_
    * range: **boolean**
    * __Local__
 * _inverse_
    * _used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')_
    * range: slot definition
    * __Local__
 * _is_class_field_
    * range: **boolean**
    * __Local__
 * _multivalued_
    * _If true slot can have many values_
    * range: **boolean**
    * __Local__
 * _not_inherited_
    * _True means that the slot is local and is not_inherited across is_a or slot_usage paths_
    * range: **boolean**
    * __Local__
 * _path_
    * _For any denormalized slot, this represents the tree or graph path used to generate the denormalized form_
    * range: **string**
    * __Local__
 * _primary_key_
    * _True means that this serves as a unique identifier_
    * range: **boolean**
    * __Local__
 * _range_
    * _The slot type.  If absent, it is the builtin type 'string'_
    * range: element
    * __Local__
 * _required_
    * _If true slot must have at least one value_
    * range: **boolean**
    * __Local__
 * _role_
    * range: **string**
    * __Local__
 * _subproperty_of_
    * _Ontolgy property which this is a subproperty of_
    * range: slot definition
    * __Local__
 * _abstract_
    * _An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored_
    * range: **boolean**
    * inherited from: definition
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
 * _is_a_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: definition
    * inherited from: definition
 * _local_names_
    * _map from local identifier to slot_
    * range: **string***
    * inherited from: definition
 * _mappings_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: **string***
    * inherited from: element
 * _mixin_
    * _Used only as a mixin -- cannot be instantiated on its own._
    * range: **boolean**
    * inherited from: definition
 * _mixins_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: definition*
    * inherited from: definition
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
 * _subclass_of_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: definition
    * inherited from: definition
 * _symmetric_
    * _Symmetric slot_
    * range: **boolean**
    * inherited from: definition
 * _union_of_
    * _list of class or slot definitions that are combined to create the union class_
    * range: definition*
    * inherited from: definition
 * _values_from_
    * _identifies the possible uri's of the range_
    * range: **string***
    * inherited from: definition
