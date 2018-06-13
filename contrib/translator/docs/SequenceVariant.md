# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [http://bioentity.io/vocab/SequenceVariant](http://bioentity.io/vocab/SequenceVariant)

![img](images/SequenceVariant.png)
## Mappings

 * [GENO:0000002](http://purl.obolibrary.org/obo/GENO_0000002)
 * [WD:Q15304597](http://purl.obolibrary.org/obo/WD_Q15304597)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)
## Inheritance

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
## Children

## Used in

 *  class: **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association.object](genotype_to_variant_association_object.md)* **[SequenceVariant](SequenceVariant.md)**
 *  class: **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association.subject](sequence_variant_modulates_treatment_association_subject.md)* **[SequenceVariant](SequenceVariant.md)**
 *  class: **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)* **[SequenceVariant](SequenceVariant.md)**
 *  class: **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[variant to phenotypic feature association.subject](variant_to_phenotypic_feature_association_subject.md)* **[SequenceVariant](SequenceVariant.md)**
 *  class: **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association.subject](variant_to_population_association_subject.md)* **[SequenceVariant](SequenceVariant.md)**
 *  class: **[VariantToThingAssociation](VariantToThingAssociation.md)** *[variant to thing association.subject](variant_to_thing_association_subject.md)* **[SequenceVariant](SequenceVariant.md)**
## Fields

 * _[sequence variant.has biological sequence](sequence_variant_has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [BiologicalSequence](BiologicalSequence.md)
    * __Local__
 * _[sequence variant.has gene](sequence_variant_has_gene.md)_
    * _Each allele can be associated with any number of genes_
    * range: **string***
    * __Local__
 * _[sequence variant.id](sequence_variant_id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [IdentifierType](IdentifierType.md)
    * __Local__
 * _[biomarker for](biomarker_for.md) *subsets*: (translator_minimal)_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[has phenotype](has_phenotype.md) *subsets*: (translator_minimal)_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * _[in taxon](in_taxon.md) *subsets*: (translator_minimal)_
    * _connects a thing to a class representing a taxon_
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)_
    * _holds between two entities that make physical contact as part of some interaction_
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets*: (translator_minimal)_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[uri](uri.md)_
    * _URI expansion of CURIE_
    * range: [uri](uri.md)
    * inherited from: [NamedThing](NamedThing.md)
