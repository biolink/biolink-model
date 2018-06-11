# Class: class definition


A class or interface

URI: [http://bioentity.io/vocab/ClassDefinition](http://bioentity.io/vocab/ClassDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClassDefinition|entity:boolean%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;values_from(i):string%20*;symmetric(i):boolean%20%3F]-%20subclass_of(i)%20%3F>\[Definition],%20\[ClassDefinition]-%20union_of(i)%20*>\[Definition],%20\[ClassDefinition]-%20mixins(i)%20*>\[Definition],%20\[ClassDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[ClassDefinition]++-%20examples(i)%20*>\[Example],%20\[ClassDefinition]-%20apply_to%20%3F>\[ClassDefinition],%20\[ClassDefinition]++-%20slot_usage%20*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%20*>\[SlotDefinition],%20\[ClassDefinition]-%20defining_slots%20*>\[SlotDefinition],%20\[ClassDefinition]-%20apply_to%20%3F>\[ClassDefinition],%20\[SlotDefinition]-%20domain(i)%20%3F>\[ClassDefinition],%20\[SchemaDefinition]++-%20classes(i)%20*>\[ClassDefinition],%20\[Definition]^-\[ClassDefinition])
## Mappings

## Inheritance

 *  is_a: definition
## Children

## Used in

 *  class: **class definition** *apply_to* **class definition**
 *  class: **schema definition** *classes* **class definition**
 *  class: **slot definition** *domain* **class definition**
## Fields

 * _apply_to_
    * _Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class._
    * range: class definition
    * __Local__
 * _defining_slots_
    * _The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom_
    * range: slot definition*
    * __Local__
 * _entity_
    * range: **boolean**
    * __Local__
 * _slot_usage_
    * _Additional info on how a slot is used in the context of a class. Many slots may be re-used across different classes, but the meaning of the slot may be refined by context. For example, a generic association model may use slots subject/predicate/object with generic semantics and minimal constraints. When this is subclasses, e.g. to disease-phenotype associations then slot_usage may specify both local naming (e.g. subject=disease) and local constraints_
    * range: slot definition*
    * __Local__
 * _slots_
    * _list of slot names that are applicable to a class. slots are by default inherited over is_a and mixins._
    * range: slot definition*
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
