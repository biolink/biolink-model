# Class: element


root of all described things

URI: [http://w3id.org/biolink/vocab/Element](http://w3id.org/biolink/vocab/Element)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element|name:string;singular_name:string%20%3F;description:string%20%3F;note:string%20%3F;comment:string%20%3F;see_also:string%20%3F;flags:string%20*;aliases:string%20*;mappings:string%20*;id_prefixes:string%20*;in_subset:string%20*;from_schema:string%20%3F]-%20alt_descriptions%20*>\[AltDescription],%20\[Element]++-%20examples%20*>\[Example],%20\[Element]^-\[TypeDefinition],%20\[Element]^-\[Definition])
## Mappings

## Inheritance

## Children

 * [Definition](Definition.md) - definition base class
 * [TypeDefinition](TypeDefinition.md) - A type definition
## Used in

## Fields

 * [aliases](aliases.md)
    * range: **string***
    * __Local__
 * [alt_descriptions](alt_descriptions.md)
    * range: [AltDescription](AltDescription.md)*
    * __Local__
 * [comment](comment.md)
    * Description: Comment about an element
    * range: **string**
    * __Local__
 * [description](description.md)
    * Description: a description
    * range: **string**
    * __Local__
 * [examples](examples.md)
    * Description: Example of usage for a slot or class
    * range: [Example](Example.md)*
    * __Local__
 * [flags](flags.md)
    * Description: State information and other details
    * range: **string***
    * __Local__
 * [from_schema](from_schema.md)
    * Description: id of the schema that the element was derived from.  Supplied by the loader.
    * range: **string**
    * __Local__
 * [id_prefixes](id_prefixes.md)
    * range: **string***
    * __Local__
 * [in_subset](in_subset.md)
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: **string***
    * __Local__
 * [mappings](mappings.md)
    * Description: list of equivalent or skos exact mappings to an ontology class
    * range: **string***
    * __Local__
 * [name](name.md)
    * Description: a unique key that identifies a slot, type or class in a schema
    * range: **string**
    * __Local__
 * [note](note.md)
    * Description: Notes about an element
    * range: **string**
    * __Local__
 * [see_also](see_also.md)
    * range: **string**
    * __Local__
 * [singular_name](singular_name.md)
    * Description: a name that is used in the singular form
    * range: **string**
    * __Local__
