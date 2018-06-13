# Class: named thing


a databased entity or concept/class

URI: [http://bioentity.io/vocab/NamedThing](http://bioentity.io/vocab/NamedThing)

![img](images/NamedThing.png)
## Mappings

 * [UMLSSG:OBJC](http://purl.obolibrary.org/obo/UMLSSG_OBJC)
 * [WD:Q35120](http://purl.obolibrary.org/obo/WD_Q35120)
 * [BFO:0000001](http://purl.obolibrary.org/obo/BFO_0000001)
## Inheritance

## Children

 * [BiologicalEntity](BiologicalEntity.md)
 * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
 * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
## Used in

 *  class: **[PropertyValuePair](PropertyValuePair.md)** *[filler](filler.md)* **[NamedThing](NamedThing.md)**
 *  class: **[Association](Association.md)** *[has evidence object](has_evidence_object.md)* **[NamedThing](NamedThing.md)**
 *  class: **[NamedThing](NamedThing.md)** *[related to](related_to.md)* **[NamedThing](NamedThing.md)**
## Fields

 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [LabelType](LabelType.md)
    * __Local__
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [NarrativeText](NarrativeText.md)
    * __Local__
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [LabelType](LabelType.md)
    * __Local__
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [IdentifierType](IdentifierType.md)
    * __Local__
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [IriType](IriType.md)
    * __Local__
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [LabelType](LabelType.md)
    * __Local__
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [LabelType](LabelType.md)
    * __Local__
