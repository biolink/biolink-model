---
parent: Class Mixins
title: biolink:GeneProductIsoformMixin
grand_parent: Classes
layout: default
---

# Class: GeneProductIsoformMixin


This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

URI: [biolink:GeneProductIsoformMixin](https://w3id.org/biolink/vocab/GeneProductIsoformMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneProductMixin],[ProteinIsoform]uses%20-.-%3E[GeneProductIsoformMixin%7Csynonym(i):label_type%20%2A;xref(i):iri_type%20%2A;name(i):symbol_type%20%3F],[RNAProductIsoform]uses%20-.-%3E[GeneProductIsoformMixin],[GeneProductMixin]%5E-[GeneProductIsoformMixin],[ProteinIsoform],[RNAProductIsoform])

---


## Parents

 *  is_a: [GeneProductMixin](GeneProductMixin.md) - The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.

## Mixin for

 * [RNAProductIsoform](RNAProductIsoform.md) (mixin)  - Represents a protein that is a specific isoform of the canonical or reference RNA
 * [ProteinIsoform](ProteinIsoform.md) (mixin)  - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

## Referenced by class


## Attributes


### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)
