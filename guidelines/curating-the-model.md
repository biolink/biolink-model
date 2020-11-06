# Curating the Biolink Model

For anyone curating the Biolink Model it is always advised that they are familiar with the basics of [BiolinkML](https://github.com/biolink/biolinkml).

In Biolink Model all the curation should happen in one place: [biolink-model.yaml](../biolink-model.yaml)

This is the one source of truth for the model and thus any changes must be directed to the Biolink Model YAML.


### Adding an Entity class

An entity class represents entities like Genes, Diseases or Chemical Substances.

Instances of these Entity class are represented as nodes in a graph.

Biolink Model has several entitie classes like `gene`, `disease`, `phenotypic feature`, `chemical substance`.

All these classes are arranged in a hierarchy with the root of all entities being the `named thing` class.

You as a curator can add new entity classes to the model.

To add an entity class to Biolink Model you need to determine the following,
  - What is an appropriate name for this entity?
    - The name for an entity should be clear and concise. It should describe the instances of this class
  - Where in the [`named thing` hierarchy](https://biolink.github.io/biolink-model/docs/NamedThing) does the new class fit?
    - Determine what the immediate parent for this is
  - What are the slots that this class can have (in addition to its inherited slots)?
    - What are the properties that this entity ought to have
  - Do certain slots have to be constrained to certain values?
    - Are there properties (new) or inherited properties whose value have to be constrained to a certain value space?
  - What are the valid namespace prefixes for identifiers of instances of this class?
    - For representing an instance of this entity determine the identifier namespace and a valid prefixes
  - What are the mapping(s) for this class?
    - Mappings are a way of rooting this new entity in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine if the level of granularity for your mappings. Mappings be divided into 5 types depending on its granularity: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`


As an example, let's consider the definition of class `gene`,

```yaml

  gene:
    is_a: gene or gene product
    aliases: ['locus']
    slots:
      - id
      - name
      - symbol
      - description
      - synonym
      - xref
    exact_mappings:
      - SO:0000704
      - SIO:010035
      - WIKIDATA:Q7187
    id_prefixes:
      - NCBIGene
      - ENSEMBL
      - HGNC
      - UniProtKB
      - MGI
      - ZFIN
      - dictyBase
      - WB
      - WormBase
      - FlyBase
      - FB
      - RGD
      - SGD
      - PomBase

```

In the above YAML snippet, `is_a`, `aliases`, `slots`, `exact_mappings`, and `id_prefixes` are slots from BiolinkML where each slot has a specific meaning and they add semantics to the class definition.

In addition to the aforementioned slots, BiolinkML provides ways to leverage mixin classes to reuse certain slots across different classes.

Say you want to use the mixin class `thing with taxon` that defines an `in taxon` slot.

You can achieve that as follows:

```yaml

  gene:
    is_a: gene or gene product
    mixins:
      - thing with taxon
    aliases: ['locus']
    ...

```

In the above YAML snippet, we are explicitly defining the `gene` class to have `in taxon` as a slot in addition to all its slots, its parent slots, and all of its ancestor slots.

There are [other BiolinkML slots](https://biolink.github.io/biolinkml/docs/ClassDefinition#Attributes) that can be used to define your class and represent the semantics of your class.


### Adding an Association class

An association represents an assertion (statement) which connects a subject to an object via a predicate.

Instances of the Association class are represented as edges in a graph.

Biolink Model has several Association classes like `gene to gene association`, `gene to disease association`, `disease to phenotypic feature association`.

All these classes are arranged in a hierarchy with the root of all associations being the `association` class.

You as a curator can add new Association classes to the model.

To add an Association class to Biolink Model you need to determine the following,
  - What is an appropriate name for this association
    - The name for an association should be clear and concise. It should capture the type of assertion that it is trying to represent
  - What type of nodes does this association link?
    - Determine what the subject and the object classes are in this assertion
  - Where in the hierarchy does the new class fit?
    - Determine where in the [`association slot` hierarchy]() does this new assocation class fit
  - What are the slots that this association class can have (in addition to inherited slots)?
    - What are the properties that this association ought to have
  - Do certain slots have to be constrained on what values it ought to have?
    - Determine whethere there are properties (new) or inherited properties whose value have to be constrained to a certain value space
  - What are the mapping(s) for this class?
    - Mappings are a way of rooting this new association in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine if the level of granularity for your mappings. Mappings be divided into 5 types depending on its granularity: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`



As an example, let's consider the definition of class  `variant to disease association`:

```yaml

  variant to disease association:
    is_a: association
    defining_slots:
      - subject
      - object
    mixins:
      - variant to thing association
      - entity to disease association
    slot_usage:
      subject:
        description: >-
          a sequence variant in which the allele state is associated in some way with the disease state
        examples:
          - value: ClinVar:52241
            description: "NM_000059.3(BRCA2):c.7007G>C (p.Arg2336Pro)"
      relation:
        description: >-
          E.g. is pathogenic for
        subproperty_of: related condition
      object:
        description: >-
          a disease that is associated with that variant
        examples:
          - value: MONDO:0016419
            description: hereditary breast cancer

```

In the above YAML snippet, `is_a`, `defining_slots`, `mixins`, and `slot_usage` are slots from BiolinkML where each slot has a specific meaning and they add semantics to the class definition.

There are [other BiolinkML slots](https://biolink.github.io/biolinkml/docs/ClassDefinition#Attributes) that can be used to define your class and represent the semantics of your class.

For more information on what each slot means and how to use them in Biolink Model, refer to [Using the Modeling Language](using-the-modeling-language.md).


### Adding a predicate/relation

A predicate is a slot that links two instances of a class. 

To add a predicate to Biolink Model you need to,
  - What is an appropriate name for this predicate?
    - A human readable name for this predicate. It should capture the nature of the relationship
  - Where in the hierarchy does the new slot fit?
    - Determine where in the [`related to` hierarchy]() does this new predicate slot fit
  - What are the domain and range constraints (if any)?
    - Determine which type of classes can this predicate link
  - What are the mapping(s) for this slot?
    - Mappings are a way of rooting this new association in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine if the level of granularity for your mappings. Mappings be divided into 5 types depending on its granularity: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`


As an example, let's consider the definition of slot `interacts with`:

```yaml

  interacts with:
    domain: named thing
    range: named thing
    description: >-
      holds between any two entities that directly or indirectly interact with each other
    is_a: related to
    in_subset:
      - translator_minimal
    symmetric: true
    exact_mappings:
      - RO:0002434
    narrow_mappings:
      - RO:0002103
      - RO:0002120
      - RO:0002130
      - SEMMEDDB:complicates

```

In the above YAML snippet, `domain`, `range`, `description`, `is_a`, `in_subset`, `symmetric`, `exact_mappings` and `narrow_mappings` are slots from BiolinkML where each slot has a specific meaning and they add semantics to the slot definition.



### Adding properties

You can add slots that represent node properties or edge properties.

To add a slot to Biolink Model you need to,
  - What is an appropriate name for this slot
  - Is it an node property or an edge property (association slot)?
  - Where in the hierarchy does the new slot fit?
  - What are the domain and range constraints (if any)?
  - What are the mapping(s) for this slot?
    - Can the mappings be divided depending on its granularity: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`
  - aliases
  - required?
  - slot_uri


Example of node property,
```
```

Example of edge property,
```
```

### Managing mappings

- Granularity of mappings
- How to interpret mappings


Example,
```
```

