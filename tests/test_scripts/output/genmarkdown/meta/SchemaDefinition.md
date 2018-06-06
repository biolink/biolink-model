# Class: schema definition


A collection of definitions

URI: [http://bioentity.io/vocab/SchemaDefinition](http://bioentity.io/vocab/SchemaDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Definition]^-\[SchemaDefinition|name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;values_from(i):string%20*;symmetric(i):boolean%20%3F;id:string;version:string%20%3F;imports:string%20*;license:string%20%3F;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_size:integer%20%3F;source_file_date:string%20%3F;generation_date:date%20%3F],%20\[SchemaDefinition]++-%20examples(i)%20*>\[Example],%20\[SchemaDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[SchemaDefinition]-%20mixins(i)%20*>\[Definition],%20\[SchemaDefinition]-%20union_of(i)%20*>\[Definition],%20\[SchemaDefinition]-%20subclass_of(i)%20%3F>\[Definition],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition])
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md) - definition base class
## Children

## Used in

## Fields

 * _[id](id.md)_
    * _a globally unique id or url for a schema_
    * range: string
    * __Local__
 * _[version](version.md)_
    * _Schema version_
    * range: string
    * __Local__
 * _[imports](imports.md)_
    * _A list of modules that are imported into the schema_
    * range: string*
    * __Local__
 * _[license](license.md)_
    * _license for the schema_
    * range: string
    * __Local__
 * _[types](types.md)_
    * _types defined in schema_
    * range: [type definition](TypeDefinition.md)*
    * __Local__
 * _[slots](slots.md)_
    * _collection of slot definitions in a schema_
    * range: [slot definition](SlotDefinition.md)*
    * __Local__
 * _[classes](classes.md)_
    * _classes defined in schema_
    * range: [class definition](ClassDefinition.md)*
    * __Local__
 * _[metamodel_version](metamodel_version.md)_
    * _Version of the metamodel used to load the schema. Supplied by the loader_
    * range: string
    * __Local__
 * _[source_file](source_file.md)_
    * _name, uri or description of the source of the schema.  Supplied by the loader_
    * range: string
    * __Local__
 * _[source_file_size](source_file_size.md)_
    * _size in bytes of the source of the schema.  Supplied by the loader_
    * range: integer
    * __Local__
 * _[source_file_date](source_file_date.md)_
    * _modification date of the source of the schema.  Supplied by the loader_
    * range: string
    * __Local__
 * _[generation_date](generation_date.md)_
    * _date that the schema was loaded/generated.  Supplied by the loader_
    * range: date
    * __Local__
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [example](Example.md)*
    * inherited from: [element](Element.md)
 * _[is_a](is_a.md)_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: [definition](Definition.md)
    * inherited from: [definition](Definition.md)
 * _[mixins](mixins.md)_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: [definition](Definition.md)*
    * inherited from: [definition](Definition.md)
 * _[union_of](union_of.md)_
    * _list of class or slot definitions that are combined to create the union class_
    * range: [definition](Definition.md)*
    * inherited from: [definition](Definition.md)
 * _[subclass_of](subclass_of.md)_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: [definition](Definition.md)
    * inherited from: [definition](Definition.md)
