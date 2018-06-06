# Class: slot definition


A property or slot

URI: [http://bioentity.io/vocab/SlotDefinition](http://bioentity.io/vocab/SlotDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Definition]^-\[SlotDefinition|name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;values_from(i):string%20*;symmetric(i):boolean%20%3F;multivalued:boolean%20%3F;required:boolean%20%3F;inlined:boolean%20%3F;primary_key:boolean%20%3F;identifier:boolean%20%3F;definitional:boolean%20%3F;alias:string%20%3F;path:string%20%3F;is_class_field:boolean%20%3F;role:string%20%3F],%20\[SlotDefinition]++-%20examples(i)%20*>\[Example],%20\[SlotDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[SlotDefinition]-%20mixins(i)%20*>\[Definition],%20\[SlotDefinition]-%20union_of(i)%20*>\[Definition],%20\[SlotDefinition]-%20subclass_of(i)%20%3F>\[Definition],%20\[SlotDefinition]-%20domain%20%3F>\[ClassDefinition],%20\[SlotDefinition]-%20range%20%3F>\[Element],%20\[SlotDefinition]-%20subproperty_of%20%3F>\[SlotDefinition],%20\[SlotDefinition]-%20inverse%20%3F>\[SlotDefinition])
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md) - definition base class
## Children

## Used in

## Fields

 * _[multivalued](multivalued.md)_
    * _If true slot can have many values_
    * range: boolean
    * __Local__
 * _[domain](domain.md)_
    * _The class to which this slot applies._
    * range: [class definition](ClassDefinition.md)
    * __Local__
 * _[range](range.md)_
    * _The slot type.  If absent, it is the builtin type 'string'_
    * range: [element](Element.md)
    * __Local__
 * _[required](required.md)_
    * _If true slot must have at least one value_
    * range: boolean
    * __Local__
 * _[inlined](inlined.md)_
    * _if true then the value of this slot is inlined (i.e. a nested object) rather linked by key_
    * range: boolean
    * __Local__
 * _[primary_key](primary_key.md)_
    * _True means that this serves as a unique identifier_
    * range: boolean
    * __Local__
 * _[identifier](identifier.md)_
    * _True means that this slot must be unique across the collection of slots_
    * range: boolean
    * __Local__
 * _[definitional](definitional.md)_
    * _slot is a defining slot -- injection into the defining_slots list_
    * range: boolean
    * __Local__
 * _[alias](alias.md)_
    * _A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference_
    * range: string
    * __Local__
 * _[path](path.md)_
    * _For any denormalized slot, this represents the tree or graph path used to generate the denormalized form_
    * range: string
    * __Local__
 * _[subproperty_of](subproperty_of.md)_
    * _Ontolgy property which this is a subproperty of_
    * range: [slot definition](SlotDefinition.md)
    * __Local__
 * _[inverse](inverse.md)_
    * _used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')_
    * range: [slot definition](SlotDefinition.md)
    * __Local__
 * _[is_class_field](is_class_field.md)_
    * range: boolean
    * __Local__
 * _[role](role.md)_
    * range: string
    * __Local__
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [example](Example.md)*
    * inherited from: [element](Element.md)
 * _[is_a](is_a.md)_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: [definition](Definition.md)
    * inherited from: [definition](Definition.md)
 * _[mixins](mixins.md)_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: [definition](Definition.md)*
    * inherited from: [definition](Definition.md)
 * _[union_of](union_of.md)_
    * _list of class or slot definitions that are combined to create the union class_
    * range: [definition](Definition.md)*
    * inherited from: [definition](Definition.md)
 * _[subclass_of](subclass_of.md)_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: [definition](Definition.md)
    * inherited from: [definition](Definition.md)
