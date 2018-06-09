# Class: treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [http://bioentity.io/vocab/Treatment](http://bioentity.io/vocab/Treatment)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Environment]^-\[Treatment|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[Treatment]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Treatment]-%20treats>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20has%20exposure%20parts%20+>\[DrugExposure])
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://semanticscience.org/resource/SIO_001398)
## Inheritance

 *  is_a: [environment](Environment.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
## Children

## Used in

 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md) references: [treatment](Treatment.md)
## Fields

 * _[has exposure parts](has_exposure_parts.md)_
    * range: [drug exposure](DrugExposure.md)* [required]
    * __Local__
 * _[treats](treats.md)_
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * __Local__
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[has phenotype](has_phenotype.md) *subsets*: (translator_minimal)_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [phenotype](Phenotype.md)
    * inherited from: [biological entity](BiologicalEntity.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
