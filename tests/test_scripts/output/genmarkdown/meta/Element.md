# Class: element


root of all described things

URI: [http://bioentity.io/vocab/Element](http://bioentity.io/vocab/Element)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element|name:string;singular_name:string%20%3F;description:string%20%3F;note:string%20%3F;comment:string%20%3F;see_also:string%20%3F;flags:string%20*;prefixes:string%20*;aliases:string%20*;mappings:string%20*;id_prefixes:string%20*;in_subset:string%20*;from_schema:string%20%3F;alt_descriptions:string%20*]++-%20examples%20*>\[Example],%20\[SlotDefinition]-%20range(i)%20%3F>\[Element],%20\[Element]^-\[TypeDefinition],%20\[Element]^-\[Definition])
## Mappings

## Inheritance

## Children

 * [Definition](Definition.md) - definition base class
 * [TypeDefinition](TypeDefinition.md) - A type definition
## Used in

 *  class: **[SlotDefinition](SlotDefinition.md)** *[range](range.md)* **[Element](Element.md)**
## Fields

 * _[aliases](aliases.md)_
    * range: **string***
    * __Local__
 * _[alt_descriptions](alt_descriptions.md)_
    * range: **string***
    * __Local__
 * _[comment](comment.md)_
    * _Comment about an element_
    * range: **string**
    * __Local__
 * _[description](description.md)_
    * _a description_
    * range: **string**
    * __Local__
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [Example](Example.md)*
    * __Local__
 * _[flags](flags.md)_
    * _State information and other details_
    * range: **string***
    * __Local__
 * _[from_schema](from_schema.md)_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * range: **string**
    * __Local__
 * _[id_prefixes](id_prefixes.md)_
    * range: **string***
    * __Local__
 * _[in_subset](in_subset.md)_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * range: **string***
    * __Local__
 * _[mappings](mappings.md)_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: **string***
    * __Local__
 * _[name](name.md)_
    * _a unique key that identifies a slot, type or class in a schema_
    * range: **string**
    * __Local__
 * _[note](note.md)_
    * _Notes about an element_
    * range: **string**
    * __Local__
 * _[prefixes](prefixes.md)_
    * _list of ID/CURIE prefixes applicable to that element_
    * range: **string***
    * __Local__
 * _[see_also](see_also.md)_
    * range: **string**
    * __Local__
 * _[singular_name](singular_name.md)_
    * _a name that is used in the singular form_
    * range: **string**
    * __Local__
