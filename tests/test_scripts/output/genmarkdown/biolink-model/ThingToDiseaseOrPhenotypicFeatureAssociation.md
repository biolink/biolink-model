# Class: thing to disease or phenotypic feature association




URI: http://bioentity.io/vocab/ThingToDiseaseOrPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object>\[DiseaseOrPhenotypicFeature],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
 *  mixin: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  mixin: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
## Used in

 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * Example: [MONDO:0017314](http://purl.obolibrary.org/obo/MONDO_0017314) Ehlers-Danlos syndrome, vascular type
    * Example: [MP:0013229](http://purl.obolibrary.org/obo/MP_0013229) abnormal brain ventricle size
    * inherited from: [object](object.md)
