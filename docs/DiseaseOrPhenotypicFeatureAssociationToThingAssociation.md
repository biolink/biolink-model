# Class: disease or phenotypic feature association to thing association




URI: http://bioentity.io/vocab/DiseaseOrPhenotypicFeatureAssociationToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]^-\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]-%20subject>\[DiseaseOrPhenotypicFeature],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  child: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)
## Used in

 *  class: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md) references: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * Example: [MONDO:0017314](http://purl.obolibrary.org/obo/MONDO_0017314) Ehlers-Danlos syndrome, vascular type
    * Example: [MP:0013229](http://purl.obolibrary.org/obo/MP_0013229) abnormal brain ventricle size
    * inherited from: [subject](subject.md)
