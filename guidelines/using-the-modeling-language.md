# Using the modeling language

The BiolinkML provides a variety of slots to define the semantics of your Biolink Model class and slots.

This document tries to address on how to use most of these slots in Biolink Model.

Please refer to [BiolinkML documentation](https://biolink.github.io/biolinkml/docs/) for an exhaustive list of slots provided by the modeling language.


## is_a

The `is_a` slot can be used to define a hierarchy for your Biolink Model class (or slot) where a new class (or slot) is defined as a subclass of another defined class (or slot).


```yaml
gene:
  is_a: gene or gene product
```

Here we define that the entity class `gene` is a sub-class of `gene or gene product`.


## aliases

The `aliases` slot can be used to define a list of aliases for a Biolink Model class (or slot). This is useful for adding synonymous names to your class (or slot).


```yaml
gene:
  is_a: gene or gene product
  aliases:
    - locus
```

Here we define that the entity class `gene` has an alias `locus`.


## domain

The `domain` slot mimics the idea of `rdfs:domain` where you constrain the type of classes that a given Biolink Model slot can be a part of.


```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
```

Here we define that the subject (source node) of the predicate slot `genetically interacts with` must be an instance of class `gene`.


## range

The `range` slot mimics the idea of `rdfs:range` where you can constrain the type of classes (or data types) a given Biolink Model slot can have as its value.

```yaml
  genetically interacts with:
    is_a: interacts with
    domain: gene
    range: gene
```

Here we define that both the subject (source node) and object (target node) of the predicate slot `genetically interacts with` must be instances of class `gene`.


## description

The `description` slot can be used to provide a human-readable description of a class (or slot).

```yaml
  genetically interacts with:
    is_a: interacts with
    description: >-
      holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    domain: gene
    range: gene
```

Here we define a human readable description that describes the predicate slot `genetically interacts with` and its purpose.


## in_subset

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


## symmetric

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


## defining_slots

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



## slot_usage

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


## abstract

The `abstract` slot can be used to define whether a Biolink Model class (or slot) is abstract.


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

Here we define that the association class `cell line to thing association` is an abstract class. Just like in Object Oriented Paradigm, another class can use this class as part of its inheritance hierarchy but there cannot be instances of the abstract class.


## mixin

The `mixin` slot can be used to define whether a Biolink Model class (or slot) is a mixin.

```yaml
  thing with taxon:
    mixin: true
    description: >-
      A mixin that can be used on any entity with a taxon
    slots:
      - in taxon
```

Here we define class `thing with taxon` as a mixin class with a slot `in taxon`. This class can be used as a mixin by other classes. 

Mixins provide the means to reusing property slots in different classes without the need to tie slots to the hierarchy of the class itself.

While mixins can be used by other classes, there cannot be instances of the mixin class.


## mixins

The `mixins` slot can be used to specify a list of mixins that a class (or slot) can use.

The mixins are separate from the `is_a` hierarchy and the mixin classes do not contribute to a classes' inheritance hierarchy.

```yaml
  individual organism:
    is_a: organismal entity
    mixins:
      - thing with taxon
```

Here we define an entity class `individual organism` that uses the mixin class `thing with taxon`. By virtue of the mixin, the class `individual organism` will have an `in taxon` slot in addition to all its own slots, its parent slots, and its ancestor slots.


## required

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


## slot_uri

The `slot_uri` slot can be used to define a canonical URI that is the true representation for that particular slot. That is, the value of `slot_uri` can be used interchangably with the slot being defined.

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


## id_prefixes

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


## exact_mappings

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

Here we define a list of 5 predicates that are semanticially equivalent to the Biolink Model predicate slot `same as`.


## close_mappings

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


## narrow_mappings

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


## broad_mappings

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


## related_mappings

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

