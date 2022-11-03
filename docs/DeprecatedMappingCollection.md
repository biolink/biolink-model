---
parent: Other Classes
title: biolink:DeprecatedMappingCollection
grand_parent: Classes
layout: default
---

# Class: DeprecatedMappingCollection


A collection of deprecated mappings.

URI: [biolink:DeprecatedMappingCollection](https://w3id.org/biolink/vocab/DeprecatedMappingCollection)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DeprecatedPredicateMapping],[DeprecatedPredicateMapping]%3Cdeprecated%20predicate%20mappings%200..%2A-++[DeprecatedMappingCollection])

---


## Attributes


### Own

 * [deprecated predicate mappings](deprecated_predicate_mappings.md)  <sub>0..\*</sub>
     * Description: A collection of relationships that are not used in biolink, but have biolink patterns that can  be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3.
     * Range: [DeprecatedPredicateMapping](DeprecatedPredicateMapping.md)
