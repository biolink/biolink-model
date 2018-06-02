# Class: genomic entity


an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

URI: [http://bioentity.io/vocab/GenomicEntity]
## Mappings

 * [SO:0000110](http://purl.obolibrary.org/obo/SO_0000110)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [molecular entity](MolecularEntity.md)
## Children

 *  child: [coding sequence](CodingSequence.md)
 *  child: [genome](Genome.md)
 *  child: [haplotype](Haplotype.md)
 *  child: [sequence variant](SequenceVariant.md)
 *  child: [exon](Exon.md)
 *  child: [transcript](Transcript.md)
 *  child: [genotype](Genotype.md)
 *  child: [macromolecular machine](MacromolecularMachine.md)
## Used in

 *  class: [genomic entity](GenomicEntity.md) references: [coding sequence](CodingSequence.md)
 *  class: [genomic entity](GenomicEntity.md) references: [genome](Genome.md)
 *  class: [genomic entity](GenomicEntity.md) references: [haplotype](Haplotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [sequence variant](SequenceVariant.md)
 *  class: [genomic entity](GenomicEntity.md) references: [exon](Exon.md)
 *  class: [genomic entity](GenomicEntity.md) references: [transcript](Transcript.md)
 *  class: [genomic entity](GenomicEntity.md) references: [genotype](Genotype.md)
 *  class: [genomic entity](GenomicEntity.md) references: [macromolecular machine](MacromolecularMachine.md)
## Fields

 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * __range__: [biological sequence](BiologicalSequence.md)
    * inherited from: [node property](node_property.md)
