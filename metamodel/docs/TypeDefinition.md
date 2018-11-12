# Class: type definition


A type definition

URI: [http://w3id.org/biolink/vocab/TypeDefinition](http://w3id.org/biolink/vocab/TypeDefinition)

![img](images/TypeDefinition.png)
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
 * [broader_matches](broader_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
    * range: **string***
    * inherited from: [Element](Element.md)
 * [close_matches](close_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity).
    * range: **string***
    * inherited from: [Element](Element.md)
 * [comment](comment.md)
    * Description: Comment about an element
    * range: **string**
    * inherited from: [Element](Element.md)
 * [description](description.md)
    * Description: a description
    * range: **string**
    * inherited from: [Element](Element.md)
 * [exact_matches](exact_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have strictly equivalent meanings. 
    * range: **string***
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
    * Description: a list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: **string***
    * inherited from: [Element](Element.md)
 * [name](name.md)
    * Description: a unique key that identifies a slot, type or class in a schema
    * range: **string**
    * inherited from: [Element](Element.md)
 * [narrower_matches](narrower_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
    * range: **string***
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
