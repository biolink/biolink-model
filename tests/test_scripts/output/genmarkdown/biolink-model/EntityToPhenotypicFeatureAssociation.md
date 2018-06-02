# Class: entity to phenotypic feature association




URI: [http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation]
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.md)
    * inherited from: [association slot](association_slot.md)
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.md)
    * inherited from: [association slot](association_slot.md)
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.md)
    * inherited from: [association slot](association_slot.md)
 * _[sex qualifier](sex_qualifier.md)_
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * __range__: [biological sex](BiologicalSex.md)
    * inherited from: [association slot](association_slot.md)
