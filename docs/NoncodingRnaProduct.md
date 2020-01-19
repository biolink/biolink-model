---
parent: Classes
title: biolink:NoncodingRNAProduct
grand_parent: Browse Biolink Model
---

# Type: NoncodingRNAProduct




URI: [biolink:NoncodingRNAProduct](https://w3id.org/biolink/vocab/NoncodingRNAProduct)

SIO:001235
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[NoncodingRNAProduct&#124;name(i):symbol_type;id(i):identifier_type;category(i):iri_type%20%2B],%20\[NoncodingRNAProduct]^-\[MicroRNA],%20\[RNAProduct]^-\[NoncodingRNAProduct])

---


## Parents

 *  is_a: [RNAProduct](RNAProduct.md)

## Children

 * [MicroRNA](MicroRNA.md)

## Referenced by class


## Attributes


### Inherited from macromolecular machine:

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](types/SymbolType.md)
    * inherited from: [MacromolecularMachine](MacromolecularMachine.md)

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
| **Mappings:** | | SIO:001235 |

