# Class: gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: http://bioentity.io/vocab/GeneToExpressionSiteAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GeneToExpressionSiteAssociation|quantifier_qualifier:string%20%3F],%20\[GeneToExpressionSiteAssociation]-%20stage_qualifier%20%3F>\[LifeStage],%20\[GeneToExpressionSiteAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToExpressionSiteAssociation]-%20object>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20relation>\[RelationshipType],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[stage qualifier](stage_qualifier.md)_
    * _stage at which the gene is expressed in the site_
    * range: [life stage](LifeStage.md)
    * Example: [UBERON:0000069](http://purl.obolibrary.org/obo/UBERON_0000069) larval stage
 * _[quantifier qualifier](quantifier_qualifier.md)_
    * _can be used to indicate magnitude, or also ranking_
    * range: string
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [anatomical entity](AnatomicalEntity.md) [required]
    * Example: [UBERON:0002037](http://purl.obolibrary.org/obo/UBERON_0002037) cerebellum
    * inherited from: [object](object.md)
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: [expressed in](expressed_in.md) *subsets: translator_minimal*
    * inherited from: [relation](relation.md)
