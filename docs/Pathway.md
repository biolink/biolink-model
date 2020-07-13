---
parent: Classes
title: biolink:Pathway
grand_parent: Browse Biolink Model
layout: default
---

# Type: Pathway




URI: [biolink:Pathway](https://w3id.org/biolink/vocab/Pathway)

GO:0007165
{: .mapping-label }

SIO:010526
{: .mapping-label }

PW:0000001
{: .mapping-label }

WIKIDATA:Q4915012
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalToPathwayAssociation]-%20object%201..1%3E[Pathway|id(i):string;name(i):label_type;category(i):category_type%20%2B],[BiologicalProcess]%5E-[Pathway],[NamedThing],[ChemicalToPathwayAssociation],[BiologicalProcess])

---


## Identifier prefixes

 * GO
 * REACT
 * KEGG
 * SMPDB
 * PHARMGKB.PATHWAYS
 * WIKIPATHWAYS

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

## Referenced by class

 *  **[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)** *[chemical to pathway association➞object](chemical_to_pathway_association_object.md)*  <sub>REQ</sub>  **[Pathway](Pathway.md)**

## Attributes


### Inherited from biological process or activity:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0007165 |
|  | | SIO:010526 |
|  | | PW:0000001 |
|  | | WIKIDATA:Q4915012 |

