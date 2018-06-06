# Class: anatomical entity


A subcellular location, cell type or gross anatomical part

URI: [http://bioentity.io/vocab/AnatomicalEntity](http://bioentity.io/vocab/AnatomicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity]^-\[AnatomicalEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[AnatomicalEntity]^-\[Cell],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]-%20related%20to(i)%20%3F>\[NamedThing],%20\[AnatomicalEntity]-%20expresses%20%3F>\[GeneOrGeneProduct],%20\[AnatomicalEntity]-%20in%20taxon%20%3F>\[OrganismTaxon],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon])
## Mappings

 * [UMLSSG:ANAT](http://purl.obolibrary.org/obo/UMLSSG_ANAT)
 * [SIO:010046](http://semanticscience.org/resource/SIO_010046)
 * [WD:Q4936952](http://purl.obolibrary.org/obo/WD_Q4936952)
 * [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [cellular component](CellularComponent.md) - A location in or around a cell
 *  child: [cell](Cell.md)
 *  child: [gross anatomical structure](GrossAnatomicalStructure.md)
## Used in

 *  class: [anatomical entity](AnatomicalEntity.md) references: [cellular component](CellularComponent.md)
 *  class: [anatomical entity](AnatomicalEntity.md) references: [cell](Cell.md)
 *  class: [anatomical entity](AnatomicalEntity.md) references: [gross anatomical structure](GrossAnatomicalStructure.md)
## Fields

 * _[expresses](expresses.md) *subsets: translator_minimal*_
    * _holds between an anatomical entity and gene or gene product that is expressed there_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * __Local__
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
