---
parent: Associations
title: biolink:Association
grand_parent: Classes
layout: default
---

# Class: Association


A typed association between two entities, supported by evidence

URI: [biolink:Association](https://w3id.org/biolink/vocab/Association)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToGeneAssociation],[VariantToDiseaseAssociation],[TaxonToTaxonAssociation],[SequenceVariantModulatesTreatmentAssociation],[SequenceFeatureRelationship],[SequenceAssociation],[RetrievalSource],[Publication],[PopulationToPopulationAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[OrganismToOrganismAssociation],[OrganismTaxonToOrganismTaxonAssociation],[OrganismTaxonToEnvironmentAssociation],[OntologyClass],[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation],[NamedThing],[MolecularActivityToPathwayAssociation],[MolecularActivityToMolecularActivityAssociation],[MolecularActivityToChemicalEntityAssociation],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[MaterialSampleDerivationAssociation],[InformationResource],[InformationContentEntityToNamedThingAssociation],[GenotypeToVariantAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeToDiseaseAssociation],[GeneToPhenotypicFeatureAssociation],[GeneToPathwayAssociation],[GeneToGeneFamilyAssociation],[GeneToGeneAssociation],[GeneToExpressionSiteAssociation],[GeneToDiseaseAssociation],[FunctionalAssociation],[ExposureEventToPhenotypicFeatureAssociation],[ExposureEventToOutcomeAssociation],[EvidenceType],[EntityToPhenotypicFeatureAssociation],[EntityToDiseaseAssociation],[Entity],[DrugToGeneAssociation],[DiseaseToPhenotypicFeatureAssociation],[DiseaseToExposureEventAssociation],[DiseaseOrPhenotypicFeatureToLocationAssociation],[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation],[ContributorAssociation],[ChemicalToPathwayAssociation],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalToChemicalAssociation],[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation],[ChemicalGeneInteractionAssociation],[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation],[ChemicalEntityAssessesNamedThingAssociation],[ChemicalAffectsGeneAssociation],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation],[BehaviorToBehavioralFeatureAssociation],[Attribute],[RetrievalSource]%3Cretrieval%20source%20ids%200..%2A-%20[Association%7Cpredicate:predicate_type;negated:boolean%20%3F;timepoint:time_type%20%3F;original_subject:string%20%3F;original_predicate:uriorcurie%20%3F;original_object:string%20%3F;subject_closure:string%20%2A;object_closure:string%20%2A;subject_namespace:string%20%3F;object_namespace:string%20%3F;subject_label_closure:string%20%2A;object_label_closure:string%20%2A;type:string%20%2A;category:category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[OntologyClass]%3Cobject%20category%20closure%200..%2A-%20[Association],[OntologyClass]%3Csubject%20category%20closure%200..%2A-%20[Association],[OntologyClass]%3Cobject%20category%200..1-%20[Association],[OntologyClass]%3Csubject%20category%200..1-%20[Association],[InformationResource]%3Caggregator%20knowledge%20source%200..%2A-%20[Association],[InformationResource]%3Cprimary%20knowledge%20source%200..1-%20[Association],[InformationResource]%3Cknowledge%20source%200..1-%20[Association],[EvidenceType]%3Chas%20evidence%200..%2A-%20[Association],[Publication]%3Cpublications%200..%2A-%20[Association],[OntologyClass]%3Cqualifiers%200..%2A-%20[Association],[NamedThing]%3Cobject%201..1-%20[Association],[NamedThing]%3Csubject%201..1-%20[Association],[Association]%5E-[VariantToPopulationAssociation],[Association]%5E-[VariantToPhenotypicFeatureAssociation],[Association]%5E-[VariantToGeneAssociation],[Association]%5E-[VariantToDiseaseAssociation],[Association]%5E-[TaxonToTaxonAssociation],[Association]%5E-[SequenceVariantModulatesTreatmentAssociation],[Association]%5E-[SequenceFeatureRelationship],[Association]%5E-[SequenceAssociation],[Association]%5E-[PopulationToPopulationAssociation],[Association]%5E-[OrganismalEntityAsAModelOfDiseaseAssociation],[Association]%5E-[OrganismToOrganismAssociation],[Association]%5E-[OrganismTaxonToOrganismTaxonAssociation],[Association]%5E-[OrganismTaxonToEnvironmentAssociation],[Association]%5E-[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation],[Association]%5E-[MolecularActivityToPathwayAssociation],[Association]%5E-[MolecularActivityToMolecularActivityAssociation],[Association]%5E-[MolecularActivityToChemicalEntityAssociation],[Association]%5E-[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[MaterialSampleDerivationAssociation],[Association]%5E-[InformationContentEntityToNamedThingAssociation],[Association]%5E-[GenotypeToVariantAssociation],[Association]%5E-[GenotypeToPhenotypicFeatureAssociation],[Association]%5E-[GenotypeToGenotypePartAssociation],[Association]%5E-[GenotypeToGeneAssociation],[Association]%5E-[GenotypeToDiseaseAssociation],[Association]%5E-[GeneToPhenotypicFeatureAssociation],[Association]%5E-[GeneToPathwayAssociation],[Association]%5E-[GeneToGeneFamilyAssociation],[Association]%5E-[GeneToGeneAssociation],[Association]%5E-[GeneToExpressionSiteAssociation],[Association]%5E-[GeneToDiseaseAssociation],[Association]%5E-[FunctionalAssociation],[Association]%5E-[ExposureEventToPhenotypicFeatureAssociation],[Association]%5E-[ExposureEventToOutcomeAssociation],[Association]%5E-[EntityToPhenotypicFeatureAssociation],[Association]%5E-[EntityToDiseaseAssociation],[Association]%5E-[DrugToGeneAssociation],[Association]%5E-[DiseaseToPhenotypicFeatureAssociation],[Association]%5E-[DiseaseToExposureEventAssociation],[Association]%5E-[DiseaseOrPhenotypicFeatureToLocationAssociation],[Association]%5E-[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation],[Association]%5E-[ContributorAssociation],[Association]%5E-[ChemicalToPathwayAssociation],[Association]%5E-[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[ChemicalToChemicalAssociation],[Association]%5E-[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[ChemicalGeneInteractionAssociation],[Association]%5E-[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation],[Association]%5E-[ChemicalEntityAssessesNamedThingAssociation],[Association]%5E-[ChemicalAffectsGeneAssociation],[Association]%5E-[CellLineToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[CaseToPhenotypicFeatureAssociation],[Association]%5E-[BehaviorToBehavioralFeatureAssociation],[Association]%5E-[AnatomicalEntityToAnatomicalEntityAssociation],[Entity]%5E-[Association],[AnatomicalEntityToAnatomicalEntityAssociation])

---


## Parents

 *  is_a: [Entity](Entity.md) - Root Biolink Model class for all things and informational relationships, real or imagined.

## Children

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
 * [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) - Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.)
 * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
 * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) - A regulatory relationship between two genes
 * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) - describes a physical interaction between a chemical entity and a gene or gene product. Any biological or chemical effect resulting from such an interaction are out of scope, and covered by the ChemicalAffectsGeneAssociation type (e.g. impact of a chemical on the abundance, activity, structure, etc, of either participant in the interaction)
 * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) - This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary undesirable effect.
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway.
 * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
 * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) - An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance.
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) - An association between an exposure event and a disease.
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
 * [DrugToGeneAssociation](DrugToGeneAssociation.md) - An interaction between a drug and a gene or gene product.
 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
 * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and a gene expression site, possibly qualified by stage/timing info.
 * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
 * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) - Set membership of a gene in a family of genes related by common evolutionary ancestry usually inferred by sequence comparisons. The genes in a given family generally share common sequence motifs which generally map onto shared gene product structure-function relationships.
 * [GeneToPathwayAssociation](GeneToPathwayAssociation.md) - An interaction between a gene or gene product and a biological process or pathway.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
 * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) - association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity from which it is derived.
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype.
 * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) - Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
 * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) - Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples
 * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) - Association that holds the relationship between a reaction and the pathway it participates in.
 * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md)
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) - A relationship between two organism taxon nodes
 * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a nucleic acid entity it is localized to.
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToGeneAssociation](VariantToGeneAssociation.md) - An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [aggregator knowledge source](aggregator_knowledge_source.md)  <sub>0..\*</sub>
     * Description: An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
     * Range: [InformationResource](InformationResource.md)
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
 * [has evidence](has_evidence.md)  <sub>0..\*</sub>
     * Description: connects an association to an instance of supporting evidence
     * Range: [EvidenceType](EvidenceType.md)
 * [knowledge source](knowledge_source.md)  <sub>0..1</sub>
     * Description: An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
     * Range: [InformationResource](InformationResource.md)
 * [negated](negated.md)  <sub>0..1</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object category](object_category.md)  <sub>0..1</sub>
     * Description: Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: biolink:Disease The object category of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'biolink:Disease'.
 * [object category closure](object_category_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: ['biolink:Disease", "biolink:NamedThing'] The object category closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all biolink classes that are ancestors of 'biolink:Disease' in the biolink model.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [object closure](object_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['MONDO:0000167', 'MONDO:0005395'] The object closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all diseases that are ancestors of 'breast cancer' in the MONDO ontology.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [object label closure](object_label_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['breast cancer', 'cancer'] The object label closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all labels that are ancestors of 'breast cancer' in the biolink model.
 * [object namespace](object_namespace.md)  <sub>0..1</sub>
     * Description: Used to hold the object namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: MONDO The object namespace of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'MONDO'.
 * [original object](original_object.md)  <sub>0..1</sub>
     * Description: used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [String](types/String.md)
 * [original predicate](original_predicate.md)  <sub>0..1</sub>
     * Description: used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [original subject](original_subject.md)  <sub>0..1</sub>
     * Description: used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [primary knowledge source](primary_knowledge_source.md)  <sub>0..1</sub>
     * Description: The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.
     * Range: [InformationResource](InformationResource.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: One or more publications that report the statement expressed in an  Association, or provide information used as evidence supporting this statement.
     * Range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [retrieval source ids](retrieval_source_ids.md)  <sub>0..\*</sub>
     * Description: A list of retrieval sources that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
     * Range: [RetrievalSource](RetrievalSource.md)
     * in subsets: (translator_minimal)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject category](subject_category.md)  <sub>0..1</sub>
     * Description: Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: biolink:Gene The subject category of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'biolink:Gene'.
 * [subject category closure](subject_category_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: ['biolink:Gene", "biolink:NamedThing'] The subject category closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all biolink classes that are ancestors of 'biolink:Gene' in the biolink model.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [subject closure](subject_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
 * [subject label closure](subject_label_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['BRACA1'] The subject label closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all labels that are ancestors of 'BRCA1' in the biolink model.
 * [subject namespace](subject_namespace.md)  <sub>0..1</sub>
     * Description: Used to hold the subject namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: NCBIGene The subject namespace of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'NCBIGene'.
 * [timepoint](timepoint.md)  <sub>0..1</sub>
     * Description: a point in time
     * Range: [TimeType](types/TimeType.md)

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

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Domain for slot:

 * [aggregator knowledge source](aggregator_knowledge_source.md)  <sub>0..\*</sub>
     * Description: An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.
     * Range: [InformationResource](InformationResource.md)
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
 * [has evidence](has_evidence.md)  <sub>0..\*</sub>
     * Description: connects an association to an instance of supporting evidence
     * Range: [EvidenceType](EvidenceType.md)
 * [knowledge source](knowledge_source.md)  <sub>0..1</sub>
     * Description: An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.
     * Range: [InformationResource](InformationResource.md)
 * [negated](negated.md)  <sub>0..1</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [object category](object_category.md)  <sub>0..1</sub>
     * Description: Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: biolink:Disease The object category of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'biolink:Disease'.
 * [object category closure](object_category_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: ['biolink:Disease", "biolink:NamedThing'] The object category closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all biolink classes that are ancestors of 'biolink:Disease' in the biolink model.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [object closure](object_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['MONDO:0000167', 'MONDO:0005395'] The object closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all diseases that are ancestors of 'breast cancer' in the MONDO ontology.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [object label closure](object_label_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the object label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['breast cancer', 'cancer'] The object label closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all labels that are ancestors of 'breast cancer' in the biolink model.
 * [object namespace](object_namespace.md)  <sub>0..1</sub>
     * Description: Used to hold the object namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: MONDO The object namespace of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'MONDO'.
 * [original object](original_object.md)  <sub>0..1</sub>
     * Description: used to hold the original object of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [String](types/String.md)
 * [original predicate](original_predicate.md)  <sub>0..1</sub>
     * Description: used to hold the original relation/predicate that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [original subject](original_subject.md)  <sub>0..1</sub>
     * Description: used to hold the original subject of a relation (or predicate) that an external knowledge source uses before transformation to match the biolink-model specification.
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [primary knowledge source](primary_knowledge_source.md)  <sub>0..1</sub>
     * Description: The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.
     * Range: [InformationResource](InformationResource.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: One or more publications that report the statement expressed in an  Association, or provide information used as evidence supporting this statement.
     * Range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [subject category](subject_category.md)  <sub>0..1</sub>
     * Description: Used to hold the biolink class/category of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: biolink:Gene The subject category of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'biolink:Gene'.
 * [subject category closure](subject_category_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [OntologyClass](OntologyClass.md)
     * Example: ['biolink:Gene", "biolink:NamedThing'] The subject category closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all biolink classes that are ancestors of 'biolink:Gene' in the biolink model.  Note: typically the "subclass of" and "part of"  relations are used to construct the closure, but other relations may be used as well.
 * [subject closure](subject_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
 * [subject label closure](subject_label_closure.md)  <sub>0..\*</sub>
     * Description: Used to hold the subject label closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: ['BRACA1'] The subject label closure of the association between the gene 'BRCA1' and the disease 'breast cancer' is the set of all labels that are ancestors of 'BRCA1' in the biolink model.
 * [subject namespace](subject_namespace.md)  <sub>0..1</sub>
     * Description: Used to hold the subject namespace of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX.
     * Range: [String](types/String.md)
     * Example: NCBIGene The subject namespace of the association between the gene 'BRCA1' and the disease 'breast cancer' is 'NCBIGene'.

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | This is roughly the model used by biolink and ontobio at the moment |
| **Exact Mappings:** | | OBAN:association |
|  | | rdf:Statement |
|  | | owl:Axiom |

