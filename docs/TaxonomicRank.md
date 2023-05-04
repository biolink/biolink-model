---
parent: Other Classes
title: biolink:TaxonomicRank
grand_parent: Classes
layout: default
---

# Class: TaxonomicRank


A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

URI: [biolink:TaxonomicRank](https://w3id.org/biolink/vocab/TaxonomicRank)

WIKIDATA:Q427626
{: .mapping-label }


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]-%20has%20taxonomic%20rank%200..1%3E[TaxonomicRank%7Cid(i):string],[OntologyClass]%5E-[TaxonomicRank],[OrganismTaxon],[OntologyClass],[NamedThing])

---


## Identifier prefixes

 * TAXRANK

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has taxonomic rank](has_taxonomic_rank.md)*  <sub>0..1</sub>  **[TaxonomicRank](TaxonomicRank.md)**
 *  **[OrganismTaxon](OrganismTaxon.md)** *[has taxonomic rank](has_taxonomic_rank.md)*  <sub>0..1</sub>  **[TaxonomicRank](TaxonomicRank.md)**

## Attributes


### Inherited from information resource:

 * [information resource status](information_resource_status.md)  <sub>0..1</sub>
     * Description: the status of the infores identifier, default is released
     * Range: [InformationResourceStatusEnum](InformationResourceStatusEnum.md)
 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WIKIDATA:Q427626 |

