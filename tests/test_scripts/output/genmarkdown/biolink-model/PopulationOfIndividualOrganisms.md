# Class: population of individual organisms




URI: [http://bioentity.io/vocab/PopulationOfIndividualOrganisms](http://bioentity.io/vocab/PopulationOfIndividualOrganisms)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PopulationOfIndividualOrganisms|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[PopulationOfIndividualOrganisms]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[PopulationToPopulationAssociation]-%20object(i)>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20subject(i)>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20object(i)>\[PopulationOfIndividualOrganisms],%20\[PopulationOfIndividualOrganisms]uses%20-.->\[ThingWithTaxon],%20\[OrganismalEntity]^-\[PopulationOfIndividualOrganisms])
## Mappings

 * [SIO:001061](http://semanticscience.org/resource/SIO_001061)
 * [PCO:0000001](http://purl.obolibrary.org/obo/PCO_0000001)
## Inheritance

 *  is_a: organismal entity
 *  mixin: thing with taxon
## Children

## Used in

 *  class: **population to population association** *population to population association object* **population of individual organisms**
 *  class: **population to population association** *population to population association subject* **population of individual organisms**
 *  class: **variant to population association** *variant to population association object* **population of individual organisms**
## Fields

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
 * _in taxon_
    * _connects a thing to a class representing a taxon_
    * range: organism taxon
    * inherited from: thing with taxon
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
