# Class: element


root of all described things

URI: [http://bioentity.io/vocab/Element]
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
    * __range__: 
 * _[singular_name](singular_name.md)_
    * _a name that is used in the singular form_
    * __range__: 
 * _[description](description.md)_
    * _a description_
    * __range__: 
 * _[note](note.md)_
    * _Notes about an element_
    * __range__: 
 * _[comment](comment.md)_
    * _Comment about an element_
    * __range__: 
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * __range__: [example](Example.md)*
 * _[see_also](see_also.md)_
    * __range__: string
 * _[flags](flags.md)_
    * _State information and other details_
    * __range__: string*
 * _[prefixes](prefixes.md)_
    * _list of ID/CURIE prefixes applicable to that element_
    * __range__: *
 * _[aliases](aliases.md)_
    * __range__: *
 * _[mappings](mappings.md)_
    * _list of equivalent or skos exact mappings to an ontology class_
    * __range__: *
 * _[id_prefixes](id_prefixes.md)_
    * __range__: *
 * _[in_subset](in_subset.md)_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * __range__: string*
 * _[from_schema](from_schema.md)_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * __range__: 
