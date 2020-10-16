---
parent: Classes
title: biolink:Protein
grand_parent: Browse Biolink Model
layout: default
---

# Type: Protein


A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

URI: [biolink:Protein](https://w3id.org/biolink/vocab/Protein)

PR:000000001
{: .mapping-label }

SIO:010043
{: .mapping-label }

WIKIDATA:Q8054
{: .mapping-label }

SO:0000104
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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProteinIsoform],[Protein%7Cname(i):label_type;description(i):narrative_text%20%3F;synonym(i):label_type%20%2A;xref(i):iri_type%20%2A;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B]%5E-[ProteinIsoform],[GeneProduct]%5E-[Protein],[OrganismTaxon],[GeneProduct])

---


## Identifier prefixes

 * UniProtKB
 * PR
 * ENSEMBL

## Parents

 *  is_a: [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

## Children

 * [ProteinIsoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

## Referenced by class


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
| **Aliases:** | | polypeptide |
| **Mappings:** | | PR:000000001 |
|  | | SIO:010043 |
|  | | WIKIDATA:Q8054 |
|  | | SO:0000104 |
|  | | UMLSSC:T087 |
|  | | UMLSST:amas |
|  | | UMLSSC:T116 |
|  | | UMLSST:aapp |

