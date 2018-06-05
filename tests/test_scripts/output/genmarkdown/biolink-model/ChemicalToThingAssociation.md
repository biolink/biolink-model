# Class: chemical to thing association


An interaction between a chemical entity and another entity

URI: http://bioentity.io/vocab/ChemicalToThingAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[ChemicalToThingAssociation],%20\[ChemicalToThingAssociation]-%20subject>\[ChemicalSubstance],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

 *  mixin: [chemical to gene association](ChemicalToGeneAssociation.md)
 *  mixin: [chemical to pathway association](ChemicalToPathwayAssociation.md)
 *  mixin: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
## Used in

 *  class: [chemical to thing association](ChemicalToThingAssociation.md) references: [chemical to gene association](ChemicalToGeneAssociation.md)
 *  class: [chemical to thing association](ChemicalToThingAssociation.md) references: [chemical to pathway association](ChemicalToPathwayAssociation.md)
 *  class: [chemical to thing association](ChemicalToThingAssociation.md) references: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [chemical substance](ChemicalSubstance.md) [required]
    * inherited from: [subject](subject.md)
