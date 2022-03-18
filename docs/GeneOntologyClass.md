# Class: GeneOntologyClass
_an ontology class that describes a functional aspect of a gene, gene prodoct or complex_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:GeneOntologyClass](https://w3id.org/biolink/vocab/GeneOntologyClass)




## Inheritance

* [OntologyClass](OntologyClass.md)
    * **GeneOntologyClass**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FunctionalAssociation](FunctionalAssociation.md) | [object](object.md) | range | gene ontology class |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object](object.md) | range | gene ontology class |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene ontology class
description: an ontology class that describes a functional aspect of a gene, gene
  prodoct or complex
in_subset:
- testing
from_schema: https://w3id.org/biolink/biolink-model
is_a: ontology class
mixin: true

```
</details>

### Induced

<details>
```yaml
name: gene ontology class
description: an ontology class that describes a functional aspect of a gene, gene
  prodoct or complex
in_subset:
- testing
from_schema: https://w3id.org/biolink/biolink-model
is_a: ontology class
mixin: true

```
</details>