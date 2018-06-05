# Class: schema definition


A collection of definitions

URI: http://bioentity.io/vocab/SchemaDefinition

![img](http://yuml.me/diagram/nofunky/class/\[Definition]^-\[SchemaDefinition|id(pk):string;version:string%20%3F;imports:string%20*;license:string%20%3F;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_size:integer%20%3F;source_file_date:string%20%3F;generation_date:date%20%3F],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition],%20)
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md)
## Children

## Used in

## Fields

 * _[id](id.md)_
    * _a globally unique id or url for a schema_
    * range: string
 * _[version](version.md)_
    * _Schema version_
    * range: string
 * _[imports](imports.md)_
    * _A list of modules that are imported into the schema_
    * range: string*
 * _[license](license.md)_
    * _license for the schema_
    * range: string
 * _[types](types.md)_
    * _types defined in schema_
    * range: [type definition](TypeDefinition.md)*
 * _[slots](slots.md)_
    * _collection of slot definitions in a schema_
    * range: [slot definition](SlotDefinition.md)*
 * _[classes](classes.md)_
    * _classes defined in schema_
    * range: [class definition](ClassDefinition.md)*
 * _[metamodel_version](metamodel_version.md)_
    * _Version of the metamodel used to load the schema. Supplied by the loader_
    * range: string
 * _[source_file](source_file.md)_
    * _name, uri or description of the source of the schema.  Supplied by the loader_
    * range: string
 * _[source_file_size](source_file_size.md)_
    * _size in bytes of the source of the schema.  Supplied by the loader_
    * range: integer
 * _[source_file_date](source_file_date.md)_
    * _modification date of the source of the schema.  Supplied by the loader_
    * range: string
 * _[generation_date](generation_date.md)_
    * _date that the schema was loaded/generated.  Supplied by the loader_
    * range: date
