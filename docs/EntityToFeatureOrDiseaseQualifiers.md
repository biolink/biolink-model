
# Class: entity to feature or disease qualifiers


Qualifiers for entity to disease or phenotype associations

URI: [biolink:EntityToFeatureOrDiseaseQualifiers](https://w3id.org/biolink/vocab/EntityToFeatureOrDiseaseQualifiers)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FrequencyValue]<frequency%20qualifier(i)%200..1-%20\[EntityToFeatureOrDiseaseQualifiers],%20\[Onset]<onset%20qualifier%200..1-%20\[EntityToFeatureOrDiseaseQualifiers],%20\[SeverityValue]<severity%20qualifier%200..1-%20\[EntityToFeatureOrDiseaseQualifiers],%20\[EntityToPhenotypicFeatureAssociation]uses%20-.->\[EntityToFeatureOrDiseaseQualifiers],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation],%20\[FrequencyQualifierMixin]^-\[EntityToFeatureOrDiseaseQualifiers])

## Parents

 *  is_a: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for freqency type associations

## Children

 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease

## Mixin for

 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
    * inherited from: [FrequencyQualifierMixin](FrequencyQualifierMixin.md)

### Domain for slot:

 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
