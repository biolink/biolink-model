---
parent: Classes
title: biolink:Snv
grand_parent: Browse Biolink Model
layout: default
---

# Type: Snv


SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist

URI: [biolink:Snv](https://w3id.org/biolink/vocab/Snv)

SO:0001483
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SequenceVariant]%5E-[Snv|id(i):string;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type;category(i):category_type%20%2B],[SequenceVariant],[OrganismTaxon],[Gene])

---


## Parents

 *  is_a: [SequenceVariant](SequenceVariant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from sequence variant:

 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [sequence variant➞has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>OPT</sub>
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [sequence variant➞has gene](sequence_variant_has_gene.md)  <sub>0..*</sub>
    * range: [Gene](Gene.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | single nucleotide variant |
| **Mappings:** | | SO:0001483 |

