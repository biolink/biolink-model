None
ayout: default
---

## biolink model


Entity and association taxonomy and datamodel for life-sciences data

<a name="classes"/>
### Classes

 * [relationship type](RelationshipType.html)
 * [named thing](NamedThing.html)
    * [biological entity](BiologicalEntity.html)
       * [organismal entity](OrganismalEntity.html)
          * [individual organism](IndividualOrganism.html)
             * [case](Case.html)
          * [population of individual organisms](PopulationOfIndividualOrganisms.html)
          * [biosample](Biosample.html)
             * [cell line](CellLine.html)
          * [anatomical entity](AnatomicalEntity.html)
             * [cellular component](CellularComponent.html)
             * [cell](Cell.html)
             * [gross anatomical structure](GrossAnatomicalStructure.html)
          * [life stage](LifeStage.html)
       * [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)
          * [disease](Disease.html)
          * [phenotypic feature](PhenotypicFeature.html)
       * [environment](Environment.html)
          * [drug exposure](DrugExposure.html)
          * [treatment](Treatment.html)
       * [molecular entity](MolecularEntity.html)
          * [chemical substance](ChemicalSubstance.html)
             * [drug](Drug.html)
             * [metabolite](Metabolite.html)
          * [genomic entity](GenomicEntity.html)
             * [genome](Genome.html)
             * [transcript](Transcript.html)
             * [exon](Exon.html)
             * [coding sequence](CodingSequence.html)
             * [macromolecular machine](MacromolecularMachine.html)
                * [gene or gene product](GeneOrGeneProduct.html)
                   * [gene](Gene.html)
                   * [gene product](GeneProduct.html)
                      * [protein](Protein.html)
                         * [protein isoform](ProteinIsoform.html)
                      * [gene product isoform](GeneProductIsoform.html)
                      * [RNA product](RnaProduct.html)
                         * [RNA product isoform](RnaProductIsoform.html)
                         * [noncoding RNA product](NoncodingRnaProduct.html)
                            * [microRNA](Microrna.html)
                * [macromolecular complex](MacromolecularComplex.html)
             * [genotype](Genotype.html)
             * [haplotype](Haplotype.html)
             * [sequence variant](SequenceVariant.html)
          * [gene family](GeneFamily.html)
       * [biological process or activity](BiologicalProcessOrActivity.html)
          * [molecular activity](MolecularActivity.html)
          * [biological process](BiologicalProcess.html)
             * [pathway](Pathway.html)
             * [physiological process](PhysiologicalProcess.html)
    * [information content entity](InformationContentEntity.html)
       * [confidence level](ConfidenceLevel.html)
       * [evidence type](EvidenceType.html)
       * [publication](Publication.html)
       * [association](Association.html)
          * [genotype to genotype part association](GenotypeToGenotypePartAssociation.html)
          * [genotype to gene association](GenotypeToGeneAssociation.html)
          * [genotype to variant association](GenotypeToVariantAssociation.html)
          * [gene to gene association](GeneToGeneAssociation.html)
             * [gene to gene homology association](GeneToGeneHomologyAssociation.html)
             * [pairwise gene or protein interaction association](PairwiseGeneOrProteinInteractionAssociation.html)
          * [molecular interaction](MolecularInteraction.html)
          * [cell line to thing association](CellLineToThingAssociation.html)
          * [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.html)
          * [chemical to thing association](ChemicalToThingAssociation.html)
          * [case to thing association](CaseToThingAssociation.html)
          * [chemical to gene association](ChemicalToGeneAssociation.html)
          * [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html)
          * [chemical to pathway association](ChemicalToPathwayAssociation.html)
          * [chemical to gene association](ChemicalToGeneAssociation.html)
          * [biosample to thing association](BiosampleToThingAssociation.html)
          * [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html)
          * [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
          * [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.html)
             * [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html)
          * [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html)
          * [disease to thing association](DiseaseToThingAssociation.html)
          * [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html)
          * [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html)
          * [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html)
          * [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html)
          * [gene to thing association](GeneToThingAssociation.html)
          * [variant to thing association](VariantToThingAssociation.html)
          * [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html)
          * [gene to disease association](GeneToDiseaseAssociation.html)
             * [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html)
             * [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html)
          * [variant to population association](VariantToPopulationAssociation.html)
          * [population to population association](PopulationToPopulationAssociation.html)
          * [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html)
          * [variant to disease association](VariantToDiseaseAssociation.html)
          * [genotype to thing association](GenotypeToThingAssociation.html)
          * [gene to expression site association](GeneToExpressionSiteAssociation.html)
          * [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html)
          * [functional association](FunctionalAssociation.html)
             * [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.html)
             * [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.html)
             * [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.html)
             * [gene to go term association](GeneToGoTermAssociation.html)
          * [genomic sequence localization](GenomicSequenceLocalization.html)
          * [sequence feature relationship](SequenceFeatureRelationship.html)
             * [transcript to gene relationship](TranscriptToGeneRelationship.html)
             * [gene to gene product relationship](GeneToGeneProductRelationship.html)
             * [exon to transcript relationship](ExonToTranscriptRelationship.html)
          * [gene regulatory relationship](GeneRegulatoryRelationship.html)
          * [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html)
             * [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.html)
             * [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.html)
    * [planetary entity](PlanetaryEntity.html)
       * [environmental process](EnvironmentalProcess.html)
       * [environmental feature](EnvironmentalFeature.html)
       * [geographic location](GeographicLocation.html)
       * [geographic location at time](GeographicLocationAtTime.html)
    * [clinical entity](ClinicalEntity.html)
       * [clinical trial](ClinicalTrial.html)
       * [clinical intervention](ClinicalIntervention.html)
    * [device](Device.html)
 * [administrative entity](AdministrativeEntity.html)
    * [provider](Provider.html)
 * [attribute](Attribute.html)
    * [biological sex](BiologicalSex.html)
       * [phenotypic sex](PhenotypicSex.html)
       * [genotypic sex](GenotypicSex.html)
    * [severity value](SeverityValue.html)
    * [frequency value](FrequencyValue.html)
    * [clinical modifier](ClinicalModifier.html)
    * [onset](Onset.html)
    * [zygosity](Zygosity.html)
 * [occurrent](Occurrent.html)
    * [activity and behavior](ActivityAndBehavior.html)
    * [procedure](Procedure.html)
    * [phenomenon](Phenomenon.html)

<a name="mixins"/>
### Mixins

 * [relationship quantifier](RelationshipQuantifier.html)
    * [senstivity quantifier](SenstivityQuantifier.html)
    * [specificity quantifier](SpecificityQuantifier.html)
       * [pathognomonicity quantifier](PathognomonicityQuantifier.html)
    * [frequency quantifier](FrequencyQuantifier.html)
 * [ontology class](OntologyClass.html)
    * [gene ontology class](GeneOntologyClass.html)
    * [organism taxon](OrganismTaxon.html)
 * [thing with taxon](ThingWithTaxon.html)
 * [gene grouping](GeneGrouping.html)
 * [entity to disease association](EntityToDiseaseAssociation.html)
 * [model to disease mixin](ModelToDiseaseMixin.html)

<a name="slots"/>
### Predicates and Properties

 * [related to](related_to.html)
    * [interacts with](interacts_with.html) *subsets: translator_minimal*
       * [physically interacts with](physically_interacts_with.html) *subsets: translator_minimal*
          * [molecularly interacts with](molecularly_interacts_with.html) *subsets: translator_minimal*
       * [genetically interacts with](genetically_interacts_with.html) *subsets: translator_minimal*
    * [affects](affects.html) *subsets: translator_minimal*
       * [regulates](regulates.html)
          * [positively regulates](positively_regulates.html)
          * [negatively regulates](negatively_regulates.html)
          * [regulates, process to process](regulates_process_to_process.html)
             * [positively regulates, process to process](positively_regulates_process_to_process.html)
             * [negatively regulates, process to process](negatively_regulates_process_to_process.html)
          * [regulates, entity to entity](regulates_entity_to_entity.html) *subsets: translator_minimal*
             * [positively regulates, entity to entity](positively_regulates_entity_to_entity.html) *subsets: translator_minimal*
             * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.html) *subsets: translator_minimal*
       * [disrupts](disrupts.html) *subsets: translator_minimal*
       * [treats](treats.html) *subsets: translator_minimal*
    * [has gene product](has_gene_product.html) *subsets: translator_minimal*
    * [homologous to](homologous_to.html) *subsets: translator_minimal*
       * [paralogous to](paralogous_to.html) *subsets: translator_minimal*
       * [orthologous to](orthologous_to.html) *subsets: translator_minimal*
       * [xenologous to](xenologous_to.html) *subsets: translator_minimal*
    * [coexists with](coexists_with.html) *subsets: translator_minimal*
       * [in pathway with](in_pathway_with.html) *subsets: translator_minimal*
       * [in complex with](in_complex_with.html) *subsets: translator_minimal*
       * [in cell population with](in_cell_population_with.html) *subsets: translator_minimal*
       * [co-localizes with](co-localizes_with.html) *subsets: translator_minimal*
    * [gene associated with condition](gene_associated_with_condition.html) *subsets: translator_minimal*
    * [affects risk for](affects_risk_for.html) *subsets: translator_minimal*
       * [predisposes](predisposes.html) *subsets: translator_minimal*
       * [prevents](prevents.html) *subsets: translator_minimal*
    * [contributes to](contributes_to.html) *subsets: translator_minimal*
       * [causes](causes.html) *subsets: translator_minimal*
    * [correlated with](correlated_with.html) *subsets: translator_minimal*
       * [has biomarker](has_biomarker.html) *subsets: translator_minimal*
       * [biomarker for](biomarker_for.html) *subsets: translator_minimal*
    * [treated by](treated_by.html) *subsets: translator_minimal*
    * [expressed in](expressed_in.html) *subsets: translator_minimal*
    * [expresses](expresses.html) *subsets: translator_minimal*
    * [has phenotype](has_phenotype.html) *subsets: translator_minimal*
    * [occurs in](occurs_in.html) *subsets: translator_minimal*
    * [located in](located_in.html) *subsets: translator_minimal*
    * [location of](location_of.html) *subsets: translator_minimal*
    * [model of](model_of.html) *subsets: translator_minimal*
    * [overlaps](overlaps.html) *subsets: translator_minimal*
       * [has part](has_part.html) *subsets: translator_minimal*
       * [part of](part_of.html) *subsets: translator_minimal*
    * [has participant](has_participant.html) *subsets: translator_minimal*
       * [has input](has_input.html) *subsets: translator_minimal*
    * [participates in](participates_in.html) *subsets: translator_minimal*
       * [actively involved in](actively_involved_in.html) *subsets: translator_minimal*
          * [capable of](capable_of.html) *subsets: translator_minimal*
    * [derives into](derives_into.html) *subsets: translator_minimal*
    * [derives from](derives_from.html) *subsets: translator_minimal*
    * [manifestation of](manifestation_of.html) *subsets: translator_minimal*
    * [produces](produces.html) *subsets: translator_minimal*
    * [precedes](precedes.html) *subsets: translator_minimal*
    * [same as](same_as.html) *subsets: translator_minimal*
    * [subclass of](subclass_of.html) *subsets: translator_minimal*
    * [in taxon](in_taxon.html) *subsets: translator_minimal*
    * [has molecular consequence](has_molecular_consequence.html)
 * [node property](node_property.html)
    * [id](id.html) *subsets: translator_minimal*
    * [iri](iri.html) *subsets: translator_minimal*
    * [name](name.html) *subsets: translator_minimal*
    * [category](category.html) *subsets: translator_minimal*
    * [full name](full_name.html)
    * [description](description.html) *subsets: translator_minimal*
    * [systematic synonym](systematic_synonym.html)
    * [creation date](creation_date.html)
    * [update date](update_date.html)
    * [latitude](latitude.html)
    * [longitude](longitude.html)
    * [has chemical formula](has_chemical_formula.html)
    * [aggregate statistic](aggregate_statistic.html)
       * [has count](has_count.html)
       * [has total](has_total.html)
       * [has quotient](has_quotient.html)
       * [has percentage](has_percentage.html)
    * [timepoint](timepoint.html)
    * [has biological sequence](has_biological_sequence.html)
    * [has gene](has_gene.html)
    * [has zygosity](has_zygosity.html)
    * [filler](filler.html)
    * [phase](phase.html)
    * [genome build](genome_build.html)
    * [interbase coordinate](interbase_coordinate.html)
       * [start interbase coordinate](start_interbase_coordinate.html)
       * [end interbase coordinate](end_interbase_coordinate.html)
 * [association slot](association_slot.html)
    * [subject](subject.html)
    * [object](object.html)
    * [edge label](edge_label.html)
    * [relation](relation.html)
    * [negated](negated.html)
    * [has confidence level](has_confidence_level.html)
    * [has evidence](has_evidence.html)
    * [provided by](provided_by.html)
    * [association type](association_type.html)
    * [stage qualifier](stage_qualifier.html)
    * [quantifier qualifier](quantifier_qualifier.html)
    * [qualifiers](qualifiers.html)
    * [frequency qualifier](frequency_qualifier.html)
    * [severity qualifier](severity_qualifier.html)
    * [sex qualifier](sex_qualifier.html)
    * [onset qualifier](onset_qualifier.html)
    * [clinical modifier qualifier](clinical_modifier_qualifier.html)
    * [sequence variant qualifier](sequence_variant_qualifier.html)
    * [publications](publications.html)
