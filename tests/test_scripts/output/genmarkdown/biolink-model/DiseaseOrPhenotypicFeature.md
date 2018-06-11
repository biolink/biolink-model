# Class: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [http://bioentity.io/vocab/DiseaseOrPhenotypicFeature](http://bioentity.io/vocab/DiseaseOrPhenotypicFeature)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DiseaseOrPhenotypicFeature|treated_by:string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DiseaseOrPhenotypicFeature]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[DiseaseOrPhenotypicFeature]-%20has%20biomarker%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20correlated%20with%20%3F>\[MolecularEntity],%20\[MolecularEntity]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject(i)>\[DiseaseOrPhenotypicFeature],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object(i)>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]-%20subject(i)>\[DiseaseOrPhenotypicFeature],%20\[Gene]-%20gene%20associated%20with%20condition(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object(i)>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20treats(i)>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20treats(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature])
## Mappings

## Inheritance

 *  is_a: biological entity
 *  mixin: thing with taxon
## Children

 * disease
 * phenotypic feature
## Used in

 *  class: **molecular entity** *biomarker for* **disease or phenotypic feature**
 *  class: **cell line to disease or phenotypic feature association** *cell line to disease or phenotypic feature association subject* **disease or phenotypic feature**
 *  class: **chemical to disease or phenotypic feature association** *chemical to disease or phenotypic feature association object* **disease or phenotypic feature**
 *  class: **disease or phenotypic feature association to thing association** *disease or phenotypic feature association to thing association subject* **disease or phenotypic feature**
 *  class: **gene** *gene associated with condition* **disease or phenotypic feature**
 *  class: **thing to disease or phenotypic feature association** *thing to disease or phenotypic feature association object* **disease or phenotypic feature**
 *  class: **treatment** *treatment treats* **disease or phenotypic feature**
 *  class: **treatment** *treats* **disease or phenotypic feature**
## Fields

 * _correlated with_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: molecular entity
    * __Local__
 * _has biomarker_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: molecular entity
    * __Local__
 * _treated by_
    * _holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition _
    * range: **string**
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
