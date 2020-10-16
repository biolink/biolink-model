---
parent: Classes
title: biolink:ProteinIsoform
grand_parent: Browse Biolink Model
layout: default
---

# Type: ProteinIsoform


Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

URI: [biolink:ProteinIsoform](https://w3id.org/biolink/vocab/ProteinIsoform)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProteinIsoform%7Cname(i):label_type;description(i):narrative_text%20%3F;synonym(i):label_type%20%2A;xref(i):iri_type%20%2A;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B]uses%20-.-%3E[GeneProductIsoform],[Protein]%5E-[ProteinIsoform],[Protein],[OrganismTaxon],[GeneProductIsoform])

---


## Identifier prefixes

 * UniProtKB
 * PR
 * ENSEMBL

## Parents

 *  is_a: [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

## Uses Mixins

 *  mixin: [GeneProductIsoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

## Attributes


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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | proteoform |

