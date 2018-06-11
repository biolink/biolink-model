# Class: drug exposure


A drug exposure is an intake of a particular chemical substance

URI: [http://bioentity.io/vocab/DrugExposure](http://bioentity.io/vocab/DrugExposure)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DrugExposure|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DrugExposure]-%20drug%20+>\[ChemicalSubstance],%20\[Treatment]-%20has%20exposure%20parts(i)%20+>\[DrugExposure],%20\[Environment]^-\[DrugExposure])
## Mappings

 * [ECTO:0000509](http://purl.obolibrary.org/obo/ECTO_0000509)
 * [SIO:001005](http://semanticscience.org/resource/SIO_001005)
## Inheritance

 *  is_a: environment
## Children

## Used in

 *  class: **treatment** *treatment has exposure parts* **drug exposure**
## Fields

 * _drug exposure drug_
    * range: chemical substance* [required]
    * __Local__
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _has phenotype_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: phenotype
    * inherited from: biological entity
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
