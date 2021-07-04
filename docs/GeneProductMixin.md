---
parent: Class Mixins
title: biolink:GeneProductMixin
grand_parent: Classes
layout: default
---

# Class: GeneProductMixin


The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules.

URI: [biolink:GeneProductMixin](https://w3id.org/biolink/vocab/GeneProductMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneToGeneProductRelationship],[GeneToGeneProductRelationship]++-%20object%201..1%3E[GeneProductMixin%7Csynonym:label_type%20%2A;xref:iri_type%20%2A;name(i):symbol_type%20%3F],[Protein]uses%20-.-%3E[GeneProductMixin],[RNAProduct]uses%20-.-%3E[GeneProductMixin],[GeneProductMixin]%5E-[GeneProductIsoformMixin],[GeneOrGeneProduct]%5E-[GeneProductMixin],[Protein],[GeneProductIsoformMixin],[GeneOrGeneProduct],[Gene],[RNAProduct])

---


## Identifier prefixes

 * UniProtKB
 * gtpo
 * PR

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another

## Children

 * [GeneProductIsoformMixin](GeneProductIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

## Mixin for

 * [RNAProduct](RNAProduct.md) (mixin) 
 * [Protein](Protein.md) (mixin)  - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)*  <sub>1..1</sub>  **[GeneProductMixin](GeneProductMixin.md)**
 *  **[Gene](Gene.md)** *[has gene product](has_gene_product.md)*  <sub>0..\*</sub>  **[GeneProductMixin](GeneProductMixin.md)**

## Attributes


### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | WIKIDATA:Q424689 |
|  | | GENO:0000907 |
|  | | NCIT:C26548 |

