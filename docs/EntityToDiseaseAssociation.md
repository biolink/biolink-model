# Class: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [http://bioentity.io/vocab/EntityToDiseaseAssociation](http://bioentity.io/vocab/EntityToDiseaseAssociation)

![img](images/EntityToDiseaseAssociation.png)
## Mappings

## Inheritance

## Children

 *  mixin: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  mixin: [gene to disease association](GeneToDiseaseAssociation.md)
 *  mixin: [variant to disease association](VariantToDiseaseAssociation.md)
## Used in

 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [gene to disease association](GeneToDiseaseAssociation.md)
 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * __Local__
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * __Local__
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * __Local__
 * _[object](object.md)_
    * _disease_
    * range: [disease](Disease.md)
    * Example: [MONDO:0020066](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
    * __Local__
