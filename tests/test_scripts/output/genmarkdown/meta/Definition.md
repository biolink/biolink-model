# Class: definition


definition base class

URI: [http://w3id.org/biolink/vocab/Definition](http://w3id.org/biolink/vocab/Definition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Definition|mixin:boolean%20%3F;abstract:boolean%20%3F;local_names:string%20*;subclass_of:uri%20%3F;values_from:string%20*;symmetric:boolean%20%3F;name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;exact_matches(i):string%20*;broader_matches(i):string%20*;narrower_matches(i):string%20*;close_matches(i):string%20*]-%20alt_descriptions(i)%20*>\[AltDescription],%20\[Definition]++-%20examples(i)%20*>\[Example],%20\[Definition]-%20union_of%20*>\[Definition],%20\[Definition]-%20mixins%20*>\[Definition],%20\[Definition]-%20is_a%20%3F>\[Definition],%20\[Definition]-%20is_a%20%3F>\[Definition],%20\[Definition]-%20mixins%20*>\[Definition],%20\[Definition]-%20union_of%20*>\[Definition],%20\[Definition]^-\[SlotDefinition],%20\[Definition]^-\[SchemaDefinition],%20\[Definition]^-\[ClassDefinition],%20\[Element]^-\[Definition])
## Mappings

## Inheritance

 *  is_a: [Element](Element.md) - root of all described things
## Children

 * [ClassDefinition](ClassDefinition.md) - A class or interface
 * [SchemaDefinition](SchemaDefinition.md) - A collection of definitions
 * [SlotDefinition](SlotDefinition.md) - A property or slot
## Used in

 *  class: **[Definition](Definition.md)** *[is_a](is_a.md)* **[Definition](Definition.md)**
 *  class: **[Definition](Definition.md)** *[mixins](mixins.md)* **[Definition](Definition.md)**
 *  class: **[Definition](Definition.md)** *[union_of](union_of.md)* **[Definition](Definition.md)**
## Fields

 * [abstract](abstract.md)
    * Description: An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored
    * range: **boolean**
    * __Local__
 * [is_a](is_a.md)
    * Description: specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
    * range: [Definition](Definition.md)
    * __Local__
 * [local_names](local_names.md)
    * Description: map from local identifier to slot
    * range: **string***
    * __Local__
 * [mixin](mixin.md)
    * Description: Used only as a mixin -- cannot be instantiated on its own.
    * range: **boolean**
    * __Local__
 * [mixins](mixins.md)
    * Description: List of definitions to be mixed in. Targets may be any definition of the same type
    * range: [Definition](Definition.md)*
    * __Local__
 * [subclass_of](subclass_of.md)
    * Description: Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes
    * range: **uri**
    * __Local__
 * [symmetric](symmetric.md)
    * Description: Symmetric slot
    * range: **boolean**
    * __Local__
 * [union_of](union_of.md)
    * Description: list of class or slot definitions that are combined to create the union class
    * range: [Definition](Definition.md)*
    * __Local__
 * [values_from](values_from.md)
    * Description: identifies the possible uri's of the range
    * range: **string***
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
