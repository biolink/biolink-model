# Class: variant to disease association




URI: http://bioentity.io/vocab/VariantToDiseaseAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[VariantToDiseaseAssociation|frequency_qualifier:frequency_value%20%3F;subject:string;object:string],%20\[VariantToDiseaseAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[VariantToDiseaseAssociation]-%20severity_qualifier%20%3F>\[SeverityValue],%20\[VariantToDiseaseAssociation]-%20onset_qualifier%20%3F>\[Onset],%20\[VariantToDiseaseAssociation]-%20relation>\[RelationshipType],%20\[VariantToDiseaseAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [variant to thing association](VariantToThingAssociation.md)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.md)
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
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * Example: [ClinVar:52241](http://purl.obolibrary.org/obo/ClinVar_52241) NM_000059.3(BRCA2):c.7007G>C (p.Arg2336Pro)
    * inherited from: [subject](subject.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: related condition
    * inherited from: [relation](relation.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * Example: [MONDO:0016419](http://purl.obolibrary.org/obo/MONDO_0016419) hereditary breast cancer
    * inherited from: [object](object.md)
