# Class: element


root of all described things

URI: http://bioentity.io/vocab/Element

![img](http://yuml.me/diagram/nofunky/class/\[Element|name(pk):string;singular_name:string%20%3F;description:string%20%3F;note:string%20%3F;comment:string%20%3F;see_also:string%20%3F;flags:string%20*;prefixes:string%20*;aliases:string%20*;mappings:string%20*;id_prefixes:string%20*;in_subset:string%20*;from_schema:string%20%3F;alt_descriptions:string%20*]^-\[Definition],%20\[Element]^-\[TypeDefinition],%20\[Element]++-%20examples%20*>\[Example],%20)
## Mappings

## Inheritance

## Children

 *  child: [definition](Definition.md)
 *  child: [type definition](TypeDefinition.md)
## Used in

 *  class: [element](Element.md) references: [definition](Definition.md)
 *  class: [element](Element.md) references: [type definition](TypeDefinition.md)
## Fields

 * _[name](name.md)_
    * _a unique key that identifies a slot, type or class in a schema_
    * range: string
 * _[singular_name](singular_name.md)_
    * _a name that is used in the singular form_
    * range: string
 * _[description](description.md)_
    * _a description_
    * range: string
 * _[note](note.md)_
    * _Notes about an element_
    * range: string
 * _[comment](comment.md)_
    * _Comment about an element_
    * range: string
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [example](Example.md)*
 * _[see_also](see_also.md)_
    * range: string
 * _[flags](flags.md)_
    * _State information and other details_
    * range: string*
 * _[prefixes](prefixes.md)_
    * _list of ID/CURIE prefixes applicable to that element_
    * range: string*
 * _[aliases](aliases.md)_
    * range: string*
 * _[mappings](mappings.md)_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: string*
 * _[id_prefixes](id_prefixes.md)_
    * range: string*
 * _[in_subset](in_subset.md)_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * range: string*
 * _[from_schema](from_schema.md)_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * range: string
 * _[alt_descriptions](alt_descriptions.md)_
    * range: string*
