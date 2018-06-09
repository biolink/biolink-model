# Class: class definition


A class or interface

URI: [http://bioentity.io/vocab/ClassDefinition](http://bioentity.io/vocab/ClassDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Definition]^-\[ClassDefinition|name(i):string;singular_name(i):string%20%3F;description(i):string%20%3F;note(i):string%20%3F;comment(i):string%20%3F;see_also(i):string%20%3F;flags(i):string%20*;prefixes(i):string%20*;aliases(i):string%20*;mappings(i):string%20*;id_prefixes(i):string%20*;in_subset(i):string%20*;from_schema(i):string%20%3F;alt_descriptions(i):string%20*;mixin(i):boolean%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;values_from(i):string%20*;symmetric(i):boolean%20%3F;entity:boolean%20%3F],%20\[ClassDefinition]++-%20examples(i)%20*>\[Example],%20\[ClassDefinition]-%20is_a(i)%20%3F>\[Definition],%20\[ClassDefinition]-%20mixins(i)%20*>\[Definition],%20\[ClassDefinition]-%20union_of(i)%20*>\[Definition],%20\[ClassDefinition]-%20subclass_of(i)%20%3F>\[Definition],%20\[ClassDefinition]-%20defining_slots%20*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%20*>\[SlotDefinition],%20\[ClassDefinition]++-%20slot_usage%20*>\[SlotDefinition],%20\[ClassDefinition]-%20apply_to%20%3F>\[ClassDefinition])
## Mappings

## Inheritance

 *  is_a: [definition](Definition.md) - definition base class
## Children

## Used in

 *  class: [class definition](ClassDefinition.md) references: [class definition](ClassDefinition.md)
 *  class: [schema definition](SchemaDefinition.md) references: [class definition](ClassDefinition.md)
 *  class: [slot definition](SlotDefinition.md) references: [class definition](ClassDefinition.md)
## Fields

 * _[apply_to](apply_to.md)_
    * _Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class._
    * range: [class definition](ClassDefinition.md)
    * __Local__
 * _[defining_slots](defining_slots.md)_
    * _The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom_
    * range: [slot definition](SlotDefinition.md)*
    * __Local__
 * _[entity](entity.md)_
    * range: boolean
    * __Local__
 * _[slot_usage](slot_usage.md)_
    * _Additional info on how a slot is used in the context of a class. Many slots may be re-used across different classes, but the meaning of the slot may be refined by context. For example, a generic association model may use slots subject/predicate/object with generic semantics and minimal constraints. When this is subclasses, e.g. to disease-phenotype associations then slot_usage may specify both local naming (e.g. subject=disease) and local constraints_
    * range: [slot definition](SlotDefinition.md)*
    * __Local__
 * _[slots](slots.md)_
    * _list of slot names that are applicable to a class. slots are by default inherited over is_a and mixins._
    * range: [slot definition](SlotDefinition.md)*
    * __Local__
