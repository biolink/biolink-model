---
parent: Classes
title: biolink:Cell
grand_parent: Browse Biolink Model
layout: default
---

# Class: Cell




URI: [biolink:Cell](https://w3id.org/biolink/vocab/Cell)

GO:0005623
{: .mapping-label }

CL:0000000
{: .mapping-label }

SIO:010001
{: .mapping-label }

WIKIDATA:Q7868
{: .mapping-label }

UMLSSC:T025
{: .mapping-label }

UMLSST:cell
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[AnatomicalEntity]%5E-[Cell%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[AnatomicalEntity])

---


## Identifier prefixes

 * CL
 * PO
 * UMLS
 * NCIT
 * MESH
 * UBERON
 * SNOMEDCT

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0005623 |
|  | | CL:0000000 |
|  | | SIO:010001 |
|  | | WIKIDATA:Q7868 |
|  | | UMLSSC:T025 |
|  | | UMLSST:cell |

