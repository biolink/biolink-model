# Class: biosample




URI: [http://bioentity.io/vocab/Biosample](http://bioentity.io/vocab/Biosample)

![img](images/Biosample.png)
## Mappings

 * [SIO:001050](http://semanticscience.org/resource/SIO_001050)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [cell line](CellLine.md)
## Used in

 *  class: [biosample](Biosample.md) references: [cell line](CellLine.md)
## Fields

 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
