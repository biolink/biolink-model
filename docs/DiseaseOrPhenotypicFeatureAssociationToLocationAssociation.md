# Class: disease or phenotypic feature association to location association


An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.

URI: http://bioentity.io/vocab/DiseaseOrPhenotypicFeatureAssociationToLocationAssociation

![img](http://yuml.me/diagram/nofunky/class/\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]^-\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation],%20\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation]-%20object>\[AnatomicalEntity],%20)
## Mappings

 * [NCIT:R100](http://purl.obolibrary.org/obo/NCIT_R100)
## Inheritance

 *  is_a: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * Example: [UBERON:0002048](http://purl.obolibrary.org/obo/UBERON_0002048) lung
    * inherited from: [object](object.md)
