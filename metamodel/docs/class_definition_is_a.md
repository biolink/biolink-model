# Slot: is_a


specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded

URI: [http://w3id.org/biolink/vocab/class_definition_is_a](slot_uri)
## Mappings

## Domain and Range

[ClassDefinition](ClassDefinition.md) -> [ClassDefinition](ClassDefinition.md)
## Inheritance

 *  is_a: [is_a](is_a.md)
## Children

## Used in

 *  usage: [ClassDefinition](ClassDefinition.md)
