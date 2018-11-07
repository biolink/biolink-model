# Class: has genomic name


mixing class for any entity that has a full name and a systematic synonym

URI: [http://w3id.org/biolink/vocab/HasGenomicName](http://w3id.org/biolink/vocab/HasGenomicName)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GoTermBioentityMixin]uses%20-.->\[HasGenomicName|full_name:label_type%20%3F;systematic_synonym:label_type%20%3F])
## Mappings

## Inheritance

## Children

 * [GoTermBioentityMixin](GoTermBioentityMixin.md) (mixin)  - mixes in GO properties to bio-entities
## Used in

## Fields

 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * __Local__
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * __Local__
