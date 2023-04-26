---
parent: Edge Properties
title: biolink:form_or_variant_qualifier
grand_parent: Slots
layout: default
---

# Slot: form_or_variant_qualifier

translator_minimal
{: .translator_minimal-subset-label }


A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’.

URI: [biolink:form_or_variant_qualifier](https://w3id.org/biolink/form_or_variant_qualifier)

## Domain and Range

[Association](Association.md) ->  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [qualifier](qualifier.md)

## Children

 *  [object form or variant qualifier](object_form_or_variant_qualifier.md)
 *  [subject form or variant qualifier](subject_form_or_variant_qualifier.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='mutation', description=None, object=None) |
|  | | Example(value='late stage', description=None, object=None) |
|  | | Example(value='severe', description=None, object=None) |
|  | | Example(value='transplant', description=None, object=None) |
|  | | Example(value='chemical analog', description=None, object=None) |
| **In Subsets:** | | translator_minimal |

