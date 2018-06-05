# Class: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: http://bioentity.io/vocab/EntityToDiseaseAssociation

![img](http://yuml.me/diagram/nofunky/class/\[EntityToDiseaseAssociation]-%20object%20%3F>\[Disease],%20)
## Mappings

## Inheritance

## Children

 *  mixin: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  mixin: [variant to disease association](VariantToDiseaseAssociation.md)
 *  mixin: [gene to disease association](GeneToDiseaseAssociation.md)
## Used in

 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.md)
 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
 *  class: [entity to disease association](EntityToDiseaseAssociation.md) references: [gene to disease association](GeneToDiseaseAssociation.md)
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
 * _[object](object.md)_
    * _disease_
    * range: [disease](Disease.md)
    * Example: [MONDO:0020066](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
