# Class: transcript to gene relationship


A gene is a collection of transcripts

URI: http://bioentity.io/vocab/TranscriptToGeneRelationship

![img](http://yuml.me/diagram/nofunky/class/\[SequenceFeatureRelationship]^-\[TranscriptToGeneRelationship],%20\[TranscriptToGeneRelationship]-%20subject>\[Transcript],%20\[TranscriptToGeneRelationship]-%20object>\[Gene],%20)
## Mappings

## Inheritance

 *  is_a: [sequence feature relationship](SequenceFeatureRelationship.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [transcript](Transcript.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene](Gene.md) [required]
    * inherited from: [object](object.md)
