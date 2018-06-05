# Class: class definition


A class or interface

URI: http://bioentity.io/vocab/ClassDefinition

![img](http://yuml.me/diagram/nofunky/class/\[Definition]^-\[ClassDefinition|entity:boolean%20%3F],%20\[ClassDefinition]-%20defining_slots%20*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%20*>\[SlotDefinition],%20\[ClassDefinition]++-%20slot_usage%20*>\[SlotDefinition],%20\[ClassDefinition]-%20apply_to%20%3F>\[ClassDefinition],%20)
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md)
## Children

## Used in

## Fields

 * _[defining_slots](defining_slots.md)_
    * _The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom_
    * range: [slot definition](SlotDefinition.md)*
 * _[slots](slots.md)_
    * _list of slot names that are applicable to a class. slots are by default inherited over is_a and mixins._
    * range: [slot definition](SlotDefinition.md)*
 * _[slot_usage](slot_usage.md)_
    * _Additional info on how a slot is used in the context of a class. Many slots may be re-used across different classes, but the meaning of the slot may be refined by context. For example, a generic association model may use slots subject/predicate/object with generic semantics and minimal constraints. When this is subclasses, e.g. to disease-phenotype associations then slot_usage may specify both local naming (e.g. subject=disease) and local constraints_
    * range: [slot definition](SlotDefinition.md)*
 * _[apply_to](apply_to.md)_
    * _Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class._
    * range: [class definition](ClassDefinition.md)
 * _[entity](entity.md)_
    * range: boolean
