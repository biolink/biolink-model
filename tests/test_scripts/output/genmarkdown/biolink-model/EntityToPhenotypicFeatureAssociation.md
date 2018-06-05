# Class: entity to phenotypic feature association




URI: http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[EntityToPhenotypicFeatureAssociation|description:narrative_text%20%3F],%20\[EntityToPhenotypicFeatureAssociation]-%20object>\[PhenotypicFeature],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
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
 * _[description](description.md) *subsets: translator_minimal*_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [description](description.md) *subsets: translator_minimal*
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [phenotypic feature](PhenotypicFeature.md) [required]
    * Example: [HP:0002487](http://purl.obolibrary.org/obo/HP_0002487) Hyperkinesis
    * Example: [WBPhenotype:0000180](http://purl.obolibrary.org/obo/WBPhenotype_0000180) axon morphology variant
    * Example: [MP:0001569](http://purl.obolibrary.org/obo/MP_0001569) abnormal circulating bilirubin level
    * inherited from: [object](object.md)
