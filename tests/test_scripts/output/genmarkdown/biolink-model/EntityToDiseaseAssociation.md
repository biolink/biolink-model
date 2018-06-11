# Class: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [http://bioentity.io/vocab/EntityToDiseaseAssociation](http://bioentity.io/vocab/EntityToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[EntityToDiseaseAssociation|frequency_qualifier:frequency_value%20%3F]-%20object%20%3F>\[Disease],%20\[EntityToDiseaseAssociation]-%20onset%20qualifier%20%3F>\[Onset],%20\[EntityToDiseaseAssociation]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[EntityToDiseaseAssociation]-%20frequency%20qualifier%20%3F>\[FrequencyValue],%20\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation])
## Mappings

## Inheritance

## Children

 * gene as a model of disease association
 * gene to disease association
 * variant to disease association
## Used in

## Fields

 * _entity to disease association object_
    * _disease_
    * range: disease
    * Example: [MONDO:0020066](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
    * __Local__
 * _frequency qualifier_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: frequency value
    * __Local__
 * _onset qualifier_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: onset
    * __Local__
 * _severity qualifier_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: severity value
    * __Local__
