# Class: cell line




URI: [http://bioentity.io/vocab/CellLine](http://bioentity.io/vocab/CellLine)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Biosample]^-\[CellLine|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[CellLine]-%20related%20to(i)%20%3F>\[NamedThing],%20\[CellLine]-%20in%20taxon(i)%20%3F>\[OrganismTaxon])
## Mappings

 * [CLO:0000031](http://purl.obolibrary.org/obo/CLO_0000031)
## Inheritance

 *  is_a: [biosample](Biosample.md)
## Children

## Used in

## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
