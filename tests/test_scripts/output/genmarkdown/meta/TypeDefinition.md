# Class: type definition


A type definition

URI: [http://bioentity.io/vocab/TypeDefinition](http://bioentity.io/vocab/TypeDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[TypeDefinition|typeof:string%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F]-%20alt_descriptions(i)%20*>\[AltDescription],%20\[TypeDefinition]++-%20examples(i)%20*>\[Example],%20\[SchemaDefinition]-%20default_type(i)%20%3F>\[TypeDefinition],%20\[SchemaDefinition]++-%20types(i)%20*>\[TypeDefinition],%20\[Element]^-\[TypeDefinition])
## Mappings

## Inheritance

 *  is_a: [Element](Element.md) - root of all described things
## Children

## Used in

 *  class: **[SchemaDefinition](SchemaDefinition.md)** *[default_type](default_type.md)* **[TypeDefinition](TypeDefinition.md)**
 *  class: **[SchemaDefinition](SchemaDefinition.md)** *[types](types.md)* **[TypeDefinition](TypeDefinition.md)**
## Fields

 * [typeof](typeof.md)
    * Description: a builtin ('string', 'integer', 'float', 'double', 'boolean', 'time', 'uri') or another type definition
    * range: **string**
    * __Local__
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
 * [mappings](mappings.md)
    * Description: list of equivalent or skos exact mappings to an ontology class
    * range: **string***
    * inherited from: [Element](Element.md)
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
