---
parent: Class Mixins
title: biolink:ThingWithTaxon
grand_parent: Classes
layout: default
---

# Class: ThingWithTaxon


A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

URI: [biolink:ThingWithTaxon](https://w3id.org/biolink/vocab/ThingWithTaxon)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]%3Cin%20taxon%200..%2A-%20[ThingWithTaxon],[Protein]uses%20-.-%3E[ThingWithTaxon],[PopulationOfIndividualOrganisms]uses%20-.-%3E[ThingWithTaxon],[Polypeptide]uses%20-.-%3E[ThingWithTaxon],[LifeStage]uses%20-.-%3E[ThingWithTaxon],[IndividualOrganism]uses%20-.-%3E[ThingWithTaxon],[DiseaseOrPhenotypicFeature]uses%20-.-%3E[ThingWithTaxon],[AnatomicalEntity]uses%20-.-%3E[ThingWithTaxon],[ThingWithTaxon]%5E-[GenomicEntity],[Protein],[PopulationOfIndividualOrganisms],[Polypeptide],[OrganismTaxon],[LifeStage],[IndividualOrganism],[GenomicEntity],[DiseaseOrPhenotypicFeature],[AnatomicalEntity])

---


## Children

 * [GenomicEntity](GenomicEntity.md)

## Mixin for

 * [AnatomicalEntity](AnatomicalEntity.md) (mixin)  - A subcellular location, cell type or gross anatomical part
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) (mixin)  - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 * [IndividualOrganism](IndividualOrganism.md) (mixin)  - An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
 * [LifeStage](LifeStage.md) (mixin)  - A stage of development or growth of an organism, including post-natal adult stages
 * [Polypeptide](Polypeptide.md) (mixin)  - A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) (mixin)  - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
 * [Protein](Protein.md) (mixin)  - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

## Referenced by class


## Attributes


### Own

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)
