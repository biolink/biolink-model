# Class: GeneProductMixin
_The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneProductMixin](https://w3id.org/biolink/vocab/GeneProductMixin)




## Inheritance

* [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * [GeneOrGeneProduct](GeneOrGeneProduct.md)
        * **GeneProductMixin**
            * [GeneProductIsoformMixin](GeneProductIsoformMixin.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [synonym](synonym.md) | [label_type](label_type.md) | 0..* | Alternate human-readable names for a thing  | . |
| [xref](xref.md) | [uriorcurie](uriorcurie.md) | 0..* | Alternate CURIEs for a thing  | . |
| [name](name.md) | [symbol_type](symbol_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object](object.md) | range | gene product mixin |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UniProtKB

* gtpo

* PR










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene product mixin
id_prefixes:
- UniProtKB
- gtpo
- PR
exact_mappings:
- WIKIDATA:Q424689
- GENO:0000907
- NCIT:C26548
description: The functional molecular product of a single gene locus. Gene products
  are either proteins or functional RNA molecules.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene or gene product
mixin: true
slots:
- synonym
- xref

```
</details>

### Induced

<details>
```yaml
name: gene product mixin
id_prefixes:
- UniProtKB
- gtpo
- PR
exact_mappings:
- WIKIDATA:Q424689
- GENO:0000907
- NCIT:C26548
description: The functional molecular product of a single gene locus. Gene products
  are either proteins or functional RNA molecules.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene or gene product
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
    owner: gene product mixin
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
    owner: gene product mixin
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
    owner: gene product mixin
    range: symbol type

```
</details>