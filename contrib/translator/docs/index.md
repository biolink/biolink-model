# Translator Biolink Mixins schema


Monarch specific extensions

### Classes

 * [AdministrativeEntity](AdministrativeEntity.md)
    * [Provider](Provider.md) - person, group, organization or project that provides a piece of information
 * [Association](Association.md) - A typed association between two entities, supported by evidence
    * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
       * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
       * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
    * [BiosampleToDiseaseOrPhenotypicFeatureAssociation](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
    * [BiosampleToThingAssociation](BiosampleToThingAssociation.md) - An association between a biosample and something
    * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
    * [CaseToThingAssociation](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
    * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
    * [CellLineToThingAssociation](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
    * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
    * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
    * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
    * [ChemicalToThingAssociation](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
    * [DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
       * [DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
    * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    * [DiseaseToThingAssociation](DiseaseToThingAssociation.md)
    * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
    * [EnvironmentToPhenotypicFeatureAssociation](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
    * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
       * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
       * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
       * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
       * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
    * [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
    * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
       * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)
       * [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)
    * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
    * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
       * [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
       * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
    * [GeneToThingAssociation](GeneToThingAssociation.md)
    * [GenomicSequenceLocalization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
    * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
    * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    * [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
    * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
    * [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities
    * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
    * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
       * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
       * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
       * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts
    * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
    * [ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
    * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
    * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
    * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
    * [VariantToThingAssociation](VariantToThingAssociation.md)
 * [Attribute](Attribute.md) - A property or characteristic of an entity
    * [BiologicalSex](BiologicalSex.md)
       * [GenotypicSex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
       * [PhenotypicSex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
    * [Onset](Onset.md) - The age group in which manifestations appear
    * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
    * [Zygosity](Zygosity.md)
 * [NamedThing](NamedThing.md) - a databased entity or concept/class
    * [BiologicalEntity](BiologicalEntity.md)
       * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities
          * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
             * [Pathway](Pathway.md)
             * [PhysiologicalProcess](PhysiologicalProcess.md)
          * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.
       * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
          * [Disease](Disease.md)
          * [PhenotypicFeature](PhenotypicFeature.md)
       * [Environment](Environment.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
          * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular chemical substance
          * [Treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
       * [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
          * [ChemicalSubstance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
             * [Drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
             * [Metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
          * [GeneFamily](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
          * [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
             * [CodingSequence](CodingSequence.md)
             * [Exon](Exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
             * [Genome](Genome.md) - A genome is the sum of genetic material within a cell or virion.
             * [Genotype](Genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
             * [Haplotype](Haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
             * [MacromolecularMachine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
                * [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
                   * [Gene](Gene.md)
                   * [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
                      * [RNAProduct](RNAProduct.md)
                         * [RNAProductIsoform](RNAProductIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference RNA
                         * [NoncodingRNAProduct](NoncodingRNAProduct.md)
                            * [MicroRNA](MicroRNA.md)
                      * [GeneProductIsoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
                      * [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
                         * [ProteinIsoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
                * [MacromolecularComplex](MacromolecularComplex.md)
             * [SequenceVariant](SequenceVariant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.
             * [Transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase
       * [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
          * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
             * [Cell](Cell.md)
             * [CellularComponent](CellularComponent.md) - A location in or around a cell
             * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
          * [Biosample](Biosample.md)
             * [CellLine](CellLine.md)
          * [IndividualOrganism](IndividualOrganism.md)
             * [Case](Case.md) - An individual organism that has a patient role in some clinical context.
          * [LifeStage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
          * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
    * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
       * [ClinicalIntervention](ClinicalIntervention.md)
       * [ClinicalTrial](ClinicalTrial.md)
    * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
       * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
       * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
       * [NamedGraph](NamedGraph.md)
       * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
    * [Occurrent](Occurrent.md) - A processual entity
       * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
       * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
       * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
    * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
       * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
       * [OrganismTaxon](OrganismTaxon.md)
       * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
    * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
       * [EnvironmentalFeature](EnvironmentalFeature.md)
       * [EnvironmentalProcess](EnvironmentalProcess.md)
       * [GeographicLocation](GeographicLocation.md) - a location that can be described in lat/long coordinates
          * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
### Mixins

 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations
    * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [FrequencyQualifier](FrequencyQualifier.md) - Qualifier for freqency type associations
    * [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations
       * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [FrequencyQuantifier](FrequencyQuantifier.md)
 * [GeneGrouping](GeneGrouping.md) - any grouping of multiple genes or gene products
 * [ModelToDiseaseMixin](ModelToDiseaseMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 * [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities
 * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [RelationshipQuantifier](RelationshipQuantifier.md)
    * [FrequencyQuantifier](FrequencyQuantifier.md)
    * [SenstivityQuantifier](SenstivityQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
       * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [SenstivityQuantifier](SenstivityQuantifier.md)
 * [SpecificityQuantifier](SpecificityQuantifier.md)
    * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
 * [VariantToThingAssociation](VariantToThingAssociation.md)
### Slots

 * [association slot](association_slot.md) - any slot that relates an association to another entity
    * [association type](association_type.md) - connects an association to the type of association (e.g. gene to phenotype)
    * [clinical modifier qualifier](clinical_modifier_qualifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [edge label](edge_label.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes. 
    * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
    * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
    * [has evidence graph](has_evidence_graph.md) - connects an association to a graph object including a path from subject to object
    * [has evidence object](has_evidence_object.md) - connects an association to an supporting entity. May be a gene/product (if evidence is homology or protein interaction). Same as WITH/FROM column in GO/GAFs
    * [has evidence type](has_evidence_type.md) - connects an association to the class of evidence used
    * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
    * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [anatomical entity to anatomical entity association.object](anatomical_entity_to_anatomical_entity_association_object.md)
          * [anatomical entity to anatomical entity ontogenic association.object](anatomical_entity_to_anatomical_entity_ontogenic_association_object.md) - the structure at an earlier time
          * [anatomical entity to anatomical entity part of association.object](anatomical_entity_to_anatomical_entity_part_of_association_object.md) - the whole
       * [chemical to disease or phenotypic feature association.object](chemical_to_disease_or_phenotypic_feature_association_object.md) - the disease or phenotype that is affected by the chemical
       * [chemical to gene association.object](chemical_to_gene_association_object.md) - the gene or gene product that is affected by the chemical
       * [chemical to pathway association.object](chemical_to_pathway_association_object.md) - the pathway that is affected by the chemical
       * [disease or phenotypic feature association to location association.object](disease_or_phenotypic_feature_association_to_location_association_object.md) - anatomical entity in which the disease or feature is found
       * [entity to disease association.object](entity_to_disease_association_object.md) - disease
       * [entity to phenotypic feature association.object](entity_to_phenotypic_feature_association_object.md) - phenotypic class
       * [functional association.object](functional_association_object.md) - class describing the activity, process or localization of the gene product
          * [gene to go term association.object](gene_to_go_term_association_object.md)
          * [macromolecular machine to biological process association.object](macromolecular_machine_to_biological_process_association_object.md)
          * [macromolecular machine to cellular component association.object](macromolecular_machine_to_cellular_component_association_object.md)
          * [macromolecular machine to molecular activity association.object](macromolecular_machine_to_molecular_activity_association_object.md)
       * [gene regulatory relationship.object](gene_regulatory_relationship_object.md)
       * [gene to expression site association.object](gene_to_expression_site_association_object.md) - location in which the gene is expressed
       * [gene to gene association.object](gene_to_gene_association_object.md) - the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
       * [genomic sequence localization.object](genomic_sequence_localization_object.md)
       * [genotype to gene association.object](genotype_to_gene_association_object.md) - gene implicated in genotype
       * [genotype to genotype part association.object](genotype_to_genotype_part_association_object.md) - child genotype
       * [genotype to variant association.object](genotype_to_variant_association_object.md) - gene implicated in genotype
       * [pairwise interaction association.object](pairwise_interaction_association_object.md)
       * [population to population association.object](population_to_population_association_object.md) - the population that form the object of the association
       * [sequence feature relationship.object](sequence_feature_relationship_object.md)
          * [exon to transcript relationship.object](exon_to_transcript_relationship_object.md)
          * [gene to gene product relationship.object](gene_to_gene_product_relationship_object.md)
          * [transcript to gene relationship.object](transcript_to_gene_relationship_object.md)
       * [sequence variant modulates treatment association.object](sequence_variant_modulates_treatment_association_object.md) - treatment whose efficacy is modulated by the subject variant
       * [thing to disease or phenotypic feature association.object](thing_to_disease_or_phenotypic_feature_association_object.md) - disease or phenotype
       * [variant to disease association.object](variant_to_disease_association_object.md) - a disease that is associated with that variant
       * [variant to population association.object](variant_to_population_association_object.md) - the population that is observed to have the frequency
    * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * [provided by](provided_by.md) - connects an association to the agent (person, organization or group) that provided it
    * [publications](publications.md) - connects an association to publications supporting the association
    * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
    * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
       * [gene to expression site association.quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md) - can be used to indicate magnitude, or also ranking
    * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [anatomical entity to anatomical entity ontogenic association.relation](anatomical_entity_to_anatomical_entity_ontogenic_association_relation.md)
       * [anatomical entity to anatomical entity part of association.relation](anatomical_entity_to_anatomical_entity_part_of_association_relation.md)
       * [gene regulatory relationship.relation](gene_regulatory_relationship_relation.md) - the direction is always from regulator to regulated
       * [gene to expression site association.relation](gene_to_expression_site_association_relation.md) - expression relationship
       * [gene to gene homology association.relation](gene_to_gene_homology_association_relation.md) - homology relationship type
       * [gene to gene product relationship.relation](gene_to_gene_product_relationship_relation.md)
       * [genotype to gene association.relation](genotype_to_gene_association_relation.md) - the relationship type used to connect genotype to gene
       * [genotype to genotype part association.relation](genotype_to_genotype_part_association_relation.md)
       * [genotype to phenotypic feature association.relation](genotype_to_phenotypic_feature_association_relation.md)
       * [genotype to variant association.relation](genotype_to_variant_association_relation.md) - the relationship type used to connect genotype to gene
       * [model to disease mixin.relation](model_to_disease_mixin_relation.md) - The relationship to the disease
       * [pairwise interaction association.relation](pairwise_interaction_association_relation.md) - interaction relationship type
          * [pairwise gene to gene interaction.relation](pairwise_gene_to_gene_interaction_relation.md)
       * [population to population association.relation](population_to_population_association_relation.md) - A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used
       * [variant to disease association.relation](variant_to_disease_association_relation.md) - E.g. is pathogenic for
    * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association where the variant
    * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * [stage qualifier](stage_qualifier.md) - stage at which expression takes place
       * [gene to expression site association.stage qualifier](gene_to_expression_site_association_stage_qualifier.md) - stage at which the gene is expressed in the site
    * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [anatomical entity to anatomical entity association.subject](anatomical_entity_to_anatomical_entity_association_subject.md)
          * [anatomical entity to anatomical entity ontogenic association.subject](anatomical_entity_to_anatomical_entity_ontogenic_association_subject.md) - the structure at a later time
          * [anatomical entity to anatomical entity part of association.subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md) - the part
       * [biosample to thing association.subject](biosample_to_thing_association_subject.md) - the biosample being described
       * [case to thing association.subject](case_to_thing_association_subject.md) - the case (e.g. patient) that has the property
       * [cell line to disease or phenotypic feature association.subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)
       * [cell line to thing association.subject](cell_line_to_thing_association_subject.md)
       * [chemical to thing association.subject](chemical_to_thing_association_subject.md) - the chemical substance or entity that is an interactor
       * [disease or phenotypic feature association to thing association.subject](disease_or_phenotypic_feature_association_to_thing_association_subject.md) - disease or phenotype
       * [disease to thing association.subject](disease_to_thing_association_subject.md) - disease class
       * [environment to phenotypic feature association.subject](environment_to_phenotypic_feature_association_subject.md)
       * [functional association.subject](functional_association_subject.md) - gene, product or macromolecular complex that has the function associated with the GO term
          * [gene to go term association.subject](gene_to_go_term_association_subject.md)
       * [gene regulatory relationship.subject](gene_regulatory_relationship_subject.md)
       * [gene to disease association.subject](gene_to_disease_association_subject.md) - gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model
          * [gene as a model of disease association.subject](gene_as_a_model_of_disease_association_subject.md) - A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
          * [gene has variant that contributes to disease association.subject](gene_has_variant_that_contributes_to_disease_association_subject.md) - A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
       * [gene to expression site association.subject](gene_to_expression_site_association_subject.md) - gene in which variation is correlated with the phenotypic feature
       * [gene to gene association.subject](gene_to_gene_association_subject.md) - the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
       * [gene to phenotypic feature association.subject](gene_to_phenotypic_feature_association_subject.md) - gene in which variation is correlated with the phenotypic feature
       * [gene to thing association.subject](gene_to_thing_association_subject.md) - gene that is the subject of the association
       * [genomic sequence localization.subject](genomic_sequence_localization_subject.md)
       * [genotype to gene association.subject](genotype_to_gene_association_subject.md) - parent genotype
       * [genotype to genotype part association.subject](genotype_to_genotype_part_association_subject.md) - parent genotype
       * [genotype to phenotypic feature association.subject](genotype_to_phenotypic_feature_association_subject.md) - genotype that is associated with the phenotypic feature
       * [genotype to thing association.subject](genotype_to_thing_association_subject.md) - genotype that is the subject of the association
       * [genotype to variant association.subject](genotype_to_variant_association_subject.md) - parent genotype
       * [model to disease mixin.subject](model_to_disease_mixin_subject.md) - The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
       * [pairwise interaction association.subject](pairwise_interaction_association_subject.md)
       * [population to population association.subject](population_to_population_association_subject.md) - the population that form the subject of the association
       * [sequence feature relationship.subject](sequence_feature_relationship_subject.md)
          * [exon to transcript relationship.subject](exon_to_transcript_relationship_subject.md)
          * [gene to gene product relationship.subject](gene_to_gene_product_relationship_subject.md)
          * [transcript to gene relationship.subject](transcript_to_gene_relationship_subject.md)
       * [sequence variant modulates treatment association.subject](sequence_variant_modulates_treatment_association_subject.md) - variant that modulates the treatment of some disease
       * [variant to disease association.subject](variant_to_disease_association_subject.md) - a sequence variant in which the allele state is associated in some way with the disease state
       * [variant to phenotypic feature association.subject](variant_to_phenotypic_feature_association_subject.md) - a sequence variant in which the allele state is associated in some way with the phenotype state
       * [variant to population association.subject](variant_to_population_association_subject.md) - an allele that has a certain frequency in a given population
       * [variant to thing association.subject](variant_to_thing_association_subject.md) - a sequence variant in which the allele state is associated with some other entity
 * [drug exposure.drug](drug.md)
 * [treatment.has exposure parts](has_exposure_parts.md)
 * [pairwise interaction association.interacting molecules category](interacting_molecules_category.md)
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
    * [aggregate statistic](aggregate_statistic.md)
       * [has count](has_count.md) - number of things with a particular property
          * [variant to population association.has count](variant_to_population_association_has_count.md) - number in object population that carry a particular allele, aka allele count
       * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
       * [has quotient](has_quotient.md)
          * [variant to population association.has quotient](variant_to_population_association_has_quotient.md) - frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
       * [has total](has_total.md) - total number of things in a particular reference set
          * [variant to population association.has total](variant_to_population_association_has_total.md) - number all populations that carry a particular allele, aka allele number
    * [association.id](association_id.md) *subsets*: (translator_minimal) - A unique identifier for an association
       * [pairwise interaction association.id](pairwise_interaction_association_id.md) *subsets*: (translator_minimal) - identifier for the interaction. This may come from an interaction database such as IMEX.
    * [category](category.md) *subsets*: (translator_minimal) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * [creation date](creation_date.md) - date on which thing was created. This can be applied to nodes or edges
    * [description](description.md) *subsets*: (translator_minimal) - a human-readable description of a thing
       * [entity to phenotypic feature association.description](entity_to_phenotypic_feature_association_description.md) *subsets*: (translator_minimal) - A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * [filler](filler.md) - The value in a property-value tuple
    * [full name](full_name.md) - a long-form human readable name for a thing
    * [genome build](genome_build.md) - TODO
    * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
       * [sequence variant.has biological sequence](sequence_variant_has_biological_sequence.md) - The state of the sequence w.r.t a reference sequence
    * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
    * [has gene](has_gene.md) - connects and entity to a single gene
       * [sequence variant.has gene](sequence_variant_has_gene.md) - Each allele can be associated with any number of genes
    * [has zygosity](has_zygosity.md)
    * [id](id.md) *subsets*: (translator_minimal) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
       * [sequence variant.id](sequence_variant_id.md) *subsets*: (translator_minimal)
    * [interbase coordinate](interbase_coordinate.md) - TODO
       * [end interbase coordinate](end_interbase_coordinate.md)
       * [start interbase coordinate](start_interbase_coordinate.md)
    * [iri](iri.md) *subsets*: (translator_minimal) - An IRI for the node. This is determined by the id using expansion rules.
    * [latitude](latitude.md) - latitude
    * [longitude](longitude.md) - longitude
    * [name](name.md) *subsets*: (translator_minimal) - A human-readable name for a thing
       * [macromolecular machine.name](macromolecular_machine_name.md) *subsets*: (translator_minimal) - genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * [phase](phase.md) - TODO
    * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
    * [timepoint](timepoint.md) - a point in time
    * [update date](update_date.md) - date on which thing was updated. This can be applied to nodes or edges
 * [object taxon](object_taxon.md) - the taxonomic class of the entity in the object slot
 * [object taxon label](object_taxon_label.md)
 * [related to](related_to.md) - A grouping for any relationship type that holds between any two things
    * [affects](affects.md) *subsets*: (translator_minimal) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
       * [affects abundance of](affects_abundance_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
          * [decreases abundance of](decreases_abundance_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
          * [increases abundance of](increases_abundance_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
       * [affects activity of](affects_activity_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
          * [decreases activity of](decreases_activity_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
          * [increases activity of](increases_activity_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
       * [affects degradation of](affects_degradation_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
          * [decreases degradation of](decreases_degradation_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
          * [increases degradation of](increases_degradation_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
       * [affects expression of](affects_expression_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
          * [decreases expression of](decreases_expression_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
          * [increases expression of](increases_expression_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
       * [affects folding of](affects_folding_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other 
          * [decreases folding of](decreases_folding_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other 
          * [increases folding of](increases_folding_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other 
       * [affects localization of](affects_localization_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
          * [decreases localization of](decreases_localization_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
          * [increases localization of](increases_localization_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
       * [affects metabolic processing of](affects_metabolic_processing_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
          * [decreases metabolic processing of](decreases_metabolic_processing_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
          * [increases metabolic processing of](increases_metabolic_processing_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
       * [affects molecular modification of](affects_molecular_modification_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
          * [decreases molecular modification of](decreases_molecular_modification_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
          * [increases molecular modification of](increases_molecular_modification_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
       * [affects mutation rate of](affects_mutation_rate_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
          * [decreases mutation rate of](decreases_mutation_rate_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
          * [increases mutation rate of](increases_mutation_rate_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
       * [affects response to](affects_response_to.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
          * [decreases response to](decreases_response_to.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
          * [increases response to](increases_response_to.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
       * [affects secretion of](affects_secretion_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
          * [decreases secretion of](decreases_secretion_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
          * [increases secretion of](increases_secretion_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
       * [affects splicing of](affects_splicing_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
          * [decreases splicing of](decreases_splicing_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
          * [increases splicing of](increases_splicing_of.md) *subsets*: (translator_minimal) - holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
       * [affects stability of](affects_stability_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
          * [decreases stability of](decreases_stability_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
          * [increases stability of](increases_stability_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
       * [affects synthesis of](affects_synthesis_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
          * [decreases synthesis of](decreases_synthesis_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
          * [increases synthesis of](increases_synthesis_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
       * [affects transport of](affects_transport_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
          * [decreases transport of](decreases_transport_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
          * [increases transport of](increases_transport_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
       * [affects uptake of](affects_uptake_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
          * [decreases uptake of](decreases_uptake_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
          * [increases uptake of](increases_uptake_of.md) *subsets*: (translator_minimal) - holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
       * [disrupts](disrupts.md) *subsets*: (translator_minimal) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
       * [regulates](regulates.md) *subsets*: (translator_minimal)
          * [negatively regulates](negatively_regulates.md) *subsets*: (translator_minimal)
          * [positively regulates](positively_regulates.md) *subsets*: (translator_minimal)
          * [regulates, entity to entity](regulates_entity_to_entity.md) *subsets*: (translator_minimal)
             * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md) *subsets*: (translator_minimal)
             * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md) *subsets*: (translator_minimal)
          * [regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)
             * [negatively regulates, process to process](negatively_regulates_process_to_process.md) *subsets*: (translator_minimal)
             * [positively regulates, process to process](positively_regulates_process_to_process.md) *subsets*: (translator_minimal)
       * [treats](treats.md) *subsets*: (translator_minimal) - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
    * [affects risk for](affects_risk_for.md) *subsets*: (translator_minimal) - holds between two entities where exposure to one entity alters the chance of developing the other 
       * [predisposes](predisposes.md) *subsets*: (translator_minimal) - holds between two entities where exposure to one entity increases the chance of developing the other 
       * [prevents](prevents.md) *subsets*: (translator_minimal) - holds between an entity whose application or use reduces the likelihood of a potential outcome.  Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
    * [coexists with](coexists_with.md) *subsets*: (translator_minimal) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
       * [co-localizes with](co-localizes_with.md) *subsets*: (translator_minimal) - holds between two entities that are observed to be located in the same place.
       * [in cell population with](in_cell_population_with.md) *subsets*: (translator_minimal) - holds between two genes or gene products that are expressed in the same cell type or population 
       * [in complex with](in_complex_with.md) *subsets*: (translator_minimal) - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
       * [in pathway with](in_pathway_with.md) *subsets*: (translator_minimal) - holds between two genes or gene products that are part of in the same biological pathway
    * [contributes to](contributes_to.md) *subsets*: (translator_minimal) - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
       * [causes](causes.md) *subsets*: (translator_minimal) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
    * [correlated with](correlated_with.md) *subsets*: (translator_minimal) - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * [biomarker for](biomarker_for.md) *subsets*: (translator_minimal) - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
       * [has biomarker](has_biomarker.md) *subsets*: (translator_minimal)
    * [derives from](derives_from.md) *subsets*: (translator_minimal) - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [derives into](derives_into.md) *subsets*: (translator_minimal) - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [expressed in](expressed_in.md) *subsets*: (translator_minimal) - holds between a gene or gene product and an anatomical entity in which it is expressed
    * [expresses](expresses.md) *subsets*: (translator_minimal) - holds between an anatomical entity and gene or gene product that is expressed there
    * [gene associated with condition](gene_associated_with_condition.md) *subsets*: (translator_minimal) - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * [has gene product](has_gene_product.md) *subsets*: (translator_minimal) - holds between a gene and a transcribed and/or translated product generated from it
    * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
    * [has participant](has_participant.md) *subsets*: (translator_minimal) - holds between a process and a continuant, where the continuant is somehow involved in the process 
       * [has input](has_input.md) *subsets*: (translator_minimal) - holds between a process and a continuant, where the continuant is an input into the process
    * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal) - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * [homologous to](homologous_to.md) *subsets*: (translator_minimal) - holds between two biological entities that have common evolutionary origin
       * [orthologous to](orthologous_to.md) *subsets*: (translator_minimal) - a homology relationship between entities (typically genes) that diverged after a speciation event.
       * [paralogous to](paralogous_to.md) *subsets*: (translator_minimal) - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
       * [xenologous to](xenologous_to.md) *subsets*: (translator_minimal) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
    * [in taxon](in_taxon.md) *subsets*: (translator_minimal) - connects a thing to a class representing a taxon
    * [interacts with](interacts_with.md) *subsets*: (translator_minimal) - holds between any two entities that directly or indirectly interact with each other
       * [genetically interacts with](genetically_interacts_with.md) *subsets*: (translator_minimal) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
       * [physically interacts with](physically_interacts_with.md) *subsets*: (translator_minimal) - holds between two entities that make physical contact as part of some interaction
          * [molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)
    * [located in](located_in.md) *subsets*: (translator_minimal) - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
    * [location of](location_of.md) *subsets*: (translator_minimal) - holds between material entity or site and a material entity that is located within it (but not considered a part of it) 
    * [manifestation of](manifestation_of.md) *subsets*: (translator_minimal) - used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
    * [model of](model_of.md) *subsets*: (translator_minimal) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.    
    * [occurs in](occurs_in.md) *subsets*: (translator_minimal) - holds between a process and a material entity or site within which the process occurs
    * [overlaps](overlaps.md) *subsets*: (translator_minimal) - holds between entties that overlap in their extents (materials or processes)
       * [has part](has_part.md) *subsets*: (translator_minimal) - holds between wholes and their parts (material entities or processes)
       * [part of](part_of.md) *subsets*: (translator_minimal) - holds between parts and wholes (material entities or processes)
    * [participates in](participates_in.md) *subsets*: (translator_minimal) - holds between a continuant and a process, where the continuant is somehow involved in the process
       * [actively involved in](actively_involved_in.md) *subsets*: (translator_minimal) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
          * [capable of](capable_of.md) *subsets*: (translator_minimal) - holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function. 
    * [precedes](precedes.md) *subsets*: (translator_minimal) - holds between two processes, where one completes before the other begins
    * [produces](produces.md) *subsets*: (translator_minimal) - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
    * [same as](same_as.md) *subsets*: (translator_minimal) - holds between two entities that are considered equivalent to each other
    * [subclass of](subclass_of.md) *subsets*: (translator_minimal) - holds between two classes where the domain class is a specialization of the range class
    * [treated by](treated_by.md) *subsets*: (translator_minimal) - holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
 * [subject taxon](subject_taxon.md) - the taxonomic class of the entity in the object slot
 * [subject taxon label](subject_taxon_label.md)
 * [title](title.md) - Narrative text describing the entity
    * [named graph.title](named_graph_title.md) - descriptive textual title
 * [uri](uri.md) - URI expansion of CURIE
### Types

#### Built in

 * **anytype**
 * **boolean**
 * **date**
 * **double**
 * **float**
 * **integer**
 * **string**
 * **time**
 * **uri**
#### Defined

 * [BiologicalSequence](BiologicalSequence.md)  (**string**) 
 * [ChemicalFormulaType](ChemicalFormulaType.md)  (**string**) 
 * [ChemicalFormulaValue](ChemicalFormulaValue.md)  (**string**) 
 * [EvidenceInstance](EvidenceInstance.md)  (**string**) 
 * [FrequencyValue](FrequencyValue.md)  (**string**) 
 * [IdentifierType](IdentifierType.md)  (**string**)  - A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form
 * [IriType](IriType.md)  (**string**)  - An IRI
 * [LabelType](LabelType.md)  (**string**)  - A string that provides a human-readable name for a thing
 * [NarrativeText](NarrativeText.md)  (**string**)  - A string that provides a human-readable description of something
 * [PerecentageFrequencyValue](PerecentageFrequencyValue.md)  (**double**) 
 * [Phenotype](Phenotype.md)  (**string**) 
 * [Quotient](Quotient.md)  (**double**) 
 * [SymbolType](SymbolType.md)  (**string**) 
 * [TimeType](TimeType.md)  (**time**) 
 * [Unit](Unit.md)  (**string**) 
