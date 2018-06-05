# Class: gene as a model of disease association




URI: http://bioentity.io/vocab/GeneAsAModelOfDiseaseAssociation

![img](http://yuml.me/diagram/nofunky/class/\[GeneToDiseaseAssociation]^-\[GeneAsAModelOfDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20)
## Mappings

## Inheritance

 *  is_a: [gene to disease association](GeneToDiseaseAssociation.md)
 *  mixin: [model to disease mixin](ModelToDiseaseMixin.md)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.md)
## Children

## Used in

## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * inherited from: [association slot](association_slot.md)
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * inherited from: [association slot](association_slot.md)
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * inherited from: [association slot](association_slot.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [subject](subject.md)
