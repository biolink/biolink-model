---
parent: Class Mixins
title: biolink:MacromolecularMachineMixin
grand_parent: Classes
layout: default
---

# Class: MacromolecularMachineMixin


A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: [biolink:MacromolecularMachineMixin](https://w3id.org/biolink/vocab/MacromolecularMachineMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MolecularActivity],[ChemicalToChemicalDerivationAssociation]++-%20catalyst%20qualifier(i)%200..%2A%3E[MacromolecularMachineMixin%7Cname:symbol_type%20%3F],[ChemicalToChemicalDerivationAssociation]++-%20catalyst%20qualifier%200..%2A%3E[MacromolecularMachineMixin],[FunctionalAssociation]++-%20subject%201..1%3E[MacromolecularMachineMixin],[MolecularActivity]++-%20enabled%20by%200..%2A%3E[MacromolecularMachineMixin],[MacromolecularComplex]uses%20-.-%3E[MacromolecularMachineMixin],[MacromolecularMachineMixin]%5E-[GeneOrGeneProduct],[MacromolecularComplex],[GeneOrGeneProduct],[FunctionalAssociation],[ChemicalToChemicalDerivationAssociation],[Association])

---


## Children

 * [GeneOrGeneProduct](GeneOrGeneProduct.md) - A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another

## Mixin for

 * [MacromolecularComplex](MacromolecularComplex.md) (mixin)  - A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.

## Referenced by class

 *  **[Association](Association.md)** *[catalyst qualifier](catalyst_qualifier.md)*  <sub>0..\*</sub>  **[MacromolecularMachineMixin](MacromolecularMachineMixin.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[catalyst qualifier](catalyst_qualifier.md)*  <sub>0..\*</sub>  **[MacromolecularMachineMixin](MacromolecularMachineMixin.md)**
 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MacromolecularMachineMixin](MacromolecularMachineMixin.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[enabled by](enabled_by.md)*  <sub>0..\*</sub>  **[MacromolecularMachineMixin](MacromolecularMachineMixin.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Domain for slot:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
