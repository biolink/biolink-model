# Class: entity to feature or disease qualifiers


Qualifiers for entity to disease or phenotype associations

URI: [http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers](http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EntityToFeatureOrDiseaseQualifiers]-%20onset%20qualifier%20%3F>\[Onset],%20\[EntityToFeatureOrDiseaseQualifiers]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[EntityToPhenotypicFeatureAssociation]uses%20-.->\[EntityToFeatureOrDiseaseQualifiers],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation],%20\[FrequencyQualifier]^-\[EntityToFeatureOrDiseaseQualifiers])
## Mappings

## Inheritance

 *  is_a: [FrequencyQualifier](FrequencyQualifier.md) - Qualifier for freqency type associations
## Children

 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) (mixin) 
## Used in

## Fields

 * [onset qualifier](onset_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
    * __Local__
 * [severity qualifier](severity_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * __Local__
