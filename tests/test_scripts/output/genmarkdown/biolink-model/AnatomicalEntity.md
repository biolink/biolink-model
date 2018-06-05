# Class: anatomical entity


A subcellular location, cell type or gross anatomical part

URI: http://bioentity.io/vocab/AnatomicalEntity

![img](http://yuml.me/diagram/nofunky/class/\[OrganismalEntity]^-\[AnatomicalEntity],%20\[AnatomicalEntity]^-\[Cell],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]-%20expresses%20%3F>\[GeneOrGeneProduct],%20\[AnatomicalEntity]-%20in_taxon%20%3F>\[OrganismTaxon],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon],%20)
## Mappings

 * [UMLSSG:ANAT](http://purl.obolibrary.org/obo/UMLSSG_ANAT)
 * [SIO:010046](http://semanticscience.org/resource/SIO_010046)
 * [WD:Q4936952](http://purl.obolibrary.org/obo/WD_Q4936952)
 * [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md)
## Children

 *  child: [gross anatomical structure](GrossAnatomicalStructure.md)
 *  child: [cell](Cell.md)
 *  child: [cellular component](CellularComponent.md)
## Used in

 *  class: [anatomical entity](AnatomicalEntity.md) references: [gross anatomical structure](GrossAnatomicalStructure.md)
 *  class: [anatomical entity](AnatomicalEntity.md) references: [cell](Cell.md)
 *  class: [anatomical entity](AnatomicalEntity.md) references: [cellular component](CellularComponent.md)
## Fields

 * _[expresses](expresses.md) *subsets: translator_minimal*_
    * _holds between an anatomical entity and gene or gene product that is expressed there_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [related to](related_to.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [related to](related_to.md)
