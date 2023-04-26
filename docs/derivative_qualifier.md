---
parent: Edge Properties
title: biolink:derivative_qualifier
grand_parent: Slots
layout: default
---

# Slot: derivative_qualifier

translator_minimal
{: .translator_minimal-subset-label }


A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’.

URI: [biolink:derivative_qualifier](https://w3id.org/biolink/derivative_qualifier)

## Domain and Range

[Association](Association.md) ->  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [qualifier](qualifier.md)

## Children

 *  [object derivative qualifier](object_derivative_qualifier.md)
 *  [subject derivative qualifier](subject_derivative_qualifier.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='metabolite', description=None, object=None) |
| **In Subsets:** | | translator_minimal |

