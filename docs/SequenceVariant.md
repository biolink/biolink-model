---
parent: Entities
title: biolink:SequenceVariant
grand_parent: Classes
layout: default
---

# Class: SequenceVariant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [biolink:SequenceVariant](https://w3id.org/biolink/vocab/SequenceVariant)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToEntityAssociationMixin],[VariantAsAModelOfDiseaseAssociation],[Snv],[SequenceVariantModulatesTreatmentAssociation],[Gene]%3Chas%20gene%200..%2A-%20[SequenceVariant%7Chas_biological_sequence:biological_sequence%20%3F;id:string;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;category(i):category_type%20%2B;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):string%20%3F],[GenotypeToVariantAssociation]-%20object%201..1%3E[SequenceVariant],[SequenceVariantModulatesTreatmentAssociation]-%20subject%201..1%3E[SequenceVariant],[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1%3E[SequenceVariant],[VariantAsAModelOfDiseaseAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToEntityAssociationMixin]-%20subject%201..1%3E[SequenceVariant],[VariantToPhenotypicFeatureAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1%3E[SequenceVariant],[SequenceVariant]uses%20-.-%3E[GenomicEntity],[SequenceVariant]uses%20-.-%3E[PhysicalEssence],[SequenceVariant]uses%20-.-%3E[OntologyClass],[SequenceVariant]%5E-[Snv],[BiologicalEntity]%5E-[SequenceVariant],[PhysicalEssence],[OrganismTaxon],[OntologyClass],[NucleicAcidEntity],[GenotypeToVariantAssociation],[GenomicEntity],[GeneHasVariantThatContributesToDiseaseAssociation],[Gene],[BiologicalEntity],[Attribute],[Association])

---


## Identifier prefixes

 * CAID
 * CLINVAR
 * ClinVarVariant
 * WIKIDATA
 * DBSNP
 * MGI
 * ZFIN
 * FB
 * RGD
 * AGRKB
 * SPDI
 * WB
 * WormBase

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [GenomicEntity](GenomicEntity.md)
 *  mixin: [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Children

 * [Snv](Snv.md) - SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist

## Referenced by class

 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has frameshift variant](has_frameshift_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has missense variant](has_missense_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has nearby variant](has_nearby_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has non coding variant](has_non_coding_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has nonsense variant](has_nonsense_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[has sequence variant](has_sequence_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has splice site variant](has_splice_site_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Gene](Gene.md)** *[has synonymous variant](has_synonymous_variant.md)*  <sub>0..\*</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Association](Association.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>0..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**

## Attributes


### Own

 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)
 * [has gene](has_gene.md)  <sub>0..\*</sub>
     * Description: connects an entity associated with one or more genes
     * Range: [Gene](Gene.md)
 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)

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
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from gene product mixin:

 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: Alternate CURIEs for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)
 * [has gene](has_gene.md)  <sub>0..\*</sub>
     * Description: connects an entity associated with one or more genes
     * Range: [Gene](Gene.md)
 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | allele |
| **Local names:** | | allele (agr) |
| **Alt Descriptions:** | | An entity that describes a single affected, endogenous allele. These can be of any type that matches that definition (AGR) |
|  | | A contiguous change at a Location (VMC) |
| **Comments:** | | This class is for modeling the specific state at a locus. A single DBSNP rs ID could correspond to more than one sequence variants (e.g CIViC:1252 and CIViC:1253, two distinct BRCA2 alleles for rs28897743) |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | GENO:0000002 |
|  | | WIKIDATA:Q15304597 |
|  | | SIO:010277 |
|  | | VMC:Allele |
|  | | SO:0001059 |
| **Close Mappings:** | | dcid:Allele |
| **Broad Mappings:** | | SO:0001060 |
