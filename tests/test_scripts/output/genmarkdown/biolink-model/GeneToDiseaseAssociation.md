# Class: gene to disease association




URI: http://bioentity.io/vocab/GeneToDiseaseAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GeneToDiseaseAssociation|frequency_qualifier:frequency_value%20%3F],%20\[GeneToDiseaseAssociation]^-\[GeneAsAModelOfDiseaseAssociation],%20\[GeneToDiseaseAssociation]^-\[GeneHasVariantThatContributesToDiseaseAssociation],%20\[GeneToDiseaseAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[GeneToDiseaseAssociation]-%20severity_qualifier%20%3F>\[SeverityValue],%20\[GeneToDiseaseAssociation]-%20onset_qualifier%20%3F>\[Onset],%20\[GeneToDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[GeneToThingAssociation],%20)
## Mappings

 * [SIO:000983](http://semanticscience.org/resource/SIO_000983)
## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.md)
 *  mixin: [gene to thing association](GeneToThingAssociation.md)
## Children

 *  child: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  child: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.md)
## Used in

 *  class: [gene to disease association](GeneToDiseaseAssociation.md) references: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  class: [gene to disease association](GeneToDiseaseAssociation.md) references: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.md)
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
