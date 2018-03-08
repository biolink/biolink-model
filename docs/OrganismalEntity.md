---
layout: default
---

## organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [http://bioentity.io/vocab/OrganismalEntity](http://bioentity.io/vocab/OrganismalEntity)
## Mappings


## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)

## Children

 *  child: [organism taxon](OrganismTaxon.html)
 *  child: [individual organism](IndividualOrganism.html)
 *  child: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  child: [biosample](Biosample.html)
 *  child: [anatomical entity](AnatomicalEntity.html)
 *  child: [life stage](LifeStage.html)

## Used in

 *  class: [thing with taxon](ThingWithTaxon.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [individual organism](IndividualOrganism.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [case](Case.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [population of individual organisms](PopulationOfIndividualOrganisms.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [biosample](Biosample.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [disease](Disease.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [phenotypic feature](PhenotypicFeature.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [molecular entity](MolecularEntity.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [chemical substance](ChemicalSubstance.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [anatomical entity](AnatomicalEntity.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [life stage](LifeStage.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [genomic entity](GenomicEntity.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [genome](Genome.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [transcript](Transcript.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [exon](Exon.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [coding sequence](CodingSequence.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [gene or gene product](GeneOrGeneProduct.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [gene](Gene.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [gene product](GeneProduct.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [protein](Protein.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [RNA product](RnaProduct.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [noncoding RNA product](NoncodingRnaProduct.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [microRNA](Microrna.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [macromolecular complex](MacromolecularComplex.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [gene family](GeneFamily.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [genotype](Genotype.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [allele](Allele.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [sequence variant](SequenceVariant.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [life stage](LifeStage.html)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity part of anatomical entity association](AnatomicalEntityPartOfAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [cellular component](CellularComponent.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [cell](Cell.html) references: [organism taxon](OrganismTaxon.html)
 *  class: [gross anatomical structure](GrossAnatomicalStructure.html) references: [organism taxon](OrganismTaxon.html)

## Fields

 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
