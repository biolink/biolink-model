# Class: chemical to disease or phenotypic feature association


An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype

URI: http://bioentity.io/vocab/ChemicalToDiseaseOrPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object>\[DiseaseOrPhenotypicFeature],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ChemicalToThingAssociation],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20)
## Mappings

 * [SIO:000993](http://semanticscience.org/resource/SIO_000993)
## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [chemical to thing association](ChemicalToThingAssociation.md)
 *  mixin: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * inherited from: [object](object.md)
