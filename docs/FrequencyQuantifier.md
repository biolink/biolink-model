# Class: FrequencyQuantifier



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:FrequencyQuantifier](https://w3id.org/biolink/vocab/FrequencyQuantifier)




## Inheritance

* [RelationshipQuantifier](RelationshipQuantifier.md)
    * **FrequencyQuantifier**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_count](has_count.md) | [integer](integer.md) | 0..1 | number of things with a particular property  | . |
| [has_total](has_total.md) | [integer](integer.md) | 0..1 | total number of things in a particular reference set  | . |
| [has_quotient](has_quotient.md) | [double](double.md) | 0..1 | None  | . |
| [has_percentage](has_percentage.md) | [double](double.md) | 0..1 | equivalent to has quotient multiplied by 100  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: frequency quantifier
from_schema: https://w3id.org/biolink/biolink-model
is_a: relationship quantifier
mixin: true
slots:
- has count
- has total
- has quotient
- has percentage

```
</details>

### Induced

<details>
```yaml
name: frequency quantifier
from_schema: https://w3id.org/biolink/biolink-model
is_a: relationship quantifier
mixin: true
attributes:
  has count:
    name: has count
    exact_mappings:
    - LOINC:has_count
    description: number of things with a particular property
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_count
    owner: frequency quantifier
    range: integer
  has total:
    name: has total
    description: total number of things in a particular reference set
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_total
    owner: frequency quantifier
    range: integer
  has quotient:
    name: has quotient
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_quotient
    owner: frequency quantifier
    range: double
  has percentage:
    name: has percentage
    description: equivalent to has quotient multiplied by 100
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_percentage
    owner: frequency quantifier
    range: double

```
</details>