# Class: entity to feature or disease qualifiers


Qualifiers for entity to disease or phenotype associations

URI: [http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers](http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EntityToFeatureOrDiseaseQualifiers]-%20onset%20qualifier%20%3F>\[Onset],%20\[EntityToFeatureOrDiseaseQualifiers]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[EntityToPhenotypicFeatureAssociation]uses%20-.->\[EntityToFeatureOrDiseaseQualifiers],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation],%20\[FrequencyQualifier]^-\[EntityToFeatureOrDiseaseQualifiers])
## Mappings

## Inheritance

 *  is_a: frequency qualifier
## Children

 * entity to disease association
 * entity to phenotypic feature association
## Used in

## Fields

 * _onset qualifier_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: onset
    * __Local__
 * _severity qualifier_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: severity value
    * __Local__
