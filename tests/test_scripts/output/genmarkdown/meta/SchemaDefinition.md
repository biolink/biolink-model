# Class: schema definition


A collection of definitions

URI: [http://bioentity.io/vocab/SchemaDefinition](http://bioentity.io/vocab/SchemaDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition|id:string;version:string%20%3F;imports:string%20*;license:string%20%3F;default_prefix:string%20%3F;default_curi_maps:string%20*;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_size:integer%20%3F;source_file_date:string%20%3F;generation_date:date%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;subclass_of(i):uri%20%3F;values_from(i):string%20*;symmetric(i):boolean%20%3F]-%20union_of(i)%20*>\[Definition],%20\[SchemaDefinition]-%20mixins(i)%20*>\[Definition],%20\[SchemaDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[SchemaDefinition]-%20alt_descriptions(i)%20*>\[AltDescription],%20\[SchemaDefinition]++-%20examples(i)%20*>\[Example],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[SchemaDefinition]-%20default_type%20%3F>\[TypeDefinition],%20\[SchemaDefinition]++-%20prefixes%20*>\[Prefix],%20\[Definition]^-\[SchemaDefinition])
## Mappings

## Inheritance

 *  is_a: [Definition](Definition.md) - definition base class
## Children

## Used in

## Fields

 * [classes](classes.md)
    * Description: classes defined in schema
    * range: [ClassDefinition](ClassDefinition.md)*
    * __Local__
 * [default_curi_maps](default_curi_maps.md)
    * Description: List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
    * range: **string***
    * __Local__
 * [default_prefix](default_prefix.md)
    * Description: default and base prefix -- used for ':' identifiers, @base and @vocab
    * range: **string**
    * __Local__
 * [default_type](default_type.md)
    * Description: the default type if range is omitted
    * range: [TypeDefinition](TypeDefinition.md)
    * __Local__
 * [generation_date](generation_date.md)
    * Description: date that the schema was loaded/generated.  Supplied by the loader
    * range: **date**
    * __Local__
 * [id](id.md)
    * Description: a globally unique id or url for a schema
    * range: **string**
    * __Local__
 * [imports](imports.md)
    * Description: A list of modules that are imported into the schema
    * range: **string***
    * __Local__
 * [license](license.md)
    * Description: license for the schema
    * range: **string**
    * __Local__
 * [metamodel_version](metamodel_version.md)
    * Description: Version of the metamodel used to load the schema. Supplied by the loader
    * range: **string**
    * __Local__
 * [prefixes](prefixes.md)
    * Description: Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes
    * range: [Prefix](Prefix.md)*
    * __Local__
 * [schema definition.slots](slot_definitions.md)
    * Description: collection of slot definitions in a schema
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * [source_file](source_file.md)
    * Description: name, uri or description of the source of the schema.  Supplied by the loader
    * range: **string**
    * __Local__
 * [source_file_date](source_file_date.md)
    * Description: modification date of the source of the schema.  Supplied by the loader
    * range: **string**
    * __Local__
 * [source_file_size](source_file_size.md)
    * Description: size in bytes of the source of the schema.  Supplied by the loader
    * range: **integer**
    * __Local__
 * [types](types.md)
    * Description: types defined in schema
    * range: [TypeDefinition](TypeDefinition.md)*
    * __Local__
 * [version](version.md)
    * Description: Schema version
    * range: **string**
    * __Local__
 * [abstract](abstract.md)
    * Description: An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [aliases](aliases.md)
    * range: **string***
    * inherited from: [Element](Element.md)
 * [alt_descriptions](alt_descriptions.md)
    * range: [AltDescription](AltDescription.md)*
    * inherited from: [Element](Element.md)
 * [comment](comment.md)
    * Description: Comment about an element
    * range: **string**
    * inherited from: [Element](Element.md)
 * [description](description.md)
    * Description: a description
    * range: **string**
    * inherited from: [Element](Element.md)
 * [examples](examples.md)
    * Description: Example of usage for a slot or class
    * range: [Example](Example.md)*
    * inherited from: [Element](Element.md)
 * [flags](flags.md)
    * Description: State information and other details
    * range: **string***
    * inherited from: [Element](Element.md)
 * [from_schema](from_schema.md)
    * Description: id of the schema that the element was derived from.  Supplied by the loader.
    * range: **string**
    * inherited from: [Element](Element.md)
 * [id_prefixes](id_prefixes.md)
    * range: **string***
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: **string***
    * inherited from: [Element](Element.md)
 * [is_a](is_a.md)
    * Description: specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * [local_names](local_names.md)
    * Description: map from local identifier to slot
    * range: **string***
    * inherited from: [Definition](Definition.md)
 * [mappings](mappings.md)
    * Description: list of equivalent or skos exact mappings to an ontology class
    * range: **string***
    * inherited from: [Element](Element.md)
 * [mixin](mixin.md)
    * Description: Used only as a mixin -- cannot be instantiated on its own.
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [mixins](mixins.md)
    * Description: List of definitions to be mixed in. Targets may be any definition of the same type
    * range: [Definition](Definition.md)*
    * inherited from: [Definition](Definition.md)
 * [name](name.md)
    * Description: a unique key that identifies a slot, type or class in a schema
    * range: **string**
    * inherited from: [Element](Element.md)
 * [note](note.md)
    * Description: Notes about an element
    * range: **string**
    * inherited from: [Element](Element.md)
 * [see_also](see_also.md)
    * range: **string**
    * inherited from: [Element](Element.md)
 * [singular_name](singular_name.md)
    * Description: a name that is used in the singular form
    * range: **string**
    * inherited from: [Element](Element.md)
 * [subclass_of](subclass_of.md)
    * Description: Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes
    * range: **uri**
    * inherited from: [Definition](Definition.md)
 * [symmetric](symmetric.md)
    * Description: Symmetric slot
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [union_of](union_of.md)
    * Description: list of class or slot definitions that are combined to create the union class
    * range: [Definition](Definition.md)*
    * inherited from: [Definition](Definition.md)
 * [values_from](values_from.md)
    * Description: identifies the possible uri's of the range
    * range: **string***
    * inherited from: [Definition](Definition.md)
