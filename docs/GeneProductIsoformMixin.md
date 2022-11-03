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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneProductMixin],[ProteinIsoform]uses%20-.-%3E[GeneProductIsoformMixin%7Csynonym(i):label_type%20%2A;xref(i):uriorcurie%20%2A;name(i):symbol_type%20%3F],[PosttranslationalModification]uses%20-.-%3E[GeneProductIsoformMixin],[NucleosomeModification]uses%20-.-%3E[GeneProductIsoformMixin],[RNAProductIsoform]uses%20-.-%3E[GeneProductIsoformMixin],[GeneProductMixin]%5E-[GeneProductIsoformMixin],[ProteinIsoform],[PosttranslationalModification],[NucleosomeModification],[RNAProductIsoform])

---


## Parents

 *  is_a: [GeneProductMixin](GeneProductMixin.md) - The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.

## Mixin for

 * [RNAProductIsoform](RNAProductIsoform.md) (mixin)  - Represents a protein that is a specific isoform of the canonical or reference RNA
 * [NucleosomeModification](NucleosomeModification.md) (mixin)  - A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A.
 * [PosttranslationalModification](PosttranslationalModification.md) (mixin)  - A chemical modification of a polypeptide or protein that occurs after translation.  e.g. polypeptide cleavage to form separate proteins, methylation or acetylation of histone tail amino acids,  protein ubiquitination.
 * [ProteinIsoform](ProteinIsoform.md) (mixin)  - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

## Referenced by class


## Attributes


### Inherited from gene product mixin:

 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: Alternate CURIEs for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
