# Class: sequence feature relationship


For example, a particular exon is part of a particular transcript or gene

URI: http://bioentity.io/vocab/SequenceFeatureRelationship

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[SequenceFeatureRelationship],%20\[SequenceFeatureRelationship]^-\[ExonToTranscriptRelationship],%20\[SequenceFeatureRelationship]^-\[GeneToGeneProductRelationship],%20\[SequenceFeatureRelationship]^-\[TranscriptToGeneRelationship],%20\[SequenceFeatureRelationship]-%20subject>\[GenomicEntity],%20\[SequenceFeatureRelationship]-%20object>\[GenomicEntity],%20)
## Mappings

 * [GMODChado:feature_relationship](http://purl.obolibrary.org/obo/GMODChado_feature_relationship)
## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  child: [exon to transcript relationship](ExonToTranscriptRelationship.md)
 *  child: [gene to gene product relationship](GeneToGeneProductRelationship.md)
 *  child: [transcript to gene relationship](TranscriptToGeneRelationship.md)
## Used in

 *  class: [sequence feature relationship](SequenceFeatureRelationship.md) references: [exon to transcript relationship](ExonToTranscriptRelationship.md)
 *  class: [sequence feature relationship](SequenceFeatureRelationship.md) references: [gene to gene product relationship](GeneToGeneProductRelationship.md)
 *  class: [sequence feature relationship](SequenceFeatureRelationship.md) references: [transcript to gene relationship](TranscriptToGeneRelationship.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * inherited from: [object](object.md)
