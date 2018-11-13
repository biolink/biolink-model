# Class: element


root of all described things

URI: [http://w3id.org/biolink/vocab/Element](http://w3id.org/biolink/vocab/Element)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element|name:string;singular_name:string%20%3F;description:string%20%3F;note:string%20%3F;comment:string%20%3F;see_also:string%20%3F;flags:string%20*;aliases:string%20*;mappings:string%20*;id_prefixes:string%20*;in_subset:string%20*;from_schema:string%20%3F;exact_matches:string%20*;broader_matches:string%20*;narrower_matches:string%20*;close_matches:string%20*]-%20alt_descriptions%20*>\[AltDescription],%20\[Element]++-%20examples%20*>\[Example],%20\[Element]^-\[TypeDefinition],%20\[Element]^-\[Definition])
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
 * [broader_matches](broader_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
    * range: **string***
    * __Local__
 * [close_matches](close_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity).
    * range: **string***
    * __Local__
 * [comment](comment.md)
    * Description: Comment about an element
    * range: **string**
    * __Local__
 * [description](description.md)
    * Description: a description
    * range: **string**
    * __Local__
 * [exact_matches](exact_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have strictly equivalent meanings. 
    * range: **string***
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
    * Description: a list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: **string***
    * __Local__
 * [name](name.md)
    * Description: a unique key that identifies a slot, type or class in a schema
    * range: **string**
    * __Local__
 * [narrower_matches](narrower_matches.md)
    * Description: a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
    * range: **string***
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
