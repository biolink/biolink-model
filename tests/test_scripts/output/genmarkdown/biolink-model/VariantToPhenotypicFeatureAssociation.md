# Class: variant to phenotypic feature association




URI: http://bioentity.io/vocab/VariantToPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[VariantToPhenotypicFeatureAssociation|frequency_qualifier:frequency_value%20%3F],%20\[VariantToPhenotypicFeatureAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[VariantToPhenotypicFeatureAssociation]-%20severity_qualifier%20%3F>\[SeverityValue],%20\[VariantToPhenotypicFeatureAssociation]-%20onset_qualifier%20%3F>\[Onset],%20\[VariantToPhenotypicFeatureAssociation]-%20sex_qualifier%20%3F>\[BiologicalSex],%20\[VariantToPhenotypicFeatureAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPhenotypicFeatureAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [variant to thing association](VariantToThingAssociation.md)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
## Children

## Used in

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
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * inherited from: [subject](subject.md)
