# Class: slot definition


A property or slot

URI: [http://bioentity.io/vocab/SlotDefinition](http://bioentity.io/vocab/SlotDefinition)

![img](images/SlotDefinition.png)
## Mappings

## Inheritance

 *  is_a: [Definition](Definition.md) - definition base class
## Children

## Used in

 *  class: **[ClassDefinition](ClassDefinition.md)** *[defining_slots](defining_slots.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[inverse](inverse.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[slot definition.is_a](slot_definition_is_a.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[slot definition.mixins](slot_definition_mixins.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[slot definition.union_of](slot_definition_union_of.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SchemaDefinition](SchemaDefinition.md)** *[schema definition.slots](slot_definitions.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[ClassDefinition](ClassDefinition.md)** *[slot_usage](slot_usage.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[ClassDefinition](ClassDefinition.md)** *[slots](slots.md)* **[SlotDefinition](SlotDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[subproperty_of](subproperty_of.md)* **[SlotDefinition](SlotDefinition.md)**
## Fields

 * [alias](alias.md)
    * Description: A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference
    * range: **string**
    * __Local__
 * [definitional](definitional.md)
    * range: **boolean**
    * __Local__
 * [domain](domain.md)
    * Description: The class to which this slot applies.
    * range: [ClassDefinition](ClassDefinition.md)
    * __Local__
 * [identifier](identifier.md)
    * Description: True means that this slot must be unique across the collection of slots
    * range: **boolean**
    * __Local__
 * [inherited](inherited.md)
    * Description: True means that the slot is an essential attribute of the container -- that the slot is carried across is_a and slot_usage paths
    * range: **boolean**
    * __Local__
 * [inlined](inlined.md)
    * Description: if true then the value of this slot is inlined (i.e. a nested object) rather linked by key
    * range: **boolean**
    * __Local__
 * [inverse](inverse.md)
    * Description: used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')
    * range: [SlotDefinition](SlotDefinition.md)
    * __Local__
 * [is_class_field](is_class_field.md)
    * range: **boolean**
    * __Local__
 * [multivalued](multivalued.md)
    * Description: If true slot can have many values
    * range: **boolean**
    * __Local__
 * [object_property](object_property.md)
    * Description: true means that this slot is part of the formal definition of a class
    * range: **boolean**
    * __Local__
 * [path](path.md)
    * Description: For any denormalized slot, this represents the tree or graph path used to generate the denormalized form
    * range: **string**
    * __Local__
 * [primary_key](primary_key.md)
    * Description: True means that this serves as a unique identifier
    * range: **boolean**
    * __Local__
 * [range](range.md)
    * Description: The slot type.  Can be any class or type
    * range: **anytype**
    * __Local__
 * [required](required.md)
    * Description: If true slot must have at least one value
    * range: **boolean**
    * __Local__
 * [role](role.md)
    * range: **string**
    * __Local__
 * [slot definition.is_a](slot_definition_is_a.md)
    * Description: specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
    * range: [SlotDefinition](SlotDefinition.md)
    * __Local__
 * [slot definition.mixins](slot_definition_mixins.md)
    * Description: List of definitions to be mixed in. Targets may be any definition of the same type
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * [slot definition.union_of](slot_definition_union_of.md)
    * Description: list of class or slot definitions that are combined to create the union class
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * [subproperty_of](subproperty_of.md)
    * Description: Ontolgy property which this is a subproperty of
    * range: [SlotDefinition](SlotDefinition.md)
    * __Local__
 * [abstract](abstract.md)
    * Description: An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [aliases](aliases.md)
    * range: **string***
    * inherited from: [Element](Element.md)
 * [alt_descriptions](alt_descriptions.md)
    * range: [AltDescription](AltDescription.md)*
    * inherited from: [Element](Element.md)
 * [comment](comment.md)
    * Description: Comment about an element
    * range: **string**
    * inherited from: [Element](Element.md)
 * [description](description.md)
    * Description: a description
    * range: **string**
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
 * [local_names](local_names.md)
    * Description: map from local identifier to slot
    * range: **string***
    * inherited from: [Definition](Definition.md)
 * [mappings](mappings.md)
    * Description: list of equivalent or skos exact mappings to an ontology class
    * range: **string***
    * inherited from: [Element](Element.md)
 * [mixin](mixin.md)
    * Description: Used only as a mixin -- cannot be instantiated on its own.
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [name](name.md)
    * Description: a unique key that identifies a slot, type or class in a schema
    * range: **string**
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
 * [subclass_of](subclass_of.md)
    * Description: Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes
    * range: **uri**
    * inherited from: [Definition](Definition.md)
 * [symmetric](symmetric.md)
    * Description: Symmetric slot
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * [values_from](values_from.md)
    * Description: identifies the possible uri's of the range
    * range: **string***
    * inherited from: [Definition](Definition.md)
