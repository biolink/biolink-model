# Class: schema definition


A collection of definitions

URI: [http://bioentity.io/vocab/SchemaDefinition](http://bioentity.io/vocab/SchemaDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition|id:string;version:string%20%3F;imports:string%20*;license:string%20%3F;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_size:integer%20%3F;source_file_date:string%20%3F;generation_date:date%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;values_from(i):string%20*;symmetric(i):boolean%20%3F]-%20subclass_of(i)%20%3F>\[Definition],%20\[SchemaDefinition]-%20union_of(i)%20*>\[Definition],%20\[SchemaDefinition]-%20mixins(i)%20*>\[Definition],%20\[SchemaDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[SchemaDefinition]++-%20examples(i)%20*>\[Example],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[Definition]^-\[SchemaDefinition])
## Mappings

## Inheritance

 *  is_a: [Definition](Definition.md) - definition base class
## Children

## Used in

## Fields

 * _[classes](classes.md)_
    * _classes defined in schema_
    * range: [ClassDefinition](ClassDefinition.md)*
    * __Local__
 * _[generation_date](generation_date.md)_
    * _date that the schema was loaded/generated.  Supplied by the loader_
    * range: **date**
    * __Local__
 * _[id](id.md)_
    * _a globally unique id or url for a schema_
    * range: **string**
    * __Local__
 * _[imports](imports.md)_
    * _A list of modules that are imported into the schema_
    * range: **string***
    * __Local__
 * _[license](license.md)_
    * _license for the schema_
    * range: **string**
    * __Local__
 * _[metamodel_version](metamodel_version.md)_
    * _Version of the metamodel used to load the schema. Supplied by the loader_
    * range: **string**
    * __Local__
 * _[schema definition.slots](slot_definitions.md)_
    * _collection of slot definitions in a schema_
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * _[source_file](source_file.md)_
    * _name, uri or description of the source of the schema.  Supplied by the loader_
    * range: **string**
    * __Local__
 * _[source_file_date](source_file_date.md)_
    * _modification date of the source of the schema.  Supplied by the loader_
    * range: **string**
    * __Local__
 * _[source_file_size](source_file_size.md)_
    * _size in bytes of the source of the schema.  Supplied by the loader_
    * range: **integer**
    * __Local__
 * _[types](types.md)_
    * _types defined in schema_
    * range: [TypeDefinition](TypeDefinition.md)*
    * __Local__
 * _[version](version.md)_
    * _Schema version_
    * range: **string**
    * __Local__
 * _[abstract](abstract.md)_
    * _An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored_
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[aliases](aliases.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[alt_descriptions](alt_descriptions.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[comment](comment.md)_
    * _Comment about an element_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[description](description.md)_
    * _a description_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [Example](Example.md)*
    * inherited from: [Element](Element.md)
 * _[flags](flags.md)_
    * _State information and other details_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[from_schema](from_schema.md)_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[id_prefixes](id_prefixes.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[in_subset](in_subset.md)_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[is_a](is_a.md)_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * _[local_names](local_names.md)_
    * _map from local identifier to slot_
    * range: **string***
    * inherited from: [Definition](Definition.md)
 * _[mappings](mappings.md)_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[mixin](mixin.md)_
    * _Used only as a mixin -- cannot be instantiated on its own._
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[mixins](mixins.md)_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: [Definition](Definition.md)*
    * inherited from: [Definition](Definition.md)
 * _[name](name.md)_
    * _a unique key that identifies a slot, type or class in a schema_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[note](note.md)_
    * _Notes about an element_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[prefixes](prefixes.md)_
    * _list of ID/CURIE prefixes applicable to that element_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[see_also](see_also.md)_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[singular_name](singular_name.md)_
    * _a name that is used in the singular form_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[subclass_of](subclass_of.md)_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * _[symmetric](symmetric.md)_
    * _Symmetric slot_
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[union_of](union_of.md)_
    * _list of class or slot definitions that are combined to create the union class_
    * range: [Definition](Definition.md)*
    * inherited from: [Definition](Definition.md)
 * _[values_from](values_from.md)_
    * _identifies the possible uri's of the range_
    * range: **string***
    * inherited from: [Definition](Definition.md)
