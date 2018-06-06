# Class: type definition


A type definition

URI: [http://bioentity.io/vocab/TypeDefinition](http://bioentity.io/vocab/TypeDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element]^-\[TypeDefinition|name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;typeof:string%20%3F],%20\[TypeDefinition]++-%20examples(i)%20*>\[Example])
## Mappings

## Inheritance

 *  is_a: [element](Element.md) - root of all described things
## Children

## Used in

## Fields

 * _[typeof](typeof.md)_
    * _a builtin ('string', 'integer', 'float', 'double', 'boolean', 'time') or another type definition_
    * range: string
    * __Local__
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [example](Example.md)*
    * inherited from: [element](Element.md)
