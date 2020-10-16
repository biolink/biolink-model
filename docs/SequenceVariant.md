---
parent: Entities
title: biolink:SequenceVariant
grand_parent: Classes
layout: default
---

# Class: SequenceVariant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [biolink:SequenceVariant](https://w3id.org/biolink/vocab/SequenceVariant)

GENO:0000002
{: .mapping-label }

WIKIDATA:Q15304597
{: .mapping-label }

SIO:010277
{: .mapping-label }

VMC:Allele
{: .mapping-label }

SO:0001059
{: .mapping-label }

SO:0001060
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToThingAssociation],[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantAsAModelOfDiseaseAssociation],[Snv],[SequenceVariantModulatesTreatmentAssociation],[Gene]%3Chas%20gene%200..%2A-%20[SequenceVariant%7Chas_biological_sequence:biological_sequence%20%3F;id:string;name(i):label_type;category(i):category_type%20%2B],[GenotypeToVariantAssociation]-%20object%201..1%3E[SequenceVariant],[SequenceVariantModulatesTreatmentAssociation]-%20subject%201..1%3E[SequenceVariant],[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1%3E[SequenceVariant],[VariantAsAModelOfDiseaseAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToPhenotypicFeatureAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToThingAssociation]-%20subject%201..1%3E[SequenceVariant],[SequenceVariant]%5E-[Snv],[GenomicEntity]%5E-[SequenceVariant],[OrganismTaxon],[GenotypeToVariantAssociation],[GenomicEntity],[GeneHasVariantThatContributesToDiseaseAssociation],[Gene],[Association])

---


## Identifier prefixes

 * CAID
 * ClinVar
 * ClinVarVariant
 * WIKIDATA
 * DBSNP
 * dbSNP
 * MGI
 * ZFIN
 * FlyBase
 * FB
 * WB
 * WormBase

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Children

 * [Snv](Snv.md) - SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist

## Referenced by class

 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞object](genotype_to_variant_association_object.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Association](Association.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>OPT</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)** *[variant as a model of disease association➞subject](variant_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[variant to phenotypic feature association➞subject](variant_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association➞subject](variant_to_population_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToThingAssociation](VariantToThingAssociation.md)** *[variant to thing association➞subject](variant_to_thing_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**

## Attributes


### Own

 * [sequence variant➞has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>OPT</sub>
    * Description: The state of the sequence w.r.t a reference sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [sequence variant➞has gene](sequence_variant_has_gene.md)  <sub>0..*</sub>
    * Description: Each allele can be associated with any number of genes
    * range: [Gene](Gene.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * Example:    
    * Example:    

### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

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

 * [sequence variant➞has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>OPT</sub>
    * Description: The state of the sequence w.r.t a reference sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [sequence variant➞has gene](sequence_variant_has_gene.md)  <sub>0..*</sub>
    * Description: Each allele can be associated with any number of genes
    * range: [Gene](Gene.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * Example:    
    * Example:    

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | allele |
| **Local names:** | | allele (agr) |
| **Mappings:** | | GENO:0000002 |
|  | | WIKIDATA:Q15304597 |
|  | | SIO:010277 |
|  | | VMC:Allele |
|  | | SO:0001059 |
|  | | SO:0001060 |
| **Alt Descriptions:** | | An enitity that describes a single affected, endogenous allele.  These can be of any type that matches that definition (AGR) |
|  | | A contiguous change at a Location (VMC) |
| **Comments:** | | This class is for modeling the specific state at a locus. A single dbSNP rs ID could correspond to more than one sequence variants (e.g CIViC:1252 and CIViC:1253, two distinct BRCA2 alleles for rs28897743) |

