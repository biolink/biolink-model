# Class: disease to thing association




URI: http://bioentity.io/vocab/DiseaseToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[DiseaseToThingAssociation],%20\[DiseaseToThingAssociation]-%20subject>\[Disease],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [disease to thing association](DiseaseToThingAssociation.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease](Disease.md) [required]
    * Example: [MONDO:0017314](http://purl.obolibrary.org/obo/MONDO_0017314) Ehlers-Danlos syndrome, vascular type
    * inherited from: [subject](subject.md)
