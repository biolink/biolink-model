# Class: slot definition


A property or slot

URI: [http://bioentity.io/vocab/SlotDefinition]
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md)
## Children

## Used in

## Fields

 * _[multivalued](multivalued.md)_
    * _If true slot can have many values_
    * __range__: boolean
 * _[domain](domain.md)_
    * _The class to which this slot applies._
    * __range__: [class definition](ClassDefinition.md)
 * _[range](range.md)_
    * _The slot type.  If absent, it is the builtin type 'string'_
    * __range__: [element](Element.md)
 * _[required](required.md)_
    * _If true slot must have at least one value_
    * __range__: boolean
 * _[inlined](inlined.md)_
    * _if true then the value of this slot is inlined (i.e. a nested object) rather linked by key_
    * __range__: boolean
 * _[primary_key](primary_key.md)_
    * _True means that this serves as a unique identifier_
    * __range__: boolean
 * _[identifier](identifier.md)_
    * _True means that this slot must be unique across the collection of slots_
    * __range__: boolean
 * _[definitional](definitional.md)_
    * _slot is a defining slot -- injection into the defining_slots list_
    * __range__: boolean
 * _[alias](alias.md)_
    * _A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference_
    * __range__: 
 * _[path](path.md)_
    * _For any denormalized slot, this represents the tree or graph path used to generate the denormalized form_
    * __range__: 
 * _[subproperty_of](subproperty_of.md)_
    * _Ontolgy property which this is a subproperty of_
    * __range__: [slot definition](SlotDefinition.md)
 * _[inverse](inverse.md)_
    * _used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')_
    * __range__: [slot definition](SlotDefinition.md)
 * _[is_class_field](is_class_field.md)_
    * __range__: boolean
