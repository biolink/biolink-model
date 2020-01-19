---
parent: Classes
title: biolink:CellularComponent
grand_parent: Browse Biolink Model
---

# Type: CellularComponent


A location in or around a cell

URI: [biolink:CellularComponent](https://w3id.org/biolink/vocab/CellularComponent)

GO:0005575
{: .mapping-label }

SIO:001400
{: .mapping-label }

WD:Q5058355
{: .mapping-label }

UMLSSC:T026
{: .mapping-label }

UMLSST:celc
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[CellularComponent&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[MacromolecularMachineToCellularComponentAssociation]-%20object%201..1>\[CellularComponent],%20\[AnatomicalEntity]^-\[CellularComponent])

---


## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part

## Referenced by class

 *  **[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)** *[macromolecular machine to cellular component association➞object](macromolecular_machine_to_cellular_component_association_object.md)*  <sub>REQ</sub>  **[CellularComponent](CellularComponent.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0005575 |
|  | | SIO:001400 |
|  | | WD:Q5058355 |
|  | | UMLSSC:T026 |
|  | | UMLSST:celc |

