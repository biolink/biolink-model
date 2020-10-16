---
parent: Classes
title: biolink:Genotype
grand_parent: Browse Biolink Model
layout: default
---

# Type: Genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background

URI: [biolink:Genotype](https://w3id.org/biolink/vocab/Genotype)

GENO:0000536
{: .mapping-label }

SIO:001079
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[OrganismTaxon],[GenotypeToVariantAssociation],[GenotypeToThingAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeAsAModelOfDiseaseAssociation],[Zygosity]%3Chas%20zygosity%200..1-%20[Genotype%7Chas_biological_sequence(i):biological_sequence%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[GenotypeAsAModelOfDiseaseAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToGeneAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToGenotypePartAssociation]-%20object%201..1%3E[Genotype],[GenotypeToGenotypePartAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToThingAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToVariantAssociation]-%20subject%201..1%3E[Genotype],[GenomicEntity]%5E-[Genotype],[GenomicEntity])

---


## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)** *[genotype as a model of disease association➞subject](genotype_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞subject](genotype_to_gene_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)** *[genotype to phenotypic feature association➞subject](genotype_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToThingAssociation](GenotypeToThingAssociation.md)** *[genotype to thing association➞subject](genotype_to_thing_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞subject](genotype_to_variant_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**

## Attributes


### Own

 * [has zygosity](has_zygosity.md)  <sub>OPT</sub>
    * range: [Zygosity](Zygosity.md)

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
| **Mappings:** | | GENO:0000536 |
|  | | SIO:001079 |
| **Comments:** | | Consider renaming as genotypic entity |

