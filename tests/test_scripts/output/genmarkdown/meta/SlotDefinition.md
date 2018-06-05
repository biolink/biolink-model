# Class: slot definition


A property or slot

URI: http://bioentity.io/vocab/SlotDefinition

![img](http://yuml.me/diagram/nofunky/class/\[Definition]^-\[SlotDefinition|multivalued:boolean%20%3F;required:boolean%20%3F;inlined:boolean%20%3F;primary_key:boolean%20%3F;identifier:boolean%20%3F;definitional:boolean%20%3F;alias:string%20%3F;path:string%20%3F;is_class_field:boolean%20%3F;role:string%20%3F],%20\[SlotDefinition]-%20domain%20%3F>\[ClassDefinition],%20\[SlotDefinition]-%20range%20%3F>\[Element],%20\[SlotDefinition]-%20subproperty_of%20%3F>\[SlotDefinition],%20\[SlotDefinition]-%20inverse%20%3F>\[SlotDefinition],%20)
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md)
## Children

## Used in

## Fields

 * _[multivalued](multivalued.md)_
    * _If true slot can have many values_
    * range: boolean
 * _[domain](domain.md)_
    * _The class to which this slot applies._
    * range: [class definition](ClassDefinition.md)
 * _[range](range.md)_
    * _The slot type.  If absent, it is the builtin type 'string'_
    * range: [element](Element.md)
 * _[required](required.md)_
    * _If true slot must have at least one value_
    * range: boolean
 * _[inlined](inlined.md)_
    * _if true then the value of this slot is inlined (i.e. a nested object) rather linked by key_
    * range: boolean
 * _[primary_key](primary_key.md)_
    * _True means that this serves as a unique identifier_
    * range: boolean
 * _[identifier](identifier.md)_
    * _True means that this slot must be unique across the collection of slots_
    * range: boolean
 * _[definitional](definitional.md)_
    * _slot is a defining slot -- injection into the defining_slots list_
    * range: boolean
 * _[alias](alias.md)_
    * _A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference_
    * range: string
 * _[path](path.md)_
    * _For any denormalized slot, this represents the tree or graph path used to generate the denormalized form_
    * range: string
 * _[subproperty_of](subproperty_of.md)_
    * _Ontolgy property which this is a subproperty of_
    * range: [slot definition](SlotDefinition.md)
 * _[inverse](inverse.md)_
    * _used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')_
    * range: [slot definition](SlotDefinition.md)
 * _[is_class_field](is_class_field.md)_
    * range: boolean
 * _[role](role.md)_
    * range: string
