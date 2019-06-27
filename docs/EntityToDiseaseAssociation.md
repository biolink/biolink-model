
# Class: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [biolink:EntityToDiseaseAssociation](https://w3id.org/biolink/vocab/EntityToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FrequencyValue]<frequency%20qualifier(i)%200..1-%20\[EntityToDiseaseAssociation],%20\[Onset]<onset%20qualifier(i)%200..1-%20\[EntityToDiseaseAssociation],%20\[SeverityValue]<severity%20qualifier(i)%200..1-%20\[EntityToDiseaseAssociation],%20\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation])

## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Inherited from entity to feature or disease qualifiers:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
    * inherited from: [FrequencyQualifierMixin](FrequencyQualifierMixin.md)

### Domain for slot:

 * [object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * range: [Disease](Disease.md)
