---
parent: Other Classes
title: biolink:MappingCollection
grand_parent: Classes
layout: default
---

# Class: MappingCollection


A collection of deprecated mappings.

URI: [biolink:MappingCollection](https://w3id.org/biolink/vocab/MappingCollection)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PredicateMapping],[PredicateMapping]%3Cpredicate%20mappings%200..%2A-++[MappingCollection])

---


## Attributes


### Own

 * [predicate mappings](predicate_mappings.md)  <sub>0..\*</sub>
     * Description: A collection of relationships that are not used in biolink, but have biolink patterns that can  be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3.
     * Range: [PredicateMapping](PredicateMapping.md)
