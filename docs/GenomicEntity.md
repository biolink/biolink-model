# Class: genomic entity


an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

URI: http://bioentity.io/vocab/GenomicEntity

![img](http://yuml.me/diagram/nofunky/class/\[MolecularEntity]^-\[GenomicEntity|has_biological_sequence:biological_sequence%20%3F],%20\[GenomicEntity]^-\[CodingSequence],%20\[GenomicEntity]^-\[Exon],%20\[GenomicEntity]^-\[Genome],%20\[GenomicEntity]^-\[Genotype],%20\[GenomicEntity]^-\[Haplotype],%20\[GenomicEntity]^-\[MacromolecularMachine],%20\[GenomicEntity]^-\[SequenceVariant],%20\[GenomicEntity]^-\[Transcript],%20)
## Mappings

 * [SO:0000110](http://purl.obolibrary.org/obo/SO_0000110)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [molecular entity](MolecularEntity.md)
## Children

 *  child: [genome](Genome.md)
 *  child: [haplotype](Haplotype.md)
 *  child: [coding sequence](CodingSequence.md)
 *  child: [macromolecular machine](MacromolecularMachine.md)
 *  child: [genotype](Genotype.md)
 *  child: [sequence variant](SequenceVariant.md)
 *  child: [exon](Exon.md)
 *  child: [transcript](Transcript.md)
## Used in

 *  class: [genomic entity](GenomicEntity.md) references: [genome](Genome.md)
 *  class: [genomic entity](GenomicEntity.md) references: [haplotype](Haplotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [coding sequence](CodingSequence.md)
 *  class: [genomic entity](GenomicEntity.md) references: [macromolecular machine](MacromolecularMachine.md)
 *  class: [genomic entity](GenomicEntity.md) references: [genotype](Genotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [sequence variant](SequenceVariant.md)
 *  class: [genomic entity](GenomicEntity.md) references: [exon](Exon.md)
 *  class: [genomic entity](GenomicEntity.md) references: [transcript](Transcript.md)
## Fields

 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [biological sequence](BiologicalSequence.md)
    * inherited from: [node property](node_property.md)
