# Class: entity to feature or disease qualifiers


Qualifiers for entity to disease or phenotype associations

URI: [http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers](http://bioentity.io/vocab/EntityToFeatureOrDiseaseQualifiers)

![img](images/EntityToFeatureOrDiseaseQualifiers.png)
## Mappings

## Inheritance

 *  is_a: [FrequencyQualifier](FrequencyQualifier.md) - Qualifier for freqency type associations
## Children

 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) (mixin) 
## Used in

## Fields

 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [Onset](Onset.md)
    * __Local__
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [SeverityValue](SeverityValue.md)
    * __Local__
