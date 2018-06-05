# Biolink Model schema


A high level datamodel of biological entities (genes, diseases, phenotypes, pathways, individuals, substances, etc) and their associations.

### Classes

 * [administrative entity](AdministrativeEntity.md)
    * [provider](Provider.md) - person, group, organization or project that provides a piece of information
 * [attribute](Attribute.md) - A property or characteristic of an entity
    * [onset](Onset.md) - The age group in which manifestations appear
    * [frequency value](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
    * [severity value](SeverityValue.md) - describes the severity of a phenotypic feature or disease
    * [zygosity](Zygosity.md)
    * [clinical modifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [biological sex](BiologicalSex.md)
       * [phenotypic sex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
       * [genotypic sex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
 * [named thing](NamedThing.md) - a databased entity or concept/class
    * [information content entity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
       * [confidence level](ConfidenceLevel.md) - Level of confidence in a statement
       * [evidence type](EvidenceType.md) - Class of evidence that supports an association
       * [publication](Publication.md) - Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
       * [association](Association.md) - A typed association between two entities, supported by evidence
          * [sequence feature relationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
             * [exon to transcript relationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
             * [transcript to gene relationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts
             * [gene to gene product relationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
          * [variant to thing association](VariantToThingAssociation.md)
          * [gene to expression site association](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
          * [chemical to pathway association](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
          * [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
          * [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
          * [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
          * [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
          * [chemical to gene association](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
          * [gene to disease association](GeneToDiseaseAssociation.md)
             * [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.md)
             * [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
          * [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
             * [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
          * [cell line to thing association](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
          * [functional association](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
             * [gene to go term association](GeneToGoTermAssociation.md)
             * [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
             * [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
             * [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
          * [gene regulatory relationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
          * [genotype to gene association](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
          * [gene to gene association](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
             * [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.md) - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
             * [gene to gene homology association](GeneToGeneHomologyAssociation.md) - A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
          * [molecular interaction](MolecularInteraction.md) - An interaction at the molecular level between two physical entities
          * [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
          * [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
          * [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
             * [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
             * [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms
          * [genotype to genotype part association](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
          * [case to thing association](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
          * [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
  definitional: true
          * [variant to disease association](VariantToDiseaseAssociation.md)
          * [genomic sequence localization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
          * [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
          * [disease to thing association](DiseaseToThingAssociation.md)
          * [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
          * [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
          * [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
          * [genotype to variant association](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
          * [gene to thing association](GeneToThingAssociation.md)
          * [population to population association](PopulationToPopulationAssociation.md) - An association between a two populations
          * [chemical to thing association](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
          * [variant to population association](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
          * [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
          * [biosample to thing association](BiosampleToThingAssociation.md) - An association between a biosample and something
          * [genotype to thing association](GenotypeToThingAssociation.md)
    * [clinical entity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
       * [clinical intervention](ClinicalIntervention.md)
       * [clinical trial](ClinicalTrial.md)
    * [device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    * [biological entity](BiologicalEntity.md)
       * [biological process or activity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities
          * [molecular activity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.
          * [biological process](BiologicalProcess.md) - One or more causally connected executions of molecular functions
             * [pathway](Pathway.md)
             * [physiological process](PhysiologicalProcess.md)
       * [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
          * [disease](Disease.md)
          * [phenotypic feature](PhenotypicFeature.md)
       * [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
          * [genomic entity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
             * [genome](Genome.md) - A genome is the sum of genetic material within a cell or virion.
             * [sequence variant](SequenceVariant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.
             * [transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase
             * [genotype](Genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
             * [haplotype](Haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
             * [coding sequence](CodingSequence.md)
             * [macromolecular machine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
                * [gene or gene product](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
                   * [gene product](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
                      * [gene product isoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
                      * [RNA product](RnaProduct.md)
                         * [noncoding RNA product](NoncodingRnaProduct.md)
                            * [microRNA](Microrna.md)
                         * [RNA product isoform](RnaProductIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference RNA
                      * [protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
                         * [protein isoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
                   * [gene](Gene.md)
                * [macromolecular complex](MacromolecularComplex.md)
             * [exon](Exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
          * [chemical substance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
             * [drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
             * [metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
          * [gene family](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
       * [environment](Environment.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
          * [drug exposure](DrugExposure.md) - A drug exposure is an intake of a particular chemical substance
          * [treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
       * [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
          * [biosample](Biosample.md)
             * [cell line](CellLine.md)
          * [life stage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
          * [individual organism](IndividualOrganism.md)
             * [case](Case.md) - An individual organism that has a patient role in some clinical context.
          * [anatomical entity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
             * [gross anatomical structure](GrossAnatomicalStructure.md)
             * [cell](Cell.md)
             * [cellular component](CellularComponent.md) - A location in or around a cell
          * [population of individual organisms](PopulationOfIndividualOrganisms.md)
    * [planetary entity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
       * [environmental feature](EnvironmentalFeature.md)
       * [geographic location at time](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
       * [environmental process](EnvironmentalProcess.md)
       * [geographic location](GeographicLocation.md) - a location that can be described in lat/long coordinates
 * [occurrent](Occurrent.md) - A processual entity
    * [phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    * [procedure](Procedure.md) - A series of actions conducted in a certain order or manner
    * [activity and behavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [ontology class](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
    * [organism taxon](OrganismTaxon.md)
    * [gene ontology class](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [relationship type](RelationshipType.md) - An OWL property used as an edge label
### Mixins

 * [entity to disease association](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [frequency quantifier](FrequencyQuantifier.md)
 * [gene grouping](GeneGrouping.md) - any grouping of multiple genes or gene products
 * [gene ontology class](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [model to disease mixin](ModelToDiseaseMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 * [molecular interaction](MolecularInteraction.md) - An interaction at the molecular level between two physical entities
 * [pathognomonicity quantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [relationship quantifier](RelationshipQuantifier.md)
    * [frequency quantifier](FrequencyQuantifier.md)
    * [senstivity quantifier](SenstivityQuantifier.md)
    * [specificity quantifier](SpecificityQuantifier.md)
       * [pathognomonicity quantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [senstivity quantifier](SenstivityQuantifier.md)
 * [specificity quantifier](SpecificityQuantifier.md)
    * [pathognomonicity quantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
 * [variant to thing association](VariantToThingAssociation.md)
### Slots

 * [association slot](association_slot.md) - any slot that relates an association to another entity
    * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
       * [relation](relation.md) - the relationship type by which a subject is connected to an object in an association
    * [edge label](edge_label.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * [stage qualifier](stage_qualifier.md) - stage at which expression takes place
    * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
    * [severity qualifier](severity_qualifier.md) - a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * [onset qualifier](onset_qualifier.md) - a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * [provided by](provided_by.md) - connects an association to the agent (person, organization or group) that provided it
    * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
    * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
    * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
    * [association type](association_type.md) - connects an association to the type of association (e.g. gene to phenotype)
    * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association where the variant
    * [clinical modifier qualifier](clinical_modifier_qualifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [sex qualifier](sex_qualifier.md) - a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * [publications](publications.md) - connects an association to publications supporting the association
    * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
    * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
       * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
 * [drug](drug.md)
 * [object](object.md) - disease
 * [quantifier qualifier](quantifier_qualifier.md) - can be used to indicate magnitude, or also ranking
 * [stage qualifier](stage_qualifier.md) - stage at which the gene is expressed in the site
 * [relation](relation.md) - The relationship to the disease
 * [subject](subject.md) - The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
 * [interacting molecules category](interacting_molecules_category.md)
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
    * [filler](filler.md) - The value in a property-value tuple
    * [full name](full_name.md) - a long-form human readable name for a thing
    * [has zygosity](has_zygosity.md)
    * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
       * [has biological sequence](has_biological_sequence.md) - connects a genomic feature to its sequence
    * [timepoint](timepoint.md) - a point in time
    * [interbase coordinate](interbase_coordinate.md) - TODO
       * [end interbase coordinate](end_interbase_coordinate.md)
       * [start interbase coordinate](start_interbase_coordinate.md)
    * [latitude](latitude.md) - latitude
    * [iri](iri.md) *subsets: translator_minimal* - An IRI for the node. This is determined by the id using expansion rules.
    * [aggregate statistic](aggregate_statistic.md)
       * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
       * [has count](has_count.md) - number of things with a particular property
       * [has total](has_total.md) - total number of things in a particular reference set
       * [has quotient](has_quotient.md)
    * [phase](phase.md) - TODO
    * [description](description.md) *subsets: translator_minimal* - a human-readable description of a thing
       * [description](description.md) *subsets: translator_minimal* - a human-readable description of a thing
    * [genome build](genome_build.md) - TODO
    * [category](category.md) *subsets: translator_minimal* - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * [id](id.md) *subsets: translator_minimal* - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
       * [id](id.md) *subsets: translator_minimal* - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * [systematic synonym](systematic_synonym.md) - more commonly used for gene symbols in yeast
    * [update date](update_date.md) - date on which thing was updated. This can be applied to nodes or edges
    * [has gene](has_gene.md) - connects and entity to a single gene
    * [creation date](creation_date.md) - date on which thing was created. This can be applied to nodes or edges
    * [longitude](longitude.md) - longitude
    * [name](name.md) *subsets: translator_minimal* - A human-readable name for a thing
       * [name](name.md) *subsets: translator_minimal* - A human-readable name for a thing
    * [has chemical formula](has_chemical_formula.md) - description of chemical compound based on element symbols
 * [related to](related_to.md) - A grouping for any relationship type that holds between any two things
    * [precedes](precedes.md) *subsets: translator_minimal* - holds between two processes, where one completes before the other begins
    * [affects risk for](affects_risk_for.md) *subsets: translator_minimal* - holds between two entities where exposure to one entity alters the chance of developing the other
       * [prevents](prevents.md) *subsets: translator_minimal* - holds between an entity whose application or use reduces the likelihood of a potential outcome.  Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
       * [predisposes](predisposes.md) *subsets: translator_minimal* - holds between two entities where exposure to one entity increases the chance of developing the other
    * [has participant](has_participant.md) *subsets: translator_minimal* - holds between a process and a continuant, where the continuant is somehow involved in the process
       * [has input](has_input.md) *subsets: translator_minimal* - holds between a process and a continuant, where the continuant is an input into the process
    * [overlaps](overlaps.md) *subsets: translator_minimal* - holds between entties that overlap in their extents (materials or processes)
       * [part of](part_of.md) *subsets: translator_minimal* - holds between parts and wholes (material entities or processes)
       * [has part](has_part.md) *subsets: translator_minimal* - holds between wholes and their parts (material entities or processes)
    * [interacts with](interacts_with.md) *subsets: translator_minimal* - holds between any two entities that directly or indirectly interact with each other
       * [physically interacts with](physically_interacts_with.md) *subsets: translator_minimal* - holds between two entities that make physical contact as part of some interaction
          * [molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*
       * [genetically interacts with](genetically_interacts_with.md) *subsets: translator_minimal* - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    * [participates in](participates_in.md) *subsets: translator_minimal* - holds between a continuant and a process, where the continuant is somehow involved in the process
       * [actively involved in](actively_involved_in.md) *subsets: translator_minimal* - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
          * [capable of](capable_of.md) *subsets: translator_minimal* - holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.
    * [affects](affects.md) *subsets: translator_minimal* - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
       * [disrupts](disrupts.md) *subsets: translator_minimal* - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
       * [treats](treats.md) *subsets: translator_minimal* - holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
       * [regulates](regulates.md)
          * [regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*
             * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md) *subsets: translator_minimal*
             * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md) *subsets: translator_minimal*
          * [regulates, process to process](regulates_process_to_process.md)
             * [positively regulates, process to process](positively_regulates_process_to_process.md)
             * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
          * [negatively regulates](negatively_regulates.md)
          * [positively regulates](positively_regulates.md)
    * [model of](model_of.md) *subsets: translator_minimal* - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.
    * [treated by](treated_by.md) *subsets: translator_minimal* - holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
    * [homologous to](homologous_to.md) *subsets: translator_minimal* - holds between two biological entities that have common evolutionary origin
       * [orthologous to](orthologous_to.md) *subsets: translator_minimal* - a homology relationship between entities (typically genes) that diverged after a speciation event.
       * [paralogous to](paralogous_to.md) *subsets: translator_minimal* - a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
       * [xenologous to](xenologous_to.md) *subsets: translator_minimal* - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
    * [expresses](expresses.md) *subsets: translator_minimal* - holds between an anatomical entity and gene or gene product that is expressed there
    * [in taxon](in_taxon.md) *subsets: translator_minimal* - connects a thing to a class representing a taxon
    * [has gene product](has_gene_product.md) *subsets: translator_minimal* - holds between a gene and a transcribed and/or translated product generated from it
    * [gene associated with condition](gene_associated_with_condition.md) *subsets: translator_minimal* - holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * [expressed in](expressed_in.md) *subsets: translator_minimal* - holds between a gene or gene product and an anatomical entity in which it is expressed
    * [has molecular consequence](has_molecular_consequence.md) - connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
    * [subclass of](subclass_of.md) *subsets: translator_minimal* - holds between two classes where the domain class is a specialization of the range class
    * [derives into](derives_into.md) *subsets: translator_minimal* - holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [manifestation of](manifestation_of.md) *subsets: translator_minimal* - used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
    * [correlated with](correlated_with.md) *subsets: translator_minimal* - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * [has biomarker](has_biomarker.md) *subsets: translator_minimal* - holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
       * [biomarker for](biomarker_for.md) *subsets: translator_minimal* - holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * [contributes to](contributes_to.md) *subsets: translator_minimal* - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
       * [causes](causes.md) *subsets: translator_minimal* - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
    * [occurs in](occurs_in.md) *subsets: translator_minimal* - holds between a process and a material entity or site within which the process occurs
    * [same as](same_as.md) *subsets: translator_minimal* - holds between two entities that are considered equivalent to each other
    * [coexists with](coexists_with.md) *subsets: translator_minimal* - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
       * [in pathway with](in_pathway_with.md) *subsets: translator_minimal* - holds between two genes or gene products that are part of in the same biological pathway
       * [co-localizes with](co-localizes_with.md) *subsets: translator_minimal* - holds between two entities that are observed to be located in the same place.
       * [in complex with](in_complex_with.md) *subsets: translator_minimal* - holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
       * [in cell population with](in_cell_population_with.md) *subsets: translator_minimal* - holds between two genes or gene products that are expressed in the same cell type or population
    * [derives from](derives_from.md) *subsets: translator_minimal* - holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [produces](produces.md) *subsets: translator_minimal* - holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
    * [location of](location_of.md) *subsets: translator_minimal* - holds between material entity or site and a material entity that is located within it (but not considered a part of it)
    * [has phenotype](has_phenotype.md) *subsets: translator_minimal* - holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * [located in](located_in.md) *subsets: translator_minimal* - holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
 * [has gene](has_gene.md) - Each allele can be associated with any number of genes
 * [has exposure parts](has_exposure_parts.md)
 * [treats](treats.md)
 * [has count](has_count.md) - number in object population that carry a particular allele, aka allele count
 * [has quotient](has_quotient.md) - frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
 * [has total](has_total.md) - number all populations that carry a particular allele, aka allele number
### Types

#### Built in

 * **boolean**
 * **date**
 * **double**
 * **float**
 * **integer**
 * **string**
 * **time**
#### Defined

 * [biological sequence](BiologicalSequence.md) (**string**)
 * [chemical formula type](ChemicalFormulaType.md) (**string**)
 * [chemical formula value](ChemicalFormulaValue.md) (**string**)
 * [evidence instance](EvidenceInstance.md) (**string**)
 * [frequency value](FrequencyValue.md) (**string**)
 * [identifier type](IdentifierType.md) (**string**) - A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form
 * [iri type](IriType.md) (**string**) - An IRI
 * [label type](LabelType.md) (**string**) - A string that provides a human-readable name for a thing
 * [narrative text](NarrativeText.md) (**string**) - A string that provides a human-readable description of something
 * [perecentage frequency value](PerecentageFrequencyValue.md) (**double**)
 * [phenotype](Phenotype.md) (**string**)
 * [quotient](Quotient.md) (**double**)
 * [symbol type](SymbolType.md) (**string**)
 * [time type](TimeType.md) (**time**)
 * [unit](Unit.md) (**string**)
