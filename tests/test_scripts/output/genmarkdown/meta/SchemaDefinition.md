# Class: schema definition


A collection of definitions

URI: [http://bioentity.io/vocab/SchemaDefinition]
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md)
## Children

## Used in

## Fields

 * _[id](id.md)_
    * _a globally unique id or url for a schema_
    * __range__: 
 * _[version](version.md)_
    * _Schema version_
    * __range__: 
 * _[imports](imports.md)_
    * _A list of modules that are imported into the schema_
    * __range__: *
 * _[license](license.md)_
    * _license for the schema_
    * __range__: 
 * _[types](types.md)_
    * _types defined in schema_
    * __range__: [type definition](TypeDefinition.md)*
 * _[slot definitions](slots.md)_
    * _collection of slot definitions in a schema_
    * __range__: [slot definition](SlotDefinition.md)*
 * _[classes](classes.md)_
    * _classes defined in schema_
    * __range__: [class definition](ClassDefinition.md)*
 * _[metamodel_version](metamodel_version.md)_
    * _Version of the metamodel used to load the schema. Supplied by the loader_
    * __range__: 
 * _[source_file](source_file.md)_
    * _name, uri or description of the source of the schema.  Supplied by the loader_
    * __range__: 
 * _[source_file_size](source_file_size.md)_
    * _size in bytes of the source of the schema.  Supplied by the loader_
    * __range__: integer
 * _[source_file_date](source_file_date.md)_
    * _modification date of the source of the schema.  Supplied by the loader_
    * __range__: 
 * _[generation_date](generation_date.md)_
    * _date that the schema was loaded/generated.  Supplied by the loader_
    * __range__: date
