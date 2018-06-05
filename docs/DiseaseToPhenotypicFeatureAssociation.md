# Class: disease to phenotypic feature association


An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way

URI: http://bioentity.io/vocab/DiseaseToPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[DiseaseToPhenotypicFeatureAssociation|frequency_qualifier:frequency_value%20%3F],%20\[DiseaseToPhenotypicFeatureAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[DiseaseToPhenotypicFeatureAssociation]-%20severity_qualifier%20%3F>\[SeverityValue],%20\[DiseaseToPhenotypicFeatureAssociation]-%20onset_qualifier%20%3F>\[Onset],%20\[DiseaseToPhenotypicFeatureAssociation]-%20sex_qualifier%20%3F>\[BiologicalSex],%20\[DiseaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[DiseaseToPhenotypicFeatureAssociation]uses%20-.->\[DiseaseToThingAssociation],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [disease to thing association](DiseaseToThingAssociation.md)
## Children

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
 * _[sex qualifier](sex_qualifier.md)_
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * range: [biological sex](BiologicalSex.md)
    * inherited from: [association slot](association_slot.md)
