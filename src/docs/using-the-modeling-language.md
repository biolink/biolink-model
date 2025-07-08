---
title: "Using the Modeling Language"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 3
---

# Using the LinkML Modeling Language

Biolink Model is built with the [Linked data Modeling Language (LinkML)](https://linkml.github.io/).

LinkML provides a variety of slots to define the semantics of your Biolink Model class and slots. This document covers how to use most of these slots in Biolink Model.

Please refer to [linkML documentation](https://linkml.github.io/linkml-model/docs/) for an exhaustive list of slots provided by the modeling language.

## Inheritance Related Slots

### is_a

The `is_a` slot can be used to define a hierarchy for your Biolink Model class, mixin or slot where a new class, mixin or slot is defined as a subclass of another defined class, mixin or slot.


```yaml
gene:
  is_a: gene or gene product
```

Here, we define the entity class `gene` as a sub-class of `gene or gene product`. Note that `is_a` has the characteristics of homeomorphicity: `is_a` **SHOULD** only connect either (1) two mixins (2) two classes (3) two slots.

### abstract

A model class (or slot) may be tagged with its `abstract` slot set to the boolean value `true`, to define whether it is abstract. This has comparable meaning to the object-oriented paradigm in software engineering: 
another class (or slot) can use the abstract class (or slot) as part of its inheritance hierarchy, but the abstract class itself _cannot_ be directly instantiated.


```yaml
  cell line to thing association:
    is_a: association
    defining_slots:
      - subject
    abstract: true
    description: >-
      A relationship between a cell line and another entity
    slot_usage:
      subject:
        range: cell line
```

Here we define that the association class `cell line to thing association` is an abstract class. In this case, the class simply constrains its child subclasses to have a subject range of `biolink:CellLine`.


### mixin

The `mixin:true` setting is used to extend the properties (or slots) of a class, without changing its
position in the class hierarchy.  Mixins can be extremely helpful in a number of ways: 1) to generalize a set
of attributes that can apply to classes in different parts of the class hierarchy, 2) reduce duplication of
shared attributes between classes that do not inherit from one another, and 3) prevent the sometimes confusing nature
of multiple inheritance noted in the '[diamond problem]'(https://tinyurl.com/4zdw9tsb).

In general, while mixin slots and classes should not be directly instantiated, or used directly as a slot in a class,
KGs can use them as a substitute for multiple inheritance. For example, a KG might wish to determine what are the parents
of a certain class.  In this case, the KG should navigate a mixin used in a domain or range of a class or slot, as it 
would for "is_a".  


```yaml
  thing with taxon:
    mixin: true
    description: >-
      A mixin that can be used on any entity with a taxon
    slots:
      - in taxon
```
Here we define the class `thing with taxon` as a mixin class with a slot `in taxon`.   

```yaml
  molecular entity:
    is_a: biological entity
    mixins:
      - thing with taxon
      - physical essence
      - ontology class
    aliases: ['bioentity']
```

In the class `molecular entity`, we use the `thing with taxon` mixin in order to add the 'in taxon' attribute (slot)
to the molecular entity class.  The other way to do this would be to duplicate the 'in taxon' attribute in every class
manually (duplicative), or have hierarchy/parent that had the `in taxon` slot (but this parent would be a sister-class to 
'named thing' as not all named-things are taxon based).  Mixins simplify modeling and should be used where appropriate.

Mixins can also be hierarchical.  For example:
```yaml
  frequency qualifier mixin:
    mixin: true
    description: >-
      Qualifier for frequency type associations
    slots:
      - frequency qualifier

```

Here we define the mixin `frequency qualifier mixin` to hold the parent slot, `frequency qualifier.`  
The slot, `frequency qualifier` is then inherited by every class in the subsequent `is_a` hierarchy of 
`entity to feature or disease qualifiers mixin.`  The `frequency quantifier` mixin was created with similar 
intentions (favoring consistency in modeling similar domains), though its reuse is not as evident in the model yet. 

Mixins enable the reuse of semantics, generally by the inclusion of specific property slots or 
other semantic constraint, in different classes or slots, without the need to tie slots to the 
hierarchy of the class itself.

```yaml
  treats:
    is_a: treats or applied or studied to treat
    mixin: true
    aliases: ['is substance that treats', 'indicated for', 'ameliorates or prevents condition']
    description: >-
      Holds between an intervention (substance, procedure, or activity) and a medical condition
      (disease or phenotypic feature), and states that the intervention is able to ameliorate,
      stabilize, or cure the condition or delay, prevent, or reduce the risk of it manifesting
      in the first place.
      ‘Treats’ edges should be asserted (knowledge_level: assertion) only in cases where there
      is strong supporting evidence - i.e. the intervention is approved for the condition, passed
      phase 3 or in phase 4 trials for the condition, or is an otherwise established 
      treatment in the medical community (e.g. a widely-accepted or formally recommended 
      off-label use). In the absence of such evidence, weaker predicates should be used in 
      asserted edges (e.g. ‘in clinical trials for’ or ‘beneficial in models of’). ‘Treats’ edges
      based on weaker or indirect forms of evidence can however be created as predictions 
      (knowledge_level: prediction) and should point to the more foundational asserted edges that 
      support them.
    domain: chemical or drug or treatment
    range: disease or phenotypic feature
    annotations:
      canonical_predicate: true
    in_subset:
      - translator_minimal
    related_mappings:
      - MONDO:disease_responds_to
    exact_mappings:
      - DRUGBANK:treats
      - WIKIDATA_PROPERTY:P2175
    narrow_mappings:
       # "is substance that treats" constrains statements to
       # a subset of the universe of all possible treatments
      - RO:0002606
      - NCIT:regimen_has_accepted_use_for_disease
       # RTX mapped REPODB terms
      - REPODB:clinically_tested_approved_unknown_phase
      - REPODB:clinically_tested_suspended_phase_0
      - REPODB:clinically_tested_suspended_phase_1
      - REPODB:clinically_tested_suspended_phase_1_or_phase_2
      - REPODB:clinically_tested_suspended_phase_2
      - REPODB:clinically_tested_suspended_phase_2_or_phase_3
      - REPODB:clinically_tested_suspended_phase_3
      - REPODB:clinically_tested_terminated_phase_0
      - REPODB:clinically_tested_terminated_phase_1
      - REPODB:clinically_tested_terminated_phase_1_or_phase_2
      - REPODB:clinically_tested_terminated_phase_2
      - REPODB:clinically_tested_terminated_phase_2_or_phase_3
      - REPODB:clinically_tested_terminated_phase_3
      - REPODB:clinically_tested_withdrawn_phase_0
      - REPODB:clinically_tested_withdrawn_phase_1
      - REPODB:clinically_tested_withdrawn_phase_1_or_phase_2
      - REPODB:clinically_tested_withdrawn_phase_2
      - REPODB:clinically_tested_withdrawn_phase_2_or_phase_3
      - REPODB:clinically_tested_withdrawn_phase_3
      - SNOMED:plays_role
    broad_mappings:
      - DRUGBANK:treats
      - SEMMEDDB:TREATS
      - WIKIDATA_PROPERTY:P2175
      - MONDO:disease_responds_to
```

`treats` is another example of a mixin.  In this case, a mixin is used to store metadata about a 
predicate or relationship between two entities at a general level.  Its subsequent children inherit these definitions
and attributes, whether the parent mixin class has any slots.


###  mixins

The `mixins` slot can be used to specify a list of mixins that a class (or slot) can use to 
include the added semantics of the mixins.

The `mixins` are separate from the `is_a` hierarchy and the mixin classes do not contribute to a 
classes inheritance hierarchy.

```yaml
  individual organism:
    is_a: organismal entity
    mixins:
      - thing with taxon
```

Here we define an entity class `individual organism` that uses the mixin class `thing with taxon`. 
By virtue of the mixin, the class `individual organism` will have an `in taxon` slot in addition to 
all its own slots, its parent slots, and its ancestor slots.


## Identification, Descriptive and Indexing Related Slots


### aliases

The `aliases` slot can be used to define a list of aliases for a Biolink Model class (or slot). This is useful for adding synonymous names to your class (or slot).


```yaml
gene:
  is_a: gene or gene product
  aliases:
    - locus
```

Here we define that the entity class `gene` has an alias `locus`.


### description

The `description` slot can be used to provide a human-readable description of a class (or slot).

```yaml
  genetically interacts with:
    is_a: interacts with
    description: >-
      holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    domain: gene
    range: gene
```

Here we define a human-readable description that describes the predicate slot `genetically interacts with` and its purpose.


### slot_uri

The `slot_uri` slot can be used to define a canonical URI that is the true representation for that particular slot. That is, the value of `slot_uri` can be used interchangeably with the slot being defined.

```yaml
  name:
    is_a: node property
    aliases: ['label', 'display name']
    domain: named thing
    range: label type
    slot_uri: rdfs:label
```

Here we define `rdfs:label` as the canonical URI for the property slot `name`. When serializing a graph into RDF, the name of an instance of entity class `named thing` will be represented using `rdfs:label` instead of `biolink:name`.

This is to ensure that we use certain core RDF predicates as is.


### in_subset

The `in_subset` slot can be used tag your class (or slot) to belong to a pre-defined subset.

The actual subset names are defined as part of the Schema definition.

```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
    range: gene
    in_subset:
      - translator_minimal
```

Here we define the predicate slot `genetically interacts with` as part of the `translator_minimal` subset.


### id_prefixes

The `id_prefixes` slot can be used to define a list of valid ID prefixes that instances of this class ought to have as part of their CURIE.

The order of the list matters since its a prioritized list with the ID prefix with the highest priority appearing at the top of the list.

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
    mappings:
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

Here we define the entity class `gene` to have a list of ID prefixes with `NCBIGene` having the highest priority.


## Slots Relating to Class Composition

### slots

The `slot` property list enumerates the names of slots which a given class, mixin or its subclasses are generally permitted to have. Unless it is designated as one of the `defining_slots` (see below) or `slot_usage` (see below) specifies that a given slot is `required: true` (see below), then it is _not_ mandatory that such a slot is instantiated in all instances of the given class, mixin or subclass inheriting it.


### defining_slots

The `defining_slots` slot can be used to specify which slots of an instance are necessary for defining an instance as a member of a class.


```yaml
  gene to gene association:
    is_a: association
    defining_slots:
      - subject
      - object
```

Here we specify that an association can be determined to be an instance of class `gene to gene association` based on the semantics of two of its slots: `subject` and `object`. 

i.e. One can infer an association to be an instance of `gene to gene association` if both its `subject` and its `object` are an instances of class `gene`.

Listing a slot as one of the `defining_slots` slots effectively makes it `required: true` (see below).


### slot_usage

The `slot_usage` slot can be used to specify how a particular slot ought to be used in a class.

This is useful for documenting what a particular slot means for instances of a particular class.


```yaml
  gene to gene association:
    aliases: ['molecular or genetic interaction']
    is_a: association
    defining_slots:
      - subject
      - object
    description: >-
      abstract parent class for different kinds of gene-gene or gene product to gene product relationships.
      Includes homology and interaction.
    slot_usage:
      subject:
        range: gene or gene product
        description: >-
          the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary.
          We allow a gene product to stand as proxy for the gene or vice versa
      object:
        range: gene or gene product
        description: >-
          the object gene in the association. If the relation is symmetric, subject vs object is arbitrary.
          We allow a gene product to stand as proxy for the gene or vice versa
```

Here we document the association class `gene to gene association` with information on how the slot `subject` and `object` ought to be used to represent this association properly.

In the `slot_usage` section we define the range and provide a description for the slot `subject` and `object`.


### required

The `required` slot can be used to define whether a slot is required.

When a slot is declared as required, any class that uses that slot must have a value for that slot.

```yaml
  id:
    is_a: node property
    required: true
    domain: named thing
    mappings:
      - alliancegenome:primaryId
      - gff3:ID
      - gpi:DB_Object_ID
```

Here we define the property slot `id` as a required field for all instances of the entity class `named thing`.


## Slots Relating to Constraints on Slot Composition


### domain

The `domain` slot mimics the idea of `rdfs:domain` where you constrain the type of classes that a given Biolink Model slot can be a part of.


```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
```

Here we define that the subject (source node) of the predicate slot `genetically interacts with` must be an instance of class `gene`.


### range

The `range` slot mimics the idea of `rdfs:range` where you can constrain the type of classes (or data types) a given Biolink Model slot can have as its value.

```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
    range: gene
```

Here we define that both the subject (source node) and object (target node) of the predicate slot `genetically interacts with` must be instances of class `gene`.


### symmetric

The `symmetric` slot can be used to specify whether a Biolink Model predicate slot is symmetric in its semantics.

i.e. if `A -[r]-> B` and `r` is symmetric then one can infer `B -[r]-> A`


```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
    range: gene
    in_subset:
      - translator_minimal
    symmetric: true
```

Here we define that the predicate slot `genetically interacts with` is symmetric.

**Note:** This property is not inherited by descendants of this predicate slot. You will have to explicitly define every predicate slot that should be considered as symmetric.


## Slots Relating Semantic Mappings and Anchoring to External Ontology

### symmetric

The `symmetric` slot can be used to specify whether a given predicate slot is symmetric.

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
``` 

**Note:** The symmetric nature of the predicate is not inherited by descendants of the predicate.


### inverse

The `inverse` slot can be used to specify the inverse predicate of a given predicate slot relationship.

```yaml
  affects:
    is_a: related to
    description: >-
      describes an entity that has a direct affect on the state or quality
      of another existing entity. Use of the 'affects' predicate implies that
      the affected entity already exists, unlike predicates such as
      'affects risk for' and 'prevents, where the outcome is something
      that may or may not come to be.
    inverse: affected by
    in_subset:
      - translator_minimal
```


### exact_mappings

The `exact_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be exact mappings to the class (or slot) being defined.


```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
      - CHEMBL.MECHANISM:equivalent_to
      - MONDO:equivalentTo
```

Here we define a list of 5 predicates that are semantically equivalent to the Biolink Model predicate slot `same as`.


### close_mappings

The `close_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be close mappings to the class (or slot) being defined.

```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
      - CHEMBL.MECHANISM:equivalent_to
      - MONDO:equivalentTo
    close_mappings:
      - owl:equivalentClass
```

Here we define `owl:equivalentClass` as being a close match to the Biolink Model predicate slot `same as`.


### narrow_mappings

The `narrow_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be narrow mappings to the class (or slot) being defined.

```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    close_mappings:
      - owl:equivalentClass
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
      - CHEMBL.MECHANISM:equivalent_to
      - MONDO:equivalentTo
    narrow_mappings:
      - DRUGBANK:external-identifier
```

Here we define `DRUGBANK:external-identifier` as being a narrow match to the predicate slot `same as`.

By narrow we mean that the scope of `DRUGBANK:external-identifier` is more narrower and restrictive than `same as`.

If we were to create a new predicate slot as a proxy for `DRUGBANK:external-identifier` then that new slot would be a child of `same as`.


### broad_mappings

The `broad_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be broad mappings to the class (or slot) being defined.

```yaml
  in complex with:
    description: >-
      holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    is_a: coexists with
    domain: gene or gene product
    range: gene or gene product
    in_subset:
      - translator_minimal
    broad_mappings:
      - SIO:010285
```

Here we define `SIO:010285` (molecular complex formation) as a broad mapping to the predicate slot `in complex with`. 

By broad we mean that the scope of `SIO:010285` is more broad and relaxed than `in complex with`.

If we were to create a new predicate slot as a proxy for `SIO:010285` then that new slot would be a parent of `in complex with`.


### related_mappings

The `related_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be related mappings to the class (or slot) being defined.

```yaml
  in complex with:
    description: >-
      holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    is_a: coexists with
    domain: gene or gene product
    range: gene or gene product
    in_subset:
      - translator_minimal
    broad_mappings:
      - SIO:010285
    related_mappings:
      - SIO:010497
```

Here we define `SIO:010497` (protein complex) as a related mapping to the predicate slot `in complex with`.

By related we mean that the scope of `SIO:010497` is related to the predicate slot `in complex with` and it's difficult to infer any further granularity.


### subproperty_of

The `subproperty_of` slot can be used (typically, under `slot_usage`) to anchor the values of a Biolink `predicate` slot of an association to a particular predicate (and its subclasses) _other than_ the top-most predicate, `biolink:related_to`.

```yaml
  gene to gene homology association:
    is_a: gene to gene association
    slot_usage:
      predicate:
        subproperty_of: homologous to
```

Here, the `predicate` of the  `biolink:GeneToGeneHomologyAssociation` is constrained to a value the subtree of predicates of `biolink:homologous_to` or its subclasses.

### subclass_of

The `subclass_of` slot can be used to anchor the semantics of a Biolink class to a particular term in an external 3rd party ontology.

```yaml
  named thing:
    description: "a databased entity or concept/class"
    slots:
      - id
      - name
      - category
    subclass_of: BFO:0000001
```

Here, `biolink:NamedThing` is anchored to ontology term `BFO:0000001` - **Entity** of the _Basic Formal Ontology_ which implies all `is_a` specified subclasses of `biolink:NamedThing` are also a subclasses of `BFO:0000001`.
