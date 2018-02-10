---
layout: default
---

## anatomical entity


A subcellular location, cell type or gross anatomical part

URI: [http://bioentity.io/vocab/AnatomicalEntity](http://bioentity.io/vocab/AnatomicalEntity)
## Mappings

 * [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062)

## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.html)
 *  mixin: [thing with taxon](ThingWithTaxon.html)

## Children

 *  child: [cellular component](CellularComponent.html)
 *  child: [cell](Cell.html)
 *  child: [gross anatomical structure](GrossAnatomicalStructure.html)

## Used in

 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity part of anatomical entity association](AnatomicalEntityPartOfAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
