# Class: named thing


a databased entity or concept/class

URI: [http://bioentity.io/vocab/NamedThing](http://bioentity.io/vocab/NamedThing)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing|id:identifier_type%20%3F;name:label_type%20%3F;category:label_type%20%3F;node_property:string%20%3F;iri:iri_type%20%3F;full_name:label_type%20%3F;description:narrative_text%20%3F;systematic_synonym:label_type%20%3F]-%20related%20to%20%3F>\[NamedThing],%20\[NamedThing]-%20filler(i)%20%3F>\[NamedThing],%20\[NamedThing]-%20related%20to%20%3F>\[NamedThing],%20\[NamedThing]^-\[PlanetaryEntity],%20\[NamedThing]^-\[InformationContentEntity],%20\[NamedThing]^-\[Device],%20\[NamedThing]^-\[ClinicalEntity],%20\[NamedThing]^-\[BiologicalEntity])
## Mappings

 * [UMLSSG:OBJC](http://purl.obolibrary.org/obo/UMLSSG_OBJC)
 * [WD:Q35120](http://purl.obolibrary.org/obo/WD_Q35120)
 * [BFO:0000001](http://purl.obolibrary.org/obo/BFO_0000001)
## Inheritance

## Children

 * biological entity
 * clinical entity
 * device
 * information content entity
 * planetary entity
## Used in

 *  class: **named thing** *filler* **named thing**
 *  class: **named thing** *related to* **named thing**
## Fields

 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * __Local__
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * __Local__
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * __Local__
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * __Local__
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * __Local__
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * __Local__
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * __Local__
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * __Local__
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * __Local__
