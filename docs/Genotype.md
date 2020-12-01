---
parent: Entities
title: biolink:Genotype
grand_parent: Classes
layout: default
---

# Class: Genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background

URI: [biolink:Genotype](https://w3id.org/biolink/vocab/Genotype)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[OrganismTaxon],[NamedThing],[GenotypeToVariantAssociation],[GenotypeToThingAssociationMixin],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeAsAModelOfDiseaseAssociation],[Zygosity]%3Chas%20zygosity%200..1-++[Genotype%7Chas_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeAsAModelOfDiseaseAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToGeneAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToGenotypePartAssociation]-%20object%201..1%3E[Genotype],[GenotypeToGenotypePartAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1%3E[Genotype],[GenotypeToThingAssociationMixin]-%20subject%201..1%3E[Genotype],[GenotypeToVariantAssociation]-%20subject%201..1%3E[Genotype],[GenomicEntity]%5E-[Genotype],[GenomicEntity],[Attribute],[Agent])

---


## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)** *[genotype as a model of disease association➞subject](genotype_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞subject](genotype_to_gene_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)** *[genotype to phenotypic feature association➞subject](genotype_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToThingAssociationMixin](GenotypeToThingAssociationMixin.md)** *[genotype to thing association mixin➞subject](genotype_to_thing_association_mixin_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞subject](genotype_to_variant_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**

## Attributes


### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a resource. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Consider renaming as genotypic entity |
| **Exact Mappings:** | | GENO:0000536 |
|  | | SIO:001079 |

