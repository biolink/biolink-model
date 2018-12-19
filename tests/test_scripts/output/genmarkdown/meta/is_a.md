# Slot: is_a


specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded

URI: [http://w3id.org/biolink/vocab/is_a](slot_uri)
## Mappings

 * [rdfs:subClassOf](http://purl.obolibrary.org/obo/rdfs_subClassOf)
## Domain and Range

[Definition](Definition.md) -> [Definition](Definition.md)
## Inheritance

## Children

 *  child: [class definition.is_a](class_definition_is_a.md)
 *  child: [slot definition.is_a](slot_definition_is_a.md)
## Used in

 *  usage: [ClassDefinition](ClassDefinition.md)
 *  usage: [Definition](Definition.md)
 *  usage: [SlotDefinition](SlotDefinition.md)
