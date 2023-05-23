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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TaxonomicRank],[RelationshipType],[ClinicalMeasurement]-%20has%20attribute%20type%201..1%3E[OntologyClass%7Cid:string],[ContributorAssociation]-%20qualifiers%200..%2A%3E[OntologyClass],[FunctionalAssociation]-%20object%201..1%3E[OntologyClass],[GeneExpressionMixin]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[GeneToGoTermAssociation]-%20object%201..1%3E[OntologyClass],[Attribute]-%20has%20attribute%20type%201..1%3E[OntologyClass],[PairwiseMolecularInteraction]-%20interacting%20molecules%20category%200..1%3E[OntologyClass],[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation]-%20object%20context%20qualifier%200..1%3E[OntologyClass],[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation]-%20subject%20context%20qualifier%200..1%3E[OntologyClass],[Association]-%20object%20category%200..1%3E[OntologyClass],[Association]-%20object%20category%20closure%200..%2A%3E[OntologyClass],[Association]-%20qualifiers%200..%2A%3E[OntologyClass],[GeneExpressionMixin]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[Association]-%20subject%20category%200..1%3E[OntologyClass],[Association]-%20subject%20category%20closure%200..%2A%3E[OntologyClass],[TranscriptionFactorBindingSite]uses%20-.-%3E[OntologyClass],[SequenceVariant]uses%20-.-%3E[OntologyClass],[RegulatoryRegion]uses%20-.-%3E[OntologyClass],[ReagentTargetedGene]uses%20-.-%3E[OntologyClass],[PhysiologicalProcess]uses%20-.-%3E[OntologyClass],[Pathway]uses%20-.-%3E[OntologyClass],[NucleicAcidEntity]uses%20-.-%3E[OntologyClass],[MolecularActivity]uses%20-.-%3E[OntologyClass],[Haplotype]uses%20-.-%3E[OntologyClass],[Genotype]uses%20-.-%3E[OntologyClass],[GenomicBackgroundExposure]uses%20-.-%3E[OntologyClass],[Genome]uses%20-.-%3E[OntologyClass],[Gene]uses%20-.-%3E[OntologyClass],[Drug]uses%20-.-%3E[OntologyClass],[BiologicalProcessOrActivity]uses%20-.-%3E[OntologyClass],[BiologicalProcess]uses%20-.-%3E[OntologyClass],[Behavior]uses%20-.-%3E[OntologyClass],[Attribute]uses%20-.-%3E[OntologyClass],[AccessibleDnaRegion]uses%20-.-%3E[OntologyClass],[OntologyClass]%5E-[TaxonomicRank],[OntologyClass]%5E-[RelationshipType],[OntologyClass]%5E-[ExposureEvent],[TranscriptionFactorBindingSite],[SequenceVariant],[RegulatoryRegion],[ReagentTargetedGene],[PhysiologicalProcess],[Pathway],[PairwiseMolecularInteraction],[NucleicAcidEntity],[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation],[NamedThing],[MolecularActivity],[Haplotype],[Genotype],[GenomicBackgroundExposure],[Genome],[GeneToGoTermAssociation],[GeneToExpressionSiteAssociation],[GeneExpressionMixin],[Gene],[FunctionalAssociation],[ExposureEvent],[Drug],[ContributorAssociation],[ClinicalMeasurement],[BiologicalProcessOrActivity],[BiologicalProcess],[Behavior],[Attribute],[Association],[AccessibleDnaRegion])

---


## Identifier prefixes

 * MESH
 * UMLS
 * KEGG.BRITE

## Children

 * [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

## Mixin for

 * [AccessibleDnaRegion](AccessibleDnaRegion.md) (mixin)  - A region (or regions) of a chromatinized genome that has been measured to be more accessible to an enzyme such as DNase-I or Tn5 Transpose
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
 * [RegulatoryRegion](RegulatoryRegion.md) (mixin)  - A region (or regions) of the genome that contains known or putative regulatory elements that act in cis- or trans- to affect the transcription of gene
 * [SequenceVariant](SequenceVariant.md) (mixin)  - A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.
 * [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) (mixin)  - A region (or regions) of the genome that contains a region of DNA known or predicted to bind a protein that modulates gene transcription

## Referenced by class

 *  **[ClinicalMeasurement](ClinicalMeasurement.md)** *[has attribute type](has_attribute_type.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[qualifiers](qualifiers.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneExpressionMixin](GeneExpressionMixin.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToGoTermAssociation](GeneToGoTermAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Attribute](Attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>1..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has topic](has_topic.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)** *[object context qualifier](object_context_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)** *[subject context qualifier](subject_context_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[object category](object_category.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[object category closure](object_category_closure.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[subject category](subject_category.md)*  <sub>0..1</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[subject category closure](subject_category_closure.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[superclass of](superclass_of.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | This is modeled as a mixin. 'ontology class' should not be the primary type of a node in the KG. Instead you should use an informative bioloink category, such as AnatomicalEntity (for Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL), etc |
|  | | Note that formally this is a metaclass. Instances of this class are instances in the graph, but can be the object of 'type' edges. For example, if we had a node in the graph representing a specific brain of a specific patient (e.g brain001), this could have a category of bl:Sample, and by typed more specifically with an ontology class UBERON:nnn, which has as category bl:AnatomicalEntity |
| **Examples:** | | Example(value='UBERON:0000955', description="the class 'brain' from the Uberon anatomy ontology", object=None) |
| **See also:** | | [https://github.com/biolink/biolink-model/issues/486](https://github.com/biolink/biolink-model/issues/486) |
| **Exact Mappings:** | | owl:Class |
|  | | schema:Class |

