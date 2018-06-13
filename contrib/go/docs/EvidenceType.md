# Class: evidence type


Class of evidence that supports an association

URI: [http://bioentity.io/vocab/EvidenceType](http://bioentity.io/vocab/EvidenceType)

![img](images/EvidenceType.png)
## Mappings

 * [ECO:0000000](http://purl.obolibrary.org/obo/ECO_0000000)
## Inheritance

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
## Children

## Used in

 *  class: **None** *[evidence object closure](evidence_object_closure.md)* **[EvidenceType](EvidenceType.md)**
 *  class: **[ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)** *[has evidence type](has_evidence_type.md)* **[EvidenceType](EvidenceType.md)**
## Fields

 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * _[title](title.md)_
    * _Narrative text describing the entity_
    * range: [LabelType](LabelType.md)
    * inherited from: [InformationContentEntity](InformationContentEntity.md)
