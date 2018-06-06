# Class: cellular component


A location in or around a cell

URI: [http://bioentity.io/vocab/CellularComponent](http://bioentity.io/vocab/CellularComponent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntity]^-\[CellularComponent|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[CellularComponent]-%20related%20to(i)%20%3F>\[NamedThing],%20\[CellularComponent]-%20expresses(i)%20%3F>\[GeneOrGeneProduct],%20\[CellularComponent]-%20in%20taxon(i)%20%3F>\[OrganismTaxon])
## Mappings

 * [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)
 * [SIO:001400](http://semanticscience.org/resource/SIO_001400)
 * [WD:Q5058355](http://purl.obolibrary.org/obo/WD_Q5058355)
## Inheritance

 *  is_a: [anatomical entity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
## Children

## Used in

## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[expresses](expresses.md) *subsets: translator_minimal*_
    * _holds between an anatomical entity and gene or gene product that is expressed there_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [anatomical entity](AnatomicalEntity.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
