# Class: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [http://bioentity.io/vocab/EntityToDiseaseAssociation](http://bioentity.io/vocab/EntityToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EntityToDiseaseAssociation]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[EntityToDiseaseAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[EntityToDiseaseAssociation]-%20object%20%3F>\[Disease],%20\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation])
## Mappings

## Inheritance

 *  is_a: entity to feature or disease qualifiers
## Children

 * gene as a model of disease association
 * gene to disease association
 * variant to disease association
## Used in

## Fields

 * _entity to disease association object_
    * _disease_
    * range: disease
    * __Local__
 * _onset qualifier_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: onset
    * inherited from: entity to feature or disease qualifiers
 * _severity qualifier_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: severity value
    * inherited from: entity to feature or disease qualifiers
