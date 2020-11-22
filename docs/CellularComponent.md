---
parent: Entities
title: biolink:CellularComponent
grand_parent: Classes
layout: default
---

# Class: CellularComponent


A location in or around a cell

URI: [biolink:CellularComponent](https://w3id.org/biolink/vocab/CellularComponent)

GO:0005575
{: .mapping-label }

SIO:001400
{: .mapping-label }

WIKIDATA:Q5058355
{: .mapping-label }

UMLSSC:T026
{: .mapping-label }

UMLSST:celc
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[MacromolecularMachineToCellularComponentAssociation],[MacromolecularMachineToCellularComponentAssociation]-%20object%201..1%3E[CellularComponent%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[AnatomicalEntity]%5E-[CellularComponent],[AnatomicalEntity])

---


## Identifier prefixes

 * GO
 * MESH
 * UMLS
 * NCIT
 * SNOMEDCT
 * CL
 * UBERON

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part

## Referenced by class

 *  **[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)** *[macromolecular machine to cellular component association➞object](macromolecular_machine_to_cellular_component_association_object.md)*  <sub>REQ</sub>  **[CellularComponent](CellularComponent.md)**

## Attributes


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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
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
| **Mappings:** | | GO:0005575 |
|  | | SIO:001400 |
|  | | WIKIDATA:Q5058355 |
|  | | UMLSSC:T026 |
|  | | UMLSST:celc |

