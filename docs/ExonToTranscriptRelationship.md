# Class: exon to transcript relationship


A transcript is formed from multiple exons

URI: http://bioentity.io/vocab/ExonToTranscriptRelationship

![img](http://yuml.me/diagram/nofunky/class/\[SequenceFeatureRelationship]^-\[ExonToTranscriptRelationship],%20\[ExonToTranscriptRelationship]-%20subject>\[Exon],%20\[ExonToTranscriptRelationship]-%20object>\[Transcript],%20)
## Mappings

## Inheritance

 *  is_a: [sequence feature relationship](SequenceFeatureRelationship.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [exon](Exon.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [transcript](Transcript.md) [required]
    * inherited from: [object](object.md)
