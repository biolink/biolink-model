# Class: anatomical entity


A subcellular location, cell type or gross anatomical part

URI: [http://bioentity.io/vocab/AnatomicalEntity](http://bioentity.io/vocab/AnatomicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[AnatomicalEntity]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[AnatomicalEntity]-%20expresses%20%3F>\[GeneOrGeneProduct],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object(i)>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject(i)>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject(i)>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20object(i)>\[AnatomicalEntity],%20\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation]-%20object(i)>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject(i)>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20object(i)>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object(i)>\[AnatomicalEntity],%20\[GeneOrGeneProduct]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[Cell],%20\[OrganismalEntity]^-\[AnatomicalEntity])
## Mappings

 * [UMLSSG:ANAT](http://purl.obolibrary.org/obo/UMLSSG_ANAT)
 * [SIO:010046](http://semanticscience.org/resource/SIO_010046)
 * [WD:Q4936952](http://purl.obolibrary.org/obo/WD_Q4936952)
 * [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062)
## Inheritance

 *  is_a: organismal entity
 *  mixin: thing with taxon
## Children

 * cell
 * cellular component
 * gross anatomical structure
## Used in

 *  class: **anatomical entity to anatomical entity association** *anatomical entity to anatomical entity association object* **anatomical entity**
 *  class: **anatomical entity to anatomical entity association** *anatomical entity to anatomical entity association subject* **anatomical entity**
 *  class: **anatomical entity to anatomical entity ontogenic association** *anatomical entity to anatomical entity ontogenic association object* **anatomical entity**
 *  class: **anatomical entity to anatomical entity ontogenic association** *anatomical entity to anatomical entity ontogenic association subject* **anatomical entity**
 *  class: **anatomical entity to anatomical entity part of association** *anatomical entity to anatomical entity part of association object* **anatomical entity**
 *  class: **anatomical entity to anatomical entity part of association** *anatomical entity to anatomical entity part of association subject* **anatomical entity**
 *  class: **disease or phenotypic feature association to location association** *disease or phenotypic feature association to location association object* **anatomical entity**
 *  class: **gene or gene product** *expressed in* **anatomical entity**
 *  class: **gene to expression site association** *gene to expression site association object* **anatomical entity**
## Fields

 * _expresses_
    * _holds between an anatomical entity and gene or gene product that is expressed there_
    * range: gene or gene product
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
