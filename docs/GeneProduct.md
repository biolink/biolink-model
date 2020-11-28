---
parent: Entities
title: biolink:GeneProduct
grand_parent: Classes
layout: default
---

# Class: GeneProduct


The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

URI: [biolink:GeneProduct](https://w3id.org/biolink/vocab/GeneProduct)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Transcript],[Protein],[OrganismTaxon],[GeneToGeneProductRelationship],[GeneToGeneProductRelationship]-%20object%201..1%3E[GeneProduct%7Cdescription:narrative_text%20%3F;synonym:label_type%20%2A;xref:iri_type%20%2A;name(i):symbol_type%20%3F;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;source(i):label_type%20%3F],[GeneProduct]%5E-[Transcript],[GeneProduct]%5E-[Protein],[GeneProduct]%5E-[RNAProduct],[GeneOrGeneProduct]%5E-[GeneProduct],[GeneOrGeneProduct],[Gene],[Attribute],[RNAProduct])

---


## Identifier prefixes

 * UniProtKB
 * gtpo
 * PR

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Children

 * [RNAProduct](RNAProduct.md)
 * [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
 * [Transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)*  <sub>REQ</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[Gene](Gene.md)** *[has gene product](has_gene_product.md)*  <sub>0..*</sub>  **[GeneProduct](GeneProduct.md)**

## Attributes


### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from macromolecular machine:

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>OPT</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from resource mixin:

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | WIKIDATA:Q424689 |
|  | | GENO:0000907 |
|  | | NCIT:C26548 |

