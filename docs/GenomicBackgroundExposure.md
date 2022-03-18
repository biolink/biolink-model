# Class: GenomicBackgroundExposure
_A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome._





URI: [biolink:GenomicBackgroundExposure](https://w3id.org/biolink/vocab/GenomicBackgroundExposure)




## Inheritance

* **GenomicBackgroundExposure** [ exposure event gene grouping mixin physical essence genomic entity ontology class]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | [Gene](Gene.md) | 0..* | connects an entity with one or more gene or gene products  | . |
| [has_biological_sequence](has_biological_sequence.md) | [biological_sequence](biological_sequence.md) | 0..1 | connects a genomic feature to its sequence  | . |
| [in_taxon](in_taxon.md) | [OrganismTaxon](OrganismTaxon.md) | 0..* | connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: genomic background exposure
description: A genomic background exposure is where an individual's specific genomic
  background of genes, sequence variants or other pre-existing genomic conditions
  constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
- gene grouping mixin
- physical essence
- genomic entity
- ontology class

```
</details>

### Induced

<details>
```yaml
name: genomic background exposure
description: A genomic background exposure is where an individual's specific genomic
  background of genes, sequence variants or other pre-existing genomic conditions
  constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
from_schema: https://w3id.org/biolink/biolink-model
mixins:
- exposure event
- gene grouping mixin
- physical essence
- genomic entity
- ontology class
attributes:
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: genomic background exposure
    range: time type
  has gene or gene product:
    name: has gene or gene product
    description: connects an entity with one or more gene or gene products
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: has_gene_or_gene_product
    owner: genomic background exposure
    range: gene
  has biological sequence:
    name: has biological sequence
    description: connects a genomic feature to its sequence
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: has_biological_sequence
    owner: genomic background exposure
    range: biological sequence
  in taxon:
    name: in taxon
    aliases:
    - instance of
    - is organism source of gene product
    - organism has gene
    - gene found in organism
    - ' gene product has organism source'
    exact_mappings:
    - RO:0002162
    - WIKIDATA_PROPERTY:P703
    narrow_mappings:
    - RO:0002160
    annotations:
      biolink:canonical_predicate:
        tag: biolink:canonical_predicate
        value: 'True'
    description: connects an entity to its taxonomic classification. Only certain
      kinds of entities can be taxonomically classified; see 'thing with taxon'
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: related to at instance level
    domain: thing with taxon
    multivalued: true
    inherited: true
    alias: in_taxon
    owner: genomic background exposure
    range: organism taxon

```
</details>