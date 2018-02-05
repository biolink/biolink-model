---
layout: default
---

[![Build Status](https://travis-ci.org/biolink/biolink-model.svg?branch=master)](https://travis-ci.org/biolink/biolink-model)

# Biolink Model

A high level datamodel of biological entities (genes, diseases,
phenotypes, pathways, individuals, substances, etc) and their
associations.

# Explore

 * Explore the model: [Datamodel index](docs/)
 * Documentation on github: [biolink/biolink-model](https://github.com/biolink/biolink-model)

## Core Semantic Types

 * [biological entity](docs/BiologicalEntity.html)
    * [organismal entity](docs/OrganismalEntity.html)
       * [organism taxon](docs/OrganismTaxon.html)
       * [individual organism](docs/IndividualOrganism.html)
          * [case](docs/Case.html)
       * [population of individual organisms](docs/PopulationOfIndividualOrganisms.html)
          * [cohort](docs/Cohort.html)
       * [biosample](docs/Biosample.html)
       * [anatomical entity](docs/AnatomicalEntity.html)
          * [cellular component](docs/CellularComponent.html)
          * [cell](docs/Cell.html)
          * [gross anatomical structure](docs/GrossAnatomicalStructure.html)
       * [life stage](docs/LifeStage.html)
    * [disease or phenotypic feature](docs/DiseaseOrPhenotypicFeature.html)
       * [disease](docs/Disease.html)
       * [phenotypic feature](docs/PhenotypicFeature.html)
    * [environment](docs/Environment.html)
       * [drug exposure](docs/DrugExposure.html)
       * [treatment](docs/Treatment.html)
    * [molecular entity](docs/MolecularEntity.html)
       * [chemical substance](docs/ChemicalSubstance.html)
       * [genomic entity](docs/GenomicEntity.html)
          * [genome](docs/Genome.html)
          * [transcript](docs/Transcript.html)
          * [exon](docs/Exon.html)
          * [coding sequence](docs/CodingSequence.html)
          * [gene or gene product](docs/GeneOrGeneProduct.html)
             * [gene](docs/Gene.html)
             * [gene product](docs/GeneProduct.html)
                * [protein](docs/Protein.html)
                * [RNA product](docs/RnaProduct.html)
                   * [microRNA](docs/Microrna.html)
          * [genotype](docs/Genotype.html)
          * [sequence variant](docs/SequenceVariant.html)
       * [macromolecular complex](docs/MacromolecularComplex.html)
       * [gene family](docs/GeneFamily.html)
       * [bioentity with go terms](docs/BioentityWithGoTerms.html)
    * [biological process](docs/BiologicalProcess.html)
       * [pathway](docs/Pathway.html)

