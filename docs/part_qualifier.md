---
parent: Edge Properties
title: biolink:part_qualifier
grand_parent: Slots
layout: default
---

# Slot: part_qualifier

translator_minimal
{: .translator_minimal-subset-label }


defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it, e.g. 'ESR1 transcript' q: polyA tail).

URI: [biolink:part_qualifier](https://w3id.org/biolink/vocab/part_qualifier)

## Domain and Range

[Association](Association.md) ->  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [qualifier](qualifier.md)

## Children

 *  [object part qualifier](object_part_qualifier.md)
 *  [subject part qualifier](subject_part_qualifier.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='polyA tail', description=None, object=None) |
|  | | Example(value='upstream control region', description=None, object=None) |
| **In Subsets:** | | translator_minimal |

