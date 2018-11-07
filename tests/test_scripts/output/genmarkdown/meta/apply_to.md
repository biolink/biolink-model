# Slot: apply_to


Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.

URI: [http://w3id.org/biolink/vocab/apply_to](slot_uri)
## Mappings

## Domain and Range

[ClassDefinition](ClassDefinition.md) -> [ClassDefinition](ClassDefinition.md)
## Inheritance

## Children

## Used in

 *  usage: [ClassDefinition](ClassDefinition.md)
