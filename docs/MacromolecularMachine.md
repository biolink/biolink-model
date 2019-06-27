
# Class: macromolecular machine


A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: [biolink:MacromolecularMachine](https://w3id.org/biolink/vocab/MacromolecularMachine)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[MacromolecularMachine|name:symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;category(i):iri_type%20%2B],%20\[FunctionalAssociation]-%20subject%201..1>\[MacromolecularMachine],%20\[MacromolecularMachine]^-\[MacromolecularComplex],%20\[MacromolecularMachine]^-\[GeneOrGeneProduct],%20\[GenomicEntity]^-\[MacromolecularMachine])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Children

 * [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
 * [MacromolecularComplex](MacromolecularComplex.md)

## Referenced by class

 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[subject](functional_association_subject.md)*  <sub>REQ</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**

## Attributes


### Own

 * [name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](SymbolType.md)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](SymbolType.md)
