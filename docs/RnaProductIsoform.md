---
parent: Classes
title: biolink:RNAProductIsoform
grand_parent: Browse Biolink Model
---

# Type: RNAProductIsoform


Represents a protein that is a specific isoform of the canonical or reference RNA

URI: [biolink:RNAProductIsoform](https://w3id.org/biolink/vocab/RNAProductIsoform)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[RNAProductIsoform&#124;name(i):symbol_type;id(i):identifier_type;category(i):iri_type%20%2B],%20\[RNAProductIsoform]uses%20-.->\[GeneProductIsoform],%20\[RNAProduct]^-\[RNAProductIsoform])

---


## Parents

 *  is_a: [RNAProduct](RNAProduct.md)

## Uses Mixins

 *  mixin: [GeneProductIsoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

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
