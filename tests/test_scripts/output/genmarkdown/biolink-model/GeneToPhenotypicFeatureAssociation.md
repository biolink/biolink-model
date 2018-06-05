# Class: gene to phenotypic feature association




URI: http://bioentity.io/vocab/GeneToPhenotypicFeatureAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GeneToPhenotypicFeatureAssociation|frequency_qualifier:frequency_value%20%3F],%20\[GeneToPhenotypicFeatureAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[GeneToPhenotypicFeatureAssociation]-%20severity_qualifier%20%3F>\[SeverityValue],%20\[GeneToPhenotypicFeatureAssociation]-%20onset_qualifier%20%3F>\[Onset],%20\[GeneToPhenotypicFeatureAssociation]-%20sex_qualifier%20%3F>\[BiologicalSex],%20\[GeneToPhenotypicFeatureAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[GeneToPhenotypicFeatureAssociation]uses%20-.->\[GeneToThingAssociation],%20)
## Mappings

 * [http://bio2rdf.org/wormbase_vocabulary:Gene-Phenotype-Association](http://purl.obolibrary.org/obo/http_//bio2rdf.org/wormbase_vocabulary_Gene-Phenotype-Association)
## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [gene to thing association](GeneToThingAssociation.md)
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
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * Example: [HGNC:2197](https://monarchinitiative.org/gene/HGNC:2197) COL1A1 (Human)
    * inherited from: [subject](subject.md)
