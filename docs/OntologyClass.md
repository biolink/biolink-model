---
parent: Class Mixins
title: biolink:OntologyClass
grand_parent: Classes
layout: default
---

# Class: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UnclassifiedOntologyClass],[TaxonomicRank],[RelationshipType],[ClinicalMeasurement]++-%20has%20attribute%20type%201..1%3E[OntologyClass],[ContributorAssociation]++-%20qualifiers%200..%2A%3E[OntologyClass],[GeneExpressionMixin]++-%20quantifier%20qualifier%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]++-%20quantifier%20qualifier%200..1%3E[OntologyClass],[Attribute]++-%20has%20attribute%20type%201..1%3E[OntologyClass],[PairwiseMolecularInteraction]++-%20interacting%20molecules%20category%200..1%3E[OntologyClass],[Association]++-%20qualifiers%200..%2A%3E[OntologyClass],[GeneExpressionMixin]++-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]++-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[SequenceVariant]uses%20-.-%3E[OntologyClass],[ReagentTargetedGene]uses%20-.-%3E[OntologyClass],[PhysiologicalProcess]uses%20-.-%3E[OntologyClass],[Pathway]uses%20-.-%3E[OntologyClass],[NucleicAcidEntity]uses%20-.-%3E[OntologyClass],[MolecularActivity]uses%20-.-%3E[OntologyClass],[Haplotype]uses%20-.-%3E[OntologyClass],[Genotype]uses%20-.-%3E[OntologyClass],[GenomicBackgroundExposure]uses%20-.-%3E[OntologyClass],[Genome]uses%20-.-%3E[OntologyClass],[Gene]uses%20-.-%3E[OntologyClass],[Drug]uses%20-.-%3E[OntologyClass],[BiologicalProcessOrActivity]uses%20-.-%3E[OntologyClass],[BiologicalProcess]uses%20-.-%3E[OntologyClass],[Behavior]uses%20-.-%3E[OntologyClass],[Attribute]uses%20-.-%3E[OntologyClass],[OntologyClass]%5E-[UnclassifiedOntologyClass],[OntologyClass]%5E-[TaxonomicRank],[OntologyClass]%5E-[RelationshipType],[OntologyClass]%5E-[GeneOntologyClass],[SequenceVariant],[ReagentTargetedGene],[PhysiologicalProcess],[Pathway],[PairwiseMolecularInteraction],[NucleicAcidEntity],[NamedThing],[MolecularActivity],[Haplotype],[Genotype],[GenomicBackgroundExposure],[Genome],[GeneToExpressionSiteAssociation],[GeneOntologyClass],[GeneExpressionMixin],[Gene],[Drug],[ContributorAssociation],[ClinicalMeasurement],[BiologicalProcessOrActivity],[BiologicalProcess],[Behavior],[Attribute],[Association])

---


## Identifier prefixes

 * MESH
 * UMLS
 * KEGG.BRITE

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
 * [UnclassifiedOntologyClass](UnclassifiedOntologyClass.md) - this is used for nodes that are taken from an ontology but are not typed using an existing biolink class

## Mixin for

 * [Attribute](Attribute.md) (mixin)  - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 * [Behavior](Behavior.md) (mixin) 
 * [BiologicalProcess](BiologicalProcess.md) (mixin)  - One or more causally connected executions of molecular functions
 * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) (mixin)  - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.
 * [Drug](Drug.md) (mixin)  - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 * [Gene](Gene.md) (mixin)  - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
 * [Genome](Genome.md) (mixin)  - A genome is the sum of genetic material within a cell or virion.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [Genotype](Genotype.md) (mixin)  - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background
 * [Haplotype](Haplotype.md) (mixin)  - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 * [MolecularActivity](MolecularActivity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.
 * [NucleicAcidEntity](NucleicAcidEntity.md) (mixin)  - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
 * [Pathway](Pathway.md) (mixin) 
 * [PhysiologicalProcess](PhysiologicalProcess.md) (mixin) 
 * [ReagentTargetedGene](ReagentTargetedGene.md) (mixin)  - A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.
 * [SequenceVariant](SequenceVariant.md) (mixin)  - An allele that varies in its sequence from what is considered the reference allele at that locus.

## Referenced by class

 *  **[ClinicalMeasurement](ClinicalMeasurement.md)** *[clinical measurement➞has attribute type](clinical_measurement_has_attribute_type.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞qualifiers](contributor_association_qualifiers.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneExpressionMixin](GeneExpressionMixin.md)** *[gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Attribute](Attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has topic](has_topic.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[superclass of](superclass_of.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | This is modeled as a mixin. 'ontology class' should not be the primary type of a node in the KG. Instead you should use an informative bioloink category, such as AnatomicalEntity (for Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL), etc |
|  | | Note that formally this is a metaclass. Instances of this class are instances in the graph, but can be the object of 'type' edges. For example, if we had a node in the graph representing a specific brain of a specific patient (e.g brain001), this could have a category of bl:Sample, and by typed more specifically with an ontology class UBERON:nnn, which has as category bl:AnatomicalEntity |
| **Examples:** | | Example(value='UBERON:0000955', description="the class 'brain' from the Uberon anatomy ontology") |
| **See also:** | | https://github.com/biolink/biolink-model/issues/486 |
| **Exact Mappings:** | | owl:Class |
|  | | schema:Class |

