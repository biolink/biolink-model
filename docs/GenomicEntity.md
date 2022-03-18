# Class: GenomicEntity



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GenomicEntity](https://w3id.org/biolink/vocab/GenomicEntity)




## Inheritance

* [ThingWithTaxon](ThingWithTaxon.md)
    * **GenomicEntity**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_biological_sequence](has_biological_sequence.md) | [biological_sequence](biological_sequence.md) | 0..1 | connects a genomic feature to its sequence  | . |
| [in_taxon](in_taxon.md) | [OrganismTaxon](OrganismTaxon.md) | 0..* | connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: genomic entity
narrow_mappings:
- STY:T028
- GENO:0000897
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: thing with taxon
mixin: true
slots:
- has biological sequence

```
</details>

### Induced

<details>
```yaml
name: genomic entity
narrow_mappings:
- STY:T028
- GENO:0000897
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: thing with taxon
mixin: true
attributes:
  has biological sequence:
    name: has biological sequence
    description: connects a genomic feature to its sequence
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: has_biological_sequence
    owner: genomic entity
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
    owner: genomic entity
    range: organism taxon

```
</details>