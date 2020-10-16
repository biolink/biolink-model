---
parent: Entities
title: biolink:OrganismTaxon
grand_parent: Classes
layout: default
---

# Class: OrganismTaxon


A classification of a set of organisms. Examples: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.

URI: [biolink:OrganismTaxon](https://w3id.org/biolink/vocab/OrganismTaxon)

WIKIDATA:Q16521
{: .mapping-label }

NCBITaxon:1
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[ThingWithTaxon]-%20in%20taxon%200..%2A%3E[OrganismTaxon%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[OntologyClass]%5E-[OrganismTaxon],[OntologyClass])

---


## Identifier prefixes

 * NCBITaxon
 * MESH

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **[ThingWithTaxon](ThingWithTaxon.md)** *[in taxon](in_taxon.md)*  <sub>0..*</sub>  **[OrganismTaxon](OrganismTaxon.md)**

## Attributes


### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WIKIDATA:Q16521 |
|  | | NCBITaxon:1 |

