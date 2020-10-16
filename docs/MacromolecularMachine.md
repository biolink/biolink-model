---
parent: Classes
title: biolink:MacromolecularMachine
grand_parent: Browse Biolink Model
layout: default
---

# Class: MacromolecularMachine


A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: [biolink:MacromolecularMachine](https://w3id.org/biolink/vocab/MacromolecularMachine)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[MolecularActivity],[ChemicalToChemicalDerivationAssociation]-%20change%20is%20catalyzed%20by(i)%200..%2A%3E[MacromolecularMachine%7Cname:symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B],[ChemicalToChemicalDerivationAssociation]-%20change%20is%20catalyzed%20by%200..%2A%3E[MacromolecularMachine],[FunctionalAssociation]-%20subject%201..1%3E[MacromolecularMachine],[MolecularActivity]-%20enabled%20by%200..%2A%3E[MacromolecularMachine],[MacromolecularMachine]%5E-[MacromolecularComplex],[MacromolecularMachine]%5E-[GeneOrGeneProduct],[GenomicEntity]%5E-[MacromolecularMachine],[MacromolecularComplex],[GenomicEntity],[GeneOrGeneProduct],[FunctionalAssociation],[ChemicalToChemicalDerivationAssociation],[Association])

---


## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Children

 * [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
 * [MacromolecularComplex](MacromolecularComplex.md)

## Referenced by class

 *  **[Association](Association.md)** *[change is catalyzed by](change_is_catalyzed_by.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞change is catalyzed by](chemical_to_chemical_derivation_association_change_is_catalyzed_by.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[functional association➞subject](functional_association_subject.md)*  <sub>REQ</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞enabled by](molecular_activity_enabled_by.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**

## Attributes


### Own

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)

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

### Domain for slot:

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
