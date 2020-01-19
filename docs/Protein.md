---
parent: Classes
title: biolink:Protein
grand_parent: Browse Biolink Model
---

# Type: Protein


A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

URI: [biolink:Protein](https://w3id.org/biolink/vocab/Protein)

PR:000000001
{: .mapping-label }

SIO:010043
{: .mapping-label }

WD:Q8054
{: .mapping-label }

UMLSSC:T087
{: .mapping-label }

UMLSST:amas
{: .mapping-label }

UMLSSC:T116
{: .mapping-label }

UMLSST:aapp
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Protein&#124;name(i):symbol_type;id(i):identifier_type;category(i):iri_type%20%2B],%20\[Protein]^-\[ProteinIsoform],%20\[GeneProduct]^-\[Protein])

---


## Parents

 *  is_a: [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

## Children

 * [ProteinIsoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

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
| **Aliases:** | | polypeptide |
| **Mappings:** | | PR:000000001 |
|  | | SIO:010043 |
|  | | WD:Q8054 |
|  | | UMLSSC:T087 |
|  | | UMLSST:amas |
|  | | UMLSSC:T116 |
|  | | UMLSST:aapp |

