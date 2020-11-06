# Understanding the Biolink Model

Biolink Model is a high-level data model built to provide a schema for representing biological and biomedical knowledge. The model itself is agnostic to the graph formalism used to represent knowledge. i.e. You can use Biolink Model as a schema for labelled property graphs (Neo4j) or for edge labelled graphs (RDF). 

Biolink Model was built with the following purposes in mind:
- A model to bridge between labelled property graphs and edge labelled graphs
- A model that is represented using a formal representation where the semantics are well defined within the model
- A model that focuses on the actual schema and its semantics instead of being weighed down by limitations of a technology
- A model that is extensible, self-documenting, and unambiguous
- A model that maps to external ontologies, thesauri, controlled vocabularies, and taxonomies

To that end, Biolink Model makes use of [BiolinkML](https://github.com/biolink/biolinkml) (Biolink Modeling Language) for defining the various semantics of the model.

## Understanding the Biolink modeling language

BiolinkML is a general purpose modeling language that follows object-oriented and ontological principles. The modeling language inherits features from the Web Ontology Language (OWL) and thus is capable of representing semantics in addition to the standard object-oriented hierarchy of a data model.

Models are authored in YAML and using BiolinkML one can generate a variety of artifacts including JSON-Schema, OWL, RDF, Python data classes, Shape Expressions, and Markdown.

The modeling language provides the following idioms,
- Class definition
  - Used to define classes
- Slot definition 
  - Used to define class properties
- Type definition
  - Used to define data types
- Schema definition
  - Used to define properties of the model itself

Refer to [BiolinkML on GitHub](https://github.com/biolink/biolinkml) for a more detailed guide on BiolinkML.

> **Note:** Biolink Model is authored using BiolinkML. While Biolink Model and BiolinkML share a "biolink" in its name, that is where the similarities end. One can use BiolinkML to author any schema in any domain.


## Structure of the model

The Biolink Model is a high-level data model where entities, associations, and predicates are arranged in a hierarchy. In addition, the model also defines node properties, edge properties, and types.

The model is organized using BiolinkML Class definition (class), Slot definition (slot), Type definition (type) and Schema definition.

> **Conventions**
> 
> In [Biolink Model YAML](../biolink-model.yaml) any class, slot, or type is defined in `sentence case` form. When this model is compiled to various forms (like JSON-Schema, OWL, Markdown) the representation is based on the following convention,
>   - classes are named in `CamelCase` form
>   - slots are named in `snake_case` form
>   - types are named in `snake_case` form
>
> To avoid ambiguity in semantics, prefixes are MUST for classes and certain slots.
>
> To avoid ambuguity it semantics, prefixes are RECOMMENDED for all slots.


The Biolink Model makes use of classes, slots, and types to define various hierarchies in the model that facilitate knowledge representation.

At a glance the structure is as follows,
- [Classes](#Classes)
    - [Entities](#Entities)
    - [Associations](#Associations)
    - [Mixins](#Mixins)
- [Slots](#Slots)
    - [Predicates](#Predicates)
    - [Node Properties](#Node%20Properties)
    - [Edge Properties](#Edge%20Properties)
- [Types](#Types)


### Classes

A class represents an entity or an association. A class can have one more more slots (properties).

In RDF sense, a class is basically `rdfs:Class`.

Within the Biolink Model there are two hierarchies of classes:
  - Entities
  - Associations

where Entities are disjoint from Associations.


#### Entities

Entities are classes that represent entities such as genes, diseases, and chemical substances.

In a graph formalism, entities represent nodes in a graph.

Each class has one or more slots (properties).

The root of all entities is the `named thing` class.

> **Note:** While we say `named thing` when defining the model using BiolinkML, the actual CURIE for this class is `biolink:NamedThing`


#### Associations

Associations are classes that represent an assertion or statement. 

In RDF sense, an association is an `rdf:Statement`.

In a graph formalism, associations represent edges in a graph.

Each class has one or more slots (or properties).

The root of all associations is the `association` class.

> **Note:** While we say `association` when defining the model using BiolinkML, the acutal CURIE for this class is `biolink:Association`

Note: talk about reified associations!

#### Mixins

Mixins are classes that contain slots (properties) for use by other classes.

Mixins are abstract classes and they cannot be instantiated by themselves. That is, there cannot be an instance of a mixin.

Mixins are defined as a way of encouraging reuse of specific slots (properties) while ensuring a clear inheritance chain.

For example, the `entity to feature or disease qualifiers` class is a mixin that defines slots `severity qualifier` and `onset qualifier`. The mixin also inherits the slot `frequency qualifier` from its parent mixin class `frequency qualifier mixin`. 

The mixin class `entity to feature or disease qualifiers` is used in the `entity to phenotypic feature association` class and thus by design the class will have `severity qualifier`, `onset qualifier`, and `frequency qualifier` in addition to all other slots it inherits from its own parent `association` class.

> **Note:** Even though `entity to phenotypic feature association` uses the mixin class `entity to feature or disease qualifiers` that does not mean that `entity to phenotypic feature association` is a child of `entity to feature or disease qualifiers`. i.e. Mixins do not contribute to the inheritance hierarchy of the class that uses them.



### Slots

In Biolink Model, slots represent properties that a class can have.

A slot is similar to `rdf:Property` where it can link,
  - an instance of a class to another instance of a class
  - an instance of a class to a literal/data type


In Biolink Model slots are used to represent,
  - [Predicates](#Predicates)
  - [Node Properties](#Node%20Properties)
  - [Edge Properties](#Edge%20Properties)


#### Predicates

Predicates are slots that connect instances of classes. 

In a graph formalism, predicates are relationships that link instances of classes.

In OWL sense, predicates are similar to `owl:ObjectProperty`.

For example, a predicate `biolink:treats` can be used to link an instance of class `biolink:ChemicalSubstance` with an instance of class `biolink:Disease`.


#### Node Properties

Node properties are slots that a class (à la nodes) can have.

The root of all node properties is `node property`.

In OWL sense, node properties are similar to `owl:DataTypeProperty`.

For example, `biolink:id` and `biolink:name` are children of `biolink:node_property` and they are slots assigned to the `biolink:NamedThing` class. So all instances of this class can have `biolink:id` and `biolink:name` as its properties that further describes the instance.


> **Note:** In many cases you may see node properties without the `biolink` prefix. This is normal since we can assume that if there is a biolink typed node in a graph, with `id` and `name` as its properties, then they correspond to `biolink:id` and `biolink:name`. But to be sure of the semantics it is advised to use the full CURIE to represent property names.


#### Edge Properties

Edge properties are slots that a class (à la edges) can have.

The root of all edge properties is `association slot`.

In OWL sense, edge properties are similar to `owl:DataTypeProperty`.

For example, `biolink:subject`, `biolink:predicate`, and `biolink:object` are children of `biolink:association_slot` and they are slots assigned to `biolink:Association` class. So all instances of this class can have `biolink:subject`, `biolink:predicate`, and `biolink:object` as its properties that further describes the instance.

> **Note:** In many cases you may see edge properties without the `biolink` prefix. This is normal since we can assume that if there is a biolink typed edge in a graph with `subject`, `predicate`, and `object` as its properties then they correspond to `biolink:subject`, `biolink:predicate`, and `biolink:object`, respectively. But to be sure of the semantics it is advised to use the full CURIE to represent property names.


### Types

BiolinkML provides a handful of inbuilt data types. But in the case where you would like to define custom data types then this can be achieved by defining types.

Data types do not have any inheritance and thus are not arranged in any hierarchy.

For example, `iri type` is a type defined in the Biolink Model where the type of value is constrained to `uriorcurie`.

> `uriorcurie` is an inbuilt data type provided by BiolinkML where the value space is constrained to either a URI or a CURIE representation.
