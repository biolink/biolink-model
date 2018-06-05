# Metamodel schema


Metamodel for biolink schema

### Classes

 * [element](Element.md) - root of all described things
    * [definition](Definition.md) - definition base class
       * [class definition](ClassDefinition.md) - A class or interface
       * [slot definition](SlotDefinition.md) - A property or slot
       * [schema definition](SchemaDefinition.md) - A collection of definitions
    * [type definition](TypeDefinition.md) - A type definition
 * [example](Example.md) - example of usage
### Mixins

### Slots

 * [abstract](abstract.md) - An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored
 * [alias](alias.md) - A name to be assigned to the slot in implementations that is different that its type.  The primary use for this is to allow class AND schema definitions to both have "slots" where one inline and the other a reference
 * [aliases](aliases.md)
 * [alt_descriptions](alt_descriptions.md)
 * [apply_to](apply_to.md) - Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.
 * [classes](classes.md) - classes defined in schema
 * [comment](comment.md) - Comment about an element
 * [defining_slots](defining_slots.md) - The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
 * [definitional](definitional.md) - slot is a defining slot -- injection into the defining_slots list
 * [description](description.md) - a description
 * [domain](domain.md) - The class to which this slot applies.
 * [entity](entity.md)
 * [examples](examples.md) - Example of usage for a slot or class
 * [flags](flags.md) - State information and other details
 * [from_schema](from_schema.md) - id of the schema that the element was derived from.  Supplied by the loader.
 * [generation_date](generation_date.md) - date that the schema was loaded/generated.  Supplied by the loader
 * [id](id.md) - a globally unique id or url for a schema
 * [id_prefixes](id_prefixes.md)
 * [identifier](identifier.md) - True means that this slot must be unique across the collection of slots
 * [imports](imports.md) - A list of modules that are imported into the schema
 * [in_subset](in_subset.md) - used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
 * [inlined](inlined.md) - if true then the value of this slot is inlined (i.e. a nested object) rather linked by key
 * [inverse](inverse.md) - used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')
 * [is_a](is_a.md) - specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
 * [is_class_field](is_class_field.md)
 * [license](license.md) - license for the schema
 * [local_names](local_names.md) - map from local identifier to slot
 * [mappings](mappings.md) - list of equivalent or skos exact mappings to an ontology class
 * [metamodel_version](metamodel_version.md) - Version of the metamodel used to load the schema. Supplied by the loader
 * [mixin](mixin.md) - Used only as a mixin -- cannot be instantiated on its own.
 * [mixins](mixins.md) - List of definitions to be mixed in. Targets may be any definition of the same type
 * [multivalued](multivalued.md) - If true slot can have many values
 * [name](name.md) - a unique key that identifies a slot, type or class in a schema
 * [note](note.md) - Notes about an element
 * [path](path.md) - For any denormalized slot, this represents the tree or graph path used to generate the denormalized form
 * [prefixes](prefixes.md) - list of ID/CURIE prefixes applicable to that element
 * [primary_key](primary_key.md) - True means that this serves as a unique identifier
 * [range](range.md) - The slot type.  If absent, it is the builtin type 'string'
 * [required](required.md) - If true slot must have at least one value
 * [role](role.md)
 * [see_also](see_also.md)
 * [singular_name](singular_name.md) - a name that is used in the singular form
 * [slots](slots.md) - collection of slot definitions in a schema
 * [slot_usage](slot_usage.md) - Additional info on how a slot is used in the context of a class. Many slots may be re-used across different classes, but the meaning of the slot may be refined by context. For example, a generic association model may use slots subject/predicate/object with generic semantics and minimal constraints. When this is subclasses, e.g. to disease-phenotype associations then slot_usage may specify both local naming (e.g. subject=disease) and local constraints
 * [slots](slots.md) - list of slot names that are applicable to a class. slots are by default inherited over is_a and mixins.
 * [source_file](source_file.md) - name, uri or description of the source of the schema.  Supplied by the loader
 * [source_file_date](source_file_date.md) - modification date of the source of the schema.  Supplied by the loader
 * [source_file_size](source_file_size.md) - size in bytes of the source of the schema.  Supplied by the loader
 * [subclass_of](subclass_of.md) - Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes
 * [subproperty_of](subproperty_of.md) - Ontolgy property which this is a subproperty of
 * [symmetric](symmetric.md) - Symmetric slot
 * [typeof](typeof.md) - a builtin ('string', 'integer', 'float', 'double', 'boolean', 'time') or another type definition
 * [types](types.md) - types defined in schema
 * [union_of](union_of.md) - list of class or slot definitions that are combined to create the union class
 * [value](value.md)
 * [description](description.md)
 * [values_from](values_from.md) - identifies the possible uri's of the range
 * [version](version.md) - Schema version
### Types

#### Built in

 * **boolean**
 * **date**
 * **double**
 * **float**
 * **integer**
 * **string**
 * **time**
#### Defined

