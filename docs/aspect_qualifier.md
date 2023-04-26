---
parent: Edge Properties
title: biolink:aspect_qualifier
grand_parent: Slots
layout: default
---

# Slot: aspect_qualifier

translator_minimal
{: .translator_minimal-subset-label }


Composes with the core concept to describe new concepts of a different ontological type. e.g. a process in which the core concept participates, a function/activity/role held by the core concept, or a characteristic/quality that inheres in the core concept.  The purpose of the aspect slot is to indicate what aspect is being affected in an  'affects' association.

URI: [biolink:aspect_qualifier](https://w3id.org/biolink/aspect_qualifier)

## Domain and Range

[Association](Association.md) ->  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [qualifier](qualifier.md)

## Children

 *  [object aspect qualifier](object_aspect_qualifier.md)
 *  [subject aspect qualifier](subject_aspect_qualifier.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='stability', description=None, object=None) |
|  | | Example(value='abundance', description=None, object=None) |
|  | | Example(value='expression', description=None, object=None) |
|  | | Example(value='exposure', description=None, object=None) |
| **In Subsets:** | | translator_minimal |

