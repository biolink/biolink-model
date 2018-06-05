# Class: sequence variant modulates treatment association


An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.

URI: http://bioentity.io/vocab/SequenceVariantModulatesTreatmentAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[SequenceVariantModulatesTreatmentAssociation]-%20subject>\[SequenceVariant],%20\[SequenceVariantModulatesTreatmentAssociation]-%20object>\[Treatment],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [treatment](Treatment.md) [required]
    * inherited from: [object](object.md)
