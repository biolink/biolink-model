# Class: GeneProductIsoformMixin
_This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneProductIsoformMixin](https://w3id.org/biolink/vocab/GeneProductIsoformMixin)




## Inheritance

* [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * [GeneOrGeneProduct](GeneOrGeneProduct.md)
        * [GeneProductMixin](GeneProductMixin.md)
            * **GeneProductIsoformMixin**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [synonym](synonym.md) | [label_type](label_type.md) | 0..* | Alternate human-readable names for a thing  | . |
| [xref](xref.md) | [uriorcurie](uriorcurie.md) | 0..* | Alternate CURIEs for a thing  | . |
| [name](name.md) | [symbol_type](symbol_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene product isoform mixin
description: This is an abstract class that can be mixed in with different kinds of
  gene products to indicate that the gene product is intended to represent a specific
  isoform rather than a canonical or reference or generic product. The designation
  of canonical or reference may be arbitrary, or it may represent the superclass of
  all isoforms.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene product mixin
mixin: true

```
</details>

### Induced

<details>
```yaml
name: gene product isoform mixin
description: This is an abstract class that can be mixed in with different kinds of
  gene products to indicate that the gene product is intended to represent a specific
  isoform rather than a canonical or reference or generic product. The designation
  of canonical or reference may be arbitrary, or it may represent the superclass of
  all isoforms.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene product mixin
mixin: true
attributes:
  synonym:
    name: synonym
    aliases:
    - alias
    narrow_mappings:
    - skos:altLabel
    - gff3:Alias
    - alliancegenome:synonyms
    - gpi:DB_Object_Synonyms
    - oboInOwl:hasExactSynonym
    - oboInOwl:hasNarrowSynonym
    - oboInOwl:hasBroadSynonym
    - oboInOwl:hasRelatedSynonym
    - HANCESTRO:0330
    - IAO:0000136
    - RXNORM:has_tradename
    description: Alternate human-readable names for a thing
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: synonym
    owner: gene product isoform mixin
    range: label type
  xref:
    name: xref
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    description: Alternate CURIEs for a thing
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: xref
    owner: gene product isoform mixin
    range: uriorcurie
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: gene product isoform mixin
    range: symbol type

```
</details>