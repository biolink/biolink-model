# Class: named thing


a databased entity or concept/class

URI: [http://bioentity.io/vocab/NamedThing]
## Mappings

 * [UMLSSG:OBJC](http://purl.obolibrary.org/obo/UMLSSG_OBJC)
 * [WD:Q35120](http://purl.obolibrary.org/obo/WD_Q35120)
 * [BFO:0000001](http://purl.obolibrary.org/obo/BFO_0000001)
## Inheritance

## Children

 *  child: [planetary entity](PlanetaryEntity.md)
 *  child: [biological entity](BiologicalEntity.md)
 *  child: [information content entity](InformationContentEntity.md)
 *  child: [clinical entity](ClinicalEntity.md)
 *  child: [device](Device.md)
## Used in

 *  class: [named thing](NamedThing.md) references: [planetary entity](PlanetaryEntity.md)
 *  class: [named thing](NamedThing.md) references: [biological entity](BiologicalEntity.md)
 *  class: [named thing](NamedThing.md) references: [information content entity](InformationContentEntity.md)
 *  class: [named thing](NamedThing.md) references: [clinical entity](ClinicalEntity.md)
 *  class: [named thing](NamedThing.md) references: [device](Device.md)
## Fields

 * _[id](id.md) *subsets: translator_minimal*_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: [identifier type](IdentifierType.md)
    * __Local__
 * _[name](name.md) *subsets: translator_minimal*_
    * _A human-readable name for a thing_
    * __range__: [label type](LabelType.md)
    * __Local__
 * _[category](category.md) *subsets: translator_minimal*_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: [label type](LabelType.md)
    * __Local__
