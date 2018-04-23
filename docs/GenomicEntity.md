---
layout: default
---

## genomic entity


an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

URI: [http://bioentity.io/vocab/GenomicEntity](http://bioentity.io/vocab/GenomicEntity)


![img](http://yuml.me/diagram/nofunky/class/[molecular entity]^-[genomic entity], [genomic entity]-in taxon >[organism taxon], [ontology class]^-[organism taxon])
## Mappings

 * [SO:0000110](http://purl.obolibrary.org/obo/SO_0000110)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)

## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)

## Children

 *  child: [genome](Genome.html)
 *  child: [transcript](Transcript.html)
 *  child: [exon](Exon.html)
 *  child: [coding sequence](CodingSequence.html)
 *  child: [gene or gene product](GeneOrGeneProduct.html)
 *  child: [genotype](Genotype.html)
 *  child: [haplotype](Haplotype.html)
 *  child: [sequence variant](SequenceVariant.html)

## Used in

 *  class: [sequence variant](SequenceVariant.html) references: [gene](Gene.html)
 *  class: [genotype to genotype part association](GenotypeToGenotypePartAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [genotype](Genotype.html)
 *  class: [genotype to variant association](GenotypeToVariantAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to gene homology association](GeneToGeneHomologyAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [variant to thing association](VariantToThingAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [variant to population association](VariantToPopulationAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [variant to disease association](VariantToDiseaseAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [genotype to thing association](GenotypeToThingAssociation.html) references: [genotype](Genotype.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [sequence variant](SequenceVariant.html)
 *  class: [genomic sequence localization](GenomicSequenceLocalization.html) references: [genomic entity](GenomicEntity.html)
 *  class: [sequence feature relationship](SequenceFeatureRelationship.html) references: [genomic entity](GenomicEntity.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [transcript](Transcript.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [exon to transcript relationship](ExonToTranscriptRelationship.html) references: [exon](Exon.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)

## Fields

 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * __Local__
 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
