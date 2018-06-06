# Class: genomic entity


an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

URI: [http://bioentity.io/vocab/GenomicEntity](http://bioentity.io/vocab/GenomicEntity)

![img](images/GenomicEntity.png)
## Mappings

 * [SO:0000110](http://purl.obolibrary.org/obo/SO_0000110)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
## Children

 *  child: [genome](Genome.md) - A genome is the sum of genetic material within a cell or virion.
 *  child: [transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase
 *  child: [genotype](Genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
 *  child: [haplotype](Haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 *  child: [macromolecular machine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
 *  child: [exon](Exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
 *  child: [coding sequence](CodingSequence.md)
 *  child: [sequence variant](SequenceVariant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.
## Used in

 *  class: [genomic entity](GenomicEntity.md) references: [genome](Genome.md)
 *  class: [genomic entity](GenomicEntity.md) references: [transcript](Transcript.md)
 *  class: [genomic entity](GenomicEntity.md) references: [genotype](Genotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [haplotype](Haplotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [macromolecular machine](MacromolecularMachine.md)
 *  class: [genomic entity](GenomicEntity.md) references: [exon](Exon.md)
 *  class: [genomic entity](GenomicEntity.md) references: [coding sequence](CodingSequence.md)
 *  class: [genomic entity](GenomicEntity.md) references: [sequence variant](SequenceVariant.md)
## Fields

 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [biological sequence](BiologicalSequence.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
